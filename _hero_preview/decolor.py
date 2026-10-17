"""Remove blue/purple/indigo/violet/cyan (hue 170–300°) from CSS/HTML text.
 - saturated (S>=.35): -> accent var (with alpha via color-mix)
 - low-sat tinted greys (S>=.04): -> neutral grey/warm grey of same lightness & alpha
Usage as module: decolor(text, warm_hue, warm_sat)"""
import re, colorsys
HUE_LO, HUE_HI = 170, 300
FAV='8a8580'
def _neutral(r,g,b,wh,ws):
    h,l,s=colorsys.rgb_to_hls(r/255,g/255,b/255)
    R,G,B=colorsys.hls_to_rgb(wh/360,l,ws if 0.04<l<0.97 else 0)
    return round(R*255),round(G*255),round(B*255)
def _map(r,g,b,a,wh,ws,acc):
    h,l,s=colorsys.rgb_to_hls(r/255,g/255,b/255)
    H=h*360
    if not (HUE_LO<=H<=HUE_HI) or s<0.04 or l<0.02 or l>0.985: return None
    if s>=0.35 and 0.25<l<0.9:
        if a is None or a>=0.999: return acc
        return f'color-mix(in srgb,{acc} {round(a*100)}%,transparent)'
    R,G,B=_neutral(r,g,b,wh,ws)
    if a is None or a>=0.999: return '#%02x%02x%02x'%(R,G,B)
    return f'rgba({R},{G},{B},{a:g})'
def decolor(t,wh=35,ws=0.06,acc='var(--acc)',log=None):
    def hexrep(m):
        pre,hx=m.group(1),m.group(2)
        if len(hx) in (3,4): hx=''.join(c*2 for c in hx)
        r,g,b=(int(hx[i:i+2],16) for i in (0,2,4)); a=int(hx[6:8],16)/255 if len(hx)==8 else None
        out=_map(r,g,b,a,wh,ws,acc)
        if out is None: return m.group(0)
        if log is not None: log.append((m.group(0),out))
        if pre=='%23':  # url-encoded inside data URI: only plain hex allowed
            if out.startswith('#'): return '%23'+out[1:]
            return '%23'+FAV
        return out
    t=re.sub(r'(#|%23)([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b',hexrep,t)
    def rgbrep(m):
        nums=re.split(r'[\s,/]+',m.group(2).strip())
        try:
            r,g,b=(float(x) for x in nums[:3]); a=float(nums[3].rstrip('%'))/(100 if nums[3].endswith('%') else 1) if len(nums)>3 else None
        except Exception: return m.group(0)
        out=_map(r,g,b,a,wh,ws,acc)
        if out is None: return m.group(0)
        if log is not None: log.append((m.group(0),out))
        return out
    t=re.sub(r'(rgba?)\(([\d.\s,/%]+)\)',rgbrep,t)
    def hslrep(m):
        nums=re.split(r'[\s,/]+',m.group(2).strip())
        try:
            H=float(nums[0].replace('deg','')); S=float(nums[1].rstrip('%'))/100; L=float(nums[2].rstrip('%'))/100
            a=float(nums[3].rstrip('%'))/(100 if nums[3].endswith('%') else 1) if len(nums)>3 else None
        except Exception: return m.group(0)
        r,g,b=(x*255 for x in colorsys.hls_to_rgb((H%360)/360,L,S))
        out=_map(r,g,b,a,wh,ws,acc)
        if out is None: return m.group(0)
        if log is not None: log.append((m.group(0),out))
        return out
    t=re.sub(r'(hsla?)\(([\d.\s,/%deg]+)\)',hslrep,t)
    return t
def audit(t):
    """return remaining colour literals with hue 170–300 and S>=.04"""
    bad=[]
    for m in re.finditer(r'(?:#|%23)([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b',t):
        hx=m.group(1); hx=''.join(c*2 for c in hx) if len(hx)==3 else hx
        r,g,b=(int(hx[i:i+2],16)/255 for i in (0,2,4)); h,l,s=colorsys.rgb_to_hls(r,g,b)
        if HUE_LO<=h*360<=HUE_HI and s>=.04 and .02<l<.985: bad.append(m.group(0))
    for m in re.finditer(r'rgba?\(([\d.\s,/%]+)\)',t):
        n=re.split(r'[\s,/]+',m.group(1).strip())
        try: r,g,b=(float(x)/255 for x in n[:3])
        except: continue
        h,l,s=colorsys.rgb_to_hls(r,g,b)
        if HUE_LO<=h*360<=HUE_HI and s>=.04 and .02<l<.985: bad.append(m.group(0))
    for m in re.finditer(r'hsla?\(([\d.\s,/%deg]+)\)',t):
        n=re.split(r'[\s,/]+',m.group(1).strip())
        try: H=float(n[0].replace('deg',''));S=float(n[1].rstrip('%'))/100
        except: continue
        if HUE_LO<=H%360<=HUE_HI and S>=.04: bad.append(m.group(0))
    return bad
