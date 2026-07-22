"""
generate_tech_stack_v2.py
Generates assets/tech-stack.svg as a FULLY self-contained SVG.
- No external references (GitHub-safe)
- Same dark style as banner, but cyan/teal neural network color
- Technologies shown as glowing pill chips with brand-color accents
- Chips have subtle pulsing animations
"""

W, H = 820, 375

# ----- Neural network nodes (id, x, y, dx, dy, dur, delay) -----
# Placed around the edges so they don't overlap the central chip rows
NODES = [
    (0,  25,  15,  3,  4, 4.1, 0.0),
    (1, 115,   8, -2,  5, 3.7, 0.4),
    (2, 220,  22,  4, -3, 4.8, 0.9),
    (3, 345,  10, -3,  4, 5.0, 0.2),
    (4, 480,   8,  2,  5, 3.9, 0.7),
    (5, 610,  18, -4,  3, 4.3, 1.1),
    (6, 720,   9,  3, -4, 4.6, 0.3),
    (7, 805,  16, -2,  5, 5.1, 0.8),
    (8,  16, 118,  5,  3, 4.5, 0.5),
    (9,  16, 218, -4,  4, 5.2, 0.1),
    (10,808, 115,  3, -5, 4.0, 0.6),
    (11,808, 215, -5,  3, 4.7, 1.0),
    (12, 22, 358,  3, -3, 4.2, 0.3),
    (13,120, 365, -3,  4, 3.8, 0.8),
    (14,255, 355,  4, -2, 5.0, 0.2),
    (15,415, 362, -2,  3, 4.4, 0.6),
    (16,575, 358,  3, -4, 3.6, 1.1),
    (17,705, 365, -3,  3, 4.9, 0.4),
    (18,800, 355,  4, -3, 5.3, 0.7),
]

CONNS = [
    (0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),  # top row
    (0,8),(8,9),(9,12),                           # left side
    (7,10),(10,11),(11,16),                       # right side
    (12,13),(13,14),(14,15),(15,16),(16,17),(17,18),  # bottom
    (2,8),(5,10),(3,14),(4,16),(1,3),(5,7),       # diagonals
]

nd = {n[0]: n for n in NODES}

# ----- Tech chip data (name, brand_color) -----
CHIP_GAP = 10
CHIP_H   = 31
CHIP_R   = 5

def chip_w(name):
    return max(int(len(name) * 7.2 + 28), 55)

SECTIONS = [
    ("AI  &amp;  DATA  SCIENCE", 60, [
        ("Python",       "#3776AB"),
        ("TensorFlow",   "#FF6F00"),
        ("PyTorch",      "#EE4C2C"),
        ("Scikit-learn", "#F7931E"),
        ("Pandas",       "#150458"),
        ("NumPy",        "#4DABCF"),
        ("Seaborn",      "#4C72B0"),
    ]),
    ("BACKEND  &amp;  DATABASES", 157, [
        ("FastAPI",      "#009688"),
        ("PostgreSQL",   "#4169E1"),
        ("MongoDB",      "#47A248"),
        ("Streamlit",    "#FF4B4B"),
        ("Git",          "#F05032"),
    ]),
    ("ADDITIONAL", 250, [
        ("C",    "#00599C"),
        ("C++",  "#00599C"),
        ("Java", "#ED8B00"),
    ]),
]


def chip_row_x_start(names):
    total = sum(chip_w(n) for n in names) + CHIP_GAP * (len(names) - 1)
    return (W - total) // 2


