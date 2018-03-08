# _*_ coding:utf-8
from urllib import  request
from urllib import error
if __name__ == "__main__":
    url = "http://www.douyu.com/white55"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
    except error.URLError as e:
        if hasattr(e,'code'):
            print('HTTPError:%s'%e.code)
        elif hasattr(e,'reason'):
            print("URLError:%s"%e.reason)
