#!/usr/bin/env python3
"""
Moon Cafe — illustration generator.

Every image on the site is an original SVG drawn by this script, so the project
ships with zero third-party assets and weighs a few hundred KB in total.
To use real photography later, replace the files in public/images/ with JPG/WebP
files of the same name (and update the extensions in src/data/*.ts).

Run:  python3 scripts/generate_images.py
"""
import math
import os
import random

OUT = os.path.join(os.path.dirname(__file__), "..", "public", "images")
os.makedirs(OUT, exist_ok=True)

INK = "#0f0d0c"
CHAR = "#1c1917"
CHAR2 = "#26211e"
CREAM = "#f1e7d6"
COFFEE = "#6b4430"
GOLD = "#b8975a"
MOON = "#efe6cf"


def write(name, w, h, body, defs=""):
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
        f"<defs>{defs}</defs>{body}</svg>"
    )
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
        f.write(svg)


def lin(id_, stops, x1=0, y1=0, x2=0, y2=1):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<linearGradient id="{id_}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{s}</linearGradient>'


def rad(id_, stops):
    s = "".join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{a}"/>' for o, c, a in stops)
    return f'<radialGradient id="{id_}">{s}</radialGradient>'


BLUR = '<filter id="blur" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="14"/></filter>'
BLUR_S = '<filter id="blurs" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="5"/></filter>'


def moon(cx, cy, r, glow=True, color=MOON):
    out = ""
    if glow:
        out += f'<circle cx="{cx}" cy="{cy}" r="{r*3.2}" fill="url(#moonglow)"/>'
    out += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'
    out += f'<circle cx="{cx-r*0.3}" cy="{cy-r*0.2}" r="{r*0.18}" fill="#d9cdb0" opacity=".55"/>'
    out += f'<circle cx="{cx+r*0.28}" cy="{cy+r*0.3}" r="{r*0.26}" fill="#d9cdb0" opacity=".4"/>'
    out += f'<circle cx="{cx+r*0.12}" cy="{cy-r*0.45}" r="{r*0.1}" fill="#d9cdb0" opacity=".5"/>'
    return out


MOONGLOW = rad("moonglow", [(0, "#efe6cf", 0.38), (0.4, "#efe6cf", 0.1), (1, "#efe6cf", 0)])
WARMGLOW = rad("warmglow", [(0, "#f3c27a", 0.55), (0.5, "#e0a458", 0.15), (1, "#e0a458", 0)])


def stars(n, w, h, seed, ymax=0.6):
    r = random.Random(seed)
    out = ""
    for _ in range(n):
        x, y = r.uniform(0, w), r.uniform(0, h * ymax)
        s = r.choice([1.2, 1.6, 2.2, 3])
        out += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{s}" fill="{MOON}" opacity="{r.uniform(.35,.9):.2f}"/>'
    return out


def skyline(w, base, seed, color, hmin, hmax, lit=0.0, wincolor="#f3c27a"):
    r = random.Random(seed)
    out, x = "", -20
    while x < w:
        bw = r.uniform(60, 150)
        bh = r.uniform(hmin, hmax)
        out += f'<rect x="{x:.0f}" y="{base-bh:.0f}" width="{bw:.0f}" height="{bh+4:.0f}" fill="{color}"/>'
        if lit:
            wy = base - bh + 18
            while wy < base - 24:
                wx = x + 12
                while wx < x + bw - 20:
                    if r.random() < lit:
                        out += f'<rect x="{wx:.0f}" y="{wy:.0f}" width="9" height="13" fill="{wincolor}" opacity="{r.uniform(.5,.95):.2f}"/>'
                    wx += 24
                wy += 30
        x += bw + r.uniform(0, 8)
    return out


# ───────────────────────── cups, glasses & food (menu illustrations) ─────────────────────────

def menu_bg(accent="#3a2a20", seed=1):
    defs = (
        lin("bg", [(0, CHAR2), (1, INK)])
        + rad("halo", [(0, accent, 0.9), (1, accent, 0)])
        + MOONGLOW
        + BLUR
        + BLUR_S
    )
    body = (
        '<rect width="800" height="1000" fill="url(#bg)"/>'
        '<circle cx="400" cy="520" r="470" fill="url(#halo)" opacity=".55"/>'
        f'<circle cx="640" cy="150" r="46" fill="{MOON}" opacity=".9"/>'
        '<circle cx="662" cy="136" r="46" fill="#26211e"/>'
    )
    return defs, body + stars(18, 800, 330, seed, 1)


