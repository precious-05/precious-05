"""
generate_tech_stack.py
Downloads real SVG icons from skillicons.dev / devicons and creates a self-contained
animated floating tech-stack SVG (assets/tech-stack.svg).

Icons float gently up/down via SMIL animateTransform.
"""

import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
import re, math, time

# ── Icon manifest ──────────────────────────────────────────────────────────────
# (slug, label, source)  source = 'skill' | 'devi' | 'simple' (fallback simple-icons CDN)
ICONS = {
    'row1': [
        ('python',      'Python',      'skill'),
        ('tensorflow',  'TensorFlow',  'skill'),
        ('pytorch',     'PyTorch',     'skill'),
        ('sklearn',     'Sklearn',     'skill'),
        ('pandas',      'Pandas',      'devi'),
        ('numpy',       'NumPy',       'devi'),
    ],
    'row2': [
        ('fastapi',     'FastAPI',     'skill'),
        ('postgres',    'PostgreSQL',  'skill'),
        ('mongodb',     'MongoDB',     'skill'),
        ('streamlit',   'Streamlit',   'skill'),
        ('git',         'Git',         'skill'),
    ],
    'row3': [
        ('c',    'C',    'skill'),
        ('cpp',  'C++',  'skill'),
        ('java', 'Java', 'skill'),
    ],
}

SKILLICONS_URL = "https://skillicons.dev/icons?i={slug}&theme=dark"
DEVICONS_URL   = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/{slug}/{slug}-original.svg"

FALLBACK_COLORS = {
    'python':     '#3776AB', 'tensorflow': '#FF6F00', 'pytorch':    '#EE4C2C',
    'sklearn':    '#F7931E', 'pandas':     '#150458', 'numpy':      '#013243',
    'fastapi':    '#009688', 'postgres':   '#4169E1', 'mongodb':    '#47A248',
    'streamlit':  '#FF4B4B', 'git':        '#F05032', 'c':          '#00599C',
    'cpp':        '#00599C', 'java':       '#007396',
}

HDR = {'User-Agent': 'Mozilla/5.0 (GitHub-README-Generator/1.0)'}

def fetch_svg(url):
    try:
        req = urllib.request.Request(url, headers=HDR)
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.read().decode('utf-8')
    except Exception as e:
        print(f"  WARN: could not fetch {url}: {e}")
        return None

def strip_ns(tag):
    return re.sub(r'\{[^}]+\}', '', tag)

def extract_inner(svg_text):
    """Return the inner group elements of a single-icon SVG as an SVG string snippet."""
    if not svg_text:
        return None
    try:
        svg_text_clean = re.sub(r'xmlns(?::\w+)?="[^"]*"', '', svg_text)
        root = ET.fromstring(svg_text_clean)
        parts = []
        for child in root:
            parts.append(ET.tostring(child, encoding='unicode'))
        return ''.join(parts) if parts else None
    except Exception as e:
        print(f"  WARN: parse error: {e}")
        return None

def fallback_icon(slug, label):
    """Return a simple colored square SVG snippet as fallback."""
    color = FALLBACK_COLORS.get(slug, '#888888')
    initials = label[:3].upper()
    return f'''<rect width="44" height="44" rx="8" fill="{color}"/>
    <text x="22" y="29" font-family="monospace" font-size="12" font-weight="bold" fill="white" text-anchor="middle">{initials}</text>'''

# ── Layout ─────────────────────────────────────────────────────────────────────
W, H = 820, 350
ICON_SIZE = 50   # rendered size of each icon (scaled to this)
SPACING   = 76   # center-to-center spacing

def row_x_start(n):
    total_w = n * SPACING
    return (W - total_w) // 2 + SPACING // 2

ROW_Y = {'row1': 85, 'row2': 185, 'row3': 280}
FLOAT_PARAMS = [
    (4, 5, 3.9, 0.0),  (-3, 6, 4.5, 0.6),  (5, -4, 4.1, 1.2),
    (-4, 4, 5.0, 0.3),  (3, 5, 3.7, 0.9),  (-5, 3, 4.8, 0.5),
    (4, -5, 4.2, 1.1),  (-3, 4, 5.3, 0.2),  (5, 3, 3.6, 0.8),
    (-4, 5, 4.9, 0.4),  (3, -4, 4.0, 1.0),
]

