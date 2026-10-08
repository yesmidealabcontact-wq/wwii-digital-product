"""Inline fonts and preview images into landing.html (Gumroad pages can't load outside files).
Usage: python3 build_landing.py <folder with resized jpgs>"""
import base64, re, sys, pathlib
here = pathlib.Path(__file__).resolve().parent
root = here.parents[1]
imgdir = pathlib.Path(sys.argv[1])
t = (here / "landing.template.html").read_text()
b64 = lambda p: base64.b64encode(p.read_bytes()).decode()
t = re.sub(r"\{\{FONT:([\w-]+)\}\}", lambda m: "data:font/woff;base64," + b64(root / "site/assets/fonts" / (m.group(1) + ".woff")), t)
t = re.sub(r"\{\{IMG:([\w-]+)\}\}", lambda m: "data:image/jpeg;base64," + b64(imgdir / (m.group(1) + ".jpg")), t)
(here / "landing.html").write_text(t)
print("landing.html", len(t) // 1024, "KB")
