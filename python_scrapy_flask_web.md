
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
- [ ] 部署上线

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

------

## flask搭建
[flask文档](http://docs.jinkan.org/docs/flask/)
1. 安装
```
$ easy_install virtualenv
$ cd /dD:\python
$ virtualenv venv
#windows下激活
$ venv\scripts\activate
#安装
$ pip install Flask
```
2. 运行
```
$ python hello.py
```

3. 安装bootstrap
[Flask-Bootstrap](http://pythonhosted.org/Flask-Bootstrap/)

```
$ bower install bootstrap
$ pip install flask-bootstrap


```

4. 编写列表和详情页
```
hello.py
templates/blocks.html
templates/detail.html
templates/hello.html
tutorial/tutorial/models/mysql.py
tutorial/tutorial/models/joke.py
tutorial/tutorial/models/category.py
```
以上是主要列表和详情的主要文件，至此大功告成！剩下的就是一些细节的修修改改了！


## 问题：
发现抓取的内容有一千多条为空，查看页面源代码是内容不是p标签所致，待处理。


## 部署到centos
1. 克隆代码
```
$ git clone git@github.com:fffy2366/crawl.git
```
2. 安装前面python相关
2.1 [Centos 6.4 python 2.6 升级到 2.7](http://blog.csdn.net/jcjc918/article/details/11022345)
```
$ cd /opt/soft/
$ ll
$ wget http://python.org/ftp/python/2.7.3/Python-2.7.3.tar.bz2  
$ tar -jxvf Python-2.7.3.tar.bz2  
$ cd Python-2.7.3
$ ./configure
$ make all
$ make install 
$ make clean
$ make distclean 
$ /usr/local/bin/python2.7 -V  
$ python -V
$ mv /usr/bin/python /usr/bin/python2.6.6  
$ ln -s /usr/local/bin/python2.7 /usr/bin/python  
$ python -V
$ vi /usr/bin/yum 
```
2.2 安装pip
```
$ wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate
$ python get-pip.py
#以上失败
$ yum install python-pip
```
2.3 安装scrapy
```
$ pip install scrapy
#抱错：ImportError: No module named pkg_resources
#解决：
$ wget https://bootstrap.pypa.io/ez_setup.py -O - | python
##仍然抱错,卸载python-pip，重新下载安装
$ yum remove python-pip
$ wget --no-check-certificate https://github.com/pypa/pip/archive/1.5.5.tar.gz

#注意：wget获取https的时候要加上：--no-check-certificate

$ tar zvxf 1.5.5.tar.gz    #解压文件
$ cd pip-1.5.5/
$ python setup.py install
#OK，这样就安装好pip了，

#下面来安装 requests吧。

$ pip install requests
$ /usr/local/bin/pip install scrapy
$ ln -s /usr/local/bin/pip /usr/bin/pip
$ pip install scrapy
$ pip install twisted
$ pip install crpytography
#以上仍然抱错
$ pip install --upgrade pip
$ pip install scrapy
#ok,成功

```

2.4 安装flask

```
$ easy_install virtualenv
$ cd /dD:\python
$ virtualenv venv
#激活
$ .venv\bin\activate
#安装
$ pip install Flask
```

2.5 部署mysql 安装python相关模块
```
$mysql -uroot -p

create database joke ;
use joke
#执行前面的sql

$ grant all privileges on joke.* to joke@localhost identified by 'db****';

#修改数据库连接
$ vim /crawl/tutorial/tutorial/models/mysql.py
#安装sqlite
$ yum install gcc
$ pip install pysqlite
# 以上抱错，执行下面
$ yum install sqlite-devel
$ wget https://pypi.python.org/packages/cc/a4/023ee9dba54b3cf0c5a4d0fb2f1ad80332ef23549dd4b551a9f2cbe88786/pysqlite-2.8.2.tar.gz
$ tar zxvf pysqlite-2.8.2.tar.gz 
$ cd pysqlite-2.8.2
$ python setup.py install
# 继续抓取
$ scrapy crawl joke

#解决没有sqlite3模块的问题
#curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
# the following to ~/.bash_profile:
export PATH="/root/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

$ pyenv install 2.7.9
# 上面的方法下载没反应 ，所以重复步骤2.1 ，重新编译python,搞定
#Install the sqlite-devel package:

$ yum install sqlite-devel -y
#Recompile python from the source:
$ ./configure
$ make
$ make altinstall

# 安装mysqldb模块
$ yum install MySQL-python -y
# 上面安装不生效，执行下面的可以了
$ easy_install MySQL-python


$ pip install Flask
$ pip install flask-bootstrap
```

2.6 [CentOS 下用 Nginx 和 uwsgi 部署 flask 项目](https://segmentfault.com/a/1190000004294634)
```
$ pip install uwsgi


```

## 代码
code at github:https://github.com/fffy2366/crawl

## 小结

这只是爬虫入门、python web入门的一个小例子，可以通过它来学习python知识，学习基本的爬虫知识，当你想学习他们并还在查询学习方法的时候，不妨从头开始动手做一个类似的例子。另外做爬虫站点并不是很光荣的事情，有时候会被封IP，有时候会被告侵权，所以大家自己权衡吧。不管如何，只要能把这个程序跑一遍相信你会跟我一样有所收获。