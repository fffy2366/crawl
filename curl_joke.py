# ! /usr/bin/python
#encoding:utf-8
__author__ = 'feng'
import re, sys, time
import httplib, os.path as osp
from urlparse import urlparse

'''
http://www.jokeji.cn/list.htm
'''
import os, urllib2, re, time, MySQLdb, sys
domain = 'www.jokeji.cn'
# 设置提交的header头
headers = {"Accept": "*/*", "Referer": "http://"+domain+"/",
           "User-Agent": "Mozilla/5.0+(compatible;+Googlebot/2.1;++http://www.google.com/bot.html)"}
# 连接服务器
dl = httplib.HTTPConnection(domain)

## 获取一个列表标题和链接
def list(url='http://www.jokeji.cn/list.htm'):
    R = 0
    urls = urlparse(url);
    path = urls[2];
    if urls[4] != '': path += '?' + urls[4]
    dl.request(method="GET", url=path, headers=headers);
    rs = dl.getresponse()
    if rs.status == 200:
        R = parseData(rs.read(), url)

    print(url)
    return R
# 清除html代码里的多余空格
def clearBlank(html):
    if len(html) == 0: return ''
    html = re.sub('\r|\n|\t', '', html)
    while html.find("  ") != -1 or html.find('&nbsp;') != -1:
        html = html.replace('&nbsp;', ' ').replace('  ', ' ')
    return html

# 格式化url
def formatURL(html, url):
    urls = re.findall('''(<a[^>]*?href="([^"]+)"[^>]*?>)|(<a[^>]*?href='([^']+)'[^>]*?>)''', html, re.I)
    if urls == None: return html
    for regs in urls:
        html = html.replace(regs[0], matchURL(regs[0], url))
    return html
# 格式化单个url
def matchURL(tag, url):
    urls = re.findall('''(.*)(src|href)=(.+?)( |/>|>).*|(.*)url\(([^\)]+)\)''', tag, re.I)
    if urls == None:
        return tag
    else:
        if urls[0][5] == '':
            urlQuote = urls[0][2]
        else:
            urlQuote = urls[0][5]

    if len(urlQuote) > 0:
        cUrl = re.sub('''['"]''', '', urlQuote)
    else:
        return tag

    urls = urlparse(url);
    scheme = urls[0];
    if scheme != '': scheme += '://'
    host = urls[1];
    host = scheme + host
    if len(host) == 0: return tag
    path = osp.dirname(urls[2]);
    if path == '/': path = '';
    if cUrl.find("#") != -1: cUrl = cUrl[:cUrl.find("#")]
    # 判断类型
    if re.search('''^(http|https|ftp):(//|\\\\)(([\w/\\\+\-~`@:%])+\.)+([\w/\\\.\=\?\+\-~`@':!%#]|(&amp;)|&)+''', cUrl,
                 re.I) != None:
        # http开头的url类型要跳过
        return tag
    elif cUrl[:1] == '/':
        # 绝对路径
        cUrl = host + cUrl
    elif cUrl[:3] == '../':
        # 相对路径
        while cUrl[:3] == '../':
            cUrl = cUrl[3:]
            if len(path) > 0:
                path = osp.dirname(path)
    elif cUrl[:2] == './':
        cUrl = host + path + cUrl[1:]
    elif cUrl.lower()[:7] == 'mailto:' or cUrl.lower()[:11] == 'javascript:':
        return tag
    else:
        cUrl = host + path + '/' + cUrl
    R = tag.replace(urlQuote, '"' + cUrl + '"')
    return R


# html代码截取函数
def sect(html, start, end, cls=''):
    if len(html) == 0: return;
    # 正则表达式截取
    if start[:1] == chr(40) and start[-1:] == chr(41) and end[:1] == chr(40) and end[-1:] == chr(41):
        reHTML = re.search(start + '(.*?)' + end, html, re.I)
        if reHTML == None: return
        reHTML = reHTML.group()
        intStart = re.search(start, reHTML, re.I).end()
        intEnd = re.search(end, reHTML, re.I).start()
        R = reHTML[intStart:intEnd]
    # 字符串截取
    else:
        # 取得开始字符串的位置
        intStart = html.lower().find(start.lower())
        # 如果搜索不到开始字符串，则直接返回空
        if intStart == -1: return
        # 取得结束字符串的位置
        intEnd = html[intStart + len(start):].lower().find(end.lower())
        # 如果搜索不到结束字符串，也返回为空
        if intEnd == -1: return
        # 开始和结束字符串都有了，可以开始截取了
        R = html[intStart + len(start):intStart + intEnd + len(start)]
    # 清理内容
    if cls != '':
        R = clear(R, cls)
    # 返回截取的字符
    return R


# 正则清除
def clear(html, regexs):
    if regexs == '': return html
    for regex in regexs.split(chr(10)):
        regex = regex.strip()
        if regex != '':
            if regex[:1] == chr(40) and regex[-1:] == chr(41):
                html = re.sub(regex, '', html, re.I | re.S)
            else:
                html = html.replace(regex, '')
    return html


# 格式化为路径
def en2path(enStr):
    return re.sub('[\W]+', '-', en2chr(enStr), re.I | re.U).strip('-')


# 替换实体为正常字符
def en2chr(enStr):
    return enStr.replace('&amp;', '&')

def parseData(html, url):
    # 格式化html代码
    format = formatURL(clearBlank(html), url)

    # 取出所有的连接
    # urls = re.findall(r'''(<a[^>]*?href="([^"]+)"[^>]*?>)|(<a[^>]*?href='([^']+)'[^>]*?>)''', format, re.I)
    # urls = re.findall(r'''(<a[^>]*?href="([^"]+)"[^>]*?target="_blank">)''', format, re.I)
    # urls = re.findall(r'''(<[^>]*?href="([^"]+)"[^>]*?target="_blank">)''', format, re.I)
    # urls = re.findall('<a href="(.*)" target="_blank">(.*)</a>', format, re.I)
    # urls = re.findall('<li><b><a href="(.*)" ', format, re.I)
    urls = sect(format, '<li><b>', '</li>','(<a[^>]*?href="([^"]+)"[^>]*?>)')

    print(urls)
    print(len(urls))


if __name__=='__main__':
    list()
    sys.exit()
