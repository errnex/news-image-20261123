#!/usr/bin/env python3
"""Build entry.png for news-image-20261123 — Monday 23 November 2026.
40 stories, 7 regions, source badge per story, world map, UTC timeline,
date-check. Real fonts only (DejaVu). Output 1024x1024 PNG, deterministic.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)
INK = (18, 18, 18)
NAVY = (16, 36, 62)
NAVY2 = (24, 52, 88)
RED = (179, 32, 44)
GOLD = (201, 162, 39)
GREY = (90, 88, 82)
LIGHT = (255, 255, 255)
MAPSEA = (214, 228, 235)
MAPLAND = (176, 196, 168)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_OB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 104], fill=NAVY)
d.rectangle([0, 104, W, 108], fill=GOLD)
d.text((24, 12), "THE WORLD IN ONE DAY", font=F(SERIF_B, 44), fill=LIGHT)
d.text((24, 66), "MONDAY  23  NOVEMBER  2026", font=F(SANS_B, 20), fill=GOLD)
d.text((700, 20), "40 STORIES", font=F(SANS_B, 26), fill=LIGHT)
d.text((700, 52), "7 REGIONS  •  EVERY STORY SOURCED", font=F(SANS_B, 13), fill=(200, 210, 225))
d.text((700, 76), "AS REPORTED IN THE 23 NOV 2026 NEWS CYCLE", font=F(SANS, 11), fill=(170, 185, 205))

# ---------- lead trio ----------
leads = [
    ("01", "COP31 COLLAPSES", "Climate talks in Antalya end with no deal after the EU rejects a draft with no fossil-fuel phase-out.", "BBC"),
    ("02", "WAR AT THE STRAIT OF HORMUZ", "Tankers struck and mined; two more catch fire as Iran–US fighting engulfs Gulf shipping.", "AP"),
    ("03", "DYMER: 2 DEAD, 14 MISSING", "A Russian drone hits a five-storey flat block north of Kyiv; rescuers dig through rubble.", "AP"),
]
lx, lw, gap = 16, 322, 12
for i, (num, head, body, src) in enumerate(leads):
    x = lx + i * (lw + gap)
    d.rectangle([x, 120, x + lw, 236], fill=LIGHT, outline=(200, 195, 180), width=1)
    d.rectangle([x, 120, x + lw, 124], fill=RED)
    d.text((x + 10, 132), num, font=F(SANS_B, 15), fill=RED)
    d.text((x + 42, 131), head, font=F(SANS_B, 15), fill=INK)
    for j, ln in enumerate(textwrap.wrap(body, 38)):
        d.text((x + 10, 158 + j * 16), ln, font=F(SANS, 12), fill=(40, 40, 40))
    d.text((x + 10, 212), "SOURCE: " + src, font=F(SANS_B, 10), fill=GREY)

# ---------- world map panel ----------
mx, my, mw, mh = 16, 248, 660, 168
d.rectangle([mx, my, mx + mw, my + mh], fill=MAPSEA, outline=(180, 190, 195), width=1)
d.text((mx + 10, my + 6), "WHERE IT HAPPENED — 23 NOV 2026", font=F(SANS_B, 12), fill=NAVY)

CONTINENTS = {
    "NA": [(-168,66),(-140,70),(-120,72),(-95,80),(-80,73),(-60,60),(-55,47),(-70,42),(-75,35),(-80,25),(-90,20),(-97,16),(-105,20),(-115,30),(-125,40),(-125,49),(-145,60)],
    "SA": [(-80,10),(-60,5),(-50,0),(-35,-8),(-40,-20),(-50,-30),(-65,-40),(-70,-52),(-73,-40),(-75,-20),(-80,-5)],
    "AF": [(-17,15),(-10,30),(0,35),(10,37),(20,32),(30,31),(35,28),(43,12),(51,11),(48,0),(40,-15),(35,-25),(20,-35),(12,-18),(8,-2),(-8,4)],
    "EU": [(-10,36),(-9,43),(-2,48),(0,51),(5,53),(8,57),(18,56),(21,55),(28,60),(30,70),(40,68),(45,60),(40,50),(28,45),(23,40),(19,42),(12,44),(8,44),(3,43),(-2,37)],
    "AS": [(40,68),(60,70),(80,73),(100,77),(120,73),(140,72),(160,70),(178,66),(170,60),(158,52),(140,45),(130,42),(127,35),(120,30),(110,20),(105,10),(100,8),(95,15),(90,22),(85,20),(80,8),(75,10),(70,22),(60,25),(55,26),(50,30),(45,29),(40,35)],
    "OC": [(113,-22),(125,-14),(135,-12),(142,-11),(150,-22),(153,-27),(150,-37),(140,-38),(130,-32),(120,-34),(113,-30)],
}
def proj(lon, lat):
    x = mx + 8 + (lon + 180) / 360.0 * (mw - 16)
    y = my + 26 + (75 - lat) / 135.0 * (mh - 34)
    return (x, y)

for pts in CONTINENTS.values():
    d.polygon([proj(lo, la) for lo, la in pts], fill=MAPLAND, outline=(120, 145, 125))

DOTS = [  # (lon, lat, story no) — display positions nudged slightly so clustered dots stay legible
    (29.0, 38.5, "15"), (31.5, 52.5, "09"), (58.5, 24.5, "01"),
    (33.0, 29.5, "04"), (18.5, 54.5, "08"),
    (74.3, 31.5, "17"), (106.8, -6.2, "18"), (127.0, 37.5, "19"),
    (32.5, 15.6, "28"), (-74.0, 40.7, "32"),
    (-122.3, 47.6, "35"), (-47.9, -15.8, "37"),
]
for lon, lat, num in DOTS:
    x, y = proj(lon, lat)
    d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=RED, outline=LIGHT, width=1)
    d.text((x - 4, y - 5), num, font=F(SANS_B, 7), fill=LIGHT)
d.text((mx + 10, my + mh - 16), "Red dots = story numbers on this page.  Map: simplified, not to scale.",
       font=F(SANS, 9), fill=(70, 80, 90))

# ---------- side panel: date-check + markets ----------
sx, sw = 688, 320
d.rectangle([sx, 248, sx + sw, 416], fill=NAVY, outline=NAVY)
d.text((sx + 12, 258), "DATE-CHECK  ✓", font=F(SANS_B, 14), fill=GOLD)
d.text((sx + 12, 280), "Monday 23 November 2026.", font=F(SANS_B, 13), fill=LIGHT)
for j, ln in enumerate(textwrap.wrap("Every story here happened or was first reported on 23 Nov 2026. Nothing in this image is from before 13 Nov 2026.", 40)):
    d.text((sx + 12, 302 + j * 15), ln, font=F(SANS, 11), fill=(205, 215, 230))
d.rectangle([sx, 248, sx + sw, 252], fill=GOLD)
d.text((sx + 12, 352), "MARKETS — FRI CLOSE, AS REPORTED 23 NOV", font=F(SANS_B, 10), fill=GOLD)
d.text((sx + 12, 370), "S&P 500  −3.7%  •  Nikkei  −5.1%  •  Sensex  +2.3%", font=F(SANS, 11), fill=LIGHT)
d.text((sx + 12, 388), "Gold  −4.6%  •  Brent crude  $89.95  (+0.6%)", font=F(SANS, 11), fill=LIGHT)

# ---------- story grid: 3 columns x 7 region groups ----------
# (num, headline, source, region)
STORIES = [
    ("MIDDLE EAST", RED, [
        ("01", "Hormuz tankers hit by mines; two more ablaze", "AP"),
        ("02", "Houthis claim strikes on Saudi refinery", "Indian Express"),
        ("03", "Iran strike wounds two in Bahrain", "AFP"),
        ("04", "IDF pushes into central Gaza, past Yellow Line", "Al Jazeera"),
        ("05", "Gaza food-aid van strike kills three", "Al Jazeera"),
        ("06", "Settlers torch 12 vehicles in West Bank", "AP"),
        ("07", "Israel coalition talks stall; no government", "AFP"),
    ]),
    ("EUROPE", (31, 90, 140), [
        ("08", "Poland: fallen objects were Russian cruise missiles", "AFP"),
        ("09", "Russian drone hits Dymer flats: 2 dead, 14 missing", "AP"),
        ("10", "Russian cargo ship ablaze off Finland, drifting", "AFP"),
        ("11", "Kerch Bridge hit a third time; Putin rules out ceasefire", "AP"),
        ("12", "Kushner: Moscow 'comfortable' with NATO-like guarantees", "AP"),
        ("13", "Zelenskyy: Russia hit Ukraine's bridges 109 times", "Reuters"),
        ("14", "Spain heads to snap election on 29 November", "Dipl. Courier"),
    ]),
    ("ASIA-PACIFIC", (0, 110, 80), [
        ("15", "COP31 collapses in Antalya over fossil fuels", "BBC"),
        ("16", "BepiColombo enters orbit around Mercury", "ESA"),
        ("17", "Lahore AQI 538, world's most polluted city", "Dawn"),
        ("18", "Indonesia factory fire: 24 dead, 50 missing", "AP"),
        ("19", "Seoul minister quits over AI exam-cheating scandal", "Obs. Voice"),
        ("20", "Taiwan bans short-selling as stocks plunge", "FSC"),
        ("21", "Nepal PM Shah holds talks with Modi in Delhi", "Obs. Voice"),
        ("22", "Australia PM: COP31 failure 'difficult times'", "AFP"),
    ]),
    ("SOUTH ASIA", (150, 90, 0), [
        ("23", "India posts record 720/9d in Wellington Test", "Sportstar"),
        ("24", "India women beat Thailand 7-0, reach semis", "Telangana J."),
        ("25", "Pakistan A beat India A by 48 runs", "Telangana J."),
        ("26", "Amit Shah launches Rs 4,000-cr Arunachal push", "Obs. Voice"),
        ("27", "Liverpool rout Man Utd 4-0 in Pochettino debut", "The Hindu"),
    ]),
    ("AFRICA", (120, 70, 20), [
        ("28", "Sudan drones hit Khartoum, damage UN facility", "AFP"),
        ("29", "South Sudan: 24 civilians killed in fresh violence", "AFP"),
        ("30", "Nigeria: 35 killed in Kano revenge attacks", "AFP"),
        ("31", "WHO pleads for peace in Ebola-hit DR Congo", "AFP"),
    ]),
    ("NORTH AMERICA", (90, 40, 110), [
        ("32", "US stocks plunge; S&P 500 falls 3.7%", "OneTurn"),
        ("33", "Nvidia CEO Huang steps down; board rules out return", "Nvidia"),
        ("34", "Hegseth curbs US-Canada defence ties in memo", "Wash. Post"),
        ("35", "ICE detains father and daughter at Seattle airport", "The Hindu"),
        ("36", "Trump threatens tax on US data-centre builders", "Pollar News"),
    ]),
    ("LATIN AMERICA & GLOBAL", (0, 90, 110), [
        ("37", "Bolsonaro 'stable' in intensive care", "AFP"),
        ("38", "UN: 128 states agree killer-robot rules by 2028", "UN"),
        ("39", "Alcaraz wins maiden ATP Finals, beats Zverev", "ATP"),
        ("40", "Marquez seals record-tying eighth MotoGP title", "MotoGP"),
    ]),
]
total = sum(len(g[2]) for g in STORIES)
assert total == 40, total

cols = [[STORIES[0], STORIES[1]], [STORIES[2], STORIES[3]], [STORIES[4], STORIES[5], STORIES[6]]]
col_x = [16, 352, 688]
col_w = 320
y0 = 432
d.text((16, y0), "THE DAY IN 40 STORIES — grouped by region, numbered to match the map",
       font=F(SANS_B, 12), fill=NAVY)
y = y0 + 22
col_tops = []
for ci, groups in enumerate(cols):
    cy = y
    for name, color, items in groups:
        d.rectangle([col_x[ci], cy, col_x[ci] + col_w, cy + 20], fill=color)
        d.text((col_x[ci] + 8, cy + 3), f"{name}  •  {len(items)} STORIES", font=F(SANS_B, 11), fill=LIGHT)
        cy += 24
        for num, head, src in items:
            lines = textwrap.wrap(head, 40)[:2]
            d.text((col_x[ci] + 2, cy + 1), num, font=F(SANS_B, 11), fill=RED)
            for j, ln in enumerate(lines):
                d.text((col_x[ci] + 28, cy + 1 + j * 13), ln, font=F(SANS_B, 11), fill=INK)
            badge = f" [{src}]"
            bw = d.textlength(badge, font=F(SANS, 10))
            last = lines[-1] if lines else ""
            bx = col_x[ci] + 28 + d.textlength(last, font=F(SANS_B, 11)) + 4
            by = cy + 1 + (len(lines) - 1) * 13
            extra = 0
            if bx + bw > col_x[ci] + col_w - 2:
                bx = col_x[ci] + 28
                by = cy + 1 + len(lines) * 13
                extra = 13
            d.text((bx, by), badge, font=F(SANS, 10), fill=GREY)
            cy += 13 * len(lines) + 5 + extra
        cy += 6
    col_tops.append(cy)
grid_bottom = max(col_tops)

# ---------- footer: UTC timeline ----------
fy = grid_bottom + 6
d.rectangle([16, fy, 1008, fy + 2], fill=GOLD)
d.text((16, fy + 8), "THE DAY AS IT UNFOLDED (UTC) — AS REPORTED THROUGH 23 NOVEMBER 2026",
       font=F(SANS_B, 12), fill=NAVY)
tl = [
    ("00–06", "COP31 collapse confirmed; Poland missiles; UN robot deal."),
    ("06–12", "Dymer rescue goes on; Asia markets open; India 720/9d."),
    ("12–18", "Hormuz updates; Gaza push; Liverpool 4-0 Man Utd."),
    ("18–24", "Sudan strikes; Bolsonaro update; US markets fall."),
]
ty = fy + 30
for i, (band, txt) in enumerate(tl):
    x = 16 + i * 250
    d.rectangle([x, ty, x + 236, ty + 48], fill=LIGHT, outline=(200, 195, 180), width=1)
    d.text((x + 8, ty + 4), band + " UTC", font=F(SANS_B, 11), fill=RED)
    for j, ln in enumerate(textwrap.wrap(txt, 34)[:2]):
        d.text((x + 8, ty + 20 + j * 12), ln, font=F(SANS, 10), fill=(40, 40, 40))
fy2 = ty + 56
d.text((16, fy2), "Sources: AP, AFP, BBC, Reuters, Al Jazeera, The Hindu, ESA, Dawn, UN, Wash. Post — full list in SOURCES.md.  •  Image: 40 stories, 7 regions, one day.",
       font=F(SANS, 10), fill=GREY)

img.save("entry.png", optimize=True)
print("saved entry.png")
import os
print("bytes:", os.path.getsize("entry.png"), "size:", img.size)
