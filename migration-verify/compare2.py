#!/usr/bin/env python3
"""Compare migrated Documentation.AI MDX against the live help.scrut.io source.

Ground truth: https://help.scrut.io/docs/<slug>.md  (Document360 canonical markdown)
Fallback for unpublished pages: the Aug-28 HTML export.

Known-lossy spots in Document360's own .md export are reconciled against the HTML
export rather than blamed on the migration (callouts, accordions, tabs).
"""
import sys, os, re, json, difflib, html, urllib.request, urllib.error
from urllib.parse import unquote

CACHE  = os.environ.get("WEBCACHE", "/tmp/webcache")
EXPORT = os.environ.get("EXPORT", "Scrut-Help-Center-2026-Aug-28-02-47-25/v1/articles")
PAREN  = r"(?:[^()]|\([^()]*\))*"
ASSET_HOST = re.compile(r'https?://(?:blob-cdn\.documentation\.ai|cdn\.document360\.io)/', re.I)
CALLOUT_MAP = {"NOTE":"info","TIP":"success","WARNING":"alert","CAUTION":"danger","IMPORTANT":"success"}
JUNK = {"null", "video", "grid view", "list view", "---", "plaintext", "text", "none"}

# ------------------------------------------------------------------ normalize
def frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m: return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        k = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', line)
        if k: fm[k.group(1)] = k.group(2).strip().strip('"').strip("'").strip()
    return fm, text[m.end():]

VIDEO_EXT = re.compile(r'\.(mp4|webm|mov)(\?|$)', re.I)

def is_video(url): return bool(VIDEO_EXT.search(url.split('?')[0] + '?'))

def imgkey(url):
    if url.strip().startswith('data:'): return '__data__'
    u = html.unescape(unquote(url.split("?")[0]))
    name = u.rsplit("/", 1)[-1]
    name = re.sub(r'^\d{10,}-[a-z0-9]{6,}-', '', name)      # documentation.ai blob prefix
    name = re.sub(r'-edited$', '', name, flags=re.I)
    name = re.sub(r'\.(png|jpe?g|gif|webp|svg|mp4|webm|mov|pdf)$', '', name, flags=re.I)
    return re.sub(r'[^a-z0-9]', '', html.unescape(name).lower())

def clean_text(s):
    s = html.unescape(s)
    s = re.sub(r'!\[[^\]]*\]\(' + PAREN + r'\)', ' ', s)          # images
    s = re.sub(r'\[([^\]]*)\]\(' + PAREN + r'\)', r'\1', s)       # links -> label
    s = re.sub(r'\\([\\`*_{}\[\]()#+\-.!|>~])', r'\1', s)         # md escapes
    s = re.sub(r'\{\s*(?:height|width)\s*=[^{}]*\}', ' ', s)      # {height="" width=""}
    s = re.sub(r'<[^>]+>', ' ', s)
    s = s.replace('**','').replace('__','').replace('`','')
    s = re.sub(r'(?<!\w)[*_](?!\s)([^*_]+)(?<!\s)[*_](?!\w)', r'\1', s)
    s = (s.replace('\u2018',"'").replace('\u2019',"'").replace('\u201c','"').replace('\u201d','"')
           .replace('\u2192','->').replace('\u2013','-').replace('\u2014','-')
           .replace('\xa0',' ').replace('\u200b',''))
    s = s.replace('\u2022', ' ')
    s = re.sub(r'\s+', ' ', s)
    return s.strip().strip('.').strip()

def strip_num(t):
    return re.sub(r'^#?\d+\s*[:.]\s*', '', t).strip()

def is_table_rule(s):   return bool(re.match(r'^\|[\s:\-|]+\|?$', s.strip()))
def is_fence(s):        return bool(re.match(r'^\s*(```|~~~)', s))

def links_of(text):
    out = []
    for m in re.finditer(r'(?<!!)\[[^\]]*\]\((' + PAREN + r')\)', text): out.append(m.group(1))
    for m in re.finditer(r'href="([^"]+)"', text):                        out.append(m.group(1))
    return [u for u in out if not ASSET_HOST.match(u.strip())]

def linkkey(u):
    u = html.unescape(u.strip()).split(' ')[0].strip('<>')
    if u.startswith('#'): return 'anchor:' + u.lower()
    u = re.sub(r'^https?://help\.scrut\.io(?=/)', '', u)
    u = re.sub(r'^/v1/docs/', '/docs/', u)
    if u.startswith('/docs/'): return 'internal:' + u.split('/')[-1].lower()
    if re.match(r'^/[a-z0-9][a-z0-9-]*(#|$)', u): return 'internal:' + u.lstrip('/').lower()
    return 'ext:' + u.rstrip('/').lower()


