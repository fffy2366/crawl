
# 从头开始搭建一个爬虫网站
------

打算用python搭建一个网站，内容用scrapy抓取网络内容。

## 用到的技术
* python
* scrapy
* flask
* sqlite
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

6.Todo :
- [x] 抓取图片到本地√
- [ ] 数据入库
- [ ] 去重
- [ ] 搭建flask


code at github:https://github.com/fffy2366/crawl