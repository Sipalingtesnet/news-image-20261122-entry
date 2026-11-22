#!/usr/bin/env python3
"""draw_news.py — deterministic PIL generator for the 22 November 2026 news page.

Writes entry.png (1024x1024) at the repo root. No randomness, no time, no network.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (245, 240, 230)
INK = (25, 25, 25)
RED = (150, 30, 30)
BLUE = (20, 40, 90)
GREEN = (40, 90, 40)
LIGHT = (205, 198, 184)
WATER = (150, 175, 195)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, max_width):
    """Wrap text into lines each no wider than max_width."""
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_lines(draw, text, font, max_width, max_lines):
    """Shorten text from the end until it wraps within max_lines, keeping a period."""
    words = text.rstrip(".").split()
    while True:
        joined = " ".join(words)
        if not joined.endswith("."):
            joined += "."
        lines = wrap(draw, joined, font, max_width)
        if len(lines) <= max_lines:
            return lines
        if len(words) <= 1:
            return lines
        words = words[:-1]


def star_points(cx, cy, outer, inner, n):
    """Points of an n-pointed star centred at (cx, cy)."""
    import math
    pts = []
    for i in range(n * 2):
        r = outer if i % 2 == 0 else inner
        ang = math.pi / 2 + math.pi * i / n
        pts.append((cx + r * math.cos(ang), cy - r * math.sin(ang)))
    return pts
def draw_poland(d, x, y, w, h):
    """NATO shield over a map of Poland with missile trails."""
    # Poland outline (rough polygon)
    pol = [(x + 0.18 * w, y + 0.72 * h), (x + 0.30 * w, y + 0.55 * h),
           (x + 0.42 * w, y + 0.48 * h), (x + 0.60 * w, y + 0.50 * h),
           (x + 0.78 * w, y + 0.58 * h), (x + 0.85 * w, y + 0.72 * h),
           (x + 0.78 * w, y + 0.85 * h), (x + 0.55 * w, y + 0.90 * h),
           (x + 0.30 * w, y + 0.86 * h)]
    d.polygon(pol, fill=(225, 218, 200), outline=INK)
    # missile trails coming down
    d.arc([x + 0.05 * w, y + 0.05 * h, x + 0.45 * w, y + 0.55 * h],
          200, 300, fill=RED, width=3)
    d.arc([x + 0.55 * w, y + 0.05 * h, x + 0.95 * w, y + 0.55 * h],
          240, 320, fill=RED, width=3)
    # small missile heads
    d.ellipse([x + 0.40 * w - 4, y + 0.42 * h - 4, x + 0.40 * w + 4, y + 0.42 * h + 4],
              fill=RED)
    d.ellipse([x + 0.66 * w - 4, y + 0.40 * h - 4, x + 0.66 * w + 4, y + 0.40 * h + 4],
              fill=RED)
    # NATO shield over the map
    cx, cy = x + 0.52 * w, y + 0.62 * h
    sw, sh = 0.34 * w, 0.30 * h
    shield = [(cx - sw / 2, cy - sh / 2), (cx + sw / 2, cy - sh / 2),
              (cx + sw / 2, cy + sh * 0.1), (cx, cy + sh / 2),
              (cx - sw / 2, cy + sh * 0.1)]
    d.polygon(shield, fill=BLUE, outline=INK)
    # compass star inside shield
    d.polygon(star_points(cx, cy, 0.11 * w, 0.045 * w, 8), fill=(235, 230, 215))
    d.ellipse([cx - 0.03 * w, cy - 0.03 * w, cx + 0.03 * w, cy + 0.03 * w],
              fill=BLUE)


def draw_cop(d, x, y, w, h):
    """Sunrise over a globe with a green leaf."""
    # sky band
    d.rectangle([x, y, x + w, y + int(0.45 * h)], fill=(250, 240, 210))
    # rising sun (semicircle)
    sx, sy = x + 0.30 * w, y + 0.42 * h
    d.pieslice([sx - 0.16 * w, sy - 0.16 * w, sx + 0.16 * w, sy + 0.16 * w],
               180, 360, fill=(230, 150, 60))
    # sun rays
    for i in range(6):
        ang = 200 + i * 14
        import math
        a = math.radians(ang)
        x1 = sx + 0.20 * w * math.cos(a)
        y1 = sy + 0.20 * w * math.sin(a)
        x2 = sx + 0.27 * w * math.cos(a)
        y2 = sy + 0.27 * w * math.sin(a)
        d.line([x1, y1, x2, y2], fill=(230, 150, 60), width=3)
    # globe
    gx, gy, gr = x + 0.66 * w, y + 0.55 * h, 0.22 * w
    d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(120, 170, 210), outline=INK)
    d.ellipse([gx - gr, gy - gr * 0.4, gx + gr, gy + gr * 0.4], outline=INK)
    d.ellipse([gx - gr * 0.4, gy - gr, gx + gr * 0.4, gy + gr], outline=INK)
    d.line([gx - gr, gy, gx + gr, gy], fill=INK)
    # green leaf
    lx, ly = x + 0.52 * w, y + 0.80 * h
    d.polygon([(lx, ly), (lx + 0.14 * w, ly - 0.10 * h),
               (lx + 0.28 * w, ly), (lx + 0.14 * w, ly + 0.10 * h)],
              fill=GREEN, outline=INK)
    d.line([lx, ly, lx + 0.28 * w, ly], fill=INK, width=2)
def draw_ship(d, x, y, w, h):
    """Ship on waves with drone silhouettes above."""
    # sky
    d.rectangle([x, y, x + w, y + int(0.55 * h)], fill=(235, 235, 230))
    # waves
    for i in range(3):
        wy = y + (0.62 + 0.12 * i) * h
        d.arc([x + 0.05 * w, wy - 0.06 * h, x + 0.40 * w, wy + 0.06 * h],
              180, 360, fill=WATER, width=3)
        d.arc([x + 0.35 * w, wy - 0.06 * h, x + 0.70 * w, wy + 0.06 * h],
              180, 360, fill=WATER, width=3)
        d.arc([x + 0.65 * w, wy - 0.06 * h, x + 1.0 * w, wy + 0.06 * h],
              180, 360, fill=WATER, width=3)
    # ship hull
    hx, hy = x + 0.50 * w, y + 0.72 * h
    d.polygon([(hx - 0.24 * w, hy), (hx + 0.24 * w, hy),
               (hx + 0.18 * w, hy + 0.10 * h), (hx - 0.18 * w, hy + 0.10 * h)],
              fill=(90, 90, 95), outline=INK)
    # mast
    d.line([hx, hy, hx, hy - 0.22 * h], fill=INK, width=4)
    d.line([hx, hy - 0.22 * h, hx + 0.08 * w, hy - 0.18 * h], fill=INK, width=3)
    # fire on deck
    d.ellipse([hx - 0.05 * w, hy - 0.05 * h, hx + 0.02 * w, hy - 0.01 * h],
              fill=(230, 120, 40))
    # drones above
    for i, (dx, dy) in enumerate([(0.30, 0.22), (0.62, 0.16), (0.80, 0.30)]):
        px, py = x + dx * w, y + dy * h
        d.line([px - 0.05 * w, py, px + 0.05 * w, py], fill=INK, width=3)
        d.line([px, py - 0.05 * h, px, py + 0.05 * h], fill=INK, width=3)


def draw_tankers(d, x, y, w, h):
    """Oil tankers on a strait with a shield."""
    # water
    d.rectangle([x, y + int(0.55 * h), x + w, y + h], fill=(160, 185, 205))
    for i in range(3):
        wy = y + (0.62 + 0.12 * i) * h
        d.line([x + 0.05 * w, wy, x + 0.95 * w, wy], fill=(120, 150, 175), width=2)
    # tanker 1
    t1x, t1y = x + 0.30 * w, y + 0.70 * h
    d.polygon([(t1x - 0.20 * w, t1y), (t1x + 0.20 * w, t1y),
               (t1x + 0.16 * w, t1y + 0.08 * h), (t1x - 0.16 * w, t1y + 0.08 * h)],
              fill=(70, 70, 75), outline=INK)
    d.rectangle([t1x - 0.06 * w, t1y - 0.10 * h, t1x + 0.06 * w, t1y],
                fill=(70, 70, 75), outline=INK)
    # tanker 2
    t2x, t2y = x + 0.72 * w, y + 0.78 * h
    d.polygon([(t2x - 0.18 * w, t2y), (t2x + 0.18 * w, t2y),
               (t2x + 0.14 * w, t2y + 0.07 * h), (t2x - 0.14 * w, t2y + 0.07 * h)],
              fill=(70, 70, 75), outline=INK)
    d.rectangle([t2x - 0.05 * w, t2y - 0.09 * h, t2x + 0.05 * w, t2y],
                fill=(70, 70, 75), outline=INK)
    # shield (defence) - clear outline so it reads as a shield, not a banner
    cx, cy = x + 0.50 * w, y + 0.30 * h
    sw, sh = 0.30 * w, 0.26 * h
    shp = [(cx - sw / 2, cy - sh / 2), (cx + sw / 2, cy - sh / 2),
           (cx + sw / 2, cy + sh * 0.1), (cx, cy + sh / 2),
           (cx - sw / 2, cy + sh * 0.1)]
    d.polygon(shp, fill=(215, 225, 240), outline=INK)
    d.line([shp[0], shp[1], shp[2], shp[3], shp[4], shp[0]], fill=INK, width=3)
    d.polygon(star_points(cx, cy, 0.09 * w, 0.04 * w, 8), fill=INK)


def draw_panel(d, x, y, w, h, label, headline, summary, illust):
    """Draw one story panel."""
    d.rectangle([x, y, x + w, y + h], fill=PAPER, outline=LIGHT, width=2)
    pad = 14
    # section label
    d.text((x + pad, y + 10), label, font=font(FONT_BOLD, 20), fill=RED)
    # headline
    hf = font(FONT_BOLD, 30)
    hlines = wrap(d, headline, hf, w - 2 * pad)
    ty = y + 38
    for ln in hlines[:2]:
        d.text((x + pad, ty), ln, font=hf, fill=INK)
        ty += 36
    # summary
    sf = font(FONT_REG, 20)
    slines = fit_lines(d, summary, sf, w - 2 * pad, 2)
    sy = y + 112
    for ln in slines:
        d.text((x + pad, sy), ln, font=sf, fill=INK)
        sy += 26
    # illustration box
    bx, by = x + pad, y + 172
    bw, bh = w - 2 * pad, h - 172 - 12
    d.rectangle([bx, by, bx + bw, by + bh], fill=(238, 233, 222), outline=LIGHT)
    illust(d, bx + 6, by + 6, bw - 12, bh - 12)
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    title = "THE WORLD IN ONE PICTURE"
    tf = font(FONT_BOLD, 54)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 34), title, font=tf, fill=INK)
    # dateline
    dl = "SUNDAY, 22 NOVEMBER 2026"
    df = font(FONT_BOLD, 26)
    dw = d.textlength(dl, font=df)
    d.text(((W - dw) / 2, 100), dl, font=df, fill=RED)
    # thin rule
    d.rectangle([40, 142, W - 40, 145], fill=RED)

    # ---- Panels (2x2) ----
    margin = 40
    gap = 14
    top = 164
    bottom = 886
    pw = (W - 2 * margin - gap) / 2
    ph = (bottom - top - gap) / 2

    panels = [
        ("WORLD", "NATO STANDS BY POLAND",
         "NATO vows to defend every inch of Poland after Russian missiles landed there.",
         draw_poland),
        ("CLIMATE", "COP31 DEAL AT DAWN",
         "COP31 in Antalya reaches a dawn deal after talks ran past the Friday deadline.",
         draw_cop),
        ("BALTIC", "BALTIC SHIP DRONE STRIKE",
         "A Russian merchant ship caught fire in the Gulf of Finland after a likely drone strike.",
         draw_ship),
        ("GULF", "GULF TENSIONS",
         "Tankers were hit off the Oman coast as Iran-US naval tensions escalate.",
         draw_tankers),
    ]

    for i, (label, headline, summary, illust) in enumerate(panels):
        col = i % 2
        row = i // 2
        px = margin + col * (pw + gap)
        py = top + row * (ph + gap)
        draw_panel(d, px, py, pw, ph, label, headline, summary, illust)

    # ---- Bottom ticker ----
    ty0 = 900
    d.text((40, ty0), "ALSO IN THE NEWS", font=font(FONT_BOLD, 20), fill=RED)
    d.rectangle([40, ty0 + 26, W - 40, ty0 + 28], fill=LIGHT)
    items = [
        "Peru quake, no casualties",
        "Estonia closes Russia border",
        "Denmark: Russia plot to kill rapper",
        "FBI probes database hack",
        "Zelensky calls Putin a killer",
        "Trump threatens AI data-centre ban",
        "Anthropic shares fall after IPO",
        "Cartel arrest sparks Sinaloa violence",
        "Bolsonaro in ICU",
        "India 159-1, trail New Zealand",
        "Australia ends England T20 streak",
    ]
    ticker = "  \u00b7  ".join(items)
    tfont = font(FONT_REG, 18)
    tlines = wrap(d, ticker, tfont, W - 2 * margin)
    ty = ty0 + 32
    for ln in tlines:
        d.text((margin, ty), ln, font=tfont, fill=INK)
        ty += 20

    img.save("entry.png")
    print("wrote entry.png")


if __name__ == "__main__":
    main()