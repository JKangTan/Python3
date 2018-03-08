# _*_ coding:utf-8 _*_

from urllib import request
from http import cookiejar

if __name__ == "__main__":
    #声明一个 CookieJar 对象实例来保存 cookie
    cookie = cookiejar.CookieJar()
    #利用 urllib.request 库的 HTTPCookieorProcessor对象来创建 cookie 处理器
    #也就是Handler
    handler = request.HTTPCookieProcessor(cookie)
    #通过 cookieHandler 创建 opener
    opener = request.build_opener(handler)
    #此处的 open 方法发开网页
    response = opener.open('http://www.baidu.com')
    #打印 cookie 信息
    for item in cookie:
        print('Name = %s'%item.name)
        print('Value = %s'%item.value)