def text_units(line):
    """Yield comparable prose units. Table rows are split into cells so that a
    layout table migrated into Image + paragraph still compares equal."""
    body = re.sub(r'^\s*[-*]\s+|^\s*\d+[.)]\s+', '', line)
    if re.match(r'^\s*\|.*\|?\s*$', body) and not is_table_rule(body):
        for cell in body.strip().strip('|').split('|'):
            t = clean_text(cell)
            if t and t.lower() not in JUNK: yield t
    else:
        t = clean_text(body)
        if t and t.lower() not in JUNK: yield t


# ------------------------------------------------------- Aug-28 HTML export
_EXPORT_CACHE = {}
def export_blob(slug):
    """Plain text + image fingerprints of the Aug-28 export, used to tell a real
    migration loss apart from content the live site gained after the export."""
    if slug in _EXPORT_CACHE: return _EXPORT_CACHE[slug]
    fp = os.path.join(EXPORT, slug + ".html")
    if not os.path.exists(fp):
        _EXPORT_CACHE[slug] = None; return None
    h = open(fp, encoding="utf-8", errors="replace").read()
    imgs = {imgkey(u) for u in re.findall(r'<(?:img|video|source|iframe)[^>]+src="([^"]+)"', h)}
    t = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', h, flags=re.S|re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = clean_text(t)
    _EXPORT_CACHE[slug] = (t, imgs)
    return _EXPORT_CACHE[slug]

def in_export(slug, phrase, kind="text"):
    blob = export_blob(slug)
    if blob is None: return None                 # no export copy -> can't tell
    txt, imgs = blob
    if kind == "img": return phrase in imgs
    ph = phrase.strip()
    if len(ph) < 6: return None                  # too short to test reliably
    return ph in txt

# ------------------------------------------------------------------ web parse
def parse_web(text):
    fm, body = frontmatter(text)
    body = re.sub(r'^> ## Documentation Index\n(?:>.*\n)*', '', body, flags=re.M)
    body = re.sub(r'^# .*\n', '', body, count=1, flags=re.M)
    items, raw, lines, i, infence = [], [], body.split("\n"), 0, False
    def emit_imgs(s):
        for mi in re.finditer(r'!\[[^\]]*\]\((' + PAREN + r')\)', s):
            k = imgkey(mi.group(1))
            if k != '__data__': items.append(('IMG', k))
    while i < len(lines):
        ln = lines[i]
        if is_fence(ln):
            infence = not infence; raw.append(ln); i += 1; continue
        if infence:
            raw.append(ln)
            t = clean_text(ln)
            if t: items.append(('CODE', t))
            i += 1; continue
        m = re.match(r'^>\s*\[!(\w+)\]', ln)
        if m:
            items.append(('CALLOUT', CALLOUT_MAP.get(m.group(1).upper(), m.group(1).lower())))
            i += 1
            while i < len(lines) and lines[i].startswith('>'):
                b = re.sub(r'^>\s?', '', lines[i]); raw.append(b); emit_imgs(b)
                for t in text_units(b): items.append(('TEXT', t))
                i += 1
            continue
        h = re.match(r'^(#{2,6})\s+(.*)$', ln)
        if h:
            raw.append(ln); lvl, txt = len(h.group(1)), clean_text(h.group(2))
            if txt: items.append(('H%d' % lvl, txt))
            i += 1; continue
        raw.append(ln); emit_imgs(ln)
        if not is_table_rule(ln):
            for t in text_units(ln): items.append(('TEXT', t))
        i += 1
    return fm, items, "\n".join(raw)