def top_cup(name, liquid, art, accent, saucer=290, cup=215, garnish=None, seed=1):
    defs, bg = menu_bg(accent, seed)
    cx, cy = 400, 560
    li = cup - 32
    defs += lin("liq", [(0, liquid[0]), (1, liquid[1])], 0, 0, 1, 1)
    b = bg
    b += f'<ellipse cx="{cx+10}" cy="{cy+30}" rx="{saucer}" ry="{saucer*0.96}" fill="#000" opacity=".5" filter="url(#blur)"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{saucer}" fill="#e8dcc6"/><circle cx="{cx}" cy="{cy}" r="{saucer-26}" fill="none" stroke="#cdbf9f" stroke-width="3"/>'
    b += f'<rect x="{cx+cup-30}" y="{cy-34}" width="{cup*0.52:.0f}" height="68" rx="34" fill="#f6eee0" stroke="#d6c8aa" stroke-width="3"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{cup}" fill="#f6eee0" stroke="#d6c8aa" stroke-width="4"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{li}" fill="url(#liq)"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="{li}" fill="none" stroke="#00000030" stroke-width="6"/>'
    cr = li
    if art == "crescent":
        b += f'<circle cx="{cx}" cy="{cy}" r="{cr*0.58}" fill="#f4e8d2"/><circle cx="{cx+cr*0.2}" cy="{cy-cr*0.08}" r="{cr*0.54}" fill="url(#liq)"/>'
        b += f'<circle cx="{cx+cr*0.52}" cy="{cy-cr*0.46}" r="5" fill="#f4e8d2"/><circle cx="{cx+cr*0.7}" cy="{cy-cr*0.22}" r="3.5" fill="#f4e8d2"/>'
    elif art == "heart":
        s = cr / 160
        b += f'<path transform="translate({cx} {cy+8}) scale({s})" d="M0 92 C-120 14 -92 -78 -40 -70 C-14 -66 0 -44 0 -30 C0 -44 14 -66 40 -70 C92 -78 120 14 0 92Z" fill="#f4e8d2"/>'
    elif art == "rosetta":
        for i in range(6):
            y = cy + cr * 0.5 - i * cr * 0.22
            rx = cr * (0.62 - i * 0.07)
            b += f'<ellipse cx="{cx}" cy="{y:.0f}" rx="{rx:.0f}" ry="{cr*0.14:.0f}" fill="#f4e8d2" opacity=".95"/>'
        b += f'<rect x="{cx-3}" y="{cy-cr*0.7:.0f}" width="6" height="{cr*1.3:.0f}" fill="{liquid[1]}"/>'
    elif art == "swirl":
        pts = []
        for i in range(0, 520, 8):
            a = i / 520 * 6.5 * math.pi
            rr = 6 + i / 520 * cr * 0.85
            pts.append(f"{cx+rr*math.cos(a):.1f},{cy+rr*math.sin(a):.1f}")
        b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{garnish or "#f4e8d2"}" stroke-width="9" stroke-linecap="round" opacity=".9"/>'
    elif art == "foam":
        b += f'<circle cx="{cx}" cy="{cy}" r="{cr*0.88}" fill="#f4e8d2" opacity=".92"/>'
        b += f'<path d="M{cx-cr*0.5} {cy-cr*0.15} Q{cx-cr*0.2} {cy-cr*0.45} {cx} {cy-cr*0.1} T{cx+cr*0.5} {cy+cr*0.1}" fill="none" stroke="#c78a4c" stroke-width="11" stroke-linecap="round"/>'
        b += f'<path d="M{cx-cr*0.45} {cy+cr*0.25} Q{cx-cr*0.1} {cy+cr*0.05} {cx+cr*0.1} {cy+cr*0.3} T{cx+cr*0.5} {cy+cr*0.3}" fill="none" stroke="#c78a4c" stroke-width="9" stroke-linecap="round" opacity=".8"/>'
    elif art == "crema":
        b += f'<circle cx="{cx}" cy="{cy}" r="{cr*0.82}" fill="#a9703e" opacity=".55"/><ellipse cx="{cx-cr*0.25}" cy="{cy-cr*0.3}" rx="{cr*0.4}" ry="{cr*0.16}" fill="#d6a56b" opacity=".6" transform="rotate(-30 {cx} {cy})"/>'
    elif art == "star":
        b += f'<circle cx="{cx}" cy="{cy}" r="{cr*0.8}" fill="#fff" opacity=".07"/>'
        pts = []
        for i in range(16):
            a = i * math.pi / 8
            rr = cr * (0.34 if i % 2 == 0 else 0.15)
            pts.append(f"{cx+rr*math.cos(a):.1f},{cy+rr*math.sin(a):.1f}")
        b += f'<polygon points="{" ".join(pts)}" fill="#5b3a22"/><circle cx="{cx}" cy="{cy}" r="9" fill="#2e1b0f"/>'
        b += f'<rect x="{cx+cr*0.2}" y="{cy+cr*0.35}" width="{cr*0.62}" height="14" rx="7" fill="#8a5632" transform="rotate(-24 {cx} {cy})"/>'
    elif art == "jasmine":
        for k in range(5):
            a = k * 2 * math.pi / 5
            b += f'<ellipse cx="{cx+math.cos(a)*34}" cy="{cy+math.sin(a)*34}" rx="30" ry="15" fill="#fbf6e9" transform="rotate({k*72} {cx+math.cos(a)*34} {cy+math.sin(a)*34})"/>'
        b += f'<circle cx="{cx}" cy="{cy}" r="12" fill="#e6c36a"/>'
        b += f'<ellipse cx="{cx-cr*0.5}" cy="{cy+cr*0.35}" rx="46" ry="16" fill="#5f7d4a" transform="rotate(-30 {cx-cr*0.5} {cy+cr*0.35})"/>'
    elif art == "lemon":
        b += f'<circle cx="{cx+cr*0.12}" cy="{cy-cr*0.1}" r="{cr*0.52}" fill="#f2cf5a"/><circle cx="{cx+cr*0.12}" cy="{cy-cr*0.1}" r="{cr*0.44}" fill="#f8e38b"/>'
        for k in range(8):
            a = k * math.pi / 4
            b += f'<line x1="{cx+cr*0.12}" y1="{cy-cr*0.1}" x2="{cx+cr*0.12+math.cos(a)*cr*0.42}" y2="{cy-cr*0.1+math.sin(a)*cr*0.42}" stroke="#f2cf5a" stroke-width="5"/>'
    elif art == "saffron":
        b += f'<circle cx="{cx}" cy="{cy}" r="{cr*0.86}" fill="#fff3c9" opacity=".18"/>'
        for k in range(14):
            a = k * 0.9
            rr = 20 + k * 11
            x, y = cx + math.cos(a) * rr * 0.8, cy + math.sin(a) * rr * 0.8
            b += f'<path d="M{x:.0f} {y:.0f} q10 -18 24 -26" stroke="#d6541f" stroke-width="5" fill="none" stroke-linecap="round" transform="rotate({k*40} {x:.0f} {y:.0f})"/>'
    # highlight
    b += f'<path d="M{cx-cup*0.82:.0f} {cy-cup*0.3:.0f} A{cup*0.86:.0f} {cup*0.86:.0f} 0 0 1 {cx-cup*0.3:.0f} {cy-cup*0.82:.0f}" fill="none" stroke="#fff" stroke-width="7" opacity=".5" stroke-linecap="round"/>'
    write(name, 800, 1000, b, defs)


def glass(name, layers, accent, kind="tall", garnish=None, seed=1):
    defs, bg = menu_bg(accent, seed)
    defs += '<clipPath id="gl"><path d="M270 250 L530 250 L498 830 Q496 850 476 850 L324 850 Q304 850 302 830 Z"/></clipPath>'
    b = bg
    b += '<ellipse cx="400" cy="860" rx="190" ry="28" fill="#000" opacity=".55" filter="url(#blur)"/>'
    b += '<g clip-path="url(#gl)">'
    y = 250
    total = 600
    for frac, col in layers:
        hh = total * frac
        b += f'<rect x="250" y="{y:.0f}" width="320" height="{hh+2:.0f}" fill="{col}"/>'
        y += hh
    rr = random.Random(seed + 5)
    for _ in range(6):
        ix, iy, s = rr.uniform(300, 450), rr.uniform(320, 700), rr.uniform(70, 96)
        b += f'<rect x="{ix:.0f}" y="{iy:.0f}" width="{s:.0f}" height="{s:.0f}" rx="14" fill="#ffffff" opacity=".13" stroke="#fff" stroke-opacity=".35" stroke-width="3" transform="rotate({rr.uniform(-25,25):.0f} {ix+40:.0f} {iy+40:.0f})"/>'
    b += '<rect x="250" y="250" width="320" height="600" fill="url(#shine)" />'
    b += "</g>"
    defs += (
        '<linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0" stop-color="#fff" stop-opacity=".22"/><stop offset=".2" stop-color="#fff" stop-opacity="0"/>'
        '<stop offset=".8" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff" stop-opacity=".16"/></linearGradient>'
    )
    b += '<path d="M270 250 L530 250 L498 830 Q496 850 476 850 L324 850 Q304 850 302 830 Z" fill="none" stroke="#f6eee0" stroke-opacity=".55" stroke-width="5"/>'
    b += '<path d="M292 290 L312 800" stroke="#fff" stroke-opacity=".35" stroke-width="9" stroke-linecap="round"/>'
    b += '<rect x="440" y="90" width="16" height="520" rx="8" fill="#e8dcc6" transform="rotate(10 448 350)"/>'
    for i in range(14):
        rr2 = random.Random(i + seed)
        b += f'<circle cx="{rr2.uniform(300,500):.0f}" cy="{rr2.uniform(380,780):.0f}" r="{rr2.uniform(2,5):.1f}" fill="#fff" opacity=".35"/>'
    if garnish == "lemon":
        b += '<circle cx="528" cy="262" r="64" fill="#f2cf5a"/><circle cx="528" cy="262" r="54" fill="#f8e38b"/>'
        for k in range(8):
            a = k * math.pi / 4
            b += f'<line x1="528" y1="262" x2="{528+math.cos(a)*52:.0f}" y2="{262+math.sin(a)*52:.0f}" stroke="#f2cf5a" stroke-width="5"/>'
        b += '<ellipse cx="300" cy="238" rx="38" ry="16" fill="#5f9a52" transform="rotate(-20 300 238)"/><ellipse cx="340" cy="226" rx="34" ry="14" fill="#74b063" transform="rotate(14 340 226)"/>'
    if garnish == "choc":
        b += '<path d="M290 252 Q330 214 400 238 Q470 214 512 252 Z" fill="#f1e7d6"/><path d="M320 244 q20 -30 40 0 M400 240 q20 -30 40 0" stroke="#3b2417" stroke-width="9" fill="none" stroke-linecap="round"/>'
    write(name, 800, 1000, b, defs)


