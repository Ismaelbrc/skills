import math, random

# ---- Brand constants -------------------------------------------------
INK = "#3A2317"          # primary text / dark ink
INK_SOFT = "#6b5645"
RUST = "#C9491F"         # primary brand colour (fire/ember)
RUST_SOFT = "#E2A98C"    # pale rust, used for inner ring / tints
GOLD = "#E8A63C"         # sun accent
CREAM = "#FCF8F1"        # light background (paper)
CREAM_DEEP = "#F3ECDF"
CHARCOAL = "#20140D"     # dark background (reverse version)
CHARCOAL_TEXT = "#F3E9DC"

FONT_DISPLAY = "Poiret One"
FONT_SUPPORT = "Outfit"
FONT_MONO = "DM Mono"

# ---- Organic ring geometry (shared by every lockup) -------------------

def _wobble(theta_deg, harmonics):
    v = 0
    for k, phase in harmonics:
        v += math.sin(math.radians(k*theta_deg + phase)) / k
    return v / sum(1/k for k, _ in harmonics)

def _polar(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r*math.cos(a), cy + r*math.sin(a)

def _organic_circle(cx, cy, radius_fn, n=240):
    pts = [_polar(cx, cy, radius_fn(360*i/n), 360*i/n) for i in range(n+1)]
    d = f"M {pts[0][0]:.2f} {pts[0][1]:.2f} "
    for p in pts[1:]:
        d += f"L {p[0]:.2f} {p[1]:.2f} "
    return d + "Z"

def icon_svg(cx, cy, R=200, stroke=RUST, stroke_soft=RUST_SOFT, dot=RUST, seed_outer=3, seed_inner=11):
    """Returns the Raviva sun/flame ring mark as an SVG fragment, centred on (cx,cy) with outer radius R.

    Every dimension is expressed as a ratio of R (calibrated against the approved R=200
    reference) so the mark is a pure uniform scale at any size — same proportions, same
    wobble, down to the last decimal. Never reintroduce an absolute-pixel offset here.
    """
    random.seed(seed_outer)
    outer_harm = [(2, random.uniform(0,360)), (3, random.uniform(0,360)), (5, random.uniform(0,360))]
    random.seed(seed_inner)
    inner_harm = [(2, random.uniform(0,360)), (4, random.uniform(0,360)), (6, random.uniform(0,360))]

    def outer_r(theta, amp=0.028):
        return R * (1 + amp*_wobble(theta, outer_harm))

    def inner_r(theta, amp=0.032):
        return R*0.67 * (1 + amp*_wobble(theta, inner_harm))

    outer_d = _organic_circle(cx, cy, outer_r)
    inner_d = _organic_circle(cx, cy, inner_r)

    top_ticks = []
    for a in range(-170, -9, 12):
        r_edge = outer_r(a)
        x1, y1 = _polar(cx, cy, r_edge-0.01*R, a)
        x2, y2 = _polar(cx, cy, r_edge+0.13*R, a)
        top_ticks.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{stroke}" stroke-width="{0.04*R:.2f}" stroke-linecap="round"/>')

    flame_pts = []
    n = 9
    for i in range(n):
        a0 = 10 + i*(160/(n-1))
        base_r = outer_r(a0) - 0.03*R
        tip_r = outer_r(a0) - 0.27*R
        xa, ya = _polar(cx, cy, base_r, a0-6)
        xb, yb = _polar(cx, cy, base_r, a0+6)
        xt, yt = _polar(cx, cy, tip_r, a0)
        flame_pts.append(f'<path d="M {xa:.2f} {ya:.2f} L {xt:.2f} {yt:.2f} L {xb:.2f} {yb:.2f} Z" fill="{stroke}"/>')

    return f'''<g>
    <path d="{outer_d}" fill="none" stroke="{stroke}" stroke-width="{0.03*R:.2f}"/>
    <path d="{inner_d}" fill="none" stroke="{stroke_soft}" stroke-width="{0.015*R:.2f}" opacity="0.7"/>
    {"".join(top_ticks)}
    {"".join(flame_pts)}
    <circle cx="{cx}" cy="{cy}" r="{0.07*R:.2f}" fill="{dot}"/>
  </g>'''

def wordmark_svg(cx, y, size=118, color=INK, letter_spacing=14, anchor="middle"):
    return f'<text x="{cx}" y="{y}" font-family="{FONT_DISPLAY}" font-size="{size}" fill="{color}" text-anchor="{anchor}" letter-spacing="{letter_spacing}">R A V I V A</text>'

def tagline_svg(cx, y, size=24, color=RUST, letter_spacing=8, anchor="middle", text="ACENDA A FAÍSCA"):
    return f'<text x="{cx}" y="{y}" font-family="{FONT_SUPPORT}" font-weight="400" font-size="{size}" fill="{color}" text-anchor="{anchor}" letter-spacing="{letter_spacing}">{text}</text>'
