mkdocs build
./scripts/SitemapConverter/main.py
./scripts/PagelinkConverter/main.py
curl -H 'Content-Type:text/plain' --data-binary @urls.txt BAIDU_API