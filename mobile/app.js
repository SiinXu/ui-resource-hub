/* UI Hub · Mobile topic. Reuses ../styles.css and the Hub's card markup; no styles of its own. */
(function(){
var I=window.MT_I18N, D=window.MT_DATA||[], LANG=window.__uhL||'zh-CN';
var CATS=['pattern','guide','kit','comp','motion','flow','store','asset','skill','web','inspo'], PLATS=['ios','android','rn','flutter','web','cross'];
D=D.map(function(x,k){return [x,k]}).sort(function(a,b){return (CATS.indexOf(a[0].cat)-CATS.indexOf(b[0].cat))||(a[1]-b[1])}).map(function(x){return x[0]});
var st={c:'',p:'',q:''}, PAGE=48, shown=PAGE;
function $(i){return document.getElementById(i)}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function t(k,v){var d=I[LANG]||I.en,s=d[k]!=null?d[k]:(I.en[k]!=null?I.en[k]:k);if(v)for(var x in v)s=s.replace('{'+x+'}',v[x]);return s}
function zh(){return LANG==='zh-CN'||LANG==='zh-TW'}
function note(i){return zh()?i.zh:i.en}
function host(u){try{var x=new URL(u);return x.hostname.replace(/^www\./,'')}catch(e){return u}}
var EXT='<svg viewBox="0 0 24 24"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>';
function meta(i){var o=['<span class="h">'+esc(i.x?'x.com/@'+i.x.handle:host(i.url))+'</span>'];
  if(i.x)o.push('<span>♥ '+i.x.likes.toLocaleString('en-US')+' '+esc(t('likes'))+'</span>');
  if(i.lic)o.push('<span>'+esc(i.lic)+'</span>');
  o.push('<span>'+esc(t('p_'+i.plat))+'</span>');
  return '<p class="cu">'+o.join('<i aria-hidden="true">·</i>')+'</p>'}
function card(i){return '<article class="card" data-url="'+esc(i.url)+'"><div class="cm"><div class="th"><img src="shots/'+esc(i.id)+'.webp" alt="'+esc(i.name)+'" loading="lazy" width="800" height="500"></div></div>'+
  '<div class="cb"><h3>'+esc(i.name)+'</h3>'+meta(i)+'<p class="note">'+esc(note(i))+'</p>'+
  '<div class="cbar"><a class="cpb" href="'+esc(i.url)+'" target="_blank" rel="noopener">'+EXT+'<span>'+esc(t('open'))+'</span></a><span class="sp"></span></div></div></article>'}
function match(i,ign){if(ign!=='c'&&st.c&&i.cat!==st.c)return false;if(ign!=='p'&&st.p&&i.plat!==st.p)return false;
  if(st.q){var h=(i.name+' '+i.url+' '+note(i)+' '+t('c_'+i.cat)+' '+t('p_'+i.plat)+(i.x?' @'+i.x.handle:'')).toLowerCase();if(h.indexOf(st.q)<0)return false}return true}
function cnt(f,ign){var c={};D.forEach(function(i){if(match(i,ign))c[i[f]]=(c[i[f]]||0)+1});return c}
function chips(){var cc=cnt('cat','c'),n=0;for(var k in cc)n+=cc[k];
  $('chips').innerHTML='<button class="chip'+(st.c?'':' on')+'" data-c="">'+esc(t('all'))+'<small>'+n+'</small></button>'+CATS.filter(function(k){return cc[k]||st.c===k}).map(function(k){return '<button class="chip'+(st.c===k?' on':'')+'" data-c="'+k+'">'+esc(t('c_'+k))+'<small>'+(cc[k]||0)+'</small></button>'}).join('');
  var pc=cnt('plat','p');
  $('platChips').innerHTML='<button class="chip c'+(st.p?'':' on')+'" data-p="">'+esc(t('plat_all'))+'</button>'+PLATS.filter(function(k){return pc[k]||st.p===k}).map(function(k){return '<button class="chip c'+(st.p===k?' on':'')+'" data-p="'+k+'">'+esc(t('p_'+k))+'<small>'+(pc[k]||0)+'</small></button>'}).join('')}
function render(){var L=D.filter(function(i){return match(i)});chips();
  $('grid').innerHTML=L.slice(0,shown).map(card).join('');
  $('meta').textContent=t('meta',{n:L.length});
  var m=$('gridMore');m.hidden=L.length<=shown;m.textContent='+ '+Math.min(PAGE,L.length-shown);
  var e=$('empty');e.hidden=L.length>0;e.textContent=t('empty')}
function statics(){document.documentElement.lang=LANG;document.title=t('title')+' · UI Hub';
  document.querySelectorAll('[data-t]').forEach(function(el){el.textContent=t(el.dataset.t)});
  document.querySelectorAll('[data-ta]').forEach(function(el){el.setAttribute('aria-label',t(el.dataset.ta))});
  $('lede').textContent=t('lede',{n:D.length.toLocaleString('en-US')});$('q').placeholder=t('search');
  var cs={};D.forEach(function(i){cs[i.cat]=1});var xn=D.filter(function(i){return i.x}).length;
  $('hstats').innerHTML=[[D.length,t('st_items')],[Object.keys(cs).length,t('st_cats')],[xn,t('st_x')],[I.langs.length,t('st_lang')]].map(function(r){return '<div><dt>'+r[0]+'</dt><dd>'+esc(r[1])+'</dd></div>'}).join('');
  $('langSel').value=LANG}
var sel=$('langSel');sel.innerHTML=I.langs.map(function(l){return '<option value="'+l[0]+'">'+l[1]+'</option>'}).join('');
sel.addEventListener('change',function(){LANG=sel.value;try{localStorage.setItem('uihub.lang',LANG)}catch(e){}statics();render()});
$('themeBtn').addEventListener('click',function(){var r=document.documentElement,n=r.dataset.theme==='dark'?'light':'dark';r.dataset.theme=n;try{localStorage.setItem('uihub.theme5',n)}catch(e){}});
$('q').addEventListener('input',function(e){st.q=e.target.value.trim().toLowerCase();shown=PAGE;render()});
document.addEventListener('keydown',function(e){if(e.key==='/'&&document.activeElement!==$('q')){e.preventDefault();$('q').focus()}});
$('gridMore').addEventListener('click',function(){shown+=PAGE;render()});
document.addEventListener('click',function(e){var b=e.target.closest('.chip');if(b){if(b.dataset.c!=null)st.c=st.c===b.dataset.c?'':b.dataset.c;if(b.dataset.p!=null)st.p=st.p===b.dataset.p?'':b.dataset.p;shown=PAGE;render();return}
  var c=e.target.closest('article.card');if(c&&!e.target.closest('a'))window.open(c.dataset.url,'_blank','noopener')});
statics();render();
})();
