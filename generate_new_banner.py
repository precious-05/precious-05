"""
generate_new_banner.py
Generates assets/precious-05-profile-banner.svg with:
- Animated neural network background
- Terminal loading animation
- Welcome glitch text
- Profile section with name + typing tagline
"""

def generate_banner():
    # Node layout: (id, x, y, float_dx, float_dy, dur, delay)
    # Kept away from center text zone (x:170-630, y:75-145)
    nodes = [
        (0, 28, 18, 4, 5, 4.2, 0.0),
        (1, 108, 10, -3, 4, 3.8, 0.5),
        (2, 198, 30, 4, -3, 5.1, 1.0),
        (3, 298, 13, -3, 5, 4.7, 0.3),
        (4, 398, 8,   3, 4, 3.5, 0.8),
        (5, 500, 18, -4, 3, 4.9, 0.2),
        (6, 592, 26,  3,-4, 3.7, 0.7),
        (7, 684, 12, -2, 5, 5.3, 1.1),
        (8, 770, 20,  4,-3, 4.1, 0.4),
        # upper sides
        (9,  58, 62,  4, 4, 4.5, 0.6),
        (10,152, 54, -3, 5, 5.2, 0.1),
        (11,682, 58,  3,-4, 4.3, 0.5),
        (12,770, 70, -4, 3, 3.6, 1.2),
        # lower sides
        (13, 48,140,  5, 3, 4.8, 0.3),
        (14,148,152, -4, 4, 5.0, 0.8),
        (15,660,138,  3, 5, 4.4, 0.2),
        (16,762,148, -5, 3, 3.8, 0.6),
        # bottom row
        (17, 26,182,  3,-4, 4.6, 1.0),
        (18,110,173, -2, 3, 5.4, 0.4),
        (19,210,185,  4,-2, 3.9, 0.7),
        (20,312,176, -3, 4, 4.2, 0.1),
        (21,400,188,  2,-3, 5.1, 0.9),
        (22,492,177, -4, 2, 4.0, 0.5),
        (23,592,185,  3,-4, 3.7, 1.1),
        (24,682,174, -2, 5, 4.8, 0.3),
        (25,770,182,  4,-3, 4.1, 0.8),
    ]

    connections = [
        # top row
        (0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),
        # top to upper sides
        (0,9),(1,9),(1,10),(2,10),(7,11),(8,11),(8,12),
        # upper side cross
        (9,10),(11,12),
        # upper sides to lower sides
        (9,13),(10,14),(11,15),(12,16),
        # lower side cross
        (13,14),(15,16),
        # lower sides to bottom
        (13,17),(13,18),(14,18),(14,19),(14,20),
        (15,22),(15,23),(16,24),(16,25),
        # bottom row
        (17,18),(18,19),(19,20),(20,21),(21,22),(22,23),(23,24),(24,25),
        # some diagonals
        (3,9),(6,11),(10,19),(15,23),
    ]

    nd = {n[0]: n for n in nodes}

    lines = []
    a = lines.append

    a('<?xml version="1.0" encoding="utf-8"?>')
    a('<svg width="800" height="200" viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg">')
    a('  <defs>')
    a('    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
    a('      <stop offset="0%" style="stop-color:#040410"/>')
    a('      <stop offset="50%" style="stop-color:#080818"/>')
    a('      <stop offset="100%" style="stop-color:#040416"/>')
    a('    </linearGradient>')
    a('    <filter id="glow" x="-60%" y="-60%" width="220%" height="220%">')
    a('      <feGaussianBlur stdDeviation="2" result="b"/>')
    a('      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>')
    a('    </filter>')
    a('    <linearGradient id="metalGrad" x1="0%" y1="0%" x2="0%" y2="100%">')
    a('      <stop offset="0%"   stop-color="#ffffff" stop-opacity="1"/>')
    a('      <stop offset="35%"  stop-color="#d8d8f0" stop-opacity="1"/>')
    a('      <stop offset="70%"  stop-color="#a0a0c0" stop-opacity="0.9"/>')
    a('      <stop offset="100%" stop-color="#787898" stop-opacity="0.8"/>')
    a('    </linearGradient>')
    a('    <linearGradient id="shineGrad" x1="0%" y1="0%" x2="100%" y2="0%">')
    a('      <stop offset="0%"   stop-color="#ffffff" stop-opacity="0"/>')
    a('      <stop offset="48%"  stop-color="#ffffff" stop-opacity="0"/>')
    a('      <stop offset="50%"  stop-color="#ffffff" stop-opacity="0.75"/>')
    a('      <stop offset="52%"  stop-color="#ffffff" stop-opacity="0"/>')
    a('      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>')
    a('      <animate attributeName="x1" values="-100%;0%;200%" dur="3.5s" begin="9.5s" repeatCount="indefinite"/>')
    a('      <animate attributeName="x2" values="0%;100%;300%" dur="3.5s" begin="9.5s" repeatCount="indefinite"/>')
    a('    </linearGradient>')
    a('    <!-- Typing reveal mask for tagline -->')
    a('    <mask id="tMask1">')
    a('      <rect x="0" y="0" width="0" height="200" fill="white">')
    a('        <animate attributeName="width" from="0" to="800" dur="1.8s" begin="9.5s" fill="freeze"/>')
    a('      </rect>')
    a('    </mask>')
    a('    <mask id="tMask2">')
    a('      <rect x="0" y="0" width="0" height="200" fill="white">')
    a('        <animate attributeName="width" from="0" to="800" dur="1.5s" begin="11.5s" fill="freeze"/>')
    a('      </rect>')
    a('    </mask>')
    a('    <filter id="emboss">')
    a('      <feGaussianBlur in="SourceAlpha" stdDeviation="0.4" result="b"/>')
    a('      <feOffset in="b" dx="0" dy="0.5" result="ob"/>')
    a('      <feSpecularLighting in="b" surfaceScale="5" specularConstant=".75" specularExponent="20" lighting-color="#aaaacc" result="sp">')
    a('        <fePointLight x="400" y="50" z="90"/>')
    a('      </feSpecularLighting>')
    a('      <feComposite in="sp" in2="SourceAlpha" operator="in" result="sp"/>')
    a('      <feComposite in="SourceGraphic" in2="sp" operator="arithmetic" k1="0" k2="1" k3="1" k4="0"/>')
    a('    </filter>')
    a('  </defs>')
    a('')
    a('  <!-- Background -->')
    a('  <rect width="800" height="200" fill="url(#bgGrad)" rx="10" ry="10"/>')
    a('  <rect width="220" height="200" fill="#4A0E8F" opacity="0.06" rx="10" ry="10"/>')
    a('  <rect x="580" y="0" width="220" height="200" fill="#0E1A55" opacity="0.06" rx="10" ry="10"/>')
    a('')
    a('  <!-- ── NEURAL NETWORK BACKGROUND ── -->')
    a('')
    a('  <!-- Connections -->')
    a('  <g stroke="#9B5DE5" stroke-width="0.6" fill="none">')
    for idx, (ai, bi) in enumerate(connections):
        na, nb = nd[ai], nd[bi]
        delay = round((idx * 0.19) % 3.5, 2)
        dur   = round(2.5 + (idx % 5) * 0.4, 1)
        a(f'    <line x1="{na[1]}" y1="{na[2]}" x2="{nb[1]}" y2="{nb[2]}">')
        a(f'      <animate attributeName="opacity" values="0.10;0.40;0.10" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>')
        a(f'    </line>')
    a('  </g>')
    a('')
    a('  <!-- Nodes -->')
    for n in nodes:
        nid, x, y, dx, dy, dur, delay = n
        r = 2.5 if (y < 35 or y > 165) else 3.0
        a(f'  <circle cx="{x}" cy="{y}" r="{r}" fill="#9B5DE5" filter="url(#glow)">')
        a(f'    <animateTransform attributeName="transform" type="translate"')
        a(f'      values="0,0;{dx},{dy};0,0;{-dx},{-dy};0,0"')
        a(f'      dur="{dur}s" begin="{delay}s" repeatCount="indefinite"')
        a(f'      calcMode="spline" keySplines="0.45,0,0.55,1;0.45,0,0.55,1;0.45,0,0.55,1;0.45,0,0.55,1"/>')
        a(f'    <animate attributeName="opacity" values="0.45;0.80;0.45" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>')
        a(f'  </circle>')
    a('')
    a('  <!-- ── TERMINAL ANIMATION (0 – 3.3 s) ── -->')
    a('  <g id="terminal">')
    a('    <text x="20" y="40" font-family="monospace" font-size="13" fill="#50fa7b">')
    a('      precious-05@github:~$ <tspan fill="#f8f8f2">GET profile precious-05 --verbose</tspan>')
    a('    </text>')
    a('    <text x="20" y="68" font-family="monospace" font-size="15" fill="#bd93f9" font-weight="bold">')
    a('      Loading precious-05\'s profile...')
    a('    </text>')
    a('    <rect x="20" y="86" width="760" height="18" rx="3" fill="#44475a"/>')
    a('    <rect x="20" y="86" width="0" height="18" rx="3" fill="#50fa7b">')
    a('      <animate attributeName="width" values="0;760" dur="2.8s" fill="freeze"/>')
    a('    </rect>')
    a('    <text x="20" y="122" font-family="monospace" font-size="11" fill="#6272a4" opacity="0">')
    a('      Initializing ML profile data...')
    a('      <animate attributeName="opacity" values="0;1" begin="0.4s" dur="0.3s" fill="freeze"/>')
    a('    </text>')
    a('    <text x="20" y="142" font-family="monospace" font-size="11" fill="#6272a4" opacity="0">')
    a('      Fetching repositories and contributions...')
    a('      <animate attributeName="opacity" values="0;1" begin="1.1s" dur="0.3s" fill="freeze"/>')
    a('    </text>')
    a('    <text x="20" y="162" font-family="monospace" font-size="11" fill="#6272a4" opacity="0">')
    a('      Compiling AI/ML project timeline...')
    a('      <animate attributeName="opacity" values="0;1" begin="1.8s" dur="0.3s" fill="freeze"/>')
    a('    </text>')
    a('    <animate attributeName="opacity" values="1;0" begin="3.0s" dur="0.35s" fill="freeze"/>')
    a('  </g>')
    a('')
    a('  <!-- ── WELCOME SECTION (3.3 – 6.5 s) ── -->')
    a('  <g id="welcome" opacity="0">')
    a('    <text x="400" y="105" font-family="Impact, Arial Narrow Bold, sans-serif" font-size="38" text-anchor="middle" fill="#ff5555" opacity="0.45">')
    a('      precious-05')
    a('      <animate attributeName="x" values="400;403;397;401;400" dur="0.5s" begin="3.5s" repeatCount="indefinite"/>')
    a('      <animate attributeName="opacity" values="0.45;0;0.55;0;0.45" dur="0.25s" begin="3.5s" repeatCount="indefinite"/>')
    a('    </text>')
    a('    <text x="400" y="105" font-family="Impact, Arial Narrow Bold, sans-serif" font-size="38" text-anchor="middle" fill="#8be9fd" opacity="0.45">')
    a('      precious-05')
    a('      <animate attributeName="x" values="400;397;403;399;400" dur="0.45s" begin="3.5s" repeatCount="indefinite"/>')
    a('      <animate attributeName="opacity" values="0.45;0;0.65;0;0.45" dur="0.3s" begin="3.5s" repeatCount="indefinite"/>')
    a('    </text>')
    a('    <text x="400" y="105" font-family="Impact, Arial Narrow Bold, sans-serif" font-size="38" text-anchor="middle" fill="#ffffff">')
    a('      precious-05')
    a('      <animate attributeName="x" values="400;399;401;400" dur="0.8s" begin="3.5s" repeatCount="indefinite"/>')
    a('    </text>')
    a('    <text x="400" y="145" font-family="monospace" font-size="15" text-anchor="middle" fill="#bd93f9" opacity="0">')
    a('      Explore my AI &amp; ML projects')
    a('      <animate attributeName="opacity" values="0;1" dur="0.5s" begin="4.0s" fill="freeze"/>')
    a('    </text>')
    a('    <animate attributeName="opacity" values="0;1" begin="3.3s" dur="0.3s" fill="freeze"/>')
    a('    <animate attributeName="opacity" values="1;0" begin="6.2s" dur="0.5s" fill="freeze"/>')
    a('  </g>')
    a('')
    a('  <!-- ── PROFILE SECTION (7 s onwards) ── -->')
    a('  <g id="profile" opacity="0">')
    a('    <!-- Divider line -->')
    a('    <rect x="200" y="98" width="0" height="1.5" fill="#9B5DE5" opacity="0.85">')
    a('      <animate attributeName="width" values="0;400" dur="1.2s" begin="8.0s" fill="freeze"')
    a('        calcMode="spline" keySplines="0.42,0,0.58,1"/>')
    a('    </rect>')
    a('    <!-- Name -->')
    a('    <text x="400" y="88" font-family="Helvetica, Arial, sans-serif" font-size="31" font-weight="bold"')
    a('          text-anchor="middle" fill="url(#metalGrad)" filter="url(#emboss)" opacity="0">')
    a('      Alina Liaquat')
    a('      <animate attributeName="opacity" values="0;1" dur="1.0s" begin="7.3s" fill="freeze"/>')
    a('      <animate attributeName="y" values="98;88" dur="1.0s" begin="7.3s" fill="freeze"')
    a('        calcMode="spline" keySplines="0.34,1.56,0.64,1"/>')
    a('    </text>')
    a('    <text x="400" y="88" font-family="Helvetica, Arial, sans-serif" font-size="31" font-weight="bold"')
    a('          text-anchor="middle" fill="url(#shineGrad)" opacity="0">')
    a('      Alina Liaquat')
    a('      <animate attributeName="opacity" values="0;1" dur="1.0s" begin="7.3s" fill="freeze"/>')
    a('    </text>')
    a('    <!-- Tagline line 1 - typing reveal -->')
    a('    <g mask="url(#tMask1)">')
    a('      <text x="400" y="129" font-family="\'Courier New\', monospace" font-size="13.5" font-weight="600"')
    a('            text-anchor="middle" fill="#8be9fd" letter-spacing="2.5">')
    a('        MACHINE LEARNING  ·  DEEP LEARNING  ·  NLP')
    a('      </text>')
    a('    </g>')
    a('    <!-- Blinking cursor after line 1 -->')
    a('    <rect x="631" y="116" width="7" height="14" fill="#8be9fd" opacity="0">')
    a('      <animate attributeName="opacity" values="0;1" begin="9.5s" dur="0.01s" fill="freeze"/>')
    a('      <animate attributeName="opacity" values="1;0;1;0" dur="0.7s" begin="11.2s" repeatCount="indefinite"/>')
    a('    </rect>')
    a('    <!-- Tagline line 2 - typing reveal -->')
    a('    <g mask="url(#tMask2)">')
    a('      <text x="400" y="157" font-family="\'Courier New\', monospace" font-size="11.5"')
    a('            text-anchor="middle" fill="#bd93f9" letter-spacing="1.5" opacity="0">')
    a('        DATA-DRIVEN AI SYSTEMS  ·  END-TO-END ML DEPLOYMENT')
    a('        <animate attributeName="opacity" values="0;1" begin="11.5s" dur="0.01s" fill="freeze"/>')
    a('      </text>')
    a('    </g>')
    a('    <animate attributeName="opacity" values="0;1" begin="7.0s" dur="0.8s" fill="freeze"/>')
    a('  </g>')
    a('')
    a('</svg>')

    return '\n'.join(lines)


if __name__ == '__main__':
    import os
    os.makedirs('assets', exist_ok=True)
    svg = generate_banner()
    with open('assets/precious-05-profile-banner.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("Banner SVG generated successfully!")
