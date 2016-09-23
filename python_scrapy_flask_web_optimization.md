# 笑话集优化
接上篇[从头开始搭建一个爬虫网站](http://www.liangcuntu.com/python_scrapy_flask_web),对网站进行一些优化，添加一些功能。

## 添加百度统计
先来添加个百度统计吧。
[Jinja2 模板引擎 ](http://jinja.pocoo.org/docs/dev/templates/)
[Flask-Bootstrap](http://pythonhosted.org/Flask-Bootstrap/basic-usage.html#examples)

```
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?436cb9b289c0af4b9ed90e2d2e944cb7";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>

```
## Flask-boostrap 加载本地资源

[Flask-Bootstrap Configuration](https://pythonhosted.org/Flask-Bootstrap/configuration.html)
```
$ vim hello.py

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

```

## 定时抓取
1. 修改抓取和数据保存程序
tutorial/tutorial/spiders/joke.py
tutorial/tutorial/models/joke.py
2. 添加定时脚本
```
$ vim bin/crawl.sh

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
```
## 修改图片和链接域名
```shell 
mkdir -p static/joke
cd tutorial
mv jokejimg ../static/joke
mv upfilesnew ../static/joke
mv UpFilesnew ../static/joke
mv UpFiles ../static/joke
```
```sql
update joke set content = replace(content,'http://gaoxiao.jokeji.cn','/static/joke') ;
update joke set content = replace(content,'src="http://www.jokeji.cn','src="/static/joke') ;
update joke set content = replace(content,'href="http://www.jokeji.cn','href="http://joke.liangcuntu.com') ;
```

## 添加分类
## 添加搜索
## 添加面包屑
## 添加阅读量
## 分类最新、热门
## 百度语音读笑话

TODO:
添加分类页面
最热排序 阅读量-
共多少页位置
听笑话



## 模板
http://www.html5tricks.com/demo/jquery-bootstrap-dropdown-menu/index.html
http://www.html5tricks.com/jquery-bootstrap-dropdown-menu.html