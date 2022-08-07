#! /usr/bin/env python3
# *-* coding: utf-8 *-*

from os import walk
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "build/html/"
SITEMAP = SRC_DIR / "sitemap.xml"
URL_LOC = "  <url><loc>https://mikemabey.com/{}</loc></url>\n"


def main():
    with open(SITEMAP, "w") as sitemap:
        sitemap.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        )
        for root, dirs, files in walk(SRC_DIR):
            for name in files:
                if name.endswith((".html", ".xsd")):
                    sitemap.write(
                        URL_LOC.format(str(Path(root) / name).split("html/", 1)[1])
                    )

        sitemap.write("</urlset>\n")


if __name__ == "__main__":
    main()
