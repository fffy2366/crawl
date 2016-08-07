#!/usr/bin/env bash
#sh bin/crawl.sh
#40 15 * * *  /opt/www/crawl/bin/crawl.sh >> /tmp/crawl.log 2>&1
# crontab -e
basepath=$(cd `dirname $0`; pwd)
project_dir=$(dirname $basepath)
cd $project_dir"/tutorial"
echo "start"
scrapy crawl joke
echo "finish"