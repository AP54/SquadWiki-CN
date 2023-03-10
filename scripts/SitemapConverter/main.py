#!/usr/bin/python

import os
import datetime
import re

sitemap_header = r"""<?xml version="1.0" encoding="UTF-8"?>
<urlset
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
"""
sitemap_tailer = r"""</urlset>"""

sitemap_timestamp = datetime.datetime.now(
).astimezone().replace(microsecond=0).isoformat()

sitemap_output = ''

sitemap_output += sitemap_header

for root, dirs, files in os.walk("./docs", topdown=False):
    for name in files:
        pagelinkmatch = re.match('.+.md$', os.path.join(root, name).replace(
            './docs', 'https://www.squadwiki.cn').replace('\\', '/'))
        if pagelinkmatch != None:
            apagelink = '<url>\n  <loc>%s</loc>\n  <lastmod></lastmod>\n  <priority>0.99</priority>\n  <changefreq>daily</changefreq>\n</url>\n' % (
                pagelinkmatch.group(0))
            sitemap_output += apagelink.replace('index.md',
                                                '').replace('.md', '')

sitemap_output += sitemap_tailer

sitemap_file = open('./site/sitemap.xml', mode='w',
                    encoding="utf-8", errors="ignore")
sitemap_file.write(sitemap_output)
sitemap_file.close()
print(sitemap_output)
