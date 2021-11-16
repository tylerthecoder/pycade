#!/bin/bash

[[ -z "$1" ]] && echo "Usage: $0 <rom_name>" && exit 1]]

curl "https://download2.vimm.net/download/?mediaId=$1" \
  -H 'Connection: keep-alive' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Sec-GPC: 1' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Referer: https://vimm.net/' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Cookie: __cf_bm=1ac1d089d43dcceb89126013998cc98a85d171b8-1629764787-1800-AWFrg8cwpE2vbjA5PNdng1fWIhrzZ0+YSyA4UvmbD096AtDHM4XZOotNA0PxoVdhZjQtUxUejRDezmE96zMkY/jdXAtMLzYL9k2ga37HBEn9P3u6GYg6yHItJjnQ+a6Bmg==' \
  --compressed \
	-o rom.zip

unzip rom.zip -d rom
rm -f rom.zip "rom/Vimm's Lair.txt"
mv rom/* roms/nes/
rm -rf rom

