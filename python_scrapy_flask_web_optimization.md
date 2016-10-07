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
	--按照发布时间更新id
	CREATE TABLE `joke_copy` (
	  `id` int(11) NOT NULL AUTO_INCREMENT,
	  `title` varchar(255) DEFAULT NULL,
	  `category_id` int(11) DEFAULT NULL,
	  `content` text,
	  `view_count` int(11) DEFAULT NULL COMMENT '浏览量',
	  `link` varchar(255) DEFAULT NULL COMMENT '抓取链接',
	  `created_at` datetime DEFAULT NULL,
	  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
	  `is_deleted` tinyint(1) DEFAULT '0',
	  PRIMARY KEY (`id`)
	) ENGINE=MyISAM AUTO_INCREMENT=11216 DEFAULT CHARSET=utf8;
	insert into joke_copy(title,category_id,content,view_count,link,created_at,updated_at,is_deleted) select title,category_id,content,view_count,link,created_at,updated_at,is_deleted from joke order by created_at asc ;
	TRUNCATE table joke ;
	insert into joke(title,category_id,content,view_count,link,created_at,updated_at,is_deleted) select title,category_id,content,view_count,link,created_at,updated_at,is_deleted from joke_copy order by created_at asc ;
	```

## TODO:
1.
- [x]添加分类
- [ ]添加搜索
- [x]添加面包屑
- [x]添加阅读量
- [x]分类最新、热门
- [ ]百度语音读笑话

2.
- [ ]添加分类页面
- [x]最热排序 阅读量-
- [ ]共多少页位置
- [ ]听笑话
- [x]添加上一篇下一篇-
- [x]去掉链接-bin/tools.py
- [ ]添加评论
- [x]添加404页面


## 模板
http://www.html5tricks.com/demo/jquery-bootstrap-dropdown-menu/index.html
http://www.html5tricks.com/jquery-bootstrap-dropdown-menu.html