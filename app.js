(function(){
'use strict';
var D = window.UI_DATA || {items:[],guides:[]}, M = window.UI_MEDIA || {}, LG = window.UI_LEGAL || {}, I18N = window.UI_I18N || {langs:[['zh-CN','中文']],'zh-CN':{}};
var LANG = (function(){try{var v=localStorage.getItem('uihub.lang');if(v&&I18N[v])return v}catch(e){}
  var n=(navigator.language||'zh-CN').toLowerCase(), m={zh:'zh-CN',en:'en',ja:'ja',ko:'ko',ms:'ms',es:'es',de:'de',fr:'fr'}[n.slice(0,2)];return m||'zh-CN'})();
function t(k,v){var s=(I18N[LANG]&&I18N[LANG][k]!=null)?I18N[LANG][k]:(I18N['zh-CN'][k]!=null?I18N['zh-CN'][k]:k);if(v)Object.keys(v).forEach(function(x){s=s.split('{'+x+'}').join(v[x])});return s}
function isZh(){return LANG==='zh-CN'}
var ITEMS = D.items, BY = {};
ITEMS.forEach(function(i){BY[i.id]=i});
var TYPES = ['all','style','library','component','effect','skill','inspiration','template','generator','guide'];
/* v3h：资源类型（rt）与页面样式风格（vs）两个多选维度 */
var RTO = ['design-system','component-library','component-demo','motion','skill','mcp','design-md','tokens-spec','a11y','anti-slop','tutorial','course','newsletter','inspiration','template','generator','tool','assets','directory'];
var VSO = ['minimal','swiss','editorial','brutalist','glass','neumorphism','skeuomorphic','material','fluent','apple','enterprise','playful','soft','dark-tech','gradient','3d','motion','retro','industrial','utilitarian'];
function RTN(k){return t('rt_'+k)}
function VSN(k){return t('vs_'+k)}
var NOTES = window.UI_NOTES || {notes:{},why:{}}, CTO = window.UI_CT_ORDER || [], SECO = window.UI_SEC_ORDER || [];
// 资源说明随界面语言切换：非中文用人工撰写的译文，缺失时回落到中文原文
// 组件样式卡：名称/说明按语言模板生成（组件类型 · 来源库）
function styleName(i){return CTN(i.kind)+' · '+i.libName+(i.var?' · '+i.var:'')}
function syncStyleNames(){ITEMS.forEach(function(i){if(i.type==='style')i.name=styleName(i)})}
function noteOf(i){if(i.type==='style')return t('cs_note',{lib:i.libName,kind:CTN(i.kind)});var m=!isZh()&&NOTES.notes[LANG];return (m&&m[i.id])||shown(i.note)}
function whyOf(p,g){var m=!isZh()&&NOTES.why[LANG];return (m&&m[p.id+'@'+g.id])||p.why}
function secOf(i){if(isZh())return i.sectionTitle;var n=SECO.indexOf(i.section);return n<0?i.sectionTitle:t('sec_'+n)}
function CTN(k){return t('ct_'+k)}
function TN(k){return t('t_'+k)}
function PR(k){return {free:1,paid:1,freemium:1}[k]?t('price_'+k):''}
var VISUAL = {style:1,library:1,component:1,effect:1,template:1,generator:1,inspiration:1,guide:1,system:1,spec:1,tutorial:1,tool:1,collection:1};
// v3h 新类型（设计系统 / 规范 / 教程 / 工具 / 合集）只有拿到原站首页真实截图才按图卡展示，否则用文字卡，不放自制示意
var NEWT = {system:1,spec:1,tutorial:1,tool:1,collection:1,inspiration:1,generator:1,guide:1};
function vis(i){return !!VISUAL[i.type]&&(i.type==='style'||!!LIVE[i.id]||!!(M[i.id]&&M[i.id].img))}

/* ---------- 精选：live = 原站页面 iframe 嵌入（裁出演示区域） ---------- */
// w: iframe 的虚拟宽度；top/view: 演示区域在页面里的纵向位置和高度（像素，按 w 宽度时）
var LIB = 'https://libraries.dev/';
function lib(p){return {src:LIB+p+'.html',w:480,top:375,view:440,scheme:'dark'}}
var FEAT = [
  {id:'metal-jakubantalik-com', live:{src:'https://metal.jakubantalik.com',w:480,top:140,view:420,scheme:'dark'}, poster:'previews/live-metal.webp', title:'Liquid Metal 液态金属', hint:'鼠标移到按钮上看金属流动', big:1},
  {id:'libraries-dev', live:lib('voice'), poster:'previews/live-voice.webp', title:'Voice 语音光效', sub:'Libraries.dev · 9 月新组件', hint:'在原站点麦克风按钮，说话时光会升起'},
  {id:'orbs-jakubantalik-com', live:lib('orbs'), poster:'previews/live-orbs.webp', title:'Thinking Orbs 思考光球', sub:'原站已迁到 libraries.dev，嵌入的是新地址'},
  {id:'beam-jakubantalik-com', live:lib('beam'), poster:'previews/live-beam.webp', title:'Border Beam 流光边框', sub:'原站已迁到 libraries.dev，嵌入的是新地址'},
  {id:'shaders-paper-design-liquid-metal', live:{src:'https://shaders.paper.design/liquid-metal',w:420,top:160,view:300,scheme:'system'}, poster:'previews/live-paper.webp', title:'Paper Shaders 液态金属', hint:'原站右侧可以调参数'},
    {id:'ui-aceternity-com',wide:1},{id:'magicui-design'},{id:'reactbits-dev'},{id:'animate-ui-com'},{id:'21st-dev'},{id:'coss-com-ui'},{id:'www-heroui-com'}
];
var MORE = ['motion-primitives-com','www-beautifului-dev','www-shadcnblocks-com','reactbits-dev-animations-metallic-paint'];
var LIVE = {}; FEAT.forEach(function(f){if(f.live)LIVE[f.id]=f});
// Libraries.dev 详情页里可以切换的全部效果（都是 libraries.dev 自己的页面，不是新资源）
var LIBTABS = [['voice','Voice'],['orbs','Thinking orbs'],['beam','Border beam'],['metal','Metal'],['gooey','Gooey'],['image','Image'],['bots','Bot avatars']];

var LS = {
  get:function(k,d){try{var v=localStorage.getItem('uihub.'+k);return v?JSON.parse(v):d}catch(e){return d}},
  set:function(k,v){try{localStorage.setItem('uihub.'+k,JSON.stringify(v))}catch(e){}}
};
var favs = LS.get('favs',{}), utags = LS.get('tags',{});
var state = {type:'all', rt:'', vs:'', ct:'', q:'', tag:'', view:'home'};
var $ = function(id){return document.getElementById(id)};
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function host(u){try{return new URL(u).hostname.replace(/^www\./,'')}catch(e){return u}}
function hash(s){var h=0;for(var i=0;i<s.length;i++)h=(h*31+s.charCodeAt(i))|0;return Math.abs(h)}
function tagsOf(i){return i.tags.concat(utags[i.id]||[])}
function shown(n){return (n||'').replace(/（@[A-Za-z0-9_]+）$/,'')}
function canFrame(i){return !!(LIVE[i.id]||(M[i.id]&&M[i.id].frame))}
var IC = {
  sun:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
  moon:'<svg viewBox="0 0 24 24"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg>',
  half:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 3a9 9 0 0 1 0 18z" fill="currentColor"/></svg>',
  ext:'<svg viewBox="0 0 24 24"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>',
  copy:'<svg viewBox="0 0 24 24"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v1"/></svg>',
  star:'<svg viewBox="0 0 24 24"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/></svg>',
  play:'<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>',
  full:'<svg viewBox="0 0 24 24"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg>',
  spark:'<svg viewBox="0 0 24 24"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/></svg>',
  x:'<svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></svg>',
  code:'<svg viewBox="0 0 24 24"><path d="m8 7-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg>',
  dots:'<svg viewBox="0 0 24 24"><circle cx="5" cy="12" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="19" cy="12" r="1.4"/></svg>',
  info:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.01"/></svg>',
  lock:'<svg viewBox="0 0 24 24"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>'
};
function favBtn(i,cls){return '<button class="ib fav'+(favs[i.id]?' on':'')+(cls?' '+cls:'')+'" data-fav="'+i.id+'" aria-label="'+esc(t('fav'))+'">'+IC.star+'</button>'}

/* ---------- 许可 / 代码 / 提示词 ---------- */
function lg(i){return LG[i.id]||(i.lib&&LG[i.lib])||{k:'unk'}}
var O = window.UI_ORIG || {};
/* v3e：原站原文在前、原样保留；聚合站补充放后面并明确标注 */
function codeParts(i){var l=lg(i),o=O[i.id]||{};if(l.k!=='oss'||o.nc)return {o:'',s:''};
  var sup=o.sup||(!o.c?(l.code||''):'');return {o:o.c||'',os:o.cs||'',lic:o.cl||l.lic,s:(o.c&&sup&&o.c.indexOf(sup)>=0)?'':sup}}
function codeOf(i){var p=codeParts(i);if(!p.o)return p.s;return p.o+(p.s?'\n\n'+t('sup_mark')+'\n'+p.s:'')}
function codeTip(i){
  var l=lg(i);if((O[i.id]||{}).nc)return O[i.id].nc;
  if(l.k==='oss')return l.code?'':t('code_oss_nosnip',{lic:l.lic});
  if(l.k==='paid'||i.pricing==='paid')return t('code_paid');
  if(l.k==='lic')return t('code_lic',{lic:l.lic});
  if(l.k==='skill')return t('code_skill');
  if(l.k==='svc')return t('code_svc');
  if(l.k==='doc')return t('code_doc');
  return i.pricing==='freemium'?t('code_paid'):t('code_unk');
}
function promptParts(i){
  var o=O[i.id]||{}, n=i.type==='style'?(i.libName+' · '+CTN(i.kind)+(i.var?' · '+i.var:'')):shown(i.name), orig='', src='';
  if(o.p){orig=o.p;src=o.ps}
  else if(o.d){orig='\u201c'+o.d+'\u201d';src=o.ds}
  if(!orig)return {o:'',s:promptOld(i)};
  var c=codeParts(i), head=(o.p?t('p_orig_h',{url:src}):t('p_desc_h',{url:src}))+'\n'+orig;
  if(i.type==='style'||src!==i.url)head+='\n'+t('p_demo',{url:i.url});
  if(c.o&&c.o.length<=12000)head+='\n\n'+t('p_code_h',{lic:c.lic})+'\n```\n'+c.o+'\n```';
  return {o:head,src:src,s:(i.type==='skill'&&o.p?t('p_task_skill'):t('p_task',{name:n}))+'\n\n'+t('p_sup',{url:i.url})};
}
function promptFor(i){var p=promptParts(i);return p.o?p.o+'\n\n'+p.s:p.s}
function promptOld(i){
  var n=shown(i.name), note=noteOf(i);
  if(i.type==='skill')return t('prompt_skill',{name:n,url:i.url,note:note||t('note_none')});
  return t('prompt_ref',{name:n,url:i.url,note:note?t('note_wrap',{note:note}):''});
}
function cardActs(i,cls){
  var c=codeOf(i), tip=codeTip(i);
  return '<div class="cacts'+(cls?' '+cls:'')+'">'+
    '<a class="ab go" href="'+esc(i.url)+'" target="_blank" rel="noopener noreferrer" title="'+esc(t('btn_original'))+'">'+IC.ext+'<span>'+esc(t('btn_original'))+'</span></a>'+
    '<button class="ab" data-cp="'+i.id+'" title="'+esc(t('btn_copy_prompt'))+'">'+IC.spark+'<span>Prompt</span></button>'+
    (c?'<button class="ab code" data-cc="'+i.id+'" title="'+esc(t('btn_copy_code'))+'">'+IC.code+'<span>'+esc(t('code_none_h'))+'</span></button>'
      :'<button class="ab off" aria-disabled="true" data-tip="'+esc(tip)+'" title="'+esc(tip)+'">'+IC.lock+'<span>'+esc(t('code_none_h'))+'</span></button>')+
  '</div>';
}

/* v4 卡片：标题 / 一行 mono 元信息 / 两行说明 / 操作栏 */
function hostPath(u){try{var x=new URL(u),p=x.pathname.replace(/\/$/,'');return x.hostname.replace(/^www\./,'')+(p.length>1?p:'')}catch(e){return u}}
function metaLine(i,path){
  var l=lg(i), out=['<span class="h">'+esc(path?hostPath(i.url):host(i.url))+'</span>'];
  if(PR(i.pricing))out.push('<span class="pr '+i.pricing+'" title="'+esc(t('price_tip_'+i.pricing))+'">'+PR(i.pricing)+'</span>');
  if(l.k==='oss')out.push('<span title="'+esc(t('kv_license'))+'">'+esc(l.lic)+'</span>');
  return '<p class="cu">'+out.join('<i aria-hidden="true">·</i>')+'</p>';
}
function ctl(i){return favBtn(i)+'<button class="ib more" data-more="'+i.id+'" aria-haspopup="menu" aria-label="'+esc(t('btn_more'))+'" title="'+esc(t('btn_more'))+'">'+IC.dots+'</button>'}
/* 卡面复制按钮：Prompt 永远可复制；代码仅限核对过许可证的片段，其余置灰并说明原因 */
function copyRow(i){
  var c=codeOf(i), tip=codeTip(i);
  return '<button class="cpb" data-cp="'+i.id+'" title="'+esc(t('btn_copy_prompt'))+'" aria-label="'+esc(t('btn_copy_prompt'))+'">'+IC.copy+'<span>Prompt</span></button>'+
    (c?'<button class="cpb" data-cc="'+i.id+'" title="'+esc(t('btn_copy_code')+' · '+lg(i).lic)+'" aria-label="'+esc(t('btn_copy_code'))+'">'+IC.code+'<span>'+esc(t('code_none_h'))+'</span></button>'
      :'<button class="cpb off" aria-disabled="true" data-tip="'+esc(tip)+'" title="'+esc(tip)+'" aria-label="'+esc(t('code_off_short'))+'">'+IC.lock+'<span>'+esc(t('code_none_h'))+'</span></button>');
}
function foot(i){return '<div class="cbar">'+copyRow(i)+'<span class="sp"></span>'+ctl(i)+'</div>'}
function menuHTML(i){
  return '<div class="mh"><b>'+esc(shown(i.name))+'</b><small>'+esc(host(i.url))+'</small></div>'+
    (vis(i)?'<button class="mi" role="menuitem" data-play="'+i.id+'">'+IC.full+'<span>'+esc(canFrame(i)?t('btn_play'):t('btn_view'))+'</span></button>':'')+
    '<a class="mi" role="menuitem" href="'+esc(i.url)+'" target="_blank" rel="noopener noreferrer">'+IC.ext+'<span>'+esc(t('btn_original'))+'</span></a>'+
    '<button class="mi" role="menuitem" data-open="'+i.id+'">'+IC.info+'<span>'+esc(t('btn_details'))+'</span></button>';
}
var menuFor=null;
function isSheetMenu(){return matchMedia('(max-width:640px),(pointer:coarse)').matches}
function openMenu(id,btn){
  var i=BY[id]; if(!i)return; var m=$('menu');
  if(menuFor===id&&!m.hidden){closeMenu();return}
  closeMenu(); menuFor=id; m.innerHTML=menuHTML(i); m.hidden=false; btn.setAttribute('aria-expanded','true'); btn.classList.add('act');
  var sheet=isSheetMenu(); m.classList.toggle('as-sheet',sheet); $('menuScrim').hidden=!sheet;
  if(sheet){m.style.left=m.style.top='';document.body.classList.add('lock')}
  else{var r=btn.getBoundingClientRect(), w=m.offsetWidth, h=m.offsetHeight;
    var left=Math.max(8,Math.min(innerWidth-w-8,r.right-w)), top=r.bottom+6; if(top+h>innerHeight-8)top=Math.max(8,r.top-h-6);
    m.style.left=left+'px'; m.style.top=top+'px'}
  requestAnimationFrame(function(){m.classList.add('show')});
}
function closeMenu(){
  var m=$('menu'); if(!m||m.hidden)return;
  m.hidden=true; m.classList.remove('show'); $('menuScrim').hidden=true; menuFor=null;
  document.querySelectorAll('[data-more].act').forEach(function(b){b.classList.remove('act');b.setAttribute('aria-expanded','false')});
  if($('sheet').classList.contains('open')||!$('play').hidden){}else document.body.classList.remove('lock');
}

/* ---------- 预览区 ---------- */
// 自制示意：本站用 CSS 画的抽象示意图，明确标注「自制示意」，不复制原站画面
function demo(i){
  var h=hash(i.id)%360, k=i.type, inner;
  if(k==='effect')inner='<i class="d-orb"></i><i class="d-ring"></i>';
  else if(k==='template')inner='<div class="d-chat"><i class="l"></i><i class="r"></i><i class="l s"></i><b></b></div>';
  else if(k==='generator')inner='<div class="d-gen"><b><i></i></b><span><i></i><i></i><i></i></span></div>';
  else if(k==='inspiration')inner='<div class="d-grid"><i></i><i></i><i></i><i></i><i></i><i></i></div>';
  else if(k==='guide')inner='<div class="d-notes"><i></i><i></i><i></i></div>';
  else inner='<div class="d-ui"><b></b><i class="w"></i><i></i><span><i></i><i class="p"></i></span></div>';
  return '<div class="demo d-'+k+'" style="--h:'+h+'">'+inner+'<em class="d-n">'+esc(i.type==='library'?shown(i.name):shown(i.name).split('/').pop())+'</em></div>';
}
function srcTag(i,live){
  if(live)return '<span class="tag-lv">'+t('tag_live')+'</span>';
  var m=M[i.id]; if(!m||!m.img)return vis(i)?'<span class="tag-dm">'+t('tag_demo')+'</span>':'';
  return '<span class="tag-pv">'+(m.src==='site'?t('tag_site'):m.src==='comp'?t('tag_comp'):m.src==='app'?t('tag_app'):m.src==='shot'?t('tag_shot'):t('tag_og'))+'</span>';
}
function liveBox(f,opts){
  opts=opts||{};
  var L=f.live;
  return '<div class="live" data-live="'+esc(L.src)+'" data-w="'+L.w+'" data-top="'+L.top+'" data-view="'+L.view+'"'+(opts.eager?' data-eager="1"':'')+'>'+
    '<img class="poster" src="'+f.poster+'" alt="" loading="lazy">'+
    '<div class="ifw"></div><div class="shield" data-play="'+f.id+'"><span class="tap">'+IC.play+esc(t('btn_tryit'))+'</span></div>'+
    '<span class="ld"><i></i>'+esc(t('loading_live'))+'</span></div>';
}
/* v5：主题 —— 自制示意随主题换色；有浅/深双截图的随主题切换；只有一张的标出是浅色还是深色截图（不伪造暗色） */
function curTheme(){return document.documentElement.dataset.theme==='light'?'light':'dark'}
function thmTag(sc){if(!sc)return '';return '<span class="thm" data-s="'+sc+'">'+(sc==='dark'?IC.moon:IC.half)+'<span>'+esc(t(sc==='dark'?'thm_dark_only':'thm_system'))+'</span></span>'}
function shotTag(m){if(m.imgL&&m.imgD)return '<span class="shot-t dual" title="'+esc(t('thm_follow'))+'">'+IC.half+'</span>';if(!m.tone)return '';return '<span class="shot-t" data-t="'+m.tone+'" title="'+esc(t(m.tone==='l'?'shot_l':'shot_d'))+'">'+(m.tone==='l'?IC.sun:IC.moon)+'</span>'}
function shotImg(m,cls,extra){cls=cls?cls+' ':'';extra=extra||'';if(m.imgL&&m.imgD)return '<img class="'+cls+'ts ts-l" src="'+m.imgL+'" alt="" '+extra+'><img class="'+cls+'ts ts-d" src="'+m.imgD+'" alt="" '+extra+'>';return '<img'+(cls?' class="'+cls.trim()+'"':'')+' src="'+m.img+'" alt="" '+extra+'>'}
function postTheme(fr,n){try{fr.style.colorScheme=n;fr.contentWindow&&fr.contentWindow.postMessage({type:'theme',theme:n,source:'uihub'},'*');fr.contentWindow&&fr.contentWindow.postMessage({type:'uihub:theme',theme:n},'*')}catch(e){}}
window.UIHUB_postTheme=function(fr){postTheme(fr,curTheme())};
function applyTheme(n){document.querySelectorAll('.pvw[data-ts]').forEach(function(p){p.removeAttribute('data-ts')});document.querySelectorAll('iframe').forEach(function(fr){postTheme(fr,n)})}
function thumb(i){var m=M[i.id]||{},lv=LIVE[i.id];return lv?'<img src="'+lv.poster+'" alt="" loading="lazy">'+thmTag(lv.live.scheme==='dark'?'dark':''):(m.img?shotImg(m,'','loading="lazy"')+shotTag(m):demo(i))}

/* ---------- 精选 ---------- */
function featCard(f,k){
  var i=BY[f.id]; if(!i)return '';
  var m=M[i.id]||{}, live=!!f.live;
  var media = live ? liveBox(f) : (m.img?shotImg(m,'poster','loading="'+(k<8?'eager':'lazy')+'"')+shotTag(m):demo(i));
  var title=isZh()?(f.title||shown(i.name)):shown(i.name), sub=isZh()?(f.sub||noteOf(i)||host(i.url)):(noteOf(i)||host(i.url));
  return '<article class="fc'+(f.big?' big':'')+(f.wide?' wide':'')+(live?' is-live':'')+'" style="--i:'+k+'">'+
    '<div class="fm" '+(live?'':'data-open="'+i.id+'"')+'>'+media+'<div class="ftop">'+(live?srcTag(i,live)+thmTag(f.live.scheme==='dark'?'dark':''):'')+'</div></div>'+
    '<div class="fb" data-open="'+i.id+'"><h3>'+esc(title)+'</h3>'+metaLine(i)+
    '<p class="note">'+esc(f.hint&&isZh()?sub+' · '+f.hint:sub)+'</p>'+foot(i)+
    '</div></article>';
}
function renderFeat(){
  $('feat').innerHTML = FEAT.map(featCard).join('');
  $('more').innerHTML = '<span class="ml">'+esc(t('more_title'))+'</span><div class="mcs">'+MORE.map(function(id){var i=BY[id];return '<button class="mc" data-open="'+id+'">'+thumb(i)+'<span><b>'+esc(shown(i.name))+'</b><small>'+esc(noteOf(i))+'</small></span></button>'}).join('')+'</div>';
  observeLive($('feat')); track($('feat'));
}

/* ---------- 目录卡片 ---------- */
function card(i){
  var m=M[i.id]||{}, live=LIVE[i.id], nm=shown(i.name);
  if(!vis(i)){
    var parts=nm.split('/');
    return '<article class="card tx" data-open="'+i.id+'"><div class="cm"><div class="th cover"><span class="cl">'+esc(i.type==='skill'?'SKILL.md':TN(i.type))+'</span>'+
      '<b>'+esc(parts[parts.length-1])+'</b><small>'+esc(parts.length>1?parts[0]:host(i.url))+'</small></div></div>'+
      '<div class="cb"><h3>'+esc(nm)+'</h3>'+metaLine(i)+'<p class="note">'+esc(noteOf(i)||host(i.url))+'</p>'+foot(i)+'</div></article>';
  }
  var tag = live?'<span class="tag-lv">'+t('tag_live')+'</span>':(m.frame?'<span class="tag-fr">'+t('tag_frame')+'</span>':'');
  if(i.type==='style')return '<article class="card cs" data-open="'+i.id+'"><div class="cm"><div class="th">'+thumb(i)+'</div></div>'+
    '<div class="cb"><h3>'+esc(CTN(i.kind))+'<span class="csl">'+esc(i.libName)+(i.var?' · '+esc(i.var):'')+'</span></h3>'+metaLine(i,1)+'<p class="note">'+esc(noteOf(i))+'</p>'+foot(i)+'</div></article>';
  return '<article class="card" data-open="'+i.id+'"><div class="cm"><div class="th">'+thumb(i)+'</div>'+(tag?'<div class="ctop">'+tag+'</div>':'')+'</div>'+
    '<div class="cb"><h3>'+esc(nm)+'</h3>'+metaLine(i)+'<p class="note">'+esc(noteOf(i)||host(i.url))+'</p>'+foot(i)+'</div></article>';
}
function match(i){
  if(state.view==='fav'&&!favs[i.id])return false;
  if(state.type!=='all'&&i.type!==state.type)return false;
  if(state.rt&&(i.rt||[]).indexOf(state.rt)<0)return false;
  if(state.vs&&(i.vs||[]).indexOf(state.vs)<0)return false;
  if(state.ct&&(i.ct||[]).indexOf(state.ct)<0)return false;
  if(state.tag&&tagsOf(i).indexOf(state.tag)<0)return false;
  if(!state.q)return true;
  var l=lg(i), hay=(i.name+' '+(i.libName||'')+' '+(i.kind||'')+' '+i.note+' '+noteOf(i)+' '+i.url+' '+i.source+' '+i.section+' '+TN(i.type)+' '+i.type+' '+(l.lic||'')+' '+tagsOf(i).join(' ')+' '+(i.ct||[]).map(function(c){return c+' '+CTN(c)}).join(' ')+' '+(i.rt||[]).map(function(c){return c+' '+RTN(c)}).join(' ')+' '+(i.vs||[]).map(function(c){return c+' '+VSN(c)}).join(' ')).toLowerCase();
  return state.q.toLowerCase().split(/\s+/).every(function(w){return hay.indexOf(w)>=0});
}
function renderChips(){
  // 分面计数：每一行的数字 = 满足其它筛选条件时该项的数量
  var base = ITEMS.filter(function(i){return state.view!=='fav'||favs[i.id]});
  function ok(i,skip){
    if(skip!=='rt'&&state.rt&&(i.rt||[]).indexOf(state.rt)<0)return false;
    if(skip!=='vs'&&state.vs&&(i.vs||[]).indexOf(state.vs)<0)return false;
    if(skip!=='ct'&&state.ct&&(i.ct||[]).indexOf(state.ct)<0)return false;
    if(skip!=='tag'&&state.tag&&tagsOf(i).indexOf(state.tag)<0)return false;
    return true}
  function cnt(skip,f){var c={},n=0;base.forEach(function(i){if(!ok(i,skip))return;n++;(i[f]||[]).forEach(function(x){c[x]=(c[x]||0)+1})});c._n=n;return c}
  var rc=cnt('rt','rt');
  function lab(id,k){var p=$(id).parentNode;p.dataset.label=t(k)}
  lab('chips','rt_h');lab('vsChips','vs_h');lab('ctChips','ct_h');lab('tagChips','tags_h');
  var html = '<button class="chip'+(state.rt?'':' on')+'" data-rt="">'+esc(t('rt_all'))+'<small>'+rc._n+'</small></button>'+
    RTO.filter(function(k){return rc[k]||state.rt===k}).map(function(k){return '<button class="chip'+(state.rt===k?' on':'')+'" data-rt="'+k+'">'+esc(RTN(k))+'<small>'+(rc[k]||0)+'</small></button>'}).join('');
  var tc={}; base.forEach(function(i){if(ok(i,'tag'))tagsOf(i).forEach(function(x){tc[x]=(tc[x]||0)+1})});
  var top=Object.keys(tc).sort(function(a,b){return tc[b]-tc[a]}).slice(0,12);
  if(state.tag&&top.indexOf(state.tag)<0)top.unshift(state.tag);
  $('tagChips').innerHTML = top.map(function(x){return '<button class="chip t'+(state.tag===x?' on':'')+'" data-tag="'+esc(x)+'">#'+esc(x)+'</button>'}).join('');
  $('chips').innerHTML = html;
  var vc=cnt('vs','vs');
  $('vsChips').innerHTML = '<button class="chip c'+(state.vs?'':' on')+'" data-vs="">'+esc(t('vs_all'))+'</button>'+
    VSO.filter(function(k){return vc[k]||state.vs===k}).map(function(k){return '<button class="chip c v'+(state.vs===k?' on':'')+'" data-vs="'+k+'"><i class="vsw vs-'+k+'"></i>'+esc(VSN(k))+'<small>'+(vc[k]||0)+'</small></button>'}).join('');
  var cc=cnt('ct','ct');
  $('ctChips').innerHTML = '<button class="chip c'+(state.ct?'':' on')+'" data-ct="">'+esc(t('ct_all'))+'</button>'+
    CTO.filter(function(c){return cc[c]||state.ct===c}).map(function(c){return '<button class="chip c'+(state.ct===c?' on':'')+'" data-ct="'+c+'">'+esc(CTN(c))+'<small>'+(cc[c]||0)+'</small></button>'}).join('');
}
/* v3e：两千多张卡分批渲染，滚到底部再追加，手机上不卡 */
var GL=[], GN=0, GIO=null;
function moreGrid(){var n=Math.min(GL.length,GN+(GN?160:96));if(n>GN)$('grid').insertAdjacentHTML('beforeend',GL.slice(GN,n).map(card).join(''));GN=n;var s=$('gridMore');if(s)s.hidden=GN>=GL.length}
function initMore(){var s=$('gridMore');if(!s||GIO||!('IntersectionObserver' in window))return;GIO=new IntersectionObserver(function(es){if(es[0].isIntersecting)moreGrid()},{rootMargin:'1200px 0px'});GIO.observe(s)}
function renderGrid(){initMore();
  var list = ITEMS.filter(match);
  list = list.map(function(i,k){return [i.type==='style'?-1:vis(i)?(M[i.id]&&M[i.id].img||LIVE[i.id]?0:1):2,k,i]}).sort(function(a,b){return a[0]-b[0]||a[1]-b[1]}).map(function(a){return a[2]});
  GL=list; GN=0; $('grid').innerHTML=''; moreGrid();
  var fc=Object.keys(favs).length; $('favCnt').textContent=fc||'';
  var isFav=state.view==='fav';
  $('empty').hidden = !!list.length;
  $('empty').textContent = isFav&&!fc?t('empty_fav'):t('empty');
  $('catTitle').textContent = isFav?t('cat_fav'):(state.q?t('cat_search'):t('cat_all'));
  $('meta').textContent = t('meta',{n:list.length})+(list.length!==ITEMS.length?t('meta_total',{t:ITEMS.length}):'')+t('meta_sort');
}
function gk(g,s){return 'g_'+g.id.replace(/-/g,'_')+'_'+s}
function renderGuides(){
  $('guideList').innerHTML = D.guides.map(function(g,n){
    return '<div class="guide" id="g-'+g.id+'" style="--i:'+n+'"><div class="gh"><span class="ge">'+g.emoji+'</span><div><h2>'+esc(t(gk(g,'t')))+'</h2><p>'+esc(t(gk(g,'p')))+'</p></div></div><ol>'+
      g.picks.map(function(p){var i=BY[p.id],m=M[i.id]||{};return '<li data-open="'+i.id+'"><span class="gt">'+(m.img?'<img src="'+m.img+'" alt="" loading="lazy">':'<b>'+esc(shown(i.name).split('/').pop().slice(0,2))+'</b>')+'</span><div><b>'+esc(shown(i.name))+'</b><span class="tp">'+TN(i.type)+'</span><p>'+esc(whyOf(p,g))+'</p></div></li>'}).join('')+'</ol></div>';
  }).join('');
}

/* ---------- iframe 实时预览 ---------- */
function fit(box){
  var w=+box.dataset.w, top=+box.dataset.top, view=+box.dataset.view, cw=box.clientWidth, ch=box.clientHeight;
  if(!cw||!ch)return;
  // contain：整块演示区（w × view）完整缩进卡片里，左右不裁切；多出的高度上下居中留白
  var s=Math.min(cw/w, ch/view), vis=ch/s;
  var off=Math.max(0, top-(vis-view)/2), fr=box.querySelector('iframe');
  if(fr){fr.style.width=w+'px';fr.style.height=(off+vis+40)+'px';fr.style.transform='translate('+((cw-w*s)/2)+'px,'+(-off*s)+'px) scale('+s+')'}
}
function loadLive(box){
  if(box.dataset.on)return; box.dataset.on='1';
  var fr=document.createElement('iframe');
  fr.src=box.dataset.live; fr.loading='eager'; fr.title='live preview'; fr.referrerPolicy='no-referrer-when-downgrade';
  fr.setAttribute('allow','microphone; autoplay; clipboard-write'); fr.tabIndex=-1;
  fr.style.colorScheme=curTheme(); box.querySelector('.ifw').appendChild(fr); fit(box); box.classList.add('loading');
  var to=setTimeout(function(){box.classList.add('slow')},12000);
  fr.addEventListener('load',function(){clearTimeout(to);postTheme(fr,curTheme());setTimeout(function(){box.classList.remove('loading','slow');box.classList.add('ready')},900)});
}
function unloadLive(box){if(!box.dataset.on)return;delete box.dataset.on;box.querySelector('.ifw').innerHTML='';box.classList.remove('ready','loading','slow')}
var io = 'IntersectionObserver' in window ? new IntersectionObserver(function(es){
  es.forEach(function(e){ if(e.isIntersecting)loadLive(e.target); else if(!e.target.dataset.eager)unloadLive(e.target) });
},{rootMargin:'120px 0px',threshold:.2}) : null;
function observeLive(root){root.querySelectorAll('.live').forEach(function(b){if(io)io.observe(b);else loadLive(b)})}
var ro = 'ResizeObserver' in window ? new ResizeObserver(function(es){es.forEach(function(e){fit(e.target)})}) : null;
function track(root){root.querySelectorAll('.live,.site').forEach(function(b){ro&&ro.observe(b)})}

// 整页嵌入（详情页里用）：按宽度缩放原站页面
function siteBox(url){return '<div class="site" data-site="'+esc(url)+'"><div class="ifw"></div><span class="ld"><i></i>'+esc(t('loading_site'))+'</span></div>'}
function loadSite(box){
  var cw=box.clientWidth, vw=cw<640?Math.max(cw,375):1180, s=cw/vw, ch=box.clientHeight;
  var fr=document.createElement('iframe'); fr.src=box.dataset.site; fr.title='original page';
  fr.style.width=vw+'px'; fr.style.height=(ch/s)+'px'; fr.style.transform='scale('+s+')';
  box.querySelector('.ifw').appendChild(fr); box.classList.add('loading');
  var to=setTimeout(function(){box.classList.add('slow')},12000);
  fr.addEventListener('load',function(){clearTimeout(to);postTheme(fr,curTheme());setTimeout(function(){box.classList.remove('loading','slow');box.classList.add('ready')},600)});
}

/* ---------- 详情 ---------- */
function related(i){
  var mine=tagsOf(i);
  return ITEMS.filter(function(x){return x.type===i.type&&x.id!==i.id}).map(function(x){
    var s=0; tagsOf(x).forEach(function(z){if(mine.indexOf(z)>=0)s+=2}); if(x.section===i.section)s+=1; if(M[x.id]&&M[x.id].img)s+=.5; return [s,x];
  }).sort(function(a,b){return b[0]-a[0]}).slice(0,6).map(function(a){return a[1]});
}
function guidesFor(i){return D.guides.filter(function(g){return g.picks.some(function(p){return p.id===i.id})})}
function preview(i){
  var f=LIVE[i.id], m=M[i.id]||{};
  if(i.id==='libraries-dev'){
    return '<div class="pv-tabs" id="libTabs">'+LIBTABS.map(function(x,k){return '<button class="'+(k?'':'on')+'" data-lib="'+x[0]+'">'+x[1]+'</button>'}).join('')+'</div>'+
      '<div class="pvw big">'+liveBox({id:i.id,live:lib('voice'),poster:'previews/live-voice.webp'},{eager:1})+'<div class="pvtag"><span class="tag-lv">'+t('tag_live')+'</span>'+thmTag('dark')+'<span>'+esc(t('pv_libtabs'))+'</span></div></div>';
  }
  if(f)return '<div class="pvw big">'+liveBox(f,{eager:1})+'<div class="pvtag"><span class="tag-lv">'+t('tag_live')+'</span>'+thmTag(f.live.scheme)+'<span>'+esc(t('pv_live_d'))+'</span></div></div>';
  if(m.frame)return '<div class="pvw big">'+tsw(m)+'<div class="site-wrap">'+(m.img?shotImg(m,'poster'):demo(i))+
    '<button class="loadsite" data-site-load="'+esc(i.url)+'">'+IC.play+'<span>'+esc(t('pv_frame_btn'))+'<small>'+esc(t('pv_frame_sub'))+'</small></span></button></div>'+
    '<div class="pvtag">'+srcTag(i)+shotNote(m)+'<span>'+esc(t('pv_frame_d'))+'</span></div></div>';
  if(m.img)return '<div class="pvw big">'+tsw(m)+shotImg(m,'poster','data-play="'+i.id+'"')+'<div class="pvtag">'+srcTag(i)+shotNote(m)+'<span>'+esc(t('pv_noframe_d'))+'</span></div></div>';
  if(vis(i))return '<div class="pvw big">'+demo(i)+'<div class="pvtag">'+srcTag(i)+'<span>'+esc(t('pv_demo_d'))+'</span></div></div>';
  var parts=shown(i.name).split('/');
  return '<div class="pvw sk"><div class="term"><i></i><i></i><i></i><span>'+esc(i.type==='skill'?'SKILL.md':host(i.url))+'</span></div><div class="skn"><small>'+esc(parts.length>1?parts[0]+' /':TN(i.type))+'</small><b>'+esc(parts[parts.length-1])+'</b></div></div>';
}
function tsw(m){if(!(m.imgL&&m.imgD))return '';return '<div class="tsw" role="group"><button data-ts="light">'+IC.sun+esc(t('shot_sw_l'))+'</button><button data-ts="dark">'+IC.moon+esc(t('shot_sw_d'))+'</button></div>'}
function shotNote(m){if(m.imgL&&m.imgD||!m.tone)return '';return '<span class="thm one" data-t="'+m.tone+'">'+(m.tone==='l'?IC.sun:IC.moon)+'<span>'+esc(t(m.tone==='l'?'shot_one_l':'shot_one_d'))+'</span></span>'}
function srcLink(u){return u?'<a class="osrc" href="'+esc(u)+'" target="_blank" rel="noopener noreferrer">'+esc(t('src_l'))+' · '+esc(host(u))+'</a>':''}
function promptBlock(i){
  var p=promptParts(i);
  if(!p.o)return '<div class="prompt"><div class="ph"><span>'+IC.spark+esc(t('prompt_h'))+'</span><button class="b sm pri" data-cp="'+i.id+'">'+IC.copy+esc(t('btn_copy_prompt'))+'</button></div><div class="ogs sup"><span class="ogh">'+esc(t('sup_h'))+'</span><pre>'+esc(p.s)+'</pre></div></div>';
  return '<div class="prompt"><div class="ph"><span>'+IC.spark+esc(t('prompt_h'))+'</span><span class="phb"><button class="b sm ghost" data-cpo="'+i.id+'">'+esc(t('btn_copy_orig'))+'</button><button class="b sm pri" data-cp="'+i.id+'">'+IC.copy+esc(t('btn_copy_prompt'))+'</button></span></div>'+
    '<div class="ogs org"><span class="ogh">'+esc(t('orig_h'))+srcLink(p.src)+'</span><pre>'+esc(p.o)+'</pre></div>'+
    '<div class="ogs sup"><span class="ogh">'+esc(t('sup_h'))+'</span><pre>'+esc(p.s)+'</pre></div></div>';
}
function codeBlock(i){
  var l=lg(i), c=codeOf(i), cp=codeParts(i);
  if(c&&cp.o)return '<div class="prompt code"><div class="ph"><span>'+IC.code+esc(t('code_h'))+'</span><span class="phb">'+(cp.s?'<button class="b sm ghost" data-cco="'+i.id+'">'+esc(t('btn_copy_orig'))+'</button>':'')+'<button class="b sm pri" data-cc="'+i.id+'">'+IC.copy+esc(t('btn_copy_code'))+'</button></span></div>'+
    '<div class="ogs org"><span class="ogh">'+esc(t('orig_h'))+((O[i.id]||{}).fw?' <span class="pill fw">'+esc(O[i.id].fw)+'</span>':'')+srcLink(cp.os)+'</span><pre>'+esc(cp.o)+'</pre><p class="cnote">'+esc(t((O[i.id]||{}).full&&/① /.test(cp.o)?'code_full_note':'code_orig_note',{lic:cp.lic}))+'</p></div>'+
    (cp.s?'<div class="ogs sup"><span class="ogh">'+esc(t('sup_h'))+'</span><pre>'+esc(cp.s)+'</pre><p class="cnote">'+esc(t('code_sup_note'))+'</p></div>':'')+
    (l.pro?'<p class="cnote">'+esc(t('pro_note',{pro:l.pro}))+'</p>':'')+'</div>';
  if(c)return '<div class="prompt code"><div class="ph"><span>'+IC.code+esc(t('code_h'))+'</span><button class="b sm pri" data-cc="'+i.id+'">'+IC.copy+esc(t('btn_copy_code'))+'</button></div><div class="ogs sup"><span class="ogh">'+esc(t('sup_h'))+'</span><pre>'+esc(c)+'</pre></div>'+
    '<p class="cnote">'+esc(t('code_note',{lic:l.lic}))+(l.pro?' '+esc(t('pro_note',{pro:l.pro})):'')+'</p></div>';
  return '<div class="prompt code off"><div class="ph"><span>'+IC.lock+esc(t('code_none_h'))+'</span><button class="b sm ghost" disabled title="'+esc(codeTip(i))+'">'+IC.copy+esc(t('btn_copy_code'))+'</button></div><p class="cnote">'+esc(codeTip(i))+'</p></div>';
}
/* v3f：Prime 系（Vue / Angular / React）同款演示互链，避免复制到错框架的代码 */
var PRIME={'lib-primevue-org':'Vue','lib-primeng-org':'Angular','lib-primereact-org':'React'};
function pslug(x){return (x.page||x.url||'').replace(/\/+$/,'').split('/').pop()}
function fwSibs(i){
  if(!PRIME[i.lib])return '';
  var s=pslug(i), seen={}, out=ITEMS.filter(function(x){return x.lib&&PRIME[x.lib]&&x.lib!==i.lib&&(pslug(x)===s||x.kind===i.kind)}).sort(function(a,b){return (pslug(b)===s)-(pslug(a)===s)}).filter(function(x){if(seen[x.lib])return false;seen[x.lib]=1;return true});
  if(!out.length)return '';
  return '<p class="fwsibs">'+esc(t('fw_sibs'))+' '+out.map(function(x){return '<button class="b sm ghost" data-open="'+x.id+'">'+esc(x.libName||x.lib)+' · '+PRIME[x.lib]+'</button>'}).join(' ')+'</p>';
}
function openSheet(id){
  var i=BY[id]; if(!i)return;
  var ut=utags[i.id]||[], gs=guidesFor(i), pr=promptFor(i), l=lg(i);
  var links=(l.npm?'<a href="'+esc(l.npm)+'" target="_blank" rel="noopener noreferrer">npm</a>':'')+(l.gh?'<a href="'+esc(l.gh)+'" target="_blank" rel="noopener noreferrer">GitHub</a>':'');
  $('sheet').innerHTML = '<div class="grab"></div><button class="ib close" data-close aria-label="'+esc(t('close'))+'">'+IC.x+'</button>'+preview(i)+
   '<div class="sb"><div class="row">'+'<span class="tp">'+TN(i.type)+'</span>'+(PR(i.pricing)?'<span class="pill '+i.pricing+'">'+PR(i.pricing)+'</span>':'')+(l.lic?'<span class="pill oss">'+esc(l.lic)+'</span>':'')+(i.source?'<span class="src">'+esc(i.source)+'</span>':'')+'</div>'+
   '<h2>'+esc(shown(i.name))+'</h2>'+(noteOf(i)?'<p class="lead">'+esc(noteOf(i))+'</p>':'')+
   '<div class="acts"><a class="b pri" href="'+esc(i.url)+'" target="_blank" rel="noopener noreferrer">'+esc(t('btn_original'))+IC.ext+'</a>'+
   (vis(i)?'<button class="b ghost" data-play="'+i.id+'">'+IC.full+esc(canFrame(i)?t('btn_play'):t('btn_view'))+'</button>':'')+
   '<button class="b ghost" data-copy="'+esc(i.url)+'" data-msg="'+esc(t('toast_link'))+'">'+IC.copy+esc(t('btn_copy_link'))+'</button>'+favBtn(i,'lg')+'</div>'+
   fwSibs(i)+
   promptBlock(i)+
   codeBlock(i)+
   '<dl class="kv"><dt>'+esc(t('kv_url'))+'</dt><dd class="u"><a href="'+esc(i.url)+'" target="_blank" rel="noopener noreferrer">'+esc(i.url)+'</a></dd>'+
   (l.lic?'<dt>'+esc(t('kv_license'))+'</dt><dd>'+esc(l.lic)+(links?'<span class="lk">'+links+'</span>':'')+'</dd>':'')+
   ((i.rt||[]).length?'<dt>'+esc(t('kv_rt'))+'</dt><dd class="fl">'+i.rt.map(function(k){return '<button class="tg lk" data-rt="'+k+'">'+esc(RTN(k))+'</button>'}).join('')+'</dd>':'')+
   ((i.vs||[]).length?'<dt>'+esc(t('kv_vs'))+'</dt><dd class="fl">'+i.vs.map(function(k){return '<button class="tg lk" data-vs="'+k+'"><i class="vsw vs-'+k+'"></i>'+esc(VSN(k))+'</button>'}).join('')+'</dd>':'')+
   '<dt>'+esc(t('kv_group'))+'</dt><dd>'+esc(secOf(i))+(i.sectionDesc&&isZh()?'<span>'+esc(i.sectionDesc)+'</span>':'')+'</dd>'+
   (gs.length?'<dt>'+esc(t('kv_guide'))+'</dt><dd>'+gs.map(function(g){return '<a href="#/guides" data-g="'+g.id+'">'+g.emoji+' '+esc(t(gk(g,'t')))+'</a>'}).join('')+'</dd>':'')+'</dl>'+
   '<h3>'+esc(t('tags_h'))+'</h3><div class="tagrow">'+i.tags.map(function(x){return '<span class="tg">'+esc(x)+'</span>'}).join('')+
     ut.map(function(x,k){return '<span class="tg u">'+esc(x)+'<b data-rmtag="'+k+'">×</b></span>'}).join('')+'</div>'+
   '<form class="addtag" data-addtag="'+i.id+'"><input name="t" maxlength="16" placeholder="'+esc(t('tag_ph'))+'"><button class="b ghost sm">'+esc(t('btn_add'))+'</button></form>'+
   '<h3>'+esc(t('related_h'))+'</h3><div class="rel">'+related(i).map(function(x){var m=M[x.id]||{},lv=LIVE[x.id];return '<button data-open="'+x.id+'">'+(m.img||lv?'<img src="'+(lv?lv.poster:m.img)+'" alt="" loading="lazy">':'<span class="rm">'+esc(shown(x.name).split('/').pop().slice(0,2))+'</span>')+'<b>'+esc(shown(x.name))+'</b></button>'}).join('')+'</div>'+
   '<p class="legal-s">'+esc(t('legal'))+'</p></div>';
  $('sheet').dataset.id=i.id;
  $('scrim').hidden=false; $('sheet').classList.add('open'); $('sheet').setAttribute('aria-hidden','false'); $('sheet').scrollTop=0;
  document.body.classList.add('lock');
  requestAnimationFrame(function(){var b=$('sheet').querySelector('.live');if(b){track($('sheet'));setTimeout(function(){loadLive(b)},280)}});
}
function closeSheet(){
  var s=$('sheet'); if(!s.classList.contains('open'))return;
  s.classList.remove('open'); $('scrim').hidden=true; s.setAttribute('aria-hidden','true'); document.body.classList.remove('lock');
  setTimeout(function(){if(!s.classList.contains('open'))s.innerHTML=''},350);
}
// 全屏：真实预览 → 裁剪页；可嵌入 → 整页原站；否则 → 原站公开图片 / 自制示意大图
function playFull(id){
  var i=BY[id], f=LIVE[id], m=M[id]||{}; if(!i)return;
  var bar=function(tag,src){return '<div class="pbar">'+tag+'<b>'+esc(shown(i.name))+'</b><a class="b ghost sm" href="'+esc(src)+'" target="_blank" rel="noopener noreferrer">'+esc(t('btn_original'))+IC.ext+'</a><button class="ib" data-closeplay aria-label="'+esc(t('close'))+'">'+IC.x+'</button></div>'};
  if(f||m.frame){
    var src=f?f.live.src:i.url;
    if(id==='libraries-dev'){var on=document.querySelector('#libTabs .on');if(on)src=LIB+on.dataset.lib+'.html'}
    $('play').innerHTML=bar('<span class="'+(f?'tag-lv':'tag-fr')+'">'+(f?t('tag_live'):t('tag_frame'))+'</span>',src)+'<iframe src="'+esc(src)+'" title="'+esc(shown(i.name))+'" style="color-scheme:'+curTheme()+'" allow="microphone; autoplay; clipboard-write" onload="window.UIHUB_postTheme&&UIHUB_postTheme(this)"></iframe>';
  }else{
    $('play').innerHTML=bar(srcTag(i),i.url)+'<div class="lb">'+(m.img?shotImg(m,'',''):'<div class="lbd">'+demo(i)+'</div>')+
      '<p>'+esc(m.img?t('lb_hint'):t('pv_demo_d'))+'</p><div class="lba"><a class="b pri" href="'+esc(i.url)+'" target="_blank" rel="noopener noreferrer">'+esc(t('btn_original'))+IC.ext+'</a>'+cardActs(i,'lbc')+'</div></div>';
  }
  $('play').hidden=false; document.body.classList.add('lock');
}
function closePlay(){$('play').hidden=true;$('play').innerHTML='';if(!$('sheet').classList.contains('open'))document.body.classList.remove('lock')}

/* ---------- 语言 ---------- */
function applyStatic(){
  document.documentElement.lang=LANG;
  document.querySelectorAll('[data-i18n]').forEach(function(el){el.textContent=t(el.dataset.i18n,{n:ITEMS.length})});
  document.querySelectorAll('[data-i18n-ph]').forEach(function(el){el.placeholder=t(el.dataset.i18nPh)});
  document.querySelectorAll('[data-i18n-aria]').forEach(function(el){el.setAttribute('aria-label',t(el.dataset.i18nAria));el.title=t(el.dataset.i18nAria)});
  var hs=$('hstats'); if(hs){var u=function(f){var s={};ITEMS.forEach(function(i){(i[f]||[]).forEach(function(x){s[x]=1})});return Object.keys(s).length};
    hs.innerHTML=[[ITEMS.length,t('cat_all')],[u('rt'),t('rt_h')],[u('vs'),t('vs_h')],[(I18N.langs||[]).length,t('lang')]].map(function(r){return '<div><dt>'+r[0]+'</dt><dd>'+esc(r[1])+'</dd></div>'}).join('')}
  var sel=$('langSel'); if(sel){sel.value=LANG}
  document.title='UI Hub · '+t('hero_title');
}
function setLang(l){
  if(!I18N[l])return; LANG=l; try{localStorage.setItem('uihub.lang',l)}catch(e){}
  syncStyleNames(); applyStatic(); renderFeat(); renderGuides(); refresh();
  var id=$('sheet').classList.contains('open')&&$('sheet').dataset.id; if(id)openSheet(id);
}

/* ---------- 通用 ---------- */
var inApp=false; window.addEventListener('hashchange',function(){inApp=true});
function back(){if(inApp)history.back();else location.hash='#/'}
function toast(x){var el=$('toast');el.textContent=x;el.classList.add('show');clearTimeout(toast.t);toast.t=setTimeout(function(){el.classList.remove('show')},x.length>30?3200:1600)}
function copy(x,msg){
  function fb(){var a=document.createElement('textarea');a.value=x;a.setAttribute('readonly','');a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();a.setSelectionRange(0,x.length);try{document.execCommand('copy');toast(msg)}catch(e){prompt('',x)}document.body.removeChild(a)}
  if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(x).then(function(){toast(msg)},fb);else fb();
}
function syncFav(id){document.querySelectorAll('[data-fav="'+id+'"]').forEach(function(b){b.classList.toggle('on',!!favs[id])})}
function toggleFav(id){if(favs[id])delete favs[id];else favs[id]=Date.now();LS.set('favs',favs);toast(favs[id]?t('toast_fav'):t('toast_unfav'));syncFav(id);$('favCnt').textContent=Object.keys(favs).length||'';if(state.view==='fav'){renderChips();renderGrid()}}
function refresh(){closeMenu();renderChips();renderGrid()}
function setView(v){
  state.view=v; $('home').hidden=v==='guides'; $('guides').hidden=v!=='guides';
  $('hero').hidden=$('featWrap').hidden=v==='fav';
  document.querySelectorAll('[data-v]').forEach(function(a){a.classList.toggle('on',a.dataset.v===v)});
  if(v!=='guides')refresh();
}
function route(){
  var h=location.hash.replace(/^#\/?/,'');
  if(h.indexOf('r/')===0){if(state.view==='guides')setView('home');openSheet(decodeURIComponent(h.slice(2)));return}
  closeSheet();
  if(h==='guides'){setView('guides');scrollTo(0,0)}else if(h==='fav'){state.type='all';state.rt='';state.vs='';setView('fav');scrollTo(0,0)}else if(state.view!=='home')setView('home');
}
function focusSearch(){if(state.view!=='home')location.hash='#/';setTimeout(function(){var q=$('q');q.scrollIntoView({behavior:'smooth',block:'center'});q.focus({preventScroll:true})},60)}

document.addEventListener('click',function(e){
  var mb=e.target.closest('[data-more]'); if(mb){e.preventDefault();e.stopPropagation();openMenu(mb.dataset.more,mb);return}
  if(!$('menu').hidden&&(!e.target.closest('#menu')||e.target.closest('.mi')))closeMenu();
  var el=e.target.closest('#gridMore,[data-copy],[data-cp],[data-cc],[data-cpo],[data-cco],[data-tip],[data-fav],[data-type],[data-rt],[data-vs],[data-ct],[data-tag],[data-close],[data-closeplay],[data-rmtag],[data-g],[data-play],[data-lib],[data-site-load],[data-ts],[data-open],a');
  if(!el)return;
  if(el.tagName==='A'&&!el.dataset.g){e.stopPropagation();return}
  if(el.dataset.copy){e.preventDefault();copy(el.dataset.copy,el.dataset.msg||t('toast_link'));return}
  if(el.dataset.cp){e.preventDefault();copy(promptFor(BY[el.dataset.cp]),t('toast_prompt'));return}
  if(el.dataset.cc){e.preventDefault();copy(codeOf(BY[el.dataset.cc]),t('toast_code'));return}
  if(el.dataset.cpo){e.preventDefault();copy(promptParts(BY[el.dataset.cpo]).o,t('toast_prompt'));return}
  if(el.id==='gridMore'){moreGrid();return}
  if(el.dataset.cco){e.preventDefault();copy(codeParts(BY[el.dataset.cco]).o,t('toast_code'));return}
  if(el.dataset.tip){e.preventDefault();toast(el.dataset.tip);return}
  if(el.dataset.fav){e.preventDefault();e.stopPropagation();toggleFav(el.dataset.fav);return}
  if(el.dataset.type){state.type=el.dataset.type;refresh();return}
  if(el.dataset.rt!=null&&el.classList.contains('chip')){state.rt=state.rt===el.dataset.rt?'':el.dataset.rt;refresh();return}
  if(el.dataset.vs!=null&&el.classList.contains('chip')){state.vs=state.vs===el.dataset.vs?'':el.dataset.vs;refresh();return}
  if(el.dataset.rt!=null||el.dataset.vs!=null){e.preventDefault();closeSheet();state.rt=el.dataset.rt||'';state.vs=el.dataset.vs||'';state.ct='';state.tag='';location.hash='#/';refresh();setTimeout(function(){$('catalog').scrollIntoView({behavior:'smooth'})},120);return}
  if(el.dataset.ct!=null&&el.classList.contains('chip')){state.ct=state.ct===el.dataset.ct?'':el.dataset.ct;refresh();return}
  if(el.dataset.tag!=null&&el.classList.contains('chip')){state.tag=state.tag===el.dataset.tag?'':el.dataset.tag;refresh();return}
  if(el.hasAttribute('data-close')){back();return}
  if(el.hasAttribute('data-closeplay')){closePlay();return}
  if(el.dataset.play){e.stopPropagation();playFull(el.dataset.play);return}
  if(el.dataset.lib){
    document.querySelectorAll('#libTabs button').forEach(function(b){b.classList.toggle('on',b===el)});
    var box=$('sheet').querySelector('.live'); unloadLive(box); box.dataset.live=LIB+el.dataset.lib+'.html';
    var p=box.querySelector('.poster'); var pm={voice:1,orbs:1,beam:1,metal:'libmetal',gooey:1,image:1}[el.dataset.lib];
    p.style.visibility=pm?'':'hidden'; if(pm)p.src='previews/live-'+(pm===1?el.dataset.lib:pm)+'.webp';
    el.scrollIntoView({inline:'center',block:'nearest',behavior:'smooth'}); loadLive(box); return}
  if(el.dataset.ts){var pw=el.closest('.pvw');if(pw){pw.dataset.ts=el.dataset.ts}return}
  if(el.dataset.siteLoad){var w=el.closest('.site-wrap');var tw=w.parentNode.querySelector('.tsw');tw&&tw.remove();w.outerHTML=siteBox(el.dataset.siteLoad);var sb=$('sheet').querySelector('.site');track($('sheet'));loadSite(sb);return}
  if(el.dataset.rmtag!=null){var id=$('sheet').dataset.id;utags[id].splice(+el.dataset.rmtag,1);if(!utags[id].length)delete utags[id];LS.set('tags',utags);openSheet(id);refresh();return}
  if(el.dataset.g){e.preventDefault();closeSheet();location.hash='#/guides';setTimeout(function(){var g=$('g-'+el.dataset.g);g&&g.scrollIntoView({behavior:'smooth'})},80);return}
  if(el.dataset.open){if(!$('play').hidden)closePlay();location.hash='#/r/'+el.dataset.open}
});
document.addEventListener('submit',function(e){
  var f=e.target; if(!f.dataset.addtag)return; e.preventDefault();
  var v=f.t.value.trim(); if(!v)return; var id=f.dataset.addtag;
  (utags[id]=utags[id]||[]); if(utags[id].indexOf(v)<0&&BY[id].tags.indexOf(v)<0)utags[id].push(v);
  LS.set('tags',utags); openSheet(id); refresh(); toast(t('toast_tag'));
});
$('scrim').addEventListener('click',back);
$('searchOpen').addEventListener('click',focusSearch);
var qt; $('q').addEventListener('input',function(e){clearTimeout(qt);qt=setTimeout(function(){
  state.q=e.target.value.trim(); renderGrid();
  if(state.q&&$('catalog').getBoundingClientRect().top>innerHeight*.6)$('catalog').scrollIntoView({behavior:'smooth'});
},160)});
document.addEventListener('keydown',function(e){
  if(e.key==='/'&&!/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)){e.preventDefault();focusSearch()}
  if(e.key==='Escape'){if(!$('menu').hidden)closeMenu();else if(!$('play').hidden)closePlay();else if($('sheet').classList.contains('open'))back()}
});
$('themeBtn').addEventListener('click',function(){var r=document.documentElement,n=r.dataset.theme==='dark'?'light':'dark';r.dataset.theme=n;try{applyTheme(n);localStorage.setItem('uihub.theme5',n);var mt=document.querySelector('meta[name=theme-color]');mt&&mt.setAttribute('content',n==='dark'?'#06070b':'#f5f6fa')}catch(e){}});
(function(){var sel=$('langSel');if(!sel)return;sel.innerHTML=I18N.langs.map(function(l){return '<option value="'+l[0]+'">'+l[1]+'</option>'}).join('');sel.addEventListener('change',function(){setLang(sel.value)})})();
(function(){var y0=null,s=$('sheet');s.addEventListener('touchstart',function(e){y0=s.scrollTop<=0&&!e.target.closest('.live,.site,.pv-tabs')?e.touches[0].clientY:null},{passive:true});
 s.addEventListener('touchend',function(e){if(y0!=null&&e.changedTouches[0].clientY-y0>90)back();y0=null},{passive:true})})();
addEventListener('scroll',function(){if(menuFor&&!isSheetMenu())closeMenu()},{passive:true});
addEventListener('resize',closeMenu);
addEventListener('scroll',function(){$('top').classList.toggle('scrolled',scrollY>8)},{passive:true});
window.addEventListener('hashchange',route);
syncStyleNames(); applyStatic(); renderFeat(); renderGuides(); setView("home"); route();
})();
