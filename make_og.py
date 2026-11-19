#!/usr/bin/env python3
"""og.png 1200x630 — The Commons Bookstore (2x supersample).
Poster share art: cream paper field, double-rule frame, tracked brick eyebrow,
ink serif masthead, brick hours line, bookshelf spine motif. Shop identity only
— no builder markers, no photo claims. Deliberately the inverse of the dark
sibling share cards.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
S = 2
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "og.png")

PAPER = (247, 242, 231); PAPER2 = (239, 230, 212); CARD = (255, 253, 247)
INK = (36, 29, 20); INK2 = (70, 60, 44); MUTE = (109, 98, 80)
BRICK = (165, 67, 42); GREEN = (51, 96, 74); GOLD = (138, 109, 53)
NAVY = (45, 74, 107); PLUM = (107, 74, 99); RULE = (217, 207, 186); RULE2 = (169, 155, 128)

def font(paths, size):
    bases = ["/System/Library/Fonts/", "/System/Library/Fonts/Supplemental/"]
    for b in bases:
        for n in paths:
            p = b + n
            if os.path.exists(p):
                try: return ImageFont.truetype(p, size * S)
                except Exception: pass
    return ImageFont.load_default()

serif = lambda s: font(["Iowan Old Style Bold.ttc", "Palatino Bold.ttc", "Georgia Bold.ttf", "Times New Roman Bold.ttf"], s)
sans  = lambda s: font(["Avenir Next.ttc", "HelveticaNeue.ttc", "Helvetica.ttc"], s)

img = Image.new("RGB", (W * S, H * S), PAPER)
d = ImageDraw.Draw(img)
px = lambda x, y: (int(x * S), int(y * S))

# faint laid-paper horizontal texture
for yy in range(40, H - 20, 26):
    d.line([px(0, yy), px(W, yy)], fill=PAPER2, width=1 * S)

def tracked(x, y, text, fnt, fill, sp):
    cx = x * S
    for ch in text:
        d.text((cx, y * S), ch, font=fnt, fill=fill)
        cx += d.textlength(ch, font=fnt) + sp * S

def left(x, y, text, fnt, fill):
    d.text((x * S, y * S), text, font=fnt, fill=fill)

tracked(72, 84, "NONFICTION-FIRST BOOKSTORE · KANSAS CITY, MO", sans(21), BRICK, 2.6)
tracked(68, 128, "THE COMMONS", serif(118), INK, 1.4)
left(72, 292, "A new bookstore on Troost Avenue.", sans(25), INK2)
left(72, 330, "Memoirs · society & power · politics · kids' books · gifts", sans(20), MUTE)
d.rectangle([72 * S, 384 * S, (72 + 340) * S, (384 + 4) * S], fill=BRICK)
left(72, 410, "Now open — Wed–Sat, 11am–7pm", sans(24), INK)
left(72, 448, "5508 Troost Ave · Kansas City, MO 64110", sans(21), MUTE)
left(72, 482, "(816) 200-1545", sans(21), MUTE)

# bookshelf motif (right): spines standing on a shelf board
shelf_x, shelf_base = 760, 508
spines = [
    (0,   44, BRICK),  (52, 62, GREEN),  (120, 38, GOLD),
    (164, 70, NAVY),   (240, 50, PLUM),  (296, 58, INK2),
    (358, 40, BRICK),  (404, 66, GOLD),  (476, 46, GREEN),
]
for dx, w, c in spines:
    h = 210 + (w * 137) % 96          # deterministic varied heights 210..305
    d.rectangle([px(shelf_x + dx, shelf_base - h), px(shelf_x + dx + w - 8, shelf_base)], fill=c)
    # two hairline title bands near the top of each spine
    d.line([px(shelf_x + dx + 7, shelf_base - h + 26), px(shelf_x + dx + w - 15, shelf_base - h + 26)], fill=PAPER, width=1 * S)
    d.line([px(shelf_x + dx + 7, shelf_base - h + 40), px(shelf_x + dx + w - 15, shelf_base - h + 40)], fill=PAPER, width=1 * S)
# shelf board + bracket
d.rectangle([px(shelf_x - 18, shelf_base), px(shelf_x + 540, shelf_base + 12)], fill=INK)
d.rectangle([px(shelf_x - 18, shelf_base + 12), px(shelf_x + 540, shelf_base + 18)], fill=RULE2)

# double-rule frame (letterpress)
d.rectangle([16 * S, 16 * S, (W - 16) * S, (H - 16) * S], outline=RULE2, width=2 * S)
d.rectangle([24 * S, 24 * S, (W - 24) * S, (H - 24) * S], outline=INK, width=1 * S)

img = img.resize((W, H), Image.LANCZOS)
img.save(OUT, "PNG", optimize=True)
print("og.png", os.path.getsize(OUT), "bytes")