def croissant(name, almond=False):
    defs, bg = menu_bg("#5a3a1f", 7)
    defs += lin("cr", [(0, "#e7b05b"), (1, "#b8702d")]) + lin("cr2", [(0, "#f0c070"), (1, "#c98539")])
    b = bg
    b += '<ellipse cx="400" cy="740" rx="300" ry="50" fill="#000" opacity=".5" filter="url(#blur)"/>'
    b += '<ellipse cx="400" cy="690" rx="340" ry="76" fill="#e8dcc6"/><ellipse cx="400" cy="680" rx="300" ry="58" fill="#f6eee0"/>'
    n = 7
    for i in range(n):
        t = i / (n - 1)
        a = math.radians(205 - t * 230)
        cx, cy = 400 + math.cos(a) * 215, 640 - math.sin(a) * 185
        size = 1 - abs(t - 0.5) * 1.15
        rx, ry = 72 + 66 * size, 46 + 52 * size
        rot = math.degrees(math.atan2(-math.cos(a), -math.sin(a)))
        b += f'<ellipse cx="{cx:.0f}" cy="{cy:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" fill="url(#{"cr" if i%2 else "cr2"})" stroke="#9a5a22" stroke-width="3" transform="rotate({rot:.0f} {cx:.0f} {cy:.0f})"/>'
        b += f'<path d="M{cx-rx*0.6:.0f} {cy:.0f} Q{cx:.0f} {cy-ry*0.5:.0f} {cx+rx*0.6:.0f} {cy:.0f}" stroke="#fbe0a3" stroke-opacity=".6" stroke-width="5" fill="none" transform="rotate({rot:.0f} {cx:.0f} {cy:.0f})"/>'
    if almond:
        r = random.Random(4)
        for _ in range(26):
            a = math.radians(r.uniform(-25, 205))
            rr = r.uniform(120, 250)
            x, y = 400 + math.cos(a) * rr * 1.0, 660 - abs(math.sin(a)) * rr * 0.62
            b += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="17" ry="8" fill="#f4e6c6" stroke="#c9a56a" stroke-width="2" transform="rotate({r.randint(0,180)} {x:.0f} {y:.0f})"/>'
        for _ in range(40):
            b += f'<circle cx="{r.uniform(200,600):.0f}" cy="{r.uniform(420,640):.0f}" r="2.6" fill="#fff" opacity=".8"/>'
    write(name, 800, 1000, b, defs)


def muffin(name):
    defs, bg = menu_bg("#3a3358", 3)
    defs += lin("mf", [(0, "#d99a52"), (1, "#a8652a")]) + lin("pp", [(0, "#efe2c8"), (1, "#cdb98f")], 0, 0, 1, 0)
    b = bg
    b += '<ellipse cx="400" cy="790" rx="250" ry="34" fill="#000" opacity=".55" filter="url(#blur)"/>'
    b += '<path d="M255 580 L545 580 L510 800 Q508 812 496 812 L304 812 Q292 812 290 800 Z" fill="url(#pp)"/>'
    for i in range(8):
        x = 285 + i * 33
        b += f'<line x1="{x}" y1="590" x2="{x+ (i-3.5)*-2.5:.0f}" y2="802" stroke="#b9a478" stroke-width="3" opacity=".7"/>'
    b += '<path d="M228 600 Q214 420 400 372 Q586 420 572 600 Q400 640 228 600Z" fill="url(#mf)"/>'
    b += '<path d="M290 470 Q330 420 400 412" stroke="#f0c487" stroke-width="10" fill="none" stroke-linecap="round" opacity=".6"/>'
    r = random.Random(11)
    for _ in range(11):
        x, y = r.uniform(290, 510), r.uniform(430, 570)
        b += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r.uniform(15,22):.0f}" fill="#3e3a78"/><circle cx="{x-5:.0f}" cy="{y-5:.0f}" r="5" fill="#8c86d6" opacity=".7"/>'
    write(name, 800, 1000, b, defs)


def toast(name):
    defs, bg = menu_bg("#4d3a22", 9)
    defs += lin("br", [(0, "#e6c48a"), (1, "#c58c4a")])
    b = bg
    b += '<ellipse cx="400" cy="800" rx="280" ry="40" fill="#000" opacity=".55" filter="url(#blur)"/>'
    b += '<ellipse cx="400" cy="770" rx="300" ry="60" fill="#e8dcc6"/><ellipse cx="400" cy="762" rx="262" ry="46" fill="#f6eee0"/>'
    b += '<path d="M240 700 L240 470 Q240 340 400 340 Q560 340 560 470 L560 700 Q400 730 240 700Z" fill="#8a5a2c"/>'
    b += '<path d="M262 690 L262 475 Q262 364 400 364 Q538 364 538 475 L538 690 Q400 714 262 690Z" fill="url(#br)"/>'
    r = random.Random(2)
    for _ in range(22):
        x, y = r.uniform(290, 510), r.uniform(430, 660)
        b += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{r.uniform(10,24):.0f}" ry="{r.uniform(6,12):.0f}" fill="#a8702f" opacity=".55"/>'
    b += '<rect x="318" y="480" width="170" height="96" rx="14" fill="#f4dd8c" transform="rotate(-8 400 520)"/><rect x="326" y="486" width="150" height="26" rx="10" fill="#fbeaa8" transform="rotate(-8 400 520)"/>'
    b += '<path d="M470 530 q22 14 12 40" stroke="#f4dd8c" stroke-width="12" fill="none" stroke-linecap="round"/>'
    write(name, 800, 1000, b, defs)


