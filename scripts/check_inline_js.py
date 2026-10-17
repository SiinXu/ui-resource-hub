"""Syntax-check every inline <script> in index.html with `node --check` (a parse error in the loader leaves the page without data/featured cards)."""
import os, re, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
bad = 0
for n, (attrs, body) in enumerate(re.findall(r'<script([^>]*)>(.*?)</script>', html, re.S)):
    if 'src=' in attrs or 'ld+json' in attrs or not body.strip():
        continue
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as f:
        f.write(body)
    r = subprocess.run(['node', '--check', f.name], capture_output=True, text=True)
    os.unlink(f.name)
    if r.returncode:
        bad += 1; print(f'inline script #{n}: SYNTAX ERROR\n{r.stderr}')
for js in ('app.js',):
    r = subprocess.run(['node', '--check', os.path.join(ROOT, js)], capture_output=True, text=True)
    if r.returncode: bad += 1; print(js, r.stderr)
print('ok' if not bad else f'{bad} error(s)'); sys.exit(1 if bad else 0)
