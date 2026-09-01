#!/usr/bin/env python3
"""Tier B: pages that exist only in the Aug-28 Document360 export (404 on the live
site). Ground truth is the export HTML itself."""
import sys, os, re, json, difflib
from html.parser import HTMLParser
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compare2 import (clean_text, imgkey, is_video, seq_diff, parse_mdx,
                      frontmatter, EXPORT, fold_splits, strip_num)

SKIP  = {'script','style','svg','noscript'}
HEAD  = {'h1','h2','h3','h4','h5','h6'}
BLOCK = {'p','li','h1','h2','h3','h4','h5','h6','td','th','pre','blockquote','div','figcaption','summary','section'}
COLOR = {'ddf7ff':'info','fdf2ce':'alert','f9e2e4':'danger','c4f2d4':'success',
         '221,247,255':'info','253,242,206':'alert','249,226,228':'danger','196,242,212':'success'}

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items, self.buf, self.cur, self.skip = [], [], 'P', 0
    def flush(self):
        t = clean_text(''.join(self.buf)); self.buf = []
        if t: self.items.append((self.cur, t))
        self.cur = 'P'
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in SKIP: self.skip += 1; return
        if self.skip: return
        if tag in ('img','video','source','iframe'):
            u = a.get('src') or ''
            if u:
                k = imgkey(u)
                if k != '__data__': self.items.append(('MEDIA' if is_video(u) else 'IMG', k))
            return
        if tag == 'br': self.buf.append(' '); return
        if tag == 'a' and a.get('href'): self.items.append(('LINK', a['href']))
        if tag in ('blockquote','section'):
            self.flush()
            st = (a.get('style') or '') + ' ' + (a.get('class') or '') + ' ' + (a.get('data-background') or '')
            kind = None
            for key, v in COLOR.items():
                if key in st.replace('#','').replace(' ',''): kind = v; break
            if kind is None and 'infoBox' in st: kind = 'info'
            if kind is None and 'warningBox' in st: kind = 'alert'
            if kind: self.items.append(('CALLOUT', kind))
            return
        if tag in BLOCK:
            self.flush()
            self.cur = tag.upper() if tag in HEAD else ('CELL' if tag in ('td','th') else 'P')
    def handle_startendtag(self, tag, attrs): self.handle_starttag(tag, attrs)
    def handle_endtag(self, tag):
        if tag in SKIP: self.skip = max(0, self.skip-1); return
        if self.skip: return
        if tag in BLOCK: self.flush()
    def handle_data(self, d):
        if not self.skip: self.buf.append(d)

def parse_export(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    title = (re.search(r'^## title:[ \t]*(.*)$', raw, re.M) or [None, ''])[1].strip()
    desc  = (re.search(r'^## description:[ \t]*(.*)$', raw, re.M) or [None, ''])[1].strip()
    raw = re.sub(r'<!--.*?-->', ' ', raw, flags=re.S)
    p = P(); p.feed(raw); p.flush()
    return {'title': title, 'description': desc}, p.items

def report(mdx_path):
    slug = os.path.basename(mdx_path)[:-4]
    res = {"slug": slug, "mdx": mdx_path, "status": "ok", "issues": [], "notes": [], "tier": "export"}
    exp = os.path.join(EXPORT, slug + ".html")
    if not os.path.exists(exp):
        res["status"] = "no-source"; res["issues"].append("no live page and no export copy"); return res
    efm, eitems = parse_export(exp)
    mfm, mitems, mraw, demoted = parse_mdx(open(mdx_path, encoding="utf-8").read())
    sel = lambda it, ks: [v for k, v in it if k in ks]

    if clean_text(efm['title']) != clean_text(mfm.get('title','')):
        res["issues"].append("TITLE  export=%r mdx=%r" % (efm['title'], mfm.get('title')))
    ed, md = clean_text(efm['description']), clean_text(mfm.get('description',''))
    if ed != md:
        res["issues"].append("DESC%s export=%r mdx=%r" % ("-TRUNCATED" if md and ed.startswith(md) else "", efm['description'], mfm.get('description')))

    HK = {'H2','H3','H4','H5','H6'}
    eh = [(k,v) for k,v in eitems if k in HK]
    mh = [(k,v) for k,v in mitems if k in HK]
    # mdx <Expandable> may carry an export heading's text
    macc = {strip_num(t) for t in sel(mitems, {'ACCORDION'})} | {strip_num(t) for t in sel(mitems, {'TEXT'})}
    eh = [x for x in eh if strip_num(x[1]) not in macc]
    mh = [x for x in mh if strip_num(x[1]) not in
          {strip_num(v) for k, v in eitems if k in ('P', 'CELL')}]
    miss, extra = seq_diff(eh, mh)
    hd = 0
    for x in list(miss):
        if '#' in x[1] and (x[0], x[1].replace('#','')) in extra:
            miss.remove(x); extra.remove((x[0], x[1].replace('#',''))); hd += 1
    if hd: res["issues"].append("HEADING-HASH-DROPPED x%d" % hd)
    for x in miss:  res["issues"].append("HEADING missing in mdx: %s %s" % x)
    for x in extra: res["issues"].append("HEADING extra in mdx:   %s %s" % x)

    ei = sel(eitems, {'IMG'}); mi = sel(mitems, {'IMG'})
    if len(ei) != len(mi): res["issues"].append("IMAGE count export=%d mdx=%d" % (len(ei), len(mi)))
    miss, extra = seq_diff(ei, mi)
    for x in miss:  res["issues"].append("IMAGE missing in mdx: %s" % x)
    for x in extra: res["issues"].append("IMAGE extra in mdx:   %s" % x)
    if demoted: res["notes"].append("%d image(s) demoted to text links" % len(demoted))

    ec, mc = sel(eitems, {'CALLOUT'}), sel(mitems, {'CALLOUT'})
    if ec != mc: res["issues"].append("CALLOUT export=%s mdx=%s" % (ec, mc))

    et = [v for k, v in eitems if k in ('P','CELL')]
    mt = sel(mitems, {'TEXT'}) + sel(mitems, {'ACCORDION'})
    et_pool = list(et)
    for t in mt:
        if t in et_pool: et_pool.remove(t)
    et_pool, splits = fold_splits(et_pool, mt)
    if splits:
        res["issues"].append("TEXT-SPLIT x%d: source paragraph broken into separate blocks "
                             "(e.g. %r)" % (len(splits), splits[0][:110]))
    lost = [t for t in et_pool if len(t) >= 12]
    for x in lost[:40]: res["issues"].append("TEXT missing in mdx: %s" % x[:180])
    if len(lost) > 40: res["issues"].append("... %d more missing text blocks" % (len(lost)-40))

    res["counts"] = {"export_text": len(et), "mdx_text": len(mt),
                     "export_img": len(ei), "mdx_img": len(mi)}
    if res["issues"]: res["status"] = "diff"
    return res

if __name__ == "__main__":
    out = [report(p) for p in sys.argv[1:]]
    if os.environ.get("JSON"): print(json.dumps(out, indent=1, ensure_ascii=False))
    else:
        for r in out:
            print("="*78); print("%s [%s] %s" % (r["slug"], r["status"], r["mdx"]))
            for n in r["notes"]:  print("   ~ "+n)
            for i in r["issues"]: print("   - "+i[:160])
            if not r["issues"]: print("   no differences found")