def plate(b, y=790):
    b += f'<ellipse cx="400" cy="{y+40}" rx="320" ry="40" fill="#000" opacity=".55" filter="url(#blur)"/>'
    b += f'<ellipse cx="400" cy="{y}" rx="330" ry="72" fill="#e8dcc6"/><ellipse cx="400" cy="{y-8}" rx="290" ry="54" fill="#f6eee0"/>'
    return b


def tiramisu(name):
    defs, bg = menu_bg("#4a3322", 5)
    b = plate(bg)
    layers = [("#4b2e1b", 40), ("#f2e5c4", 78), ("#a47443", 56), ("#f2e5c4", 78), ("#a47443", 56)]
    y = 750
    for col, hh in reversed(layers):
        y -= hh
    top = y
    y = top
    for col, hh in layers:
        b += f'<rect x="250" y="{y}" width="300" height="{hh}" fill="{col}"/>'
        y += hh
    r = random.Random(8)
    for _ in range(70):
        b += f'<circle cx="{r.uniform(252,548):.0f}" cy="{top+r.uniform(2,36):.0f}" r="{r.uniform(2,5):.1f}" fill="#7a5233" opacity=".8"/>'
    for i in range(10):
        b += f'<circle cx="{r.uniform(262,540):.0f}" cy="{r.uniform(top+130,top+180):.0f}" r="3" fill="#f2e5c4" opacity=".5"/>'
    b += f'<path d="M250 {top} L550 {top} L550 750 L250 750Z" fill="none" stroke="#00000033" stroke-width="3"/>'
    b += f'<ellipse cx="400" cy="{top}" rx="150" ry="16" fill="#5a3822"/>'
    b += f'<path d="M256 {top+4} L256 745" stroke="#fff" stroke-opacity=".12" stroke-width="10"/>'
    b += f'<circle cx="470" cy="{top-14}" r="22" fill="#2a170c"/><circle cx="470" cy="{top-14}" r="14" fill="#3b2417"/>'
    write(name, 800, 1000, b, defs)


def cheesecake(name):
    defs, bg = menu_bg("#5a331c", 6)
    defs += lin("bk", [(0, "#8b4a22"), (1, "#3b1c0c")])
    b = plate(bg)
    b += '<path d="M180 640 L620 640 L548 400 Q400 330 252 400 Z" fill="#f2e2b8" transform="translate(0 70)"/>'
    b += '<path d="M180 640 Q400 700 620 640 L620 700 Q400 770 180 700 Z" fill="#d9c28b"/>'
    b += '<path d="M252 470 Q400 400 548 470 L620 700 Q400 780 180 700 Z" fill="none"/>'
    b += '<path d="M252 470 Q400 392 548 470 Q540 520 400 530 Q260 520 252 470Z" fill="url(#bk)"/>'
    b += '<path d="M180 710 Q400 780 620 710 L620 740 Q400 810 180 740Z" fill="#c9a96a"/>'
    b += '<path d="M200 700 Q400 764 600 700" stroke="#a07a3c" stroke-width="6" fill="none"/>'
    r = random.Random(3)
    for _ in range(26):
        b += f'<circle cx="{r.uniform(290,520):.0f}" cy="{r.uniform(440,500):.0f}" r="{r.uniform(3,8):.1f}" fill="#2a1208" opacity=".6"/>'
    b += '<circle cx="640" cy="760" r="30" fill="#b3263a"/><circle cx="676" cy="772" r="26" fill="#8f1d2e"/><circle cx="634" cy="752" r="8" fill="#e9707f" opacity=".7"/>'
    write(name, 800, 1000, b, defs)


def brownie(name):
    defs, bg = menu_bg("#3b2418", 12)
    defs += lin("bw", [(0, "#4a2a18"), (1, "#24120a")]) + rad("ic", [(0, "#fff8e6", 1), (1, "#eadfbf", 1)])
    b = plate(bg, 800)
    b += '<path d="M222 620 L560 600 L580 740 L240 760 Z" fill="#1c0e07"/><path d="M222 620 L560 600 L548 520 L236 546 Z" fill="url(#bw)"/><path d="M236 546 L548 520 L560 600 L222 620 Z" fill="#3a2013"/>'
    b += '<path d="M244 560 L540 536 M240 580 L548 558" stroke="#6b3d22" stroke-width="5" stroke-opacity=".6"/>'
    r = random.Random(1)
    for _ in range(28):
        b += f'<circle cx="{r.uniform(250,545):.0f}" cy="{r.uniform(530,610):.0f}" r="{r.uniform(2,5):.1f}" fill="#7a4a2a" opacity=".7"/>'
    b += '<circle cx="470" cy="470" r="104" fill="url(#ic)"/><path d="M394 452 q76 -34 150 6" stroke="#fff" stroke-opacity=".6" stroke-width="9" fill="none" stroke-linecap="round"/>'
    b += '<path d="M380 478 Q470 530 560 468" fill="none" stroke="#3a1a0c" stroke-width="12" stroke-linecap="round" opacity=".9"/>'
    b += '<path d="M410 500 q4 40 -6 60 M470 520 q4 40 -2 70 M530 496 q4 30 -2 48" stroke="#3a1a0c" stroke-width="9" fill="none" stroke-linecap="round"/>'
    write(name, 800, 1000, b, defs)


def panna(name):
    defs, bg = menu_bg("#5a2234", 14)
    defs += lin("pc", [(0, "#fff8ea"), (1, "#ecdcbd")], 0, 0, 1, 0)
    b = plate(bg)
    b += '<path d="M240 740 Q226 500 400 430 Q574 500 560 740 Q400 780 240 740Z" fill="url(#pc)"/>'
    b += '<path d="M300 700 Q290 540 360 480" stroke="#fff" stroke-width="12" fill="none" stroke-linecap="round" opacity=".7"/>'
    b += '<path d="M290 520 Q400 400 510 520 Q500 560 470 540 Q456 600 424 548 Q400 640 370 550 Q330 590 322 540 Q300 560 290 520Z" fill="#a31f3a"/>'
    b += '<path d="M410 436 q60 -10 96 40" stroke="#c6334f" stroke-width="10" fill="none" stroke-linecap="round" opacity=".7"/>'
    for (x, y) in [(400, 428), (352, 450), (448, 452)]:
        b += f'<circle cx="{x}" cy="{y}" r="26" fill="#6b2a6e"/><circle cx="{x-7}" cy="{y-7}" r="7" fill="#b077b2" opacity=".7"/>'
    b += '<path d="M400 396 q14 -30 36 -34 q-6 22 -36 34Z" fill="#6b9a52"/>'
    write(name, 800, 1000, b, defs)


