# -*- coding: utf-8 -*-
__author__ = 'feng'
import os
def replace_test():
    str = '浏览：8993次'
    print str.replace("浏览：","").replace("次","")

def get_img():
    picurl = "http://images.51cto.com/files/uploadimg/20100630/104906665.jpg"
    #判断是否有http
    if not picurl.find("http") == -1:
        host = picurl.split("/")
        print host
        print "/".join(host[0:3])
        print host[-1]
        print "/".join(host[3:-1])

### 创建多层目录
def mkdirs(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        # 创建目录操作函数
        os.makedirs(path)
        # 如果不存在则创建目录
        print path + u' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path + u' 目录已存在'
        return False



if __name__ == '__main__':
    get_img()
    dst_dir = os.path.abspath(os.curdir)
    if(not os.path.isdir(dst_dir)):
        mkdirs(dst_dir)