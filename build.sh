mkdocs build;
chmod 777 ./scripts/SitemapConverter/main.py;
chmod 777 ./scripts/PagelinkConverter/main.py;
./scripts/SitemapConverter/main.py;
./scripts/PagelinkConverter/main.py;
chmod 777 ./urls.txt;
curl -H 'Content-Type:text/plain' --data-binary @urls.txt BAIDU_API;