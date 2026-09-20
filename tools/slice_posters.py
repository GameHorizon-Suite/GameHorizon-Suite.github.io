"""Slice the provided 7x3 poster grid into 21 individual posters."""
from PIL import Image
import os

SRC = "/Users/raymondwang/.cursor/projects/Users-raymondwang-workspace-code-search-idea/assets/image-4e6d27af-3ff8-4ad1-b404-3728dd725461.jpg"
DST = "/Users/raymondwang/workspace/code/GameHorizon-Suite.github.io/assets/posters"
os.makedirs(DST, exist_ok=True)

NAMES = [
    ["Valorant","RedDeadRedemption","GTA5","TheWitcher3","WutheringWaves","Palworld","Minecraft"],
    ["Cyberpunk2077","EscapeFromTarkov","EldenRing","RocoKingdomWorld","PUBG","DeltaForce","GenshinImpact"],
    ["AssassinsCreed","ApexLegends","EldenRingNightreign","BlackMythWukong","NTE","WatchDogs","HonorOfKingsWorld"],
]

im = Image.open(SRC).convert("RGB")
W, H = im.size
COLS, ROWS = 7, 3
cw, ch = W / COLS, H / ROWS
inset = 3  # trim thin separators

for r in range(ROWS):
    for c in range(COLS):
        left = round(c * cw) + inset
        upper = round(r * ch) + inset
        right = round((c + 1) * cw) - inset
        lower = round((r + 1) * ch) - inset
        tile = im.crop((left, upper, right, lower))
        name = NAMES[r][c]
        tile.save(f"{DST}/{name}.jpg", quality=92)
        print("saved", name, tile.size)
print("total:", sum(len(r) for r in NAMES))