def build_menu():
    top_cup("moon-latte", ("#c8975f", "#9a6a3a"), "crescent", "#6a4528", seed=1)
    top_cup("caramel-cappuccino", ("#9b6a3b", "#6b4228"), "foam", "#7a4a1f", seed=2)
    top_cup("dark-mocha", ("#3d2214", "#24120a"), "swirl", "#4a2a18", seed=3, garnish="#e9d5b0")
    top_cup("flat-white", ("#b88650", "#8a5a30"), "heart", "#5e3d22", seed=4)
    top_cup("espresso-doppio", ("#2b1608", "#160a03"), "crema", "#4a2a14", saucer=250, cup=150, seed=5)

    glass("midnight-cold-brew", [(0.12, "#d9c7a6"), (0.88, "#1a0d06")], "#3a2a40", seed=21)
    glass("iced-spanish-latte", [(0.1, "#f4e8d2"), (0.38, "#e5c28a"), (0.52, "#7b4a28")], "#5e4122", garnish="choc", seed=22)
    glass("salted-caramel-frappe", [(0.14, "#fbf3e2"), (0.2, "#b8742f"), (0.66, "#d8a870")], "#6a4220", garnish="choc", seed=23)
    glass("lemon-mint-cooler", [(0.12, "#d9ef9b"), (0.88, "#f3dc6a")], "#4a5a20", garnish="lemon", seed=24)

    top_cup("masala-chai", ("#c9915a", "#a06a3a"), "star", "#5a3820", seed=31)
    top_cup("jasmine-green-tea", ("#d6d98a", "#aab45e"), "jasmine", "#46552a", seed=32)
    top_cup("earl-grey", ("#b4742f", "#7a4417"), "lemon", "#5a3c18", seed=33)
    top_cup("saffron-moon-milk", ("#f0d08a", "#d9a64a"), "saffron", "#6a4a1c", seed=34)

    croissant("butter-croissant")
    croissant("almond-croissant", almond=True)
    muffin("blueberry-muffin")
    toast("sourdough-toast")

    tiramisu("classic-tiramisu")
    cheesecake("basque-cheesecake")
    brownie("warm-brownie")
    panna("panna-cotta")


# ───────────────────────── scenes ─────────────────────────

SKY = {
    "night": ([(0, "#07060c"), (0.55, "#1b1730"), (1, "#3b2a3a")], "#0d0b14", "#1a1424"),
    "evening": ([(0, "#241833"), (0.5, "#8d4a45"), (1, "#e3a65f")], "#1a1018", "#2c1c26"),
    "afternoon": ([(0, "#ead6ad"), (1, "#f6ead2")], "#cdb68a", "#b99f72"),
    "morning": ([(0, "#e9b48f"), (0.6, "#f5d6b3"), (1, "#fbeccf")], "#c79a78", "#a98262"),
}


def cup_side(x, y, s=1.0, col=CREAM, steam=True, liquid="#6b4430"):
    b = f'<ellipse cx="{x}" cy="{y+4*s}" rx="{86*s}" ry="{12*s}" fill="#000" opacity=".4"/>'
    b += f'<ellipse cx="{x}" cy="{y}" rx="{80*s}" ry="{10*s}" fill="#d8c9aa"/>'
    b += f'<path d="M{x-56*s} {y-80*s} L{x+56*s} {y-80*s} Q{x+50*s} {y-6*s} {x} {y-6*s} Q{x-50*s} {y-6*s} {x-56*s} {y-80*s}Z" fill="{col}"/>'
    b += f'<ellipse cx="{x}" cy="{y-80*s}" rx="{56*s}" ry="{9*s}" fill="{liquid}"/>'
    b += f'<path d="M{x+54*s} {y-66*s} q{34*s} {2*s} {26*s} {30*s} q{-8*s} {18*s} {-34*s} {16*s}" fill="none" stroke="{col}" stroke-width="{9*s}" stroke-linecap="round"/>'
    if steam:
        for dx in (-22, 4, 28):
            b += f'<path d="M{x+dx*s} {y-98*s} q{-14*s} {-24*s} 0 {-46*s} q{14*s} {-22*s} 0 {-46*s}" fill="none" stroke="#fff" stroke-opacity=".28" stroke-width="{5*s}" stroke-linecap="round"/>'
    return b


