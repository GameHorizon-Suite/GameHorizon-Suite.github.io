"""Make white-background logos transparent and web-sized.

Global near-white keying (not flood fill): removes pure/near-white pixels
everywhere, so letter counters (o/e/a) become transparent too, while the
emblem's cream/blue interior (not near-white) is preserved.
"""
from PIL import Image
import sys

SRC = "/Users/raymondwang/workspace/code/benchmark/Paper/Project_page/assets"
DST = "/Users/raymondwang/workspace/code/GameHorizon-Suite.github.io/assets"

def key_white(src, dst, max_w, thresh=240):
    im = Image.open(src).convert("RGBA")
    px = im.getdata()
    out = []
    for r, g, b, a in px:
        if r >= thresh and g >= thresh and b >= thresh:
            out.append((r, g, b, 0))
        else:
            out.append((r, g, b, a))
    im.putdata(out)
    # trim fully-transparent border
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    # downscale for web
    if im.width > max_w:
        h = round(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.LANCZOS)
    im.save(dst)
    print("wrote", dst, im.size)

key_white(f"{SRC}/logo.png",                 f"{DST}/logo.png",      600)
key_white(f"{SRC}/gamehorizon_logo_flat.png", f"{DST}/logo_flat.png", 900)
