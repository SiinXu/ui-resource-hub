#!/usr/bin/env python3
"""Local-only: add 「质感动效」section + 2 entries. No push/deploy."""
import json, os, re, shutil
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
U = ROOT / '_ued'
ns = {}
exec((U / 'items_q.py').read_text(encoding='utf-8'), ns)
NEW = ns['Q']
SEC_SHORT = '质感动效 · 新增'
SEC_TITLE = '十七、质感动效（Transitions.dev / 物理冲击波参考）· 2026-11 新增'
LANGS7 = ['en','ja','ko','ms','es','de','fr']
VI = {
 'ued-transitions-dev-craft': 'Thư viện chuyển động UI và công cụ agent của Jakub Antalik: 43+ chuyển cảnh trên site; Skill miễn phí ~27+ lõi (npx skills add Jakubantalik/transitions.dev; tooling MIT); Pro (~12$/tháng) mở công thức React/TS và Pro Skill — không sao chép mã Pro, chỉ liên kết; transitions-agent miễn phí chấm điểm cục bộ (MIT); Builder MCP cần Pro/Business. Phù hợp: mở hộp thoại, hiện panel, đổi trang, dấu thành công. Tránh: hiệu ứng toàn màn hình, làm giảm khả năng đọc, chồng trang trí lên điều khiển thường dùng. Bắt buộc: prefers-reduced-motion → mờ dần hoặc tắt. Giấy phép: dùng không giới hạn trong sản phẩm; không tái phân phối thư viện; Pro chỉ liên kết https://transitions.dev/pro.html.',
 'ued-kubai-shockwave-ref': 'Tham chiếu X (tác giả Kubai @Kubai087, bài 2119359092334743735, 2026-11-08). Sáu lớp: ảnh chụp trang, biến dạng thấu kính, tách kênh RGB ±8%, bốn vòng màu, khúc xạ cạnh, phản chiếu đường viền; tên bảng màu Aurora / Halo / Frost / Spark (không ghi hex chưa xác minh). Chỉ tham khảo — không có giấy phép mã; không sao chép nguồn. Phù hợp: phản hồi hoàn thành hiếm, một nhịp hero landing. Tránh: trang đọc dài, form thường xuyên, UI ưu tiên a11y, vòng lặp toàn màn hình. Giảm chuyển động: dưới prefers-reduced-motion, fade tại chỗ nửa cường độ, 600ms.',
}
SEC_I18N = {
 'zh-CN': '质感动效 · 新增',
 'zh-TW': '質感動效 · 新增',
 'en': 'Craft motion · new',
 'ja': '質感モーション・新着',
 'ko': '질감 모션 · 신규',
 'ms': 'Animasi berkualiti · baharu',
 'vi': 'Chuyển động chất cảm · mới',
 'es': 'Motion con craft · nuevo',
 'de': 'Craft-Motion · neu',
 'fr': 'Motion craft · nouveau',
}

# --- patch build_ued.py SEC map (idempotent) ---
bp = (ROOT / 'build_ued.py').read_text(encoding='utf-8')
if "'Q':" not in bp:
  bp = bp.replace(
    "'A': ('AI Coding × 设计', '十六、AI Coding × 设计：工作流、工具、DESIGN.md、课程与资讯')}",
    "'A': ('AI Coding × 设计', '十六、AI Coding × 设计：工作流、工具、DESIGN.md、课程与资讯'),\n"
    f"       'Q': ({SEC_SHORT!r}, {SEC_TITLE!r})}}"
  )
  bp = bp.replace(
    "for f in ('items_a.py','items_b.py','items_c.py','items_d.py'): exec(open(os.path.join(U, f), encoding='utf-8').read(), ns)\nNEW = ns['A'] + ns['B'] + ns['C'] + ns['D']",
    "for f in ('items_a.py','items_b.py','items_c.py','items_d.py','items_q.py'): exec(open(os.path.join(U, f), encoding='utf-8').read(), ns)\nNEW = ns['A'] + ns['B'] + ns['C'] + ns['D'] + ns.get('Q', [])"
  )
  (ROOT / 'build_ued.py').write_text(bp, encoding='utf-8')
  print('build_ued.py patched')
else:
  print('build_ued.py already has Q')

