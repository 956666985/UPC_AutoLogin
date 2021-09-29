'''
UPC自动WEB登录脚本      BY JZZP  
更新记录
V1.3
增加wifi连接功能(已删除)
V1.2
加入连接成功验证，每1s连接一次，直到连接成功
增加执行完批处理命令后CMD窗口可选择不关闭功能
V1.1
修正url为wlan.upc.edu.cn，导致的有几率不能连接问题，
'''
cmd_choose=1    #可以选择连接成功后是否关闭cmd窗口      默认不关闭      0为不关闭

#coding=UTF-8
#!/usr/bin/python #可作为脚本写入开机自启动
import time
import schedule
import sys
import requests
#import bs4
#from bs4 import BeautifulSoup    #导入BeautifulSoup
#from requests.models import Response  #导入requests库
#from threading import Timer

url="http://wlan.upc.edu.cn/eportal/InterFace.do?method=login"    #把将要POST的地址赋值给url,该地址就是我们发送请求给服务器的地址。**********这个地址需要修改*******************

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cookie': 'EPORTAL_COOKIE_DOMAIN=true; EPORTAL_COOKIE_USERNAME=1916030128; EPORTAL_COOKIE_SERVER=ctcc; EPORTAL_COOKIE_SAVEPASSWORD=true; EPORTAL_COOKIE_SERVER_NAME=%E4%B8%AD%E5%9B%BD%E7%94%B5%E4%BF%A1; EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_COOKIE_PASSWORD=8b877d46a342b78fff4d31dbc958b81636eae6227ac78bd983ad1dd30d1cb5358c7d25b26b10d6a3c59f445f6a3a4e0408417cc93949e9a99cb56197efe2ea49a4dcd69fbb214a3f951f5dba771099816faef0cd9306a7f36a534b61167828db1b2050caa0d9c12a142f4b547af0036c9ccb4fa26c956db3762e97f234ad562b; EPORTAL_AUTO_LAND=; EPORTAL_USER_GROUP=%E6%9C%AC%E7%A7%91%E7%94%9F%E7%BB%84; JSESSIONID=AFDD688067EAC7C1D4B21FD11796A40E',
        'Host': 'wlan.upc.edu.cn',
        'Content-Length': '619',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Connection': 'keep-alive',
        'Origin': 'http://wlan.upc.edu.cn',
        'Referer': 'http://wlan.upc.edu.cn/eportal/index.jsp?wlanuserip=172.24.181.144&wlanacname=&nasip=172.22.242.22&wlanparameter=98-2c-bc-8a-da-22&url=http://www.msftconnecttest.com/redirect&uerlocation=ethtrunk/62:3071.0',    
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31'}
        #请求的头文件，一般不需要修改
formdata={
    "method":"login",
    "queryString":"wlanuserip%3D172.24.181.144%26wlanacname%3D%26nasip%3D172.22.242.22%26wlanparameter%3D98-2c-bc-8a-da-22%26url%3Dhttp%3A%2F%2Fwww.msftconnecttest.com%2Fredirect%26uerlocation%3Dethtrunk%2F62%3A3071.0",
    "passwordEncrypt" :"false",
    "service":"ctcc",
    "userId":"xxxxxx",      #账号 需要修改       
    "password":"xxxxxxx.",     #密码 需要修改
    "operatorPwd":"",
    "operatorUserId":"",
    "validcode":"",
#将要post的表单数据，也就是把这里的数据发送给服务器******************发送的数据需要修改****************
        }
#response=requests.post(url,data=formdata,headers=headers)    #发送POST请求 

#定时1s重复连接，直到连接成功，前提是开机后WIFI连接到UPC
def task(): 
        response=requests.post(url,data=formdata,headers=headers)    #发送POST请求 
        r=response.text.encode('ISO-8859-1')    #回应编码
        rr=r.decode('utf8')                     #回应解码
        print(rr) 
        if(rr.find("已经")!=-1):
                print("连接成功")
                if cmd_choose==1:
                        temps=input("\n")
                sys.exit() 
schedule.every(1).seconds.do(task)        
while True:
     schedule.run_pending()
     time.sleep(1)


#soup = bs4.BeautifulSoup(response.text,'lxml')
#soup.encode('ISO-8859-1')
#find1="1916"
#print(find1 in soup)
#print(rr)    #打印服务器的响应信息    解码
#print(aaa.decode('gbk'))


