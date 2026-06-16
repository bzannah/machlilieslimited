#!/usr/bin/env python3
"""
Mach Lilies — bespoke brand asset generator.

One source of geometry -> SVG logos/icons (scalable, used on-site & by modern
browsers) AND pixel-identical PNG rasters (for social sharing, iOS, PWA, which
genuinely require raster). Concept: "The Mach Lily" — a two-whorl botanical
bloom (3 outer + 3 inner recurved petals), tilted into motion. Mach + Lily.

Run from repo root:  python3 tools/generate_brand_assets.py
"""

import math, os, struct, zlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
os.makedirs(os.path.join(ASSETS, "media"), exist_ok=True)

# ----------------------------------------------------------------------------
# palette
# ----------------------------------------------------------------------------
INK     = (13, 12, 10)      # #0d0c0a
INK2    = (21, 18, 11)      # #15120b
ACCENT  = (201, 242, 76)    # #c9f24c
ACCENT2 = (230, 255, 156)   # #e6ff9c
ACCENTD = (159, 207, 43)    # deeper stem
BONE    = (241, 235, 220)   # #f1ebdc

def hx(c): return "#%02x%02x%02x" % c

# ----------------------------------------------------------------------------
# geometry — one petal, placed twice in two whorls
# ----------------------------------------------------------------------------
def _cubic(p0, p1, p2, p3, n):
    out = []
    for i in range(n + 1):
        t = i / n; mt = 1 - t
        x = mt**3*p0[0] + 3*mt*mt*t*p1[0] + 3*mt*t*t*p2[0] + t**3*p3[0]
        y = mt**3*p0[1] + 3*mt*mt*t*p1[1] + 3*mt*t*t*p2[1] + t**3*p3[1]
        out.append((x, y))
    return out

def _petal(length, hw, recurve, n=22):
    """A slender, recurved lily petal pointing 'up' (-y) from local origin."""
    base, tip = (0.0, 0.0), (0.0, -length)
    L1 = (-hw*0.80, -length*0.16); L2 = (-hw*0.98 - recurve, -length*0.82)
    R1 = ( hw*0.98 + recurve, -length*0.82); R2 = ( hw*0.80, -length*0.16)
    left  = _cubic(base, L1, L2, tip, n)
    right = _cubic(tip, R1, R2, base, n)
    return left[:-1] + right[:-1]

def _place(pts, ang_deg, cx, cy, s):
    a = math.radians(ang_deg); ca, sa = math.cos(a), math.sin(a)
    out = []
    for (x, y) in pts:
        x *= s; y *= s
        out.append((cx + x*ca - y*sa, cy + x*sa + y*ca))
    return out

def mark_polys(cx, cy, R, tilt=-8.0):
    """Return [(points, 'outer'|'inner'), ...] and core (cx,cy,r) for radius R."""
    outer_len, outer_hw, outer_rc = R*1.00, R*0.300, R*0.06
    inner_len, inner_hw, inner_rc = R*0.70, R*0.250, R*0.04
    po = _petal(outer_len, outer_hw, outer_rc)
    pi = _petal(inner_len, inner_hw, inner_rc)
    polys = []
    for a in (0, 120, 240):
        polys.append((_place(po, a + tilt, cx, cy, 1.0), "outer"))
    for a in (60, 180, 300):
        polys.append((_place(pi, a + tilt, cx, cy, 1.0), "inner"))
    return polys, (cx, cy, R*0.135)

# ============================================================================
# SVG output
# ============================================================================
def _pts(points): return " ".join("%.2f,%.2f" % p for p in points)

