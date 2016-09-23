## 正则表达式 - 语法
http://www.runoob.com/regexp/regexp-syntax.html
## python实现简易采集爬虫
http://www.cnblogs.com/txw1958/archive/2012/07/28/python-spider.html
$ sudo pip install pysqlite


## scrapy
http://scrapy.org/download/
https://pypi.python.org/pypi/pysqlite
http://doc.scrapy.org/en/1.1/

$ sudo python setup.py install

## issue
q:Scrapy throws ImportError: cannot import name xmlrpc_client
a:
sudo rm -rf /Library/Python/2.7/site-packages/six*
sudo rm -rf /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/six*
sudo pip install six


scrapy -h

scrapy startproject tutorial
cd tutorial
scrapy genspider example example.com

cd tutorial
scrapy genspider liangcuntu liangcuntu.com

scrapy crawl dmoz

scrapy crawl liangcuntu

scrapy runspider myspider.py

scrapy  view http://www.liangcuntu.com

## spider
https://segmentfault.com/a/1190000002544142
http://www.zhihu.com/question/20899988
http://www.360doc.cn/article/972619_34106632.html

[用python爬取文章链接并分类](http://blog.csdn.net/yuxiangyunei/article/details/50438936)
[使用scrapy实现爬网站例子和实现网络爬虫(蜘蛛)的步骤](http://www.jb51.net/article/46107.htm)

[QQ 聊天机器人小薇发布](http://www.oschina.net/news/73874/qq-xiaov)
[xiaov](https://github.com/b3log/xiaov)

## flask
[Jinja2中文文档](http://www.kancloud.cn/manual/jinja2/70468)

## Todo:抓取图片到本地√
## Todo:数据入库
## Todo:去重


##文字转声音
1. pyttsx
https://github.com/parente/pyttsx

- 安装
```
pip install pyttsx
```
http://stackoverflow.com/questions/15653145/using-google-text-to-speech-in-javascript
2. google
```javascript
var audio = new Audio();
audio.src ='http://translate.google.com/translate_tts?ie=utf-8&tl=en&q=Hello%20World.';
audio.play();
```
3. ResponsiveVoice
[ResponsiveVoice.JS](http://responsivevoice.org/)
4. 科大讯飞
[科大讯飞和Tizen-TTS语音合成引擎说明](http://bbs.tizennet.com/thread-100426-1-1.html)

5. 百度语音合成
[语音合成服务](http://yuyin.baidu.com/tts)