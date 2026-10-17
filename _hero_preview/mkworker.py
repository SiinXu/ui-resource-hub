"""Emit a Cloudflare Worker (module) for preview a|b: serves the preview index.html, styles.hx.css and hero/*.webp from embedded copies; everything else proxies to the live GitHub Pages origin (same CDN as ui.incidental.site)."""
import base64, json, os, sys
key = sys.argv[1]; R = f'/workspace/uihub-hero/{key}'
files = {'/index.html': ('text/html; charset=utf-8', open(f'{R}/index.html', 'rb').read()),
         '/styles.hx.css': ('text/css; charset=utf-8', open(f'{R}/styles.hx.css', 'rb').read())}
for f in sorted(os.listdir(f'{R}/hero')):
    files['/hero/' + f] = ('image/webp', open(f'{R}/hero/{f}', 'rb').read())
emb = {p: [ct, base64.b64encode(b).decode()] for p, (ct, b) in files.items()}
js = """const F=%s;
const ORIGIN='https://siinxu.github.io/ui-resource-hub';
function b64(s){const b=atob(s),u=new Uint8Array(b.length);for(let i=0;i<b.length;i++)u[i]=b.charCodeAt(i);return u}
export default{async fetch(req){const u=new URL(req.url);let p=u.pathname;if(p==='/')p='/index.html';
 const e=F[p];if(e){const cc=p.startsWith('/hero/')||p==='/styles.hx.css'?'public, max-age=3600':'public, max-age=60';
  return new Response(b64(e[1]),{headers:{'content-type':e[0],'cache-control':cc,'x-robots-tag':'noindex, nofollow','x-uihub-preview':'%s'}})}
 const r=await fetch(ORIGIN+u.pathname+u.search,{headers:{'user-agent':req.headers.get('user-agent')||'',accept:req.headers.get('accept')||'*/*'},redirect:'manual',cf:{cacheEverything:true,cacheTtl:300}});
 const h=new Headers(r.headers);const loc=h.get('location');if(loc&&loc.startsWith(ORIGIN))h.set('location',loc.slice(ORIGIN.length)||'/');
 h.set('x-robots-tag','noindex, nofollow');return new Response(r.body,{status:r.status,headers:h})}};
""" % (json.dumps(emb), key)
open(f'/workspace/uihub-hero/worker-{key}.mjs', 'w').write(js)
print(key, len(js), 'bytes')
