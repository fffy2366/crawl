#!/usr/bin/env bash
#sh bin/crawl.sh
#chmod -R 755 /opt/www/crawl/bin/crawl.sh
#0 15 * * *  /opt/www/crawl/bin/crawl.sh >> /tmp/crawl.log 2>&1
# crontab -e
basepath=$(cd `dirname $0`; pwd)
project_dir=$(dirname $basepath)
cd $project_dir"/tutorial"
echo "start"
. /etc/profile
. /root/.bash_profile
/usr/local/bin/scrapy crawl joke
echo "finish"