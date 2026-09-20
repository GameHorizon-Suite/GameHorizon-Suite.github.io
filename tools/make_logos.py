"""Make white-background logos transparent, cleanly.

Emblem (logo.png): edge flood-fill from the four corners removes only the
exterior white + anti-aliased halo, preserving the bright cream/moon interior.

Banner (logo_flat.png): feathered near-white removal so letter counters (o/e/a)
become transparent and the halo is feathered out.
"""
from PIL import Image, ImageDraw

SRC = "/Users/raymondwang/workspace/code/benchmark/Paper/Project_page/assets"
DST = "/Users/raymondwang/workspace/code/GameHorizon-Suite.github.io/assets"

def _finish(im, dst, max_w):
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    if im.width > max_w:
        h = round(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.LANCZOS)
    im.save(dst)
    print("wrote", dst, im.size)

def key_emblem(src, dst, max_w, thresh=55):
    im = Image.open(src).convert("RGBA")
    rgb = im.convert("RGB")
    seed = (255, 0, 255)
    w, h = rgb.size
    for c in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]:
        ImageDraw.floodfill(rgb, c, seed, thresh=thresh)
    src_px = im.load(); mark = rgb.load()
    for y in range(h):
        for x in range(w):
            if mark[x, y] == seed:
                r, g, b, a = src_px[x, y]
                src_px[x, y] = (r, g, b, 0)
    _finish(im, dst, max_w)

def key_text(src, dst, max_w, hi=248, lo=232):
    im = Image.open(src).convert("RGBA")
    out = []
    for r, g, b, a in im.getdata():
        m = min(r, g, b)
        if m >= hi:
            na = 0
        elif m <= lo:
            na = a
        else:
            na = int(a * (hi - m) / (hi - lo))
        out.append((r, g, b, na))
    im.putdata(out)
    _finish(im, dst, max_w)

key_emblem(f"{SRC}/logo.png", f"{DST}/logo.png", 600)
key_text(f"{SRC}/gamehorizon_logo_flat.png", f"{DST}/logo_flat.png", 900)
