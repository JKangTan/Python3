# _*_ coding:utf-8

from urllib import  request

if __name__ == '__main__':
    #以 CSDN 为例,CSDN 不更改 userAgent 无法访问
    url = "http://www.csdn.net/"
    head = {}
    #写入 User Agent 信息
    head["User-Agent"] = "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19"
    req = request.Request(url,headers=head)
    # req.add_header("User-Agent",head["User-Agent"]) //作用相同
    resp = request.urlopen(req)
    html = resp.read().decode("utf-8")
    print(html)


    #使用 IP 代理