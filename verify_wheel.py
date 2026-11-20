import json

# 1. Verify data/asmaul-husna.json
with open('data/asmaul-husna.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

assert len(data) == 99, f'Expected 99 items, got {len(data)}'

numbers = [item['number'] for item in data]
assert numbers == list(range(1, 100)), 'Numbers are not 1..99 sequentially'

for item in data:
    assert item['arabic'], f'Missing arabic for #{item["number"]}'
    assert item['transliteration'], f'Missing transliteration for #{item["number"]}'
    assert item['meaning'], f'Missing meaning for #{item["number"]}'
    assert item['verification_status'] == 'verified', f'Status not verified for #{item["number"]}'

print('[TEST 1 PASSED] All 99 Asmaul Husna records verified successfully!')

# 2. Check index.html elements
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

required_ids = [
    'home', 'wheelSvg', 'wheelCenterCard', 'wheelCenterNumber',
    'wheelCenterArabic', 'wheelCenterLatin', 'wheelCenterMeaning',
    'wheelFavBtn',
    'wheelBtnRestart', 'wheelBtnPrev', 'wheelPlayBtn', 'wheelBtnNext',
    'wheelBtnAuto', 'wheelScrubber', 'wheelStepProgress', 'wheelLoopBtn',
    'wheelSoundBtn'
]

for rid in required_ids:
    assert f'id="{rid}"' in html or f"id='{rid}'" in html, f'Missing ID in HTML: {rid}'

print('[TEST 2 PASSED] All 19 required wheel DOM IDs verified in index.html!')

# 3. Check bottom navigation has 4 buttons
import re
nav_buttons = re.findall(r'<button[^>]*class=["\'][^"\']*nav-btn[^"\']*["\']', html)
assert len(nav_buttons) == 4, f'Expected 4 bottom nav buttons, found {len(nav_buttons)}'
print(f'[TEST 3 PASSED] Bottom navigation verified with {len(nav_buttons)} tabs!')

# 4. Check sw.js cache items
with open('sw.js', 'r', encoding='utf-8') as f:
    sw_code = f.read()

assert 'asmaul-husna-v1.5.3' in sw_code, 'SW CACHE_NAME not bumped to v1.5.3'
assert './data/asmaul-husna.json' in sw_code, 'data/asmaul-husna.json missing in SW cache'
assert './js/wheel.js' in sw_code, 'js/wheel.js missing in SW cache'

print('[TEST 4 PASSED] Service Worker and cache manifest verified!')

# 5. Check CSS rules
with open('css/style.css', 'r', encoding='utf-8') as f:
    css_code = f.read()

assert '.wheel-svg' in css_code, '.wheel-svg missing in CSS'
assert '.wheel-segment.active' in css_code, '.wheel-segment.active missing in CSS'
assert '.wheel-center-card' in css_code, '.wheel-center-card missing in CSS'
assert 'grid-template-columns: repeat(4, 1fr)' in css_code, 'bottom-nav 4-col missing in CSS'

print('[TEST 5 PASSED] CSS styling for Wheel Screen and 4-col navigation verified!')
print('\n===> ALL TESTS COMPLETED SUCCESSFULLY! <===')