def svg_mark_filled(size=100, **kw):
    """Monochrome bloom: accent petals separated by thin ink strokes + seed."""
    cx = cy = size/2; R = size*0.45
    polys, (ccx, ccy, cr) = mark_polys(cx, cy, R)
    sw = size*0.017
    out = []
    for points, layer in polys:  # outer (3) then inner (3) on top
        out.append('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%.2f" stroke-linejoin="round"/>'
                   % (_pts(points), hx(ACCENT), hx(INK), sw))
    out.append('<circle cx="%.2f" cy="%.2f" r="%.2f" fill="%s"/>' % (ccx, ccy, R*0.17, hx(ACCENT)))   # hub
    out.append('<circle cx="%.2f" cy="%.2f" r="%.2f" fill="%s"/>' % (ccx, ccy, R*0.075, hx(INK)))      # seed
    return "\n".join(out)

def svg_mark_line(size=100, color=ACCENT, sw=1.4):
    cx = cy = size/2; R = size*0.45
    polys, (ccx, ccy, cr) = mark_polys(cx, cy, R)
    out = []
    for points, _ in polys:
        out.append('<polygon points="%s" fill="none" stroke="%s" stroke-width="%.2f" stroke-linejoin="round"/>' % (_pts(points), hx(color), sw))
    out.append('<circle cx="%.2f" cy="%.2f" r="%.2f" fill="none" stroke="%s" stroke-width="%.2f"/>' % (ccx, ccy, cr, hx(color), sw))
    return "\n".join(out)

def write(path, content):
    full = os.path.join(ASSETS, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print("  wrote", os.path.relpath(full, ROOT), "(%d B)" % len(content))

def gen_svgs():
    print("SVG logos & icons:")
    # favicon — clean, bold, transparent
    write("favicon.svg",
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">\n%s\n</svg>\n'
        % svg_mark_filled(100, two_tone=True, core="light"))
    # logo mark (transparent, two-tone)
    write("logo-mark.svg",
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">\n%s\n</svg>\n'
        % svg_mark_filled(100, two_tone=True))
    # line mark
    write("logo-mark-line.svg",
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">\n%s\n</svg>\n'
        % svg_mark_line(100))
    # maskable / app icon — mark on ink rounded square, safe-zone padded
    inner = svg_mark_filled(60, two_tone=True)  # 60 within 100 -> ~40% padding
    masklike = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">\n'
        '<rect width="100" height="100" rx="22" fill="%s"/>\n'
        '<g transform="translate(20,20)">%s</g>\n</svg>\n' % (hx(INK), inner))
    write("icon-maskable.svg", masklike)
    # horizontal lockup: mark + wordmark
    lock = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 120" font-family="Fraunces, Georgia, serif">\n'
        '<g transform="translate(0,10)">%s</g>\n'
        '<text x="130" y="62" font-size="52" font-weight="600" fill="%s">Mach<tspan fill="%s"> Lilies</tspan></text>\n'
        '<text x="132" y="92" font-family="\'Space Mono\', monospace" font-size="13" letter-spacing="5" fill="%s">TECHNOLOGY CONSULTANCY</text>\n'
        '</svg>\n' % (
            '<g transform="scale(1.0)">' + svg_mark_filled(100, two_tone=True) + '</g>',
            hx(BONE), hx(ACCENT), hx((139,132,114))))
    write("logo-lockup.svg", lock)
    # og image as svg (on-site + svg-friendly platforms)
    write("og-image.svg", og_svg())