def window_scene(name, w, h, t, fg):
    stops, wall, wall2 = SKY[t]
    ww = w * 0.62
    cx = w / 2
    top = h * 0.07
    sill = h * 0.66
    defs = lin("sky", stops) + lin("wall", [(0, wall2), (1, wall)]) + MOONGLOW + WARMGLOW + BLUR
    defs += f'<clipPath id="arch"><path d="M{cx-ww/2} {sill} L{cx-ww/2} {top+ww/2} A{ww/2} {ww/2} 0 0 1 {cx+ww/2} {top+ww/2} L{cx+ww/2} {sill}Z"/></clipPath>'
    dark = t in ("night", "evening")
    b = f'<rect width="{w}" height="{h}" fill="url(#wall)"/>'
    b += '<g clip-path="url(#arch)">'
    b += f'<rect x="{cx-ww/2}" y="{top}" width="{ww}" height="{sill-top}" fill="url(#sky)"/>'
    if t == "night":
        b += stars(60, w, h * 0.5, 11, 1)
        b += moon(cx + ww * 0.14, top + ww * 0.34, ww * 0.12)
    elif t == "evening":
        b += f'<circle cx="{cx-ww*0.1}" cy="{sill-h*0.1}" r="{ww*0.16}" fill="#f6c97a" opacity=".9"/>'
        b += stars(18, w, h * 0.3, 5, 1)
    elif t == "afternoon":
        b += f'<circle cx="{cx+ww*0.12}" cy="{top+ww*0.3}" r="{ww*0.1}" fill="#fff6d8"/><circle cx="{cx+ww*0.12}" cy="{top+ww*0.3}" r="{ww*0.28}" fill="#fff6d8" opacity=".25"/>'
    else:
        b += f'<circle cx="{cx-ww*0.18}" cy="{sill-h*0.14}" r="{ww*0.12}" fill="#fff0c9"/><circle cx="{cx-ww*0.18}" cy="{sill-h*0.14}" r="{ww*0.3}" fill="#fff0c9" opacity=".25"/>'
    far = {"night": "#171227", "evening": "#4a2a3a", "afternoon": "#d7c29a", "morning": "#dcae8c"}[t]
    near = {"night": "#0d0a15", "evening": "#2a1722", "afternoon": "#b9a276", "morning": "#c08f72"}[t]
    b += skyline(w, sill - 10, 21, far, h * 0.07, h * 0.16, 0.18 if dark else 0)
    b += skyline(w, sill + 6, 33, near, h * 0.03, h * 0.09, 0.3 if dark else 0)
    b += "</g>"
    b += f'<path d="M{cx-ww/2} {sill} L{cx-ww/2} {top+ww/2} A{ww/2} {ww/2} 0 0 1 {cx+ww/2} {top+ww/2} L{cx+ww/2} {sill}" fill="none" stroke="{INK}" stroke-width="16"/>'
    b += f'<line x1="{cx}" y1="{top}" x2="{cx}" y2="{sill}" stroke="{INK}" stroke-width="9"/>'
    b += f'<line x1="{cx-ww/2}" y1="{top+ww*0.52}" x2="{cx+ww/2}" y2="{top+ww*0.52}" stroke="{INK}" stroke-width="9"/>'
    b += f'<rect x="{cx-ww/2-34}" y="{sill}" width="{ww+68}" height="26" fill="#3a2a20"/><rect x="{cx-ww/2-34}" y="{sill}" width="{ww+68}" height="6" fill="#5a4030"/>'
    b += f'<rect x="0" y="{sill+26}" width="{w}" height="{h-sill-26}" fill="#1c1510"/>'
    if dark:
        b += f'<ellipse cx="{cx}" cy="{sill+60}" rx="{ww*0.5}" ry="{h*0.14}" fill="url(#warmglow)"/>'
    y0 = sill + 6
    if fg == "morning":
        b += cup_side(cx - ww * 0.14, y0, ww / 520)
        b += f'<path d="M{cx+ww*0.12} {y0} q{ww*0.1} {-ww*0.14} {ww*0.2} 0 q{-ww*0.04} {ww*0.02} {-ww*0.1} {ww*0.02} q{-ww*0.06} 0 {-ww*0.1} {-ww*0.02}Z" fill="#d99a46"/>'
    elif fg == "afternoon":
        b += cup_side(cx - ww * 0.2, y0, ww / 560, steam=True)
        b += cup_side(cx + ww * 0.12, y0, ww / 600, col="#e6d6b4", liquid="#9a6a3a")
        b += f'<rect x="{cx+ww*0.26}" y="{y0-ww*0.1}" width="{ww*0.14}" height="{ww*0.1}" fill="#8b4a30"/><rect x="{cx+ww*0.26}" y="{y0-ww*0.1}" width="{ww*0.14}" height="{ww*0.016}" fill="#f1e7d6"/>'
    elif fg == "evening":
        b += cup_side(cx, y0, ww / 480, liquid="#3d2214")
        b += f'<circle cx="{cx-ww*0.3}" cy="{y0-ww*0.2}" r="{ww*0.1}" fill="#f3c27a" opacity=".6" filter="url(#blur)"/><rect x="{cx-ww*0.3-6}" y="{y0-ww*0.2}" width="12" height="{ww*0.2}" fill="#d8c9aa"/><circle cx="{cx-ww*0.3}" cy="{y0-ww*0.22}" r="{ww*0.03}" fill="#fff0c9"/>'
    else:
        b += cup_side(cx - ww * 0.12, y0, ww / 520, liquid="#c8975f")
        b += f'<rect x="{cx+ww*0.17}" y="{y0-ww*0.1}" width="{ww*0.07}" height="{ww*0.1}" rx="4" fill="#e8dcc6"/><ellipse cx="{cx+ww*0.205}" cy="{y0-ww*0.14}" rx="{ww*0.016}" ry="{ww*0.032}" fill="#ffd27a"/><circle cx="{cx+ww*0.205}" cy="{y0-ww*0.12}" r="{ww*0.1}" fill="url(#warmglow)"/>'
    write(name, w, h, b, defs)


def street_scene(name, w, h, t="night", moon_big=True):
    stops = SKY[t][0]
    defs = lin("sky", stops) + MOONGLOW + WARMGLOW + BLUR + lin("floor", [(0, "#1a1410"), (1, "#0c0908")])
    b = f'<rect width="{w}" height="{h}" fill="url(#sky)"/>'
    if t == "night":
        b += stars(int(w / 14), w, h, 2, 0.6)
    mx = w * 0.72 if w > h else w * 0.6
    my = h * 0.28
    mr = min(w, h) * (0.13 if moon_big else 0.08)
    b += moon(mx, my, mr)
    b += skyline(w, h * 0.74, 5, "#1a1530" if t == "night" else "#4a2a3a", h * 0.12, h * 0.34, 0.14)
    b += skyline(w, h * 0.8, 9, "#0e0b17" if t == "night" else "#2a1722", h * 0.06, h * 0.2, 0.22)
    # café façade
    fw, fx = w * 0.46, w * 0.27
    fy = h * 0.5
    b += f'<rect x="{fx}" y="{fy}" width="{fw}" height="{h*0.42}" fill="#1f1815"/>'
    b += f'<rect x="{fx-10}" y="{fy-8}" width="{fw+20}" height="{h*0.07}" fill="#120d0b"/>'
    b += f'<text x="{w/2}" y="{fy+h*0.047}" text-anchor="middle" font-family="Georgia, serif" font-size="{h*0.04:.0f}" fill="{GOLD}" letter-spacing="{h*0.012:.0f}">MOON CAFE</text>'
    wy = fy + h * 0.1
    wh = h * 0.24
    for i, wx in enumerate([fx + fw * 0.06, fx + fw * 0.54]):
        ww = fw * 0.4
        b += f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" fill="#f0b565"/><rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" fill="url(#warmglow)" opacity=".4"/>'
        b += f'<line x1="{wx+ww/2}" y1="{wy}" x2="{wx+ww/2}" y2="{wy+wh}" stroke="#1a120d" stroke-width="6"/><line x1="{wx}" y1="{wy+wh*0.5}" x2="{wx+ww}" y2="{wy+wh*0.5}" stroke="#1a120d" stroke-width="6"/>'
        b += f'<ellipse cx="{wx+ww/2}" cy="{wy+wh}" rx="{ww*0.9}" ry="{h*0.07}" fill="url(#warmglow)"/>'
    b += f'<path d="M{fx-20} {fy+h*0.07} L{fx+fw+20} {fy+h*0.07} L{fx+fw+4} {fy+h*0.11} L{fx-4} {fy+h*0.11}Z" fill="#6b4430"/>'
    b += f'<rect x="{fx+fw*0.46}" y="{fy+h*0.18}" width="{fw*0.08}" height="{h*0.24}" fill="#120d0b"/>'
    # string lights
    r = random.Random(3)
    pts = ""
    for i in range(0, 21):
        x = fx - 40 + i * (fw + 80) / 20
        y = fy - 6 + math.sin(i / 20 * math.pi) * h * 0.04 + h * 0.01
        pts += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{max(3,h*0.006):.0f}" fill="#ffd9a0"/><circle cx="{x:.0f}" cy="{y:.0f}" r="{h*0.02:.0f}" fill="url(#warmglow)"/>'
    b += pts
    b += f'<rect y="{h*0.92}" width="{w}" height="{h*0.08}" fill="url(#floor)"/>'
    b += f'<ellipse cx="{w/2}" cy="{h*0.95}" rx="{fw*0.7}" ry="{h*0.03}" fill="#f3c27a" opacity=".25" filter="url(#blur)"/>'
    # tiny table + chairs
    for tx in (fx - w * 0.04, fx + fw + w * 0.04):
        b += f'<ellipse cx="{tx}" cy="{h*0.915}" rx="{w*0.02}" ry="{h*0.008}" fill="#3a2a20"/><rect x="{tx-2}" y="{h*0.915}" width="4" height="{h*0.04}" fill="#3a2a20"/>'
    write(name, w, h, b, defs)