# ── Build SVG ──────────────────────────────────────────────────────────────────
def build():
    L = []
    a = L.append

    a('<?xml version="1.0" encoding="utf-8"?>')
    a(f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">')
    a('  <defs>')

    # Background gradient
    a('    <linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%">')
    a('      <stop offset="0%"   style="stop-color:#04040F"/>')
    a('      <stop offset="50%"  style="stop-color:#07071A"/>')
    a('      <stop offset="100%" style="stop-color:#040415"/>')
    a('    </linearGradient>')

    # Node glow filter
    a('    <filter id="ng" x="-70%" y="-70%" width="240%" height="240%">')
    a('      <feGaussianBlur stdDeviation="2.5" result="b"/>')
    a('      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>')
    a('    </filter>')

    # Chip glow filter
    a('    <filter id="cg" x="-20%" y="-40%" width="140%" height="180%">')
    a('      <feGaussianBlur stdDeviation="3" result="b"/>')
    a('      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>')
    a('    </filter>')

    # Chip shimmer gradient
    a('    <linearGradient id="chipShimmer" x1="0%" y1="0%" x2="100%" y2="0%">')
    a('      <stop offset="0%"   stop-color="#ffffff" stop-opacity="0"/>')
    a('      <stop offset="45%"  stop-color="#ffffff" stop-opacity="0"/>')
    a('      <stop offset="50%"  stop-color="#ffffff" stop-opacity="0.08"/>')
    a('      <stop offset="55%"  stop-color="#ffffff" stop-opacity="0"/>')
    a('      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>')
    a('      <animate attributeName="x1" values="-100%;0%;200%" dur="5s" begin="0s" repeatCount="indefinite"/>')
    a('      <animate attributeName="x2" values="0%;100%;300%"  dur="5s" begin="0s" repeatCount="indefinite"/>')
    a('    </linearGradient>')

    a('  </defs>')
    a('')
    # Background
    a(f'  <rect width="{W}" height="{H}" fill="url(#bgG)" rx="12" ry="12"/>')
    a(f'  <rect width="240" height="{H}" fill="#00D4FF" opacity="0.025" rx="12" ry="12"/>')
    a(f'  <rect x="{W-240}" y="0" width="240" height="{H}" fill="#00B4D8" opacity="0.02" rx="12" ry="12"/>')
    a('')

    # ── Neural network connections (CYAN theme) ──
    a('  <!-- Neural Network (cyan) -->')
    a('  <g stroke="#00D4FF" stroke-width="0.6" fill="none">')
    for idx, (ai, bi) in enumerate(CONNS):
        na, nb = nd[ai], nd[bi]
        delay = round((idx * 0.21) % 4.0, 2)
        dur   = round(2.5 + (idx % 6) * 0.45, 1)
        a(f'    <line x1="{na[1]}" y1="{na[2]}" x2="{nb[1]}" y2="{nb[2]}">')
        a(f'      <animate attributeName="opacity" values="0.06;0.35;0.06" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>')
        a(f'    </line>')
    a('  </g>')
    a('')

    # ── Neural network nodes ──
    for n in NODES:
        nid, x, y, dx, dy, dur, delay = n
        r = 2.5 if (y < 30 or y > 340) else 3.0
        a(f'  <circle cx="{x}" cy="{y}" r="{r}" fill="#00D4FF" filter="url(#ng)">')
        a(f'    <animateTransform attributeName="transform" type="translate"')
        a(f'      values="0,0;{dx},{dy};0,0;{-dx},{-dy};0,0"')
        a(f'      dur="{dur}s" begin="{delay}s" repeatCount="indefinite"')
        a(f'      calcMode="spline" keySplines="0.45,0,0.55,1;0.45,0,0.55,1;0.45,0,0.55,1;0.45,0,0.55,1"/>')
        a(f'    <animate attributeName="opacity" values="0.4;0.85;0.4" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>')
        a(f'  </circle>')
    a('')

    # ── Section chips ──
    chip_pulse_delays = [0.0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4]

    for sec_label, label_y, chips in SECTIONS:
        names = [c[0] for c in chips]
        widths = [chip_w(n) for n in names]
        sx = chip_row_x_start(names)

        # Section label
        a(f'  <text x="{W//2}" y="{label_y}" font-family="\'Courier New\', monospace" font-size="10"')
        a(f'    text-anchor="middle" fill="#00D4FF" letter-spacing="4" font-weight="600">{sec_label}</text>')

        # Thin divider
        a(f'  <line x1="80" y1="{label_y+6}" x2="{W-80}" y2="{label_y+6}" stroke="#00D4FF" stroke-width="0.4" stroke-opacity="0.2"/>')

        chip_y = label_y + 16  # top of chip row
        cx = sx
        for i, (name, color) in enumerate(chips):
            cw = widths[i]
            pd = chip_pulse_delays[i % len(chip_pulse_delays)]
            pd2 = round(pd + 0.15, 2)
            dur_chip = round(3.0 + i * 0.3, 1)

            a(f'  <!-- chip: {name} -->')
            a(f'  <g opacity="0">')
            a(f'    <animate attributeName="opacity" values="0;1" begin="{pd}s" dur="0.5s" fill="freeze"/>')

            # Background rect
            a(f'    <rect x="{cx}" y="{chip_y}" width="{cw}" height="{CHIP_H}" rx="{CHIP_R}"')
            a(f'      fill="#0A0A20" stroke="{color}" stroke-width="0.6" stroke-opacity="0.5"/>')

            # Brand accent left bar
            a(f'    <rect x="{cx}" y="{chip_y+4}" width="3" height="{CHIP_H-8}" rx="1.5" fill="{color}" opacity="0.9"/>')

            # Shimmer overlay
            a(f'    <rect x="{cx}" y="{chip_y}" width="{cw}" height="{CHIP_H}" rx="{CHIP_R}" fill="url(#chipShimmer)"/>')

            # Name text
            tx = cx + cw // 2 + 2
            ty = chip_y + CHIP_H // 2 + 4
            a(f'    <text x="{tx}" y="{ty}" font-family="\'Courier New\', monospace" font-size="11"')
            a(f'      text-anchor="middle" fill="#D8D8F8" font-weight="500">{name}</text>')

            # Subtle pulsing glow on the border
            a(f'    <rect x="{cx}" y="{chip_y}" width="{cw}" height="{CHIP_H}" rx="{CHIP_R}"')
            a(f'      fill="none" stroke="{color}" stroke-width="1.5" stroke-opacity="0">')
            a(f'      <animate attributeName="stroke-opacity" values="0;0.3;0" dur="{dur_chip}s" begin="{pd2}s" repeatCount="indefinite"/>')
            a(f'    </rect>')

            a(f'  </g>')
            cx += cw + CHIP_GAP
        a('')

    a('</svg>')
    return '\n'.join(L)


if __name__ == '__main__':
    import os
    os.makedirs('assets', exist_ok=True)
    svg = build()
    out = 'assets/tech-stack.svg'
    with open(out, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Done -> {out}")
    print(f"Size: {len(svg)} bytes")
