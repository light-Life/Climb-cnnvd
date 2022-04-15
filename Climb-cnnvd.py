# !/usr/bin/python
# -*- coding:utf-8 -*-
# time: 2022.4.15

#有时间需要改的：1。cve单独写一个文件 2.cve和链接再单独写一个文件
import requests,re,time
data = {
    'qcvCnnvdid' :'cnnvd-2022'
}
for x in range(1,440):
    time.sleep(1)
    url = 'http://www.cnnvd.org.cn/web/vulnerability/queryLds.tag?pageno=' + str(x)
    response = requests.post(str(url),data=data)
    for i in range(10):
        a = 'id="vulner_'+ str(i) +'">(.*?)" src="/web'
        re1 = re.findall(a,response.text,re.S)
        if ("高危" or "低危" or "中危" or "超危") in re1[0]:
            re_url = re.findall('<p><a href="(.*?)" target="_blank"',re1[0],re.S)
            print('http://www.cnnvd.org.cn'+re_url[0])