def og_svg():
    W, H = 1200, 630
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d">' % (W, H)]
    parts.append('<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
                 '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>' % (hx(INK), hx(INK2)))
    parts.append('<rect width="%d" height="%d" fill="url(#bg)"/>' % (W, H))
    # dot field
    for y in range(40, H, 34):
        for x in range(40, W, 34):
            parts.append('<circle cx="%d" cy="%d" r="1" fill="%s" opacity="0.06"/>' % (x, y, hx(BONE)))
    # big watermark mark (right)
    polys, (ccx, ccy, cr) = mark_polys(940, 315, 250)
    for points, _ in polys:
        parts.append('<polygon points="%s" fill="none" stroke="%s" stroke-width="2" opacity="0.5"/>' % (_pts(points), hx(ACCENT)))
    # small solid lockup mark (left)
    parts.append('<g transform="translate(90,250)">%s</g>' % svg_mark_filled(86, two_tone=True))
    parts.append('<text x="92" y="300" font-family="\'Space Mono\', monospace" font-size="20" letter-spacing="6" fill="%s">TECHNOLOGY CONSULTANCY</text>' % hx(ACCENT))
    parts.append('<text x="88" y="400" font-family="Fraunces, Georgia, serif" font-size="120" font-weight="600" fill="%s">Mach<tspan fill="%s"> Lilies</tspan></text>' % (hx(BONE), hx(ACCENT)))
    parts.append('<rect x="92" y="440" width="80" height="3" fill="%s"/>' % hx(ACCENT))
    parts.append('<text x="92" y="500" font-family="Fraunces, Georgia, serif" font-style="italic" font-size="34" fill="%s">Mach speed. Lily craft.</text>' % hx(BONE))
    parts.append('<rect x="20" y="20" width="%d" height="%d" fill="none" stroke="%s" stroke-width="1" opacity="0.25"/>' % (W-40, H-40, hx(BONE)))
    parts.append('</svg>')
    return "\n".join(parts) + "\n"

# ============================================================================
# PNG output (Pillow)
# ============================================================================
from PIL import Image, ImageDraw, ImageFont

DEJAVU_SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
DEJAVU_MONO       = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

def _draw_mark_px(d, cx, cy, R, tilt=-8.0):
    polys, (ccx, ccy, cr) = mark_polys(cx, cy, R, tilt)
    sw = max(2, int(round(R*0.034)))
    for points, layer in [p for p in polys if p[1] == "outer"]:
        d.polygon(points, fill=ACCENT, outline=INK, width=sw)
    for points, layer in [p for p in polys if p[1] == "inner"]:
        d.polygon(points, fill=ACCENT, outline=INK, width=sw)
    hub = R*0.17;  d.ellipse([cx-hub, cy-hub, cx+hub, cy+hub], fill=ACCENT)
    seed = R*0.075; d.ellipse([cx-seed, cy-seed, cx+seed, cy+seed], fill=INK)

def render_icon_png(path, size, bg=None, rounded=False, scale_frac=0.92):
    ss = 4; S = size*ss
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if bg is not None:
        if rounded:
            d.rounded_rectangle([0, 0, S-1, S-1], radius=int(S*0.22), fill=bg + (255,))
        else:
            d.rectangle([0, 0, S, S], fill=bg + (255,))
    R = S*scale_frac/2
    _draw_mark_px(d, S/2, S/2, R)
    img = img.resize((size, size), Image.LANCZOS)
    full = os.path.join(ASSETS, path)
    img.save(full)
    print("  wrote", os.path.relpath(full, ROOT), "(%dx%d)" % (size, size))

def _spaced(d, xy, text, font, fill, ls):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        w = d.textlength(ch, font=font)
        x += w + ls
    return x