# ------------------------------------------------------------------ mdx parse
def parse_mdx(text):
    fm, body = frontmatter(text)
    items, raw, infence = [], [], False
    demoted = []
    for ln in body.split("\n"):
        s = ln.strip()
        if is_fence(ln):
            infence = not infence; raw.append(ln); continue
        if infence:
            raw.append(ln)
            t = clean_text(ln)
            if t: items.append(('CODE', t))
            continue
        if not s: continue
        raw.append(ln)
        for c in re.finditer(r'<Callout[^>]*\bkind="([^"]+)"', s):
            items.append(('CALLOUT', c.group(1).lower()))
        for e in re.finditer(r'<(?:Expandable|Accordion)[^>]*\btitle="([^"]*)"', s):
            items.append(('ACCORDION', clean_text(e.group(1))))
        for t_ in re.finditer(r'<Tab\b[^>]*\btitle="([^"]*)"', s):
            items.append(('TAB', clean_text(t_.group(1))))
        for st in re.finditer(r'<(?:Step|Card|BoardCard)[^>]*\btitle="([^"]*)"', s):
            items.append(('TEXT', clean_text(st.group(1))))
        for cap in re.finditer(r'<(?:Image|img|Video|Iframe)[^>]*\bcaption="([^"]+)"', s):
            t = clean_text(cap.group(1))
            if t: items.append(('TEXT', t))
        for im in re.finditer(r'<(?:Image|img|Video|Iframe)[^>]*\bsrc="([^"]+)"', s):
            u = im.group(1); k = imgkey(u)
            if k == '__data__': continue
            items.append(('MEDIA' if is_video(u) or '<Video' in s or '<Iframe' in s else 'IMG', k))
        for im in re.finditer(r'!\[[^\]]*\]\((' + PAREN + r')\)', s):
            k = imgkey(im.group(1))
            if k != '__data__': items.append(('IMG', k))
        # images demoted to a plain "[label](asset-url)" link (happens inside tables)
        for im in re.finditer(r'(?<!!)\[([^\]]*)\]\((' + PAREN + r')\)', s):
            url = im.group(2)
            if ASSET_HOST.match(url.strip()) and re.search(
                    r'\.(png|jpe?g|gif|webp|svg)(\?|$)', url.split('?')[0] + '?', re.I):
                k = imgkey(url)
                items.append(('IMG', k)); demoted.append(k)
        h = re.match(r'^(#{2,6})\s+(.*)$', s)
        if h:
            t = clean_text(h.group(2))
            if t: items.append(('H%d' % len(h.group(1)), t))
            continue
        if re.match(r'^</?[A-Z][A-Za-z]*[\s/>]', s) and not re.search(r'>[^<]*\w', s):
            continue
        if is_table_rule(s): continue
        for t in text_units(s):
            if t != 'View image': items.append(('TEXT', t))
    return fm, items, "\n".join(raw), demoted


def fold_splits(missing, mdx_texts, max_parts=5):
    """A source block the migration broke into consecutive mdx blocks (usually at a
    bold run) is a SPLIT, not a loss. Returns (still_missing, split_examples)."""
    joined, out, splits = " ".join(mdx_texts), [], []
    norm = lambda t: re.sub(r'\s+', ' ', t).strip()
    jn = norm(joined)
    for t in missing:
        tn = norm(t)
        if len(tn) >= 12 and tn in jn: splits.append(t)
        else: out.append(t)
    return out, splits


# Link targets the SOURCE points at that 404 on the live site: the source's own
# dead links. The migration retargeting them is a fix, not a loss.
_DEADLINK = None
def dead_target(slug):
    global _DEADLINK
    if _DEADLINK is None:
        _DEADLINK = {}
        fp = os.environ.get("LINKSTATUS", "")
        if os.path.exists(fp):
            for ln in open(fp):
                parts = ln.split()
                if len(parts) == 2: _DEADLINK[parts[0]] = parts[1]
    return _DEADLINK.get(slug) == "404"

