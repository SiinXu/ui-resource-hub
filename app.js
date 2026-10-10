(function(){
'use strict';
var D = window.UI_DATA || {items:[],guides:[]}, M = window.UI_MEDIA || {};
var ITEMS = D.items, BY = {};
ITEMS.forEach(function(i){BY[i.id]=i});
var TYPES = [['all','全部'],['component','组件'],['effect','特效'],['skill','Skill'],['inspiration','灵感'],['template','模板'],['generator','AI 生成'],['guide','思路']];
var TNAME = {prompt:'Prompt'}; TYPES.forEach(function(t){TNAME[t[0]]=t[1]});
var PRICE = {free:'免费',paid:'付费',freemium:'免费+Pro'};
var VISUAL = {component:1,effect:1,template:1,generator:1,inspiration:1,guide:1};

/* ---------- 精选：live = 原站页面 iframe 嵌入（裁出演示区域） ---------- */
// w: iframe 的虚拟宽度；top/view: 演示区域在页面里的纵向位置和高度（像素，按 w 宽度时）
var LIB = 'https://libraries.dev/';
function lib(p){return {src:LIB+p+'.html',w:480,top:375,view:440}}
var FEAT = [
  {id:'metal-jakubantalik-com', live:{src:'https://metal.jakubantalik.com',w:420,top:60,view:340}, poster:'previews/live-metal.webp', title:'Liquid Metal 液态金属', hint:'鼠标移到按钮上看金属流动', big:1},
  {id:'libraries-dev', live:lib('voice'), poster:'previews/live-voice.webp', title:'Voice 语音光效', sub:'Libraries.dev · 9 月新组件', hint:'在原站点麦克风按钮，说话时光会升起'},
  {id:'orbs-jakubantalik-com', live:lib('orbs'), poster:'previews/live-orbs.webp', title:'Thinking Orbs 思考光球', sub:'原站已迁到 libraries.dev，嵌入的是新地址'},
  {id:'beam-jakubantalik-com', live:lib('beam'), poster:'previews/live-beam.webp', title:'Border Beam 流光边框', sub:'原站已迁到 libraries.dev，嵌入的是新地址'},
  {id:'shaders-paper-design-liquid-metal', live:{src:'https://shaders.paper.design/liquid-metal',w:420,top:160,view:300}, poster:'previews/live-paper.webp', title:'Paper Shaders 液态金属', hint:'原站右侧可以调参数'},
    {id:'ui-aceternity-com',wide:1},{id:'magicui-design'},{id:'reactbits-dev'},{id:'animate-ui-com'},{id:'21st-dev'},{id:'coss-com-ui'},{id:'www-heroui-com'}
];
var MORE = ['motion-primitives-com','www-beautifului-dev','www-shadcnblocks-com','reactbits-dev-animations-metallic-paint'];
var LIVE = {}; FEAT.forEach(function(f){if(f.live)LIVE[f.id]=f});
// Libraries.dev 详情页里可以切换的全部效果（都是 libraries.dev 自己的页面，不是新资源）
var LIBTABS = [['voice','Voice 语音光效'],['orbs','Thinking orbs'],['beam','Border beam'],['metal','Metal 液态金属'],['gooey','Gooey 黏液'],['image','Image 生成加载'],['bots','Bot avatars']];

var LS = {
  get:function(k,d){try{var v=localStorage.getItem('uihub.'+k);return v?JSON.parse(v):d}catch(e){return d}},
  set:function(k,v){try{localStorage.setItem('uihub.'+k,JSON.stringify(v))}catch(e){}}
};
var favs = LS.get('favs',{}), utags = LS.get('tags',{});
var state = {type:'all', q:'', tag:'', view:'home'};
var $ = function(id){return document.getElementById(id)};
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function host(u){try{return new URL(u).hostname.replace(/^www\./,'')}catch(e){return u}}
function hash(s){var h=0;for(var i=0;i<s.length;i++)h=(h*31+s.charCodeAt(i))|0;return Math.abs(h)}
function tagsOf(i){return i.tags.concat(utags[i.id]||[])}
function shown(n){return (n||'').replace(/（@[A-Za-z0-9_]+）$/,'')}
function canFrame(i){return !!(LIVE[i.id]||(M[i.id]&&M[i.id].frame))}
var IC = {
  ext:'<svg viewBox="0 0 24 24"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>',
  copy:'<svg viewBox="0 0 24 24"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v1"/></svg>',
  star:'<svg viewBox="0 0 24 24"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/></svg>',
  play:'<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>',
  full:'<svg viewBox="0 0 24 24"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg>',
  spark:'<svg viewBox="0 0 24 24"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/></svg>',
  x:'<svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></svg>'
};
function favBtn(i,cls){return '<button class="ib fav'+(favs[i.id]?' on':'')+(cls?' '+cls:'')+'" data-fav="'+i.id+'" aria-label="收藏">'+IC.star+'</button>'}

/* ---------- 预览区 ---------- */
function mono(i){ // 没有图片时的字母封面
  var h=hash(i.id), a=h%360;
  return '<div class="mono" style="--h:'+a+'"><span>'+esc(shown(i.name).replace(/^[^A-Za-z\u4e00-\u9fa5]+/,'').slice(0,2))+'</span></div>';
}
function srcTag(i,live){
  if(live)return '<span class="tag-lv">真实预览</span>';
  var m=M[i.id]; if(!m||!m.img)return '';
  return '<span class="tag-pv">'+(m.src==='shot'?'原站截图':'原站封面')+'</span>';
}
function liveBox(f,opts){ // 裁剪窗口：iframe 懒加载，加载前显示截图
  opts=opts||{};
  var L=f.live;
  return '<div class="live" data-live="'+esc(L.src)+'" data-w="'+L.w+'" data-top="'+L.top+'" data-view="'+L.view+'"'+(opts.eager?' data-eager="1"':'')+'>'+
    '<img class="poster" src="'+f.poster+'" alt="" loading="lazy">'+
    '<div class="ifw"></div><div class="shield" data-play="'+f.id+'"><span class="tap">'+IC.play+'点开试玩</span></div>'+
    '<span class="ld"><i></i>正在连接原站…</span></div>';
}

/* ---------- 精选 ---------- */
function featCard(f,k){
  var i=BY[f.id]; if(!i)return '';
  var m=M[i.id]||{}, live=!!f.live;
  var media = live ? liveBox(f) : (m.img?'<img class="poster kb" src="'+m.img+'" alt="'+esc(i.name)+' 预览" loading="'+(k<8?'eager':'lazy')+'">':mono(i));
  return '<article class="fc'+(f.big?' big':'')+(f.wide?' wide':'')+(live?' is-live':'')+'" style="--i:'+k+'">'+
    '<div class="fm" '+(live?'':'data-open="'+i.id+'"')+'>'+media+'<div class="ftop">'+srcTag(i,live)+favBtn(i)+'</div></div>'+
    '<div class="fb"><div class="ft"><h3 data-open="'+i.id+'">'+esc(f.title||shown(i.name))+'</h3>'+
    '<p>'+esc(f.sub||shown(i.note)||host(i.url))+'</p>'+(f.hint?'<p class="hint">'+esc(f.hint)+'</p>':'')+'</div>'+
    '<div class="fa">'+(live?'<button class="b pri" data-play="'+i.id+'">'+IC.full+'全屏试玩</button><button class="b ghost" data-open="'+i.id+'">详情</button>'+
      '<a class="b ghost sq" href="'+esc(f.live.src)+'" target="_blank" rel="noopener noreferrer" aria-label="在原站预览" title="在原站预览">'+IC.ext+'</a>'
     :'<a class="b pri" href="'+esc(i.url)+'" target="_blank" rel="noopener noreferrer">在原站预览'+IC.ext+'</a><button class="b ghost" data-open="'+i.id+'">详情</button>')+
    '</div></div></article>';
}
function renderFeat(){
  $('feat').innerHTML = FEAT.map(featCard).join('');
  $('more').innerHTML = '<span class="ml">还值得看</span>'+MORE.map(function(id){var i=BY[id],m=M[id]||{};return '<button class="mc" data-open="'+id+'">'+(m.img?'<img src="'+m.img+'" alt="" loading="lazy">':mono(i))+'<span><b>'+esc(shown(i.name))+'</b><small>'+esc(shown(i.note))+'</small></span></button>'}).join('');
  observeLive($('feat'));
}

/* ---------- 目录卡片 ---------- */
function card(i){
  var m=M[i.id]||{}, live=LIVE[i.id];
  var price = PRICE[i.pricing]?'<span class="pill '+i.pricing+'">'+PRICE[i.pricing]+'</span>':'';
  if(!VISUAL[i.type]){ // Skill / Prompt：排版卡片
    var parts=shown(i.name).split('/');
    return '<article class="card sk" data-open="'+i.id+'"><div class="skm"><div class="term"><i></i><i></i><i></i><span>SKILL.md</span></div>'+
      '<div class="skn"><small>'+esc(parts.length>1?parts[0]+' /':TNAME[i.type])+'</small><b>'+esc(parts[parts.length-1])+'</b></div></div>'+
      '<div class="cb"><p class="note">'+esc(shown(i.note)||host(i.url))+'</p><div class="row"><span class="tp">'+TNAME[i.type]+'</span>'+price+(i.source?'<span class="src">'+esc(i.source)+'</span>':'')+favBtn(i,'r')+'</div></div></article>';
  }
  var media = m.img?'<img src="'+(live?live.poster:m.img)+'" alt="" loading="lazy">':(live?'<img src="'+live.poster+'" alt="" loading="lazy">':mono(i));
  return '<article class="card" data-open="'+i.id+'"><div class="cm">'+media+
    '<div class="cmo">'+(canFrame(i)?'<span class="play-i">'+IC.play+'</span>':'')+'</div>'+
    '<div class="ctop">'+(live?'<span class="tag-lv">真实预览</span>':(canFrame(i)?'<span class="tag-fr">可嵌入试看</span>':srcTag(i)))+'</div></div>'+
    '<div class="cb"><h3>'+esc(shown(i.name))+'</h3><p class="note">'+esc(shown(i.note)||host(i.url))+'</p>'+
    '<div class="row"><span class="tp">'+TNAME[i.type]+'</span>'+price+(i.source?'<span class="src">'+esc(i.source)+'</span>':'')+favBtn(i,'r')+'</div></div></article>';
}
function match(i){
  if(state.view==='fav'&&!favs[i.id])return false;
  if(state.type!=='all'&&i.type!==state.type)return false;
  if(state.tag&&tagsOf(i).indexOf(state.tag)<0)return false;
  if(!state.q)return true;
  var hay=(i.name+' '+i.note+' '+i.url+' '+i.source+' '+i.section+' '+TNAME[i.type]+' '+tagsOf(i).join(' ')).toLowerCase();
  return state.q.toLowerCase().split(/\s+/).every(function(w){return hay.indexOf(w)>=0});
}
function renderChips(){
  var base = ITEMS.filter(function(i){return state.view!=='fav'||favs[i.id]});
  var html = TYPES.map(function(t){
    var n = t[0]==='all'?base.length:base.filter(function(i){return i.type===t[0]}).length;
    if(!n&&t[0]!=='all')return '';
    return '<button class="chip'+(state.type===t[0]?' on':'')+'" data-type="'+t[0]+'">'+t[1]+'<small>'+n+'</small></button>';
  }).join('');
  var tc={}; base.forEach(function(i){tagsOf(i).forEach(function(t){tc[t]=(tc[t]||0)+1})});
  var top=Object.keys(tc).sort(function(a,b){return tc[b]-tc[a]}).slice(0,12);
  if(state.tag&&top.indexOf(state.tag)<0)top.unshift(state.tag);
  html += '<span class="sep"></span>' + top.map(function(t){return '<button class="chip t'+(state.tag===t?' on':'')+'" data-tag="'+esc(t)+'">#'+esc(t)+'</button>'}).join('');
  $('chips').innerHTML = html;
}
function renderGrid(){
  var list = ITEMS.filter(match);
  // 有画面的排前面，Skill 排后面，组内保持原顺序
  list = list.map(function(i,k){return [VISUAL[i.type]?(M[i.id]&&M[i.id].img||LIVE[i.id]?0:1):2,k,i]}).sort(function(a,b){return a[0]-b[0]||a[1]-b[1]}).map(function(a){return a[2]});
  $('grid').innerHTML = list.map(card).join('');
  var fc=Object.keys(favs).length; $('favCnt').textContent=fc||'';
  var isFav=state.view==='fav';
  $('empty').hidden = !!list.length;
  $('empty').textContent = isFav&&!fc?'还没有收藏。点卡片右下角的星标就能收藏，只存在这台设备上。':'没有匹配的资源，换个关键词试试。';
  $('catTitle').textContent = isFav?'我的收藏':(state.q?'搜索结果':'全部资源');
  $('meta').textContent = list.length+' 个'+(list.length!==ITEMS.length?' / 共 '+ITEMS.length:'')+' · 有图的排在前面';
}
function renderGuides(){
  $('guideList').innerHTML = D.guides.map(function(g,gk){
    return '<div class="guide" id="g-'+g.id+'" style="--i:'+gk+'"><div class="gh"><span class="ge">'+g.emoji+'</span><div><h2>'+esc(g.title)+'</h2><p>'+esc(g.problem)+'</p></div></div><ol>'+
      g.picks.map(function(p){var i=BY[p.id],m=M[i.id]||{};return '<li data-open="'+i.id+'"><span class="gt">'+(m.img?'<img src="'+m.img+'" alt="" loading="lazy">':'<b>'+esc(shown(i.name).split('/').pop().slice(0,2))+'</b>')+'</span><div><b>'+esc(shown(i.name))+'</b><span class="tp">'+TNAME[i.type]+'</span><p>'+esc(p.why)+'</p></div></li>'}).join('')+'</ol></div>';
  }).join('');
}

/* ---------- iframe 实时预览 ---------- */
function fit(box){
  var w=+box.dataset.w, top=+box.dataset.top, view=+box.dataset.view, cw=box.clientWidth, ch=box.clientHeight;
  if(!cw||!ch)return;
  var s=Math.max(cw/w, ch/view), vis=ch/s;
  var off=top+Math.max(0,(view-vis)/2), fr=box.querySelector('iframe');
  if(fr){fr.style.width=w+'px';fr.style.height=(off+vis+40)+'px';fr.style.transform='translate('+((cw-w*s)/2)+'px,'+(-off*s)+'px) scale('+s+')'}
}
function loadLive(box){
  if(box.dataset.on)return; box.dataset.on='1';
  var fr=document.createElement('iframe');
  fr.src=box.dataset.live; fr.loading='eager'; fr.title='原站实时预览'; fr.referrerPolicy='no-referrer-when-downgrade';
  fr.setAttribute('allow','microphone; autoplay; clipboard-write'); fr.tabIndex=-1;
  box.querySelector('.ifw').appendChild(fr); fit(box); box.classList.add('loading');
  var to=setTimeout(function(){box.classList.add('slow')},12000);
  fr.addEventListener('load',function(){clearTimeout(to);setTimeout(function(){box.classList.remove('loading','slow');box.classList.add('ready')},900)});
}
function unloadLive(box){if(!box.dataset.on)return;delete box.dataset.on;box.querySelector('.ifw').innerHTML='';box.classList.remove('ready','loading','slow')}
var io = 'IntersectionObserver' in window ? new IntersectionObserver(function(es){
  es.forEach(function(e){ if(e.isIntersecting)loadLive(e.target); else if(!e.target.dataset.eager)unloadLive(e.target) });
},{rootMargin:'120px 0px',threshold:.2}) : null;
function observeLive(root){root.querySelectorAll('.live').forEach(function(b){if(io)io.observe(b);else loadLive(b)})}
var ro = 'ResizeObserver' in window ? new ResizeObserver(function(es){es.forEach(function(e){fit(e.target)})}) : null;
function track(root){root.querySelectorAll('.live,.site').forEach(function(b){ro&&ro.observe(b)})}

// 整页嵌入（详情页里用）：按宽度缩放原站页面
function siteBox(url){return '<div class="site" data-site="'+esc(url)+'"><div class="ifw"></div><span class="ld"><i></i>正在加载原站页面…</span></div>'}
function loadSite(box){
  var cw=box.clientWidth, vw=cw<640?Math.max(cw,375):1180, s=cw/vw, ch=box.clientHeight;
  var fr=document.createElement('iframe'); fr.src=box.dataset.site; fr.title='原站页面';
  fr.style.width=vw+'px'; fr.style.height=(ch/s)+'px'; fr.style.transform='scale('+s+')';
  box.querySelector('.ifw').appendChild(fr); box.classList.add('loading');
  var to=setTimeout(function(){box.classList.add('slow')},12000);
  fr.addEventListener('load',function(){clearTimeout(to);setTimeout(function(){box.classList.remove('loading','slow');box.classList.add('ready')},600)});
}

/* ---------- 详情 ---------- */
function promptFor(i){
  var n=shown(i.name);
  if(i.type==='skill')return '请帮我安装并使用「'+n+'」这个 Skill（'+i.url+'）。它的作用：'+(shown(i.note)||'见链接')+'。装好后，用它检查并改进我当前项目的界面：先列出你发现的问题，再逐条修改，改完告诉我改了哪些地方。';
  return '请参考「'+n+'」（'+i.url+'）的设计语言和交互，帮我做一个类似效果：\n- 我要做的是：【在这里写你的页面或组件，比如 AI 聊天输入框】\n- 参考它的：视觉风格、动效节奏、细节处理（'+(shown(i.note)||'见链接')+'）\n- 技术栈：React + Tailwind，动效用 CSS 或 Motion\n- 要求：深色和浅色都好看，手机上也能用，动效流畅不卡顿，不要直接照抄它的代码和文案';
}
function related(i){
  var mine=tagsOf(i);
  return ITEMS.filter(function(x){return x.type===i.type&&x.id!==i.id}).map(function(x){
    var s=0; tagsOf(x).forEach(function(t){if(mine.indexOf(t)>=0)s+=2}); if(x.section===i.section)s+=1; if(M[x.id]&&M[x.id].img)s+=.5; return [s,x];
  }).sort(function(a,b){return b[0]-a[0]}).slice(0,6).map(function(a){return a[1]});
}
function guidesFor(i){return D.guides.filter(function(g){return g.picks.some(function(p){return p.id===i.id})})}
function preview(i){
  var f=LIVE[i.id], m=M[i.id]||{};
  if(i.id==='libraries-dev'){
    return '<div class="pv-tabs" id="libTabs">'+LIBTABS.map(function(t,k){return '<button class="'+(k?'':'on')+'" data-lib="'+t[0]+'">'+t[1]+'</button>'}).join('')+'</div>'+
      '<div class="pvw big">'+liveBox({id:i.id,live:lib('voice'),poster:'previews/live-voice.webp'},{eager:1})+'<div class="pvtag"><span class="tag-lv">真实预览</span><span>原站页面嵌入，上方可切换 7 个效果</span></div></div>';
  }
  if(f)return '<div class="pvw big">'+liveBox(f,{eager:1})+'<div class="pvtag"><span class="tag-lv">真实预览</span><span>原站页面嵌入'+(f.sub&&/迁/.test(f.sub)?'（已迁到 libraries.dev）':'')+'</span></div></div>';
  if(m.frame)return '<div class="pvw big"><div class="site-wrap">'+(m.img?'<img class="poster" src="'+m.img+'" alt="">':mono(i))+
    '<button class="loadsite" data-site-load="'+esc(i.url)+'">'+IC.play+'<span>在这里加载原站页面<small>原站允许嵌入，缩小显示</small></span></button></div>'+
    '<div class="pvtag">'+srcTag(i)+'<span>'+(m.img?'先看封面，点按钮在这里打开原站':'点按钮在这里打开原站')+'</span></div></div>';
  if(m.img)return '<div class="pvw big"><img class="poster" src="'+m.img+'" alt="'+esc(i.name)+'"><div class="pvtag">'+srcTag(i)+'<span>原站不允许嵌入，完整效果去原站看</span></div></div>';
  if(VISUAL[i.type])return '<div class="pvw big">'+mono(i)+'<div class="pvtag"><span>暂无预览图，去原站看</span></div></div>';
  var parts=shown(i.name).split('/');
  return '<div class="pvw sk"><div class="term"><i></i><i></i><i></i><span>SKILL.md</span></div><div class="skn"><small>'+esc(parts.length>1?parts[0]+' /':TNAME[i.type])+'</small><b>'+esc(parts[parts.length-1])+'</b></div></div>';
}
function openSheet(id){
  var i=BY[id]; if(!i)return;
  var ut=utags[i.id]||[], gs=guidesFor(i), pr=promptFor(i), f=LIVE[i.id];
  $('sheet').innerHTML = '<div class="grab"></div><button class="ib close" data-close aria-label="关闭">'+IC.x+'</button>'+preview(i)+
   '<div class="sb"><div class="row">'+'<span class="tp">'+TNAME[i.type]+'</span>'+(PRICE[i.pricing]?'<span class="pill '+i.pricing+'">'+PRICE[i.pricing]+'</span>':'')+(i.source?'<span class="src">'+esc(i.source)+' 推荐</span>':'')+'</div>'+
   '<h2>'+esc(shown(i.name))+'</h2>'+(i.note?'<p class="lead">'+esc(i.note)+'</p>':'')+
   '<div class="acts"><a class="b pri" href="'+esc(i.url)+'" target="_blank" rel="noopener noreferrer">打开原站'+IC.ext+'</a>'+
   (f?'<button class="b ghost" data-play="'+i.id+'">'+IC.full+'全屏试玩</button>':'')+
   '<button class="b ghost" data-copy="'+esc(i.url)+'" data-msg="链接已复制">'+IC.copy+'复制链接</button>'+favBtn(i,'lg')+'</div>'+
   '<div class="prompt"><div class="ph"><span>'+IC.spark+'给 AI 的提示词</span><button class="b sm pri" data-copyp>'+IC.copy+'复制</button></div><pre>'+esc(pr)+'</pre></div>'+
   '<dl class="kv"><dt>网址</dt><dd class="u">'+esc(i.url)+'</dd><dt>分组</dt><dd>'+esc(i.sectionTitle)+(i.sectionDesc?'<span>'+esc(i.sectionDesc)+'</span>':'')+'</dd>'+
   (gs.length?'<dt>指南</dt><dd>'+gs.map(function(g){return '<a href="#/guides" data-g="'+g.id+'">'+g.emoji+' '+esc(g.title)+'</a>'}).join('')+'</dd>':'')+'</dl>'+
   '<h3>标签</h3><div class="tagrow">'+i.tags.map(function(t){return '<span class="tg">'+esc(t)+'</span>'}).join('')+
     ut.map(function(t,k){return '<span class="tg u">'+esc(t)+'<b data-rmtag="'+k+'">×</b></span>'}).join('')+'</div>'+
   '<form class="addtag" data-addtag="'+i.id+'"><input name="t" maxlength="16" placeholder="加个自己的标签，比如：下个项目用"><button class="b ghost sm">添加</button></form>'+
   '<h3>同类推荐</h3><div class="rel">'+related(i).map(function(x){var m=M[x.id]||{},lv=LIVE[x.id];return '<button data-open="'+x.id+'">'+(m.img||lv?'<img src="'+(lv?lv.poster:m.img)+'" alt="" loading="lazy">':'<span class="rm">'+esc(shown(x.name).split('/').pop().slice(0,2))+'</span>')+'<b>'+esc(shown(x.name))+'</b></button>'}).join('')+'</div></div>';
  $('sheet').dataset.id=i.id; $('sheet').dataset.prompt=pr;
  $('scrim').hidden=false; $('sheet').classList.add('open'); $('sheet').setAttribute('aria-hidden','false'); $('sheet').scrollTop=0;
  document.body.classList.add('lock');
  requestAnimationFrame(function(){var b=$('sheet').querySelector('.live');if(b){track($('sheet'));setTimeout(function(){loadLive(b)},280)}});
}
function closeSheet(){
  var s=$('sheet'); if(!s.classList.contains('open'))return;
  s.classList.remove('open'); $('scrim').hidden=true; s.setAttribute('aria-hidden','true'); document.body.classList.remove('lock');
  setTimeout(function(){if(!s.classList.contains('open'))s.innerHTML=''},350);
}
function playFull(id){
  var i=BY[id], f=LIVE[id]; if(!f)return;
  var src=f.live.src;
  if(id==='libraries-dev'){var on=document.querySelector('#libTabs .on');if(on)src=LIB+on.dataset.lib+'.html'}
  $('play').innerHTML='<div class="pbar"><span class="tag-lv">真实预览</span><b>'+esc(f.title||shown(i.name))+'</b><a class="b ghost sm" href="'+esc(src)+'" target="_blank" rel="noopener noreferrer">新窗口'+IC.ext+'</a><button class="ib" data-closeplay aria-label="关闭">'+IC.x+'</button></div><iframe src="'+esc(src)+'" title="原站实时预览" allow="microphone; autoplay; clipboard-write"></iframe>';
  $('play').hidden=false; document.body.classList.add('lock');
}
function closePlay(){$('play').hidden=true;$('play').innerHTML='';if(!$('sheet').classList.contains('open'))document.body.classList.remove('lock')}

/* ---------- 通用 ---------- */
var inApp=false; window.addEventListener('hashchange',function(){inApp=true});
function back(){if(inApp)history.back();else location.hash='#/'}
function toast(t){var el=$('toast');el.textContent=t;el.classList.add('show');clearTimeout(toast.t);toast.t=setTimeout(function(){el.classList.remove('show')},1500)}
function copy(t,msg){
  function fb(){var a=document.createElement('textarea');a.value=t;a.setAttribute('readonly','');a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();a.setSelectionRange(0,t.length);try{document.execCommand('copy');toast(msg)}catch(e){prompt('复制下面的内容',t)}document.body.removeChild(a)}
  if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(t).then(function(){toast(msg)},fb);else fb();
}
function syncFav(id){document.querySelectorAll('[data-fav="'+id+'"]').forEach(function(b){b.classList.toggle('on',!!favs[id])})}
function toggleFav(id){if(favs[id])delete favs[id];else favs[id]=Date.now();LS.set('favs',favs);toast(favs[id]?'已收藏':'已取消收藏');syncFav(id);$('favCnt').textContent=Object.keys(favs).length||'';if(state.view==='fav'){renderChips();renderGrid()}}
function refresh(){renderChips();renderGrid()}
function setView(v){
  state.view=v; $('home').hidden=v==='guides'; $('guides').hidden=v!=='guides';
  $('hero').hidden=$('featWrap').hidden=v==='fav';
  document.querySelectorAll('[data-v]').forEach(function(a){a.classList.toggle('on',a.dataset.v===v)});
  if(v!=='guides')refresh();
}
function route(){
  var h=location.hash.replace(/^#\/?/,'');
  if(h.indexOf('r/')===0){if(!$('home').hidden||$('guides').hidden){if(state.view==='guides')setView('home')}openSheet(decodeURIComponent(h.slice(2)));return}
  closeSheet();
  if(h==='guides'){setView('guides');scrollTo(0,0)}else if(h==='fav'){state.type='all';setView('fav');scrollTo(0,0)}else if(state.view!=='home')setView('home');
}
function focusSearch(){if(state.view!=='home')location.hash='#/';setTimeout(function(){var q=$('q');q.scrollIntoView({behavior:'smooth',block:'center'});q.focus({preventScroll:true})},60)}

document.addEventListener('click',function(e){
  var t=e.target.closest('[data-copy],[data-copyp],[data-fav],[data-type],[data-tag],[data-close],[data-closeplay],[data-rmtag],[data-g],[data-play],[data-lib],[data-site-load],[data-open],a');
  if(!t)return;
  if(t.tagName==='A'&&!t.dataset.g)return;
  if(t.dataset.copy){e.preventDefault();copy(t.dataset.copy,t.dataset.msg||'已复制');return}
  if(t.hasAttribute('data-copyp')){copy($('sheet').dataset.prompt,'提示词已复制，粘贴给 AI 就行');return}
  if(t.dataset.fav){e.preventDefault();e.stopPropagation();toggleFav(t.dataset.fav);return}
  if(t.dataset.type){state.type=t.dataset.type;refresh();return}
  if(t.dataset.tag!=null&&t.classList.contains('chip')){state.tag=state.tag===t.dataset.tag?'':t.dataset.tag;refresh();return}
  if(t.hasAttribute('data-close')){back();return}
  if(t.hasAttribute('data-closeplay')){closePlay();return}
  if(t.dataset.play){playFull(t.dataset.play);return}
  if(t.dataset.lib){
    document.querySelectorAll('#libTabs button').forEach(function(b){b.classList.toggle('on',b===t)});
    var box=$('sheet').querySelector('.live'); unloadLive(box); box.dataset.live=LIB+t.dataset.lib+'.html';
    var p=box.querySelector('.poster'); var pm={voice:1,orbs:1,beam:1,metal:'libmetal',gooey:1,image:1}[t.dataset.lib];
    p.style.visibility=pm?'':'hidden'; if(pm)p.src='previews/live-'+(pm===1?t.dataset.lib:pm)+'.webp';
    t.scrollIntoView({inline:'center',block:'nearest',behavior:'smooth'}); loadLive(box); return}
  if(t.dataset.siteLoad){var w=t.closest('.site-wrap');w.outerHTML=siteBox(t.dataset.siteLoad);var sb=$('sheet').querySelector('.site');track($('sheet'));loadSite(sb);return}
  if(t.dataset.rmtag!=null){var id=$('sheet').dataset.id;utags[id].splice(+t.dataset.rmtag,1);if(!utags[id].length)delete utags[id];LS.set('tags',utags);openSheet(id);refresh();return}
  if(t.dataset.g){e.preventDefault();closeSheet();location.hash='#/guides';setTimeout(function(){var el=$('g-'+t.dataset.g);el&&el.scrollIntoView({behavior:'smooth'})},80);return}
  if(t.dataset.open){location.hash='#/r/'+t.dataset.open}
});
document.addEventListener('submit',function(e){
  var f=e.target; if(!f.dataset.addtag)return; e.preventDefault();
  var v=f.t.value.trim(); if(!v)return; var id=f.dataset.addtag;
  (utags[id]=utags[id]||[]); if(utags[id].indexOf(v)<0&&BY[id].tags.indexOf(v)<0)utags[id].push(v);
  LS.set('tags',utags); openSheet(id); refresh(); toast('标签已添加');
});
$('scrim').addEventListener('click',back);
$('searchOpen').addEventListener('click',focusSearch);
var qt; $('q').addEventListener('input',function(e){clearTimeout(qt);qt=setTimeout(function(){
  state.q=e.target.value.trim(); renderGrid();
  if(state.q&&$('catalog').getBoundingClientRect().top>innerHeight*.6)$('catalog').scrollIntoView({behavior:'smooth'});
},160)});
document.addEventListener('keydown',function(e){
  if(e.key==='/'&&!/INPUT|TEXTAREA/.test(document.activeElement.tagName)){e.preventDefault();focusSearch()}
  if(e.key==='Escape'){if(!$('play').hidden)closePlay();else if($('sheet').classList.contains('open'))back()}
});
$('themeBtn').addEventListener('click',function(){var r=document.documentElement,n=r.dataset.theme==='dark'?'light':'dark';r.dataset.theme=n;try{localStorage.setItem('uihub.theme',n)}catch(e){}});
// 手机上下滑关闭详情
(function(){var y0=null,s=$('sheet');s.addEventListener('touchstart',function(e){y0=s.scrollTop<=0&&!e.target.closest('.live,.site,.pv-tabs')?e.touches[0].clientY:null},{passive:true});
 s.addEventListener('touchend',function(e){if(y0!=null&&e.changedTouches[0].clientY-y0>90)back();y0=null},{passive:true})})();
// 顶栏滚动后加玻璃底
addEventListener('scroll',function(){$('top').classList.toggle('scrolled',scrollY>8)},{passive:true});
window.addEventListener('hashchange',route);
$('statAll').textContent=ITEMS.length;
renderFeat(); track($("feat")); renderGuides(); setView("home"); route();
})();