def render_og_png(path="og-image.png"):
    ss = 2; W, H = 1200, 630
    img = Image.new("RGB", (W*ss, H*ss), INK)
    d = ImageDraw.Draw(img)
    # vertical gradient
    for y in range(H*ss):
        t = y/(H*ss)
        c = tuple(int(INK[i]+(INK2[i]-INK[i])*t) for i in range(3))
        d.line([(0, y), (W*ss, y)], fill=c)
    # dot field
    step = 34*ss
    for y in range(40*ss, H*ss, step):
        for x in range(40*ss, W*ss, step):
            d.ellipse([x, y, x+2, y+2], fill=(BONE[0], BONE[1], BONE[2]))
    # faint big mark outline on right
    polys, (ccx, ccy, cr) = mark_polys(940*ss, 315*ss, 250*ss)
    for points, _ in polys:
        d.line(points + [points[0]], fill=ACCENTD, width=2*ss, joint="curve")
    # solid lockup mark left
    _draw_mark_px(d, 133*ss, 207*ss, 44*ss)
    # text
    f_eyebrow = ImageFont.truetype(DEJAVU_MONO, 20*ss)
    f_title   = ImageFont.truetype(DEJAVU_SERIF_BOLD, 116*ss)
    f_tag     = ImageFont.truetype(DEJAVU_SERIF_BOLD, 30*ss)
    _spaced(d, (92*ss, 286*ss), "TECHNOLOGY CONSULTANCY", f_eyebrow, ACCENT, 6*ss)
    # title with two-tone
    tx, ty = 88*ss, 320*ss
    d.text((tx, ty), "Mach", font=f_title, fill=BONE)
    w_mach = d.textlength("Mach", font=f_title)
    d.text((tx + w_mach, ty), " Lilies", font=f_title, fill=ACCENT)
    d.rectangle([92*ss, 470*ss, 172*ss, 474*ss], fill=ACCENT)
    d.text((92*ss, 500*ss), "Mach speed.  Lily craft.", font=f_tag, fill=BONE)
    # frame
    d.rectangle([20*ss, 20*ss, (W-20)*ss, (H-20)*ss], outline=(60, 56, 44), width=1*ss)
    img = img.resize((W, H), Image.LANCZOS)
    full = os.path.join(ASSETS, path)
    img.save(full, quality=92)
    print("  wrote", os.path.relpath(full, ROOT), "(%dx%d)" % (W, H))

def gen_pngs():
    print("PNG rasters:")
    render_icon_png("favicon-16.png", 16, scale_frac=1.0)
    render_icon_png("favicon-32.png", 32, scale_frac=0.96)
    render_icon_png("favicon-48.png", 48, scale_frac=0.96)
    render_icon_png("apple-touch-icon.png", 180, bg=INK, rounded=True, scale_frac=0.62)
    render_icon_png("icon-192.png", 192, bg=INK, rounded=True, scale_frac=0.62)
    render_icon_png("icon-512.png", 512, bg=INK, rounded=True, scale_frac=0.62)
    render_og_png()

# ============================================================================
# manifest + inline symbols for index.html
# ============================================================================
def gen_manifest():
    man = (
        '{\n'
        '  "name": "Mach Lilies",\n'
        '  "short_name": "Mach Lilies",\n'
        '  "description": "Independent technology consultancy. Mach speed. Lily craft.",\n'
        '  "start_url": "/",\n'
        '  "display": "standalone",\n'
        '  "background_color": "#0d0c0a",\n'
        '  "theme_color": "#0d0c0a",\n'
        '  "icons": [\n'
        '    { "src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable" },\n'
        '    { "src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable" },\n'
        '    { "src": "logo-mark.svg", "sizes": "any", "type": "image/svg+xml" }\n'
        '  ]\n'
        '}\n')
    write("site.webmanifest", man)

def gen_inline_symbols():
    """Emit the <defs> symbol block to paste into index.html."""
    block = (
        '    <svg width="0" height="0" style="position:absolute" aria-hidden="true">\n'
        '        <defs>\n'
        '            <g id="mark">\n'
        + "\n".join("                " + l for l in svg_mark_filled(100, two_tone=True).splitlines())
        + '\n            </g>\n'
        '            <g id="mark-line">\n'
        + "\n".join("                " + l for l in svg_mark_line(100, sw=1.3).splitlines())
        + '\n            </g>\n'
        '        </defs>\n'
        '    </svg>\n')
    with open(os.path.join(ASSETS, "_symbols.html"), "w") as f:
        f.write(block)
    print("  wrote assets/_symbols.html (for index.html injection)")

if __name__ == "__main__":
    print("== Mach Lilies brand asset generator ==")
    gen_svgs()
    gen_pngs()
    gen_manifest()
    gen_inline_symbols()
    print("done.")
