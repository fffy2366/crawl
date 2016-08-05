
# 从头开始搭建一个爬虫网站
------

打算用python搭建一个网站，内容用scrapy抓取网络内容。

## 用到的技术
* python
* scrapy
* flask
* sqlite
* mysql
* bootstrap

## scrapy 爬内容
1. scrapy 下载 

http://scrapy.org/download/

2. 安装
```
$ sudo python setup.py install
```
3. pip在线安装
```
$  pip install scrapy
```
window安装报错：

error: Microsoft Visual C++ 9.0 is required (Unable to find vcvarsall.bat). Get it from http://aka.ms/vcpython27

解决：

安装 [Micorsoft Visual C++ Compiler for Python 2.7](http://www.microsoft.com/en-us/download/details.aspx?id=44266)

参考：http://www.cnblogs.com/ldm1989/p/4210743.html

安装lxml依然报错：

从http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml下载whl包安装
```
$ pip install lxml-3.6.1-cp27-cp27m-win_amd64.whl
```
继续安装scrapy：
```
$ pip install scrapy
```
查看是否安装成功
```
$ scrapy -h
```
4. 创建项目
```
mkdir crawl
scrapy startproject tutorial
scrapy genspider joke jokeji.cn
```


5. 抓取
```
$ scrapy crawl joke
```

报错：
exceptions.ImportError: No module named win32api

解决：
pip install pypiwin32

6. Todo :
- [x] 列表详情√
- [x] 抓取图片到本地√
- [x] 遍历所有列表页√
- [x] 数据入库
- [ ] 搭建flask
- [ ] 定时程序抓取内容

7. 创建数据库
```sql
CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `is_deleted` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `joke` (
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
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

```

8. 编写分类和内容入库程序，如下：

crawl/tutorial/tutorial/models/mysql.py
crawl/tutorial/tutorial/models/category.py
crawl/tutorial/tutorial/models/joke.py

```
$ scrapy crawl joke
```
总共抓取11215条数据

## flask搭建
[flask文档](http://docs.jinkan.org/docs/flask/)
1. 安装
```
$ easy_install virtualenv
$ cd /dD:\python
$ virtualenv venv
#激活
$ venv\scripts\activate
#安装
$ pip install Flask
```
2. 编写列表和详情页



## 代码
code at github:https://github.com/fffy2366/crawl