def lamps_scene(name, w, h):
    defs = lin("bg", [(0, "#0c0a09"), (1, "#241a14")]) + WARMGLOW + BLUR
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    xs = [(0.25, 0.28, 0.1), (0.55, 0.42, 0.13), (0.8, 0.22, 0.08), (0.42, 0.62, 0.07)]
    for fx, fy, fr in xs:
        x, y, r = w * fx, h * fy, w * fr
        b += f'<line x1="{x}" y1="0" x2="{x}" y2="{y-r*0.9}" stroke="#3a2a20" stroke-width="3"/>'
        b += f'<circle cx="{x}" cy="{y}" r="{r*3.4}" fill="url(#warmglow)"/>'
        b += f'<path d="M{x-r*0.45} {y-r*0.9} L{x+r*0.45} {y-r*0.9} L{x+r} {y+r*0.4} Q{x} {y+r*0.6} {x-r} {y+r*0.4}Z" fill="#b8975a"/>'
        b += f'<ellipse cx="{x}" cy="{y+r*0.42}" rx="{r*0.95}" ry="{r*0.16}" fill="#ffe3ac"/>'
    b += f'<rect y="{h*0.86}" width="{w}" height="{h*0.14}" fill="#120d0b"/>'
    b += cup_side(w * 0.3, h * 0.93, w / 700)
    write(name, w, h, b, defs)


def beans_scene(name, w, h, seed=2):
    defs = lin("bg", [(0, "#2a1a10"), (1, "#0f0a07")]) + BLUR_S
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    r = random.Random(seed)
    for _ in range(int(w * h / 4200)):
        x, y, s = r.uniform(-20, w + 20), r.uniform(-20, h + 20), r.uniform(0.7, 1.4)
        a = r.uniform(0, 180)
        tone = r.choice(["#4a2a18", "#5a3622", "#3a2013", "#6b4430"])
        b += f'<g transform="translate({x:.0f} {y:.0f}) rotate({a:.0f}) scale({s:.2f})"><ellipse rx="34" ry="22" fill="{tone}"/><path d="M-30 0 Q0 -10 30 2" stroke="#1a0d06" stroke-width="4" fill="none"/><ellipse cx="-8" cy="-9" rx="12" ry="4" fill="#fff" opacity=".12"/></g>'
    b += f'<circle cx="{w*0.8}" cy="{h*0.2}" r="{min(w,h)*0.07}" fill="{MOON}" opacity=".9"/><circle cx="{w*0.8+min(w,h)*0.03}" cy="{h*0.2-min(w,h)*0.02}" r="{min(w,h)*0.07}" fill="#2a1a10"/>'
    write(name, w, h, b, defs)


def table_scene(name, w, h):
    defs = lin("wood", [(0, "#2b1f17"), (1, "#1a120d")]) + BLUR + WARMGLOW
    b = f'<rect width="{w}" height="{h}" fill="url(#wood)"/>'
    for i in range(0, w, 90):
        b += f'<line x1="{i}" y1="0" x2="{i+6}" y2="{h}" stroke="#000" stroke-opacity=".25" stroke-width="3"/>'
    b += f'<circle cx="{w*0.32}" cy="{h*0.4}" r="{w*0.4}" fill="url(#warmglow)" opacity=".5"/>'
    def cup(cx, cy, r):
        s = f'<circle cx="{cx+r*0.12}" cy="{cy+r*0.14}" r="{r*1.28}" fill="#000" opacity=".4" filter="url(#blur)"/>'
        s += f'<circle cx="{cx}" cy="{cy}" r="{r*1.25}" fill="#e8dcc6"/><rect x="{cx+r*0.8}" y="{cy-r*0.12}" width="{r*0.7}" height="{r*0.24}" rx="{r*0.12}" fill="#f6eee0"/>'
        s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f6eee0"/><circle cx="{cx}" cy="{cy}" r="{r*0.84}" fill="#6b4430"/>'
        s += f'<circle cx="{cx}" cy="{cy}" r="{r*0.5}" fill="#f4e8d2"/><circle cx="{cx+r*0.12}" cy="{cy-r*0.04}" r="{r*0.46}" fill="#6b4430"/>'
        return s
    b += cup(w * 0.32, h * 0.42, w * 0.17)
    b += cup(w * 0.7, h * 0.64, w * 0.12)
    b += f'<rect x="{w*0.52}" y="{h*0.1}" width="{w*0.3}" height="{h*0.2}" rx="8" fill="#8b4a30" transform="rotate(8 {w*0.6} {h*0.2})"/><rect x="{w*0.52}" y="{h*0.1}" width="{w*0.3}" height="{h*0.02}" fill="#f1e7d6" transform="rotate(8 {w*0.6} {h*0.2})"/>'
    b += f'<circle cx="{w*0.18}" cy="{h*0.82}" r="{w*0.07}" fill="#e7b05b"/><circle cx="{w*0.18}" cy="{h*0.82}" r="{w*0.045}" fill="#c98539"/>'
    write(name, w, h, b, defs)


def counter_scene(name, w, h):
    defs = lin("bg", [(0, "#17120f"), (1, "#2a1f18")]) + WARMGLOW + BLUR
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    for i in range(3):
        y = h * (0.16 + i * 0.13)
        b += f'<rect x="{w*0.08}" y="{y}" width="{w*0.84}" height="10" fill="#5a4030"/>'
        for k in range(7):
            x = w * (0.12 + k * 0.12)
            b += f'<path d="M{x} {y} l6 -{h*0.06} h{w*0.06} l6 {h*0.06}Z" fill="#e8dcc6" opacity="{0.9 - k%3*0.15:.2f}"/>'
    # espresso machine
    mx, my, mw, mh = w * 0.18, h * 0.58, w * 0.64, h * 0.2
    b += f'<circle cx="{w/2}" cy="{my}" r="{w*0.5}" fill="url(#warmglow)" opacity=".4"/>'
    b += f'<rect x="{mx}" y="{my}" width="{mw}" height="{mh}" rx="14" fill="#b8975a"/><rect x="{mx}" y="{my}" width="{mw}" height="{mh*0.25}" rx="14" fill="#d8bc7a"/>'
    for k in range(2):
        gx = mx + mw * (0.25 + k * 0.4)
        b += f'<rect x="{gx}" y="{my+mh}" width="{mw*0.14}" height="{h*0.05}" fill="#2a1f18"/><rect x="{gx+mw*0.05}" y="{my+mh+h*0.05}" width="{mw*0.04}" height="{h*0.1}" fill="#6b4430"/>'
        b += f'<path d="M{gx+mw*0.07} {my+mh+h*0.04} v{h*0.12}" stroke="#6b4430" stroke-width="5"/>'
    b += f'<circle cx="{mx+mw*0.1}" cy="{my+mh*0.6}" r="{mh*0.14}" fill="#f1e7d6"/><circle cx="{mx+mw*0.9}" cy="{my+mh*0.6}" r="{mh*0.14}" fill="#f1e7d6"/>'
    b += f'<rect x="0" y="{h*0.86}" width="{w}" height="{h*0.14}" fill="#0e0a08"/><rect x="0" y="{h*0.86}" width="{w}" height="6" fill="#5a4030"/>'
    write(name, w, h, b, defs)