def build_svg():
    symbols = []
    uses    = []
    slug_fp = {}  # slug -> float params
    all_slugs = []

    for row, icon_list in ICONS.items():
        for slug, label, source in icon_list:
            all_slugs.append(slug)

    fp_cycle = FLOAT_PARAMS * (len(all_slugs) // len(FLOAT_PARAMS) + 1)

    for i, slug in enumerate(all_slugs):
        slug_fp[slug] = fp_cycle[i]

    # Fetch and build symbols
    for row, icon_list in ICONS.items():
        n = len(icon_list)
        sx = row_x_start(n)
        cy = ROW_Y[row]

        for j, (slug, label, source) in enumerate(icon_list):
            cx = sx + j * SPACING
            dx, dy, dur, delay = slug_fp[slug]
            sym_id = f"icon_{slug}"

            # Fetch icon SVG
            inner = None
            if source == 'skill':
                url = SKILLICONS_URL.format(slug=slug)
                svg_text = fetch_svg(url)
                inner = extract_inner(svg_text) if svg_text else None
            elif source == 'devi':
                url = DEVICONS_URL.format(slug=slug)
                svg_text = fetch_svg(url)
                inner = extract_inner(svg_text) if svg_text else None

            if inner is None:
                inner = fallback_icon(slug, label)
                viewbox = "0 0 44 44"
            else:
                viewbox = "0 0 48 48"

            symbols.append(f'''  <symbol id="{sym_id}" viewBox="{viewbox}">
    {inner}
  </symbol>''')

            tx_vals = f"0,0;{dx},{dy};0,0;{-dx},{-dy};0,0"
            uses.append(f'''  <!-- {label} -->
  <g>
    <animateTransform attributeName="transform" type="translate"
      values="{tx_vals}" additive="sum"
      dur="{dur}s" begin="{delay}s" repeatCount="indefinite"
      calcMode="spline" keySplines="0.45,0,0.55,1;0.45,0,0.55,1;0.45,0,0.55,1;0.45,0,0.55,1"/>
    <use href="#{sym_id}" x="{cx - ICON_SIZE//2}" y="{cy - ICON_SIZE//2}" width="{ICON_SIZE}" height="{ICON_SIZE}"/>
    <text x="{cx}" y="{cy + ICON_SIZE//2 + 14}" font-family="'Inter', 'Helvetica', sans-serif"
          font-size="10" text-anchor="middle" fill="#8888aa" font-weight="500">{label}</text>
  </g>''')

    # Build section labels
    section_labels = []
    for row, cy in ROW_Y.items():
        if row == 'row1':
            label_text = 'AI &amp; Data Science'
        elif row == 'row2':
            label_text = 'Backend &amp; Databases'
        else:
            label_text = 'Additional'
        section_labels.append(
            f'  <text x="{W//2}" y="{cy - 44}" font-family="\'Inter\', \'Helvetica\', sans-serif" '
            f'font-size="11" text-anchor="middle" fill="#9B5DE5" letter-spacing="3" '
            f'font-weight="600" text-transform="uppercase">{label_text.upper()}</text>'
        )

    # Divider lines
    dividers = []
    for cy in [ROW_Y['row1'], ROW_Y['row2'], ROW_Y['row3']]:
        lx1, lx2 = 80, W - 80
        ly = cy - 40
        dividers.append(
            f'  <line x1="{lx1}" y1="{ly}" x2="{lx2}" y2="{ly}" '
            f'stroke="#9B5DE5" stroke-width="0.5" stroke-opacity="0.25"/>'
        )

    svg = f'''<?xml version="1.0" encoding="utf-8"?>
<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"   style="stop-color:#040410"/>
      <stop offset="100%" style="stop-color:#08081A"/>
    </linearGradient>
{chr(10).join(symbols)}
  </defs>

  <rect width="{W}" height="{H}" fill="url(#bg)" rx="12" ry="12"/>

{chr(10).join(dividers)}
{chr(10).join(section_labels)}
{chr(10).join(uses)}

</svg>'''
    return svg


if __name__ == '__main__':
    import os
    os.makedirs('assets', exist_ok=True)
    print("Building tech stack SVG (fetching icons)...")
    svg = build_svg()
    out = 'assets/tech-stack.svg'
    with open(out, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Done -> {out}")
