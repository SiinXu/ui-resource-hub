/* hero preview: results jump in the filter rail (mirrors #catTitle/#meta, existing i18n) + React Bits Tilted Card on gallery prints */
(function(){var go=document.getElementById('hxGo'),ct=document.getElementById('catTitle'),me=document.getElementById('meta');
function upd(){if(!me.textContent)return;go.innerHTML='';var s=document.createElement('span');s.textContent=ct.textContent+' · '+me.textContent.split(' · ')[0].split(' / ')[0];var b=document.createElement('b');b.setAttribute('aria-hidden','true');b.textContent='\u2193';go.appendChild(s);go.appendChild(b)}
if(go&&me&&window.MutationObserver){new MutationObserver(upd).observe(me,{childList:true,characterData:true,subtree:true});go.addEventListener('click',function(){document.getElementById('catalog').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth'})})}
var tip=document.getElementById('hxTip');if(!tip||!matchMedia('(pointer:fine)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
var A=10,raf=0,ev=null,cur=null;
function frame(){raf=0;if(!cur||!ev)return;var r=cur.getBoundingClientRect(),x=(ev.clientX-r.left)/r.width-.5,y=(ev.clientY-r.top)/r.height-.5,f=cur.firstChild;f.style.setProperty('--ry',(x*A*2).toFixed(2)+'deg');f.style.setProperty('--rx',(-y*A*2).toFixed(2)+'deg');tip.style.transform='translate('+(ev.clientX+14)+'px,'+(ev.clientY+16)+'px)'}
document.querySelectorAll('.hx-p').forEach(function(p){p.addEventListener('pointerenter',function(){cur=p;tip.textContent=p.getAttribute('data-cap');tip.style.opacity='1'});
p.addEventListener('pointermove',function(e){ev=e;if(!raf)raf=requestAnimationFrame(frame)});
p.addEventListener('pointerleave',function(){cur=null;tip.style.opacity='0';p.firstChild.style.removeProperty('--rx');p.firstChild.style.removeProperty('--ry')})})})();