def pastry_scene(name, w, h):
    defs = lin("bg", [(0, "#241a14"), (1, "#120d0a")]) + BLUR
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    b += f'<ellipse cx="{w/2}" cy="{h*0.56}" rx="{w*0.46}" ry="{h*0.4}" fill="#000" opacity=".5" filter="url(#blur)"/>'
    b += f'<ellipse cx="{w/2}" cy="{h*0.5}" rx="{w*0.46}" ry="{h*0.42}" fill="#cdbf9f"/><ellipse cx="{w/2}" cy="{h*0.5}" rx="{w*0.42}" ry="{h*0.37}" fill="#f6eee0"/>'
    r = random.Random(6)
    for i, (fx, fy) in enumerate([(0.3, 0.42), (0.5, 0.34), (0.7, 0.44), (0.4, 0.62), (0.62, 0.64)]):
        x, y = w * fx, h * fy
        s = w * 0.07
        if i % 2 == 0:
            b += f'<g transform="translate({x} {y}) rotate({r.randint(-30,30)})"><path d="M{-s*1.6} {s*0.4} Q{-s*1.8} {-s*0.9} 0 {-s} Q{s*1.8} {-s*0.9} {s*1.6} {s*0.4} Q{s} {s*0.1} 0 {s*0.6} Q{-s} {s*0.1} {-s*1.6} {s*0.4}Z" fill="#d99a46"/><path d="M{-s} {-s*0.4} Q0 {-s*0.8} {s} {-s*0.4}" stroke="#f0c070" stroke-width="5" fill="none"/></g>'
        else:
            b += f'<circle cx="{x}" cy="{y}" r="{s}" fill="#c98539"/><circle cx="{x}" cy="{y}" r="{s*0.7}" fill="#e7b05b"/>'
            for _ in range(5):
                b += f'<circle cx="{x+r.uniform(-s*0.5,s*0.5):.0f}" cy="{y+r.uniform(-s*0.5,s*0.5):.0f}" r="{s*0.1:.0f}" fill="#4b2e1b"/>'
    write(name, w, h, b, defs)


def map_scene(name, w, h):
    defs = lin("bg", [(0, "#1c1815"), (1, "#14100e")]) + WARMGLOW
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    # blocks
    r = random.Random(14)
    for gx in range(0, w, 110):
        for gy in range(0, h, 90):
            if r.random() < 0.8:
                b += f'<rect x="{gx+10}" y="{gy+10}" width="{r.randint(70,92)}" height="{r.randint(52,70)}" rx="6" fill="#26211e"/>'
    # park + river
    b += f'<path d="M0 {h*0.78} Q{w*0.3} {h*0.66} {w*0.55} {h*0.8} T{w} {h*0.7} L{w} {h*0.84} Q{w*0.7} {h*0.94} {w*0.5} {h*0.9} T0 {h*0.9}Z" fill="#1d2a30"/>'
    b += f'<ellipse cx="{w*0.2}" cy="{h*0.25}" rx="{w*0.1}" ry="{h*0.12}" fill="#202b21"/>'
    # roads
    b += f'<path d="M0 {h*0.3} L{w} {h*0.42}" stroke="#3a322c" stroke-width="16"/><path d="M{w*0.3} 0 L{w*0.38} {h}" stroke="#3a322c" stroke-width="12"/>'
    b += f'<path d="M{w*0.2} {h*0.62} Q{w*0.5} {h*0.28} {w*0.82} {h*0.52}" stroke="{GOLD}" stroke-width="10" fill="none" stroke-linecap="round" opacity=".9"/>'
    b += f'<text x="{w*0.52}" y="{h*0.3}" font-family="Georgia, serif" font-style="italic" font-size="22" fill="{GOLD}" transform="rotate(-14 {w*0.52} {h*0.3})">Crescent Street</text>'
    # pin
    px, py = w * 0.58, h * 0.42
    b += f'<circle cx="{px}" cy="{py}" r="120" fill="url(#warmglow)"/>'
    b += f'<circle cx="{px}" cy="{py}" r="34" fill="none" stroke="{GOLD}" stroke-width="2" opacity=".6"/><circle cx="{px}" cy="{py}" r="58" fill="none" stroke="{GOLD}" stroke-width="1.5" opacity=".35"/>'
    b += f'<circle cx="{px}" cy="{py}" r="16" fill="{CREAM}"/><circle cx="{px+6}" cy="{py-4}" r="14" fill="#1c1815"/>'
    write(name, w, h, b, defs)


def og_image():
    street_scene("og-image", 1200, 630, "night")


def build_scenes():
    street_scene("hero-night", 1920, 1200, "night")
    street_scene("hero-night-mobile", 900, 1400, "night")
    window_scene("exp-morning", 1200, 1400, "morning", "morning")
    window_scene("exp-afternoon", 1200, 1400, "afternoon", "afternoon")
    window_scene("exp-evening", 1200, 1400, "evening", "evening")
    window_scene("exp-latenight", 1200, 1400, "night", "night")
    window_scene("about-space", 1100, 1400, "evening", "evening")
    street_scene("about-story", 1100, 1400, "evening", moon_big=False)
    beans_scene("about-coffee", 1100, 1400, seed=4)
    lamps_scene("about-philosophy", 1100, 1400)
    counter_scene("about-preview", 1000, 1250)
    table_scene("experience-preview", 1200, 900)

    # gallery
    window_scene("gallery-1", 1200, 1500, "night", "night")
    table_scene("gallery-2", 1000, 1000)
    pastry_scene("gallery-3", 1400, 900)
    lamps_scene("gallery-4", 800, 1100)
    beans_scene("gallery-5", 1000, 700, seed=9)
    street_scene("gallery-6", 1400, 900, "evening")
    counter_scene("gallery-7", 900, 1200)
    window_scene("gallery-8", 1000, 1250, "morning", "morning")
    street_scene("gallery-9", 1000, 1000, "night", moon_big=False)
    map_scene("map", 1200, 800)


if __name__ == "__main__":
    build_menu()
    build_scenes()
    og_image()
    n = len([f for f in os.listdir(OUT) if f.endswith(".svg")])
    print(f"Generated {n} images in {os.path.abspath(OUT)}")
