#! /usr/bin/env python3
# *-* coding: utf-8 *-*

from os import walk
from os.path import join, abspath, dirname

SRC_DIR = join(dirname(abspath(__file__)), '_build/html/')
SITEMAP = join(SRC_DIR, 'sitemap.xml')
URL_LOC = '  <url><loc>https://mikemabey.com/{}</loc></url>\n'


def main():
    with open(SITEMAP, 'w') as sitemap:
        sitemap.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for root, dirs, files in walk(SRC_DIR):
            for name in files:
                if name.endswith(('.html', '.xsd')):
                    sitemap.write(URL_LOC.format(join(root, name).split('html/', 1)[1]))

        sitemap.write('</urlset>\n')

if __name__ == '__main__':
    main()
