#!/usr/bin/env python3
"""Validate every internal link in the migrated docs: does the target page exist,
and does the #anchor resolve to a real heading / expandable on that page?"""
import os, re, sys, json, glob

def slugify(t):
    t = re.sub(r'`|\*\*|__', '', t)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = t.lower().replace("'", "").replace('’', '')
    t = re.sub(r'[^a-z0-9\s-]', '', t)
    return re.sub(r'\s+', '-', t.strip())

pages, anchors = {}, {}
for f in glob.glob('docs/**/*.mdx', recursive=True):
    route = '/' + f[:-4]                       # docs/a/b -> /docs/a/b
    slug = os.path.basename(f)[:-4]
    pages[route] = f; pages.setdefault(slug, f)
    a = set()
    for line in open(f, encoding='utf-8'):
        h = re.match(r'^(#{2,6})\s+(.*)$', line.strip())
        if h: a.add(slugify(h.group(2)))
        for m in re.finditer(r'<(?:Expandable|Accordion|Step|Tab)[^>]*\btitle="([^"]*)"', line):
            a.add(slugify(m.group(1)))
    anchors[f] = a

bad = []
for f in sorted(glob.glob('docs/**/*.mdx', recursive=True)):
    src = open(f, encoding='utf-8').read()
    for m in re.finditer(r'\]\((/docs/[^)\s]*)\)', src):
        target = m.group(1)
        path, _, frag = target.partition('#')
        path = path.rstrip('/')
        tf = pages.get(path) or pages.get(path.split('/')[-1])
        if not tf:
            bad.append((f, target, 'target page does not exist')); continue
        if frag and frag not in anchors[tf]:
            bad.append((f, target, 'anchor not found in ' + tf))
print(json.dumps(bad, indent=1))
