#!/usr/bin/env python3
"""
Mach Lilies — bespoke media art panels (replace all stock photography).

Generative, on-brand abstract artwork for every capability, case study and the
studio visual. One visual language: warm ink ground, fine dot grid, the Mach
Lily watermark, electric-chartreuse motifs. Rendered as crisp 2x PNG via Pillow.

Run:  python3 tools/generate_media.py
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_brand_assets import mark_polys, INK, INK2, ACCENT, ACCENT2, ACCENTD, BONE
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = os.path.join(ROOT, "assets", "media")
os.makedirs(MEDIA, exist_ok=True)

MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

def mix(a, b, t): return tuple(int(a[i] + (b[i]-a[i])*t) for i in range(3))
LINE  = mix(INK, BONE, 0.10)
LINE2 = mix(INK, BONE, 0.20)
DIMB  = mix(INK, BONE, 0.45)
ACCD  = mix(INK, ACCENT, 0.55)
ACCF  = mix(INK, ACCENT, 0.28)

SS = 2  # supersample

class Panel:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.W, self.H = w*SS, h*SS
        self.img = Image.new("RGB", (self.W, self.H), INK)
        self.d = ImageDraw.Draw(self.img)
        self._ground()

    def s(self, v): return int(round(v*SS))

    def _ground(self):
        d, W, H = self.d, self.W, self.H
        for y in range(H):                      # vertical ink gradient
            t = y/H
            d.line([(0, y), (W, y)], fill=mix(INK, INK2, t))
        step = self.s(28)                       # dot grid
        for y in range(step, H, step):
            for x in range(step, W, step):
                d.point((x, y), fill=LINE)
        # corner accent wash (very soft)
        self.glow(W*0.85, H*0.2, self.s(220), ACCENT, steps=10, maxa=0.10)

    def glow(self, cx, cy, r, color, steps=9, maxa=0.22):
        for i in range(steps, 0, -1):
            rr = r*i/steps
            t = maxa*(1-(i-1)/steps)
            self.d.ellipse([cx-rr, cy-rr, cx+rr, cy+rr], fill=mix(INK, color, t))

    def watermark(self, cx, cy, R):
        polys, _ = mark_polys(cx, cy, R)
        for points, _l in polys:
            self.d.line(points + [points[0]], fill=ACCF, width=self.s(1), joint="curve")

    def frame(self):
        self.d.rectangle([self.s(14), self.s(14), self.W-self.s(14), self.H-self.s(14)],
                         outline=LINE2, width=self.s(1))

    def spaced(self, x, y, text, font, fill, ls):
        for ch in text:
            self.d.text((x, y), ch, font=font, fill=fill)
            x += self.d.textlength(ch, font=font) + ls

    def label(self, idx, name):
        f = ImageFont.truetype(MONO, self.s(11))
        self.spaced(self.s(26), self.s(26), "MACH LILIES", f, DIMB, self.s(2))
        self.spaced(self.W-self.s(26)-self._tw("/ "+idx, f, self.s(2)), self.s(26), "/ "+idx, f, ACCENT, self.s(2))
        fn = ImageFont.truetype(MONO, self.s(12))
        self.spaced(self.s(26), self.H-self.s(34), name.upper(), fn, mix(INK, BONE, 0.7), self.s(3))

    def _tw(self, text, font, ls):
        return sum(self.d.textlength(c, font=font)+ls for c in text)

    def line(self, pts, fill, w=1, joint="curve"):
        self.d.line([(self.s(x), self.s(y)) for x, y in pts], fill=fill, width=self.s(w), joint=joint)

    def dot(self, x, y, r, fill, outline=None, ow=0):
        self.d.ellipse([self.s(x-r), self.s(y-r), self.s(x+r), self.s(y+r)],
                       fill=fill, outline=outline, width=self.s(ow) if ow else 1)

    def rect(self, x, y, w, h, fill=None, outline=None, ow=1, rad=0):
        box = [self.s(x), self.s(y), self.s(x+w), self.s(y+h)]
        if rad:
            self.d.rounded_rectangle(box, radius=self.s(rad), fill=fill, outline=outline, width=self.s(ow))
        else:
            self.d.rectangle(box, fill=fill, outline=outline, width=self.s(ow))

    def arc(self, cx, cy, r, a0, a1, fill, w=1):
        self.d.arc([self.s(cx-r), self.s(cy-r), self.s(cx+r), self.s(cy+r)], a0, a1, fill=fill, width=self.s(w))

    def text(self, x, y, s, font, fill):
        self.d.text((self.s(x), self.s(y)), s, font=ImageFont.truetype(font, self.s(font_sz_cache[0])), fill=fill)

    def save(self, name):
        out = self.img.resize((self.w, self.h), Image.LANCZOS)
        out.save(os.path.join(MEDIA, name))
        return out

font_sz_cache = [20]

# ----------------------------------------------------------------------------
# motifs (drawn in panel coordinate space = w x h, before supersample scaling)
# ----------------------------------------------------------------------------
def m_engineering(p):
    cx, cy = p.w*0.5, p.h*0.52
    # connection nodes around
    nodes = [(cx-160, cy-90), (cx+170, cy-60), (cx+150, cy+95), (cx-150, cy+90)]
    for nx, ny in nodes:
        p.line([(cx, cy), (nx, ny)], LINE2, 1)
    for nx, ny in nodes:
        p.dot(nx, ny, 7, INK, outline=ACCENT, ow=2)
    # central "module" card
    cardw, cardh = 230, 150
    p.rect(cx-cardw/2, cy-cardh/2, cardw, cardh, fill=mix(INK, BONE, 0.04), outline=ACCENT, ow=2, rad=10)
    p.dot(cx-cardw/2+18, cy-cardh/2+16, 4, ACCENT)
    p.dot(cx-cardw/2+34, cy-cardh/2+16, 4, ACCD)
    p.dot(cx-cardw/2+50, cy-cardh/2+16, 4, DIMB)
    for i, lw in enumerate([150, 110, 170, 90, 130]):
        col = ACCENT if i == 2 else LINE2
        p.rect(cx-cardw/2+18, cy-cardh/2+40+i*18, lw, 6, fill=col, rad=3)

def m_ai(p):
    cols = [p.w*0.30, p.w*0.5, p.w*0.70]
    rows = {0: [p.h*0.30, p.h*0.5, p.h*0.70], 1: [p.h*0.24, p.h*0.42, p.h*0.60, p.h*0.78], 2: [p.h*0.34, p.h*0.5, p.h*0.66]}
    pts = {i: [(cols[i], y) for y in rows[i]] for i in range(3)}
    for a in pts[0]:
        for b in pts[1]:
            p.line([a, b], LINE, 1)
    for a in pts[1]:
        for b in pts[2]:
            p.line([a, b], LINE, 1)
    p.glow(p.s(p.w*0.5), p.s(p.h*0.5), p.s(70), ACCENT, steps=8, maxa=0.30)
    for i in range(3):
        for (x, y) in pts[i]:
            if abs(x-p.w*0.5) < 1 and abs(y-p.h*0.5) < 1:
                p.dot(x, y, 11, ACCENT)
            else:
                p.dot(x, y, 7, INK, outline=mix(INK, BONE, 0.6), ow=2)

def m_cloud(p):
    cx, cy = p.w*0.5, p.h*0.46
    for r in (60, 105, 150):
        p.d.ellipse([p.s(cx-r), p.s(cy-r*0.5), p.s(cx+r), p.s(cy+r*0.5)], outline=LINE2, width=p.s(1))
    p.glow(p.s(cx), p.s(cy), p.s(40), ACCENT, steps=7, maxa=0.28)
    p.dot(cx, cy, 13, ACCENT)
    import math as _m
    for k, r in enumerate((60, 105, 150)):
        ang = _m.radians(35 + k*60)
        sx, sy = cx + r*_m.cos(ang), cy + (r*0.5)*_m.sin(ang)
        p.dot(sx, sy, 6, INK, outline=ACCENT, ow=2)
    # stacked platform slabs
    for i in range(3):
        w = 250 - i*40
        p.rect(cx-w/2, p.h*0.72 + i*16, w, 12, fill=mix(INK, ACCENT, 0.16 + i*0.18), rad=6)

def m_data(p):
    base = p.h*0.74
    xs = [p.w*0.22 + i*((p.w*0.56)/6) for i in range(7)]
    hs = [50, 80, 65, 110, 95, 140, 120]
    p.line([(p.w*0.16, base), (p.w*0.84, base)], LINE2, 1)
    for i, x in enumerate(xs):
        col = ACCENT if i in (3, 5) else mix(INK, BONE, 0.16)
        p.rect(x-14, base-hs[i], 28, hs[i], fill=col, rad=4)
    line_pts = [(x, base-hs[i]-24) for i, x in enumerate(xs)]
    p.line(line_pts, ACCENT, 2)
    for x, y in line_pts:
        p.dot(x, y, 4, INK, outline=ACCENT, ow=2)

def m_design(p):
    # bezier curve with handles
    a, b = (p.w*0.18, p.h*0.72), (p.w*0.82, p.h*0.34)
    c1, c2 = (p.w*0.42, p.h*0.10), (p.w*0.60, p.h*0.95)
    pts = []
    for i in range(61):
        t = i/60; mt = 1-t
        x = mt**3*a[0]+3*mt*mt*t*c1[0]+3*mt*t*t*c2[0]+t**3*b[0]
        y = mt**3*a[1]+3*mt*mt*t*c1[1]+3*mt*t*t*c2[1]+t**3*b[1]
        pts.append((x, y))
    p.line(pts, ACCENT, 2)
    for hp, anchor in ((c1, a), (c2, b)):
        # dashed handle
        steps = 14
        for k in range(0, steps, 2):
            x0 = anchor[0]+(hp[0]-anchor[0])*k/steps; y0 = anchor[1]+(hp[1]-anchor[1])*k/steps
            x1 = anchor[0]+(hp[0]-anchor[0])*(k+1)/steps; y1 = anchor[1]+(hp[1]-anchor[1])*(k+1)/steps
            p.line([(x0, y0), (x1, y1)], LINE2, 1)
        p.dot(hp[0], hp[1], 6, INK, outline=ACCENT, ow=2)
    for x, y in (a, b):
        p.dot(x, y, 7, ACCENT)
    f = ImageFont.truetype(SERIF, p.s(78))
    p.d.text((p.s(p.w*0.62), p.s(p.h*0.55)), "Aa", font=f, fill=mix(INK, BONE, 0.5))

def m_strategy(p):
    # roadmap path with milestones
    pts = [(p.w*0.14, p.h*0.72), (p.w*0.34, p.h*0.46), (p.w*0.52, p.h*0.60), (p.w*0.72, p.h*0.32), (p.w*0.88, p.h*0.44)]
    p.line(pts, LINE2, 2)
    for i, (x, y) in enumerate(pts):
        if i == 3:
            p.glow(p.s(x), p.s(y), p.s(34), ACCENT, steps=6, maxa=0.28)
            p.dot(x, y, 9, ACCENT)
            p.line([(x, y), (x, y-34)], ACCENT, 2)
            p.rect(x, y-44, 30, 18, fill=ACCENT, rad=3)
        else:
            p.dot(x, y, 6, INK, outline=mix(INK, BONE, 0.6), ow=2)
    # compass
    cx, cy = p.w*0.80, p.h*0.74
    for r in (22, 34):
        p.dot(cx, cy, r, None, outline=LINE2, ow=1)
    p.line([(cx, cy-30), (cx, cy+30)], LINE, 1)
    p.line([(cx-30, cy), (cx+30, cy)], LINE, 1)
    p.line([(cx, cy+18), (cx-8, cy-2), (cx, cy-22), (cx+8, cy-2), (cx, cy+18)], ACCENT, 2)

def m_trading(p):
    base = p.h*0.5
    xs = [p.w*0.20 + i*((p.w*0.6)/8) for i in range(9)]
    seq = [(-30, 40), (-10, 55), (-50, 20), (10, 70), (-20, 60), (20, 90), (-15, 75), (30, 110), (10, 95)]
    trend = []
    for i, x in enumerate(xs):
        lo, hi = seq[i]
        top = base - hi*0.7; bot = base - lo*0.7
        up = hi >= 70
        col = ACCENT if up else mix(INK, BONE, 0.30)
        p.line([(x, top-16), (x, bot+16)], col, 1)         # wick
        p.rect(x-7, min(top, bot), 14, abs(top-bot)+1, fill=col, rad=2)
        trend.append((x, top-22))
    p.line(trend, ACCD, 2)
    p.dot(trend[-1][0], trend[-1][1], 6, ACCENT)

def m_health(p):
    midy = p.h*0.5
    x0, x1 = p.w*0.12, p.w*0.88
    pts = [(x0, midy)]
    seg = [(0.30, 0), (0.40, -10), (0.46, 60), (0.52, -90), (0.58, 30), (0.66, 0), (1.0, 0)]
    for fx, dy in seg:
        pts.append((x0 + (x1-x0)*fx, midy - dy))
    p.line(pts, ACCENT, 2)
    p.glow(p.s(x0 + (x1-x0)*0.52), p.s(midy-90), p.s(26), ACCENT, steps=6, maxa=0.25)
    # plus / cross node
    cx, cy = p.w*0.80, p.h*0.30
    p.dot(cx, cy, 22, INK, outline=ACCENT, ow=2)
    p.rect(cx-9, cy-3, 18, 6, fill=ACCENT, rad=3)
    p.rect(cx-3, cy-9, 6, 18, fill=ACCENT, rad=3)
    for fx in (0.30, 0.66):
        p.dot(x0 + (x1-x0)*fx, midy, 4, INK, outline=mix(INK, BONE, 0.6), ow=2)

def m_logistics(p):
    # faint map grid
    for gx in range(1, 7):
        p.line([(p.w*gx/7, p.h*0.16), (p.w*gx/7, p.h*0.86)], LINE, 1)
    for gy in range(1, 5):
        p.line([(p.w*0.10, p.h*gy/5), (p.w*0.90, p.h*gy/5)], LINE, 1)
    way = [(p.w*0.16, p.h*0.70), (p.w*0.34, p.h*0.40), (p.w*0.55, p.h*0.62), (p.w*0.74, p.h*0.30), (p.w*0.86, p.h*0.56)]
    # route (dashed accent)
    for i in range(len(way)-1):
        ax, ay = way[i]; bx, by = way[i+1]
        steps = 16
        for k in range(0, steps, 2):
            p.line([(ax+(bx-ax)*k/steps, ay+(by-ay)*k/steps),
                    (ax+(bx-ax)*(k+1)/steps, ay+(by-ay)*(k+1)/steps)], ACCENT, 2)
    for i, (x, y) in enumerate(way):
        if i in (0, len(way)-1):
            p.dot(x, y-16, 9, ACCENT)                       # pin head
            p.line([(x, y-9), (x, y)], ACCENT, 2)
            p.dot(x, y-16, 3, INK)
        else:
            p.dot(x, y, 5, INK, outline=mix(INK, BONE, 0.6), ow=2)

def m_commerce(p):
    # dashboard tiles
    ox, oy = p.w*0.16, p.h*0.22
    tw, th, gap = 120, 70, 18
    for r in range(2):
        for c in range(3):
            x = ox + c*(tw+gap); y = oy + r*(th+gap)
            p.rect(x, y, tw, th, fill=mix(INK, BONE, 0.05), outline=LINE2, ow=1, rad=8)
            if r == 0 and c == 0:
                # donut
                p.arc(x+tw/2, y+th/2, 22, 0, 360, LINE2, 4)
                p.arc(x+tw/2, y+th/2, 22, -90, 150, ACCENT, 4)
            elif r == 0 and c == 2:
                for i, bh in enumerate([18, 30, 24, 40]):
                    p.rect(x+16+i*22, y+th-12-bh, 12, bh, fill=ACCENT if i == 3 else LINE2, rad=2)
            else:
                p.rect(x+14, y+20, 80, 6, fill=LINE2, rad=3)
                p.rect(x+14, y+36, 54, 6, fill=ACCENT if (r+c) % 2 else LINE2, rad=3)
    # up arrow
    ax, ay = p.w*0.5, p.h*0.80
    p.line([(p.w*0.20, p.h*0.86), (p.w*0.40, p.h*0.80), (p.w*0.56, p.h*0.83), (p.w*0.80, p.h*0.70)], ACCENT, 2)
    p.line([(p.w*0.80, p.h*0.70), (p.w*0.72, p.h*0.71)], ACCENT, 2)
    p.line([(p.w*0.80, p.h*0.70), (p.w*0.79, p.h*0.78)], ACCENT, 2)

def m_studio(p):
    cx, cy = p.w*0.5, p.h*0.44
    for r in (120, 175, 230):
        p.dot(cx, cy, r, None, outline=LINE, ow=1)
    p.glow(p.s(cx), p.s(cy), p.s(120), ACCENT, steps=10, maxa=0.16)
    polys, (hubx, huby, _) = mark_polys(cx*SS, cy*SS, p.s(150))
    for points, _l in polys:
        p.d.line(points + [points[0]], fill=ACCENT, width=p.s(2), joint="curve")
    p.d.ellipse([hubx-p.s(8), huby-p.s(8), hubx+p.s(8), huby+p.s(8)], fill=ACCENT)
    # orbiting dots
    for k in range(6):
        ang = math.radians(k*60+20)
        for r in (175,):
            p.dot(cx + r*math.cos(ang), cy + r*math.sin(ang), 4, ACCENT if k % 2 == 0 else DIMB)
    f = ImageFont.truetype(MONO, p.s(13))
    p.spaced(p.s(cx)-p.s(108), p.s(p.h*0.88), "MACH SPEED · LILY CRAFT", f, mix(INK, BONE, 0.6), p.s(2))

# ----------------------------------------------------------------------------
PANELS = [
    ("cap-01.png", 720, 520, "01", "Product Engineering", m_engineering),
    ("cap-02.png", 720, 520, "02", "Applied Intelligence", m_ai),
    ("cap-03.png", 720, 520, "03", "Cloud & Platform", m_cloud),
    ("cap-04.png", 720, 520, "04", "Data & Analytics", m_data),
    ("cap-05.png", 720, 520, "05", "Design & Experience", m_design),
    ("cap-06.png", 720, 520, "06", "Strategy & Advisory", m_strategy),
    ("work-01.png", 1200, 820, "01", "CryptoFlow Analytics", m_trading),
    ("work-02.png", 1200, 820, "02", "MediConnect Pro", m_health),
    ("work-03.png", 1200, 820, "03", "Atlas Routing", m_logistics),
    ("work-04.png", 1200, 820, "04", "Verve Commerce OS", m_commerce),
    ("studio.png", 880, 1080, "00", "The Studio", m_studio),
]

def build():
    outs = []
    for name, w, h, idx, label, motif in PANELS:
        p = Panel(w, h)
        motif(p)
        p.watermark(p.W - p.s(70), p.H - p.s(70), p.s(48))
        p.frame()
        p.label(idx, label)
        out = p.save(name)
        outs.append((name, out))
        print("  wrote assets/media/%s (%dx%d)" % (name, w, h))
    # contact sheet
    cols, cell = 4, 320
    rows = (len(outs)+cols-1)//cols
    sheet = Image.new("RGB", (cols*cell, rows*cell), (8, 8, 7))
    for i, (name, im) in enumerate(outs):
        th = im.copy(); th.thumbnail((cell-20, cell-20))
        cxp = (i % cols)*cell + (cell-th.width)//2
        cyp = (i//cols)*cell + (cell-th.height)//2
        sheet.paste(th, (cxp, cyp))
    sheet.save(os.path.join(MEDIA, "_preview.png"))
    print("  wrote assets/media/_preview.png")

if __name__ == "__main__":
    print("== media panels ==")
    build()
    print("done.")
