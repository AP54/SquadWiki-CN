import os
import re

links_output = ''

for root, dirs, files in os.walk("./docs", topdown=False):
    for name in files:
        pagelinkmatch = re.match('.+.md$', os.path.join(root, name).replace(
            './docs', 'https://www.squadwiki.cn').replace('\\', '/'))
        if pagelinkmatch != None:
            apagelink = pagelinkmatch.group(0)+'\n'
            links_output += apagelink.replace('index.md',
                                              '').replace('.md', '')

sitemap_file = open('./site/urls.txt', mode='w',
                    encoding="utf-8", errors="ignore")
sitemap_file.write(links_output)
sitemap_file.close()
print(links_output)