# ------------------------------------------------------------------ compare
def seq_diff(a, b):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    miss, extra = [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ('delete','replace'): miss  += a[i1:i2]
        if tag in ('insert','replace'): extra += b[j1:j2]
    return miss, extra

def fetch(slug):
    p = os.path.join(CACHE, slug + ".md")
    return open(p, encoding="utf-8").read() if os.path.exists(p) and os.path.getsize(p) else None

def report(mdx_path):
    slug = os.path.basename(mdx_path)[:-4]
    res = {"slug": slug, "mdx": mdx_path, "status": "ok", "issues": [], "notes": []}
    web = fetch(slug)
    if web is None:
        res["status"] = "no-live-source"; return res
    wfm, witems, wraw = parse_web(web)
    mfm, mitems, mraw, demoted = parse_mdx(open(mdx_path, encoding="utf-8").read())
    sel = lambda it, ks: [v for k, v in it if k in ks]

    if clean_text(wfm.get("title","")) != clean_text(mfm.get("title","")):
        res["issues"].append("TITLE  web=%r mdx=%r" % (wfm.get("title"), mfm.get("title")))
    wd, md = clean_text(wfm.get("description","")), clean_text(mfm.get("description",""))
    if wd != md:
        res["issues"].append("DESC%s web=%r mdx=%r" % (
            "-TRUNCATED" if md and wd.startswith(md) else "", wfm.get("description"), mfm.get("description")))

    HK = {'H2','H3','H4','H5','H6'}
    wh   = [(k,v) for k,v in witems if k in HK]
    wtxt = sel(witems, {'TEXT'})
    macc = sel(mitems, {'ACCORDION'})
    wacc = sel(witems, {'ACCORDION'})

    # --- reconcile mdx accordions against web accordions / H4+ headings / plain text
    flat = 0
    for title in list(macc):
        if title in wacc: wacc.remove(title); macc.remove(title); continue
        hit = next((x for x in wh if x[0] in ('H3','H4','H5','H6')
                     and strip_num(x[1]) == strip_num(title)), None)
        if hit: wh.remove(hit); macc.remove(title); flat += 1; continue
        if title in wtxt: wtxt.remove(title); macc.remove(title); flat += 1
    if flat: res["notes"].append("%d accordion(s) flattened by the .md export" % flat)

    # --- reconcile mdx <Tab> titles: the .md export concatenates them into one line
    mtabs = sel(mitems, {'TAB'})
    tabflat = 0
    for t in list(mtabs):
        if t in wtxt: wtxt.remove(t); mtabs.remove(t); tabflat += 1
    for w in list(wtxt):
        joined = [t for t in mtabs if t and t in w]
        if joined and ''.join(joined) == w.replace(' ', '')[:0] + w and len(joined) > 1:
            pass
    # concatenated form, e.g. "Grid ViewList View"
    for w in list(wtxt):
        acc, rest = [], w
        for t in mtabs:
            if rest.startswith(t): acc.append(t); rest = rest[len(t):]
        if acc and not rest.strip():
            for t in acc: mtabs.remove(t)
            wtxt.remove(w); tabflat += len(acc)
    if tabflat: res["notes"].append("%d tab label(s) flattened by the .md export" % tabflat)

    for x in macc:  res["issues"].append("FAQ extra in mdx: %s" % x)
    for x in wacc:  res["issues"].append("FAQ missing in mdx: %s" % x)

    mh = [(k,v) for k,v in mitems if k in HK]
    miss, extra = seq_diff(wh, mh)
    hashdrop = 0
    for x in list(miss):
        if '#' in x[1]:
            twin = (x[0], x[1].replace('#', ''))
            if twin in extra:
                miss.remove(x); extra.remove(twin); hashdrop += 1
    if hashdrop:
        res["issues"].append("HEADING-HASH-DROPPED x%d: '#N:' numbering lost its '#' (e.g. %s)"
                             % (hashdrop, [v for _, v in mh][:2]))
    for x in miss:  res["issues"].append("HEADING missing in mdx: %s %s" % x)
    for x in extra: res["issues"].append("HEADING extra in mdx:   %s %s" % x)

    wi, mi = sel(witems, {'IMG'}), sel(mitems, {'IMG'})
    miss, extra = seq_diff(wi, mi)
    if len(wi) != len(mi): res["issues"].append("IMAGE count web=%d mdx=%d" % (len(wi), len(mi)))
    for x in miss:  res["issues"].append("IMAGE missing in mdx: %s" % x)
    for x in extra: res["issues"].append("IMAGE extra in mdx:   %s" % x)
    mmedia = sel(mitems, {'MEDIA'})
    if mmedia:
        blob = export_blob(slug)
        if blob is not None:
            absent = [k for k in mmedia if k not in blob[1]]
            if absent: res["issues"].append("MEDIA not found in source export: %s" % ", ".join(absent[:5]))
    if demoted:
        res["notes"].append("%d image(s) rendered as '[View image]' links instead of images: %s"
                            % (len(demoted), ", ".join(sorted(set(demoted))[:6])))

    wc, mc = sel(witems, {'CALLOUT'}), sel(mitems, {'CALLOUT'})
    if wc != mc:
        exp = os.path.join(EXPORT, slug + ".html")
        n = len(re.findall(r'<section class="\w+Box"', open(exp, encoding="utf-8", errors="replace").read())) \
            if os.path.exists(exp) else 0
        if n and len(mc) - len(wc) == n:
            res["notes"].append("%d callout(s) flattened by the .md export - mdx is correct" % n)
        else:
            res["issues"].append("CALLOUT kinds web=%s mdx=%s" % (wc, mc))

    wl = sorted({linkkey(u) for u in links_of(wraw)})
    ml = sorted({linkkey(u) for u in links_of(mraw)})
    deadfix, renamed = 0, 0
    ml_pages = {u.split('#')[0] for u in ml}
    for x in [u for u in wl if u not in ml]:
        m = re.match(r'^internal:([a-z0-9._-]+)', x)
        if m and dead_target(m.group(1)): deadfix += 1; continue
        if '#' in x and x.split('#')[0] in ml_pages: renamed += 1; continue
        res["issues"].append("LINK missing in mdx: %s" % x)
    if renamed:
        res["issues"].append("ANCHOR-RENAMED x%d: same target page, different #fragment "
                             "(resolves locally)" % renamed)
    if deadfix:
        res["notes"].append("%d source link(s) pointed at pages that 404 on the live site; "
                            "the migration retargeted them" % deadfix)
    wl_pages = {u.split('#')[0] for u in wl}
    extras = [u for u in ml if u not in wl
              and not ('#' in u and u.split('#')[0] in wl_pages)]
    if deadfix: extras = extras[deadfix:]
    for x in extras: res["issues"].append("LINK extra in mdx:   %s" % x)

    miss, extra = seq_diff(sel(witems,{'CODE'}), sel(mitems,{'CODE'}))
    for x in miss:  res["issues"].append("CODE missing in mdx: %s" % x[:160])
    for x in extra: res["issues"].append("CODE extra in mdx:   %s" % x[:160])

    mtxt = sel(mitems, {'TEXT'})
    miss, extra = seq_diff(wtxt, mtxt)
    # whitespace-only corruption: a space lost where a bold/inline run ended
    squash = lambda t: re.sub(r'[^a-z0-9]', '', t.lower())
    ws = 0
    for a in list(miss):
        twin = next((b for b in extra if squash(b) == squash(a) and b != a), None)
        if twin is not None:
            miss.remove(a); extra.remove(twin); ws += 1
    if ws:
        res["issues"].append("SPACING x%d: text identical except lost/added whitespace "
                             "at a formatting boundary" % ws)
    miss, splits = fold_splits(miss, mtxt)
    if splits:
        res["issues"].append("TEXT-SPLIT x%d: source paragraph broken into separate blocks "
                             "(e.g. %r)" % (len(splits), splits[0][:110]))
    for x in miss:  res["issues"].append("TEXT missing in mdx: %s" % x[:200])
    for x in extra: res["issues"].append("TEXT extra in mdx:   %s" % x[:200])

    res["counts"] = {"web_text": len(wtxt), "mdx_text": len(sel(mitems,{'TEXT'})),
                     "web_img": len(wi), "mdx_img": len(mi),
                     "web_head": len(wh), "mdx_head": len([1 for k,_ in mitems if k in HK])}
    # The migration was built from the Aug-28 export, so separate "the live page
    # changed since then" (drift) from "the migration lost something" (a defect):
    #   missing in mdx + NOT in export  -> live page gained it after the export
    #   extra in mdx   + IS  in export  -> live page dropped it after the export
    kept, drift = [], 0
    for i in res["issues"]:
        m = re.match(r'^(TEXT|HEADING|IMAGE|FAQ) (missing|extra) in mdx: +(.*)$', i)
        if m:
            kind, direction, payload = m.group(1), m.group(2), m.group(3)
            probe = payload.split(" ", 1)[-1] if kind == "HEADING" else payload
            hit = in_export(slug, probe.strip(), "img" if kind == "IMAGE" else "text")
            if (direction == "missing" and hit is False) or (direction == "extra" and hit is True):
                drift += 1; continue
        kept.append(i)
    # page-level: how much of the live page still matches the export at all
    live_txt = [t for t in wtxt if len(t) >= 6]
    probes = live_txt[:80]
    hits = [in_export(slug, t) for t in probes]
    known = [h for h in hits if h is not None]
    match = (sum(1 for h in known if h) / len(known)) if known else 1.0
    if known and match < 0.75:
        res["source_changed"] = round(match, 2)
        res["notes"].append("live page only %d%% matches the Aug-28 export it was migrated "
                            "from - source rewritten since" % round(match * 100))
    if drift:
        res["notes"].append("%d item(s) reconciled as post-export source drift" % drift)
    res["issues"] = kept
    if res["issues"]: res["status"] = "diff"
    return res

if __name__ == "__main__":
    out = [report(p) for p in sys.argv[1:]]
    if os.environ.get("JSON"): print(json.dumps(out, indent=1, ensure_ascii=False))
    else:
        for r in out:
            print("="*78); print("%s  [%s]  %s" % (r["slug"], r["status"], r["mdx"]))
            print("   https://help.scrut.io/docs/%s" % r["slug"])
            if r.get("counts"): print("   counts:", r["counts"])
            for n in r["notes"]:  print("   ~ " + n)
            for i in r["issues"]: print("   - " + i)
            if not r["issues"]: print("   no differences found")
