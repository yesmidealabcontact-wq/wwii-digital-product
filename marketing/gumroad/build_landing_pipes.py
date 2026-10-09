"""Build landing-pipes.html: a self-contained Gumroad landing page for The Pipes at Dawn.
Fonts and images are inlined as data: URIs (Gumroad blocks outside image hosts).
Needs the archive photo private/photos/b5103.jpg for the hero background.
Usage: python3 build_landing_pipes.py"""
import base64, io, re, pathlib
from PIL import Image

here = pathlib.Path(__file__).resolve().parent
root = here.parents[1]
img = root / "site/assets/img/pipes"
IMAGES = {
    "cover": img / "cover-small.jpg", "maps": img / "pack-maps-small.jpg", "prints": img / "pack-prints-small.jpg",
    "certificate": img / "pack-certificate-small.jpg", "workbook": img / "pack-workbook-small.jpg",
    "p03": img / "p03-record-check-small.jpg", "p09": img / "p09-night-attack-small.jpg", "p10": img / "p10-into-the-dust-small.jpg",
    "p12": img / "p12-roll-small.jpg", "p15": img / "p15-millin-map-small.jpg", "p16": img / "p16-millin-photo-small.jpg",
}


def b64(data, mime):
    return f"data:{mime};base64," + base64.b64encode(data).decode()


def hero():
    im = Image.open(root / "private/photos/b5103.jpg").convert("L")
    im.thumbnail((900, 900))
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=55, optimize=True, progressive=True)
    return b64(buf.getvalue(), "image/jpeg")


t = (here / "landing-pipes.template.html").read_text()
t = re.sub(r"\{\{FONT:([\w-]+)\}\}", lambda m: b64((root / "site/assets/fonts" / (m.group(1) + ".woff")).read_bytes(), "font/woff"), t)
cache = {"hero": hero()}


def image(key):
    if key not in cache:
        cache[key] = b64(IMAGES[key].read_bytes(), "image/jpeg")
    return cache[key]


t = re.sub(r"\{\{IMG:([\w-]+)\}\}", lambda m: image(m.group(1)), t)
(here / "landing-pipes.html").write_text(t)
print("landing-pipes.html", len(t) // 1024, "KB")