# --- data.json ---
d = json.loads((ROOT / 'data.json').read_text(encoding='utf-8'))
# remove prior craft-motion batch if re-run
items = [i for i in d['items'] if i.get('batch') != 'craft-motion-q']
have = {i['url'].rstrip('/') for i in items}
have_id = {i['id'] for i in items}
added = []
for x in NEW:
  key, sec, typ, name, url, rt, vs, price, src = x[:9]
  zh = x[9]
  rid = 'ued-' + key
  if url.rstrip('/') in have or rid in have_id:
    print('skip dup', rid); continue
  rts = rt.split()
  tags = []
  for r in rts:
    tags.append({'motion':'动效','skill':'Skill','mcp':'MCP','inspiration':'灵感'}.get(r, r))
  tags = list(dict.fromkeys(tags))
  it = dict(id=rid, name=name, url=url, note=zh, type=typ, section=SEC_SHORT, sectionTitle=SEC_TITLE,
            sectionDesc='', source=src, pricing=price, tags=tags, ct=['motion'] if 'motion' in rts else [],
            rt=rts, vs=vs.split(), batch='craft-motion-q')
  added.append(it); have.add(url.rstrip('/')); have_id.add(rid)
items = added + items
d['items'] = items; d['count'] = len(items)
(ROOT / 'data.json').write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding='utf-8')
(ROOT / 'data.js').write_text('window.UI_DATA=' + json.dumps(d, ensure_ascii=False) + ';\n', encoding='utf-8')
print('data added', [i['id'] for i in added], 'total', d['count'])

# --- notes ---
def rjs(f, pre):
  s = (ROOT / f).read_text(encoding='utf-8'); return json.loads(s[len(pre):].rstrip().rstrip(';'))
def wjs(f, pre, o):
  (ROOT / f).write_text(pre + json.dumps(o, ensure_ascii=False) + ';\n', encoding='utf-8')

NI = json.loads((ROOT / 'notes_src' / 'notes_i18n.json').read_text(encoding='utf-8'))
NOTES = rjs('notes.js', 'window.UI_NOTES=')
for x in NEW:
  rid = 'ued-' + x[0]
  for k, lang in enumerate(LANGS7):
    NI.setdefault('notes', {}).setdefault(lang, {})[rid] = x[10 + k]
    NOTES.setdefault('notes', {}).setdefault(lang, {})[rid] = x[10 + k]
  if rid in VI:
    NI['notes'].setdefault('vi', {})[rid] = VI[rid]
    NOTES['notes'].setdefault('vi', {})[rid] = VI[rid]
(ROOT / 'notes_src' / 'notes_i18n.json').write_text(json.dumps(NI, ensure_ascii=False, indent=1), encoding='utf-8')
wjs('notes.js', 'window.UI_NOTES=', NOTES)
print('notes ok')

# --- legal ---
LG = rjs('legal.js', 'window.UI_LEGAL=')
for it in added:
  if it['id'].endswith('kubai-shockwave-ref'):
    LG[it['id']] = {'k': 'svc', 'note': 'reference-only; no code license'}
  elif it['pricing'] == 'freemium':
    LG[it['id']] = {'k': 'paid'}  # freemium / Pro gated; no republished code
  else:
    LG[it['id']] = {'k': 'unk'}
wjs('legal.js', 'window.UI_LEGAL=', LG)

# --- i18n: append sec + SEC_ORDER (idempotent marker) ---
marker = '/* craft-motion-q：质感动效 */'
i18n = (ROOT / 'i18n.js').read_text(encoding='utf-8')
if marker in i18n:
  # strip old block
  i18n = i18n[:i18n.index(marker)]
block = marker + '\n(function(){\n'
block += f'var SO=window.UI_SEC_ORDER=window.UI_SEC_ORDER||[],K={SEC_SHORT!r},n=SO.indexOf(K);if(n<0)n=SO.push(K)-1;\n'
block += 'var A=' + json.dumps(SEC_I18N, ensure_ascii=False) + ';\n'
block += "Object.keys(A).forEach(function(l){var d=window.UI_I18N[l];if(!d)return;if(d['sec_'+n]==null)d['sec_'+n]=A[l];});\n"
block += '})();\n'
(ROOT / 'i18n.js').write_text(i18n + block, encoding='utf-8')
print('i18n ok')

# verify no CJK in non-zh/ja notes for new ids
CJK = re.compile(r'[\u3400-\u9fff]')
for rid, langs in NI['notes'].items():
  pass
for lang in ['en','ko','ms','es','de','fr','vi']:
  for rid in ('ued-transitions-dev-craft','ued-kubai-shockwave-ref'):
    t = NI['notes'].get(lang, {}).get(rid, '')
    if CJK.search(t):
      raise SystemExit(f'CJK in {lang} {rid}: {CJK.findall(t)[:6]}')
print('CJK check ok')
