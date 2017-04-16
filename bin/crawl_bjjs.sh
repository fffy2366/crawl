#!/usr/bin/env bash
#sh bin/crawl_bjjs.sh
#chmod -R 755 /opt/www/crawl/bin/crawl_bjjs.sh
#0 */1 * * *  /opt/www/crawl/bin/crawl_bjjs.sh >> /tmp/crawl_bjjs.log 2>&1
# crontab -e
basepath=$(cd `dirname $0`; pwd)
project_dir=$(dirname $basepath)
cd $project_dir"/tutorial"
echo "start"
. /etc/profile
. /root/.bash_profile
/usr/local/bin/scrapy crawl bjjs
echo "finish"