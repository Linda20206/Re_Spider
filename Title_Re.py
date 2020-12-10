
# coding: utf-8

# In[1]:


import requests
import time
import re


# In[2]:


def Get_Html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36 Edg/86.0.622.63'}
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        print('请求失败')


# In[3]:


def Get_Info(html):
    pat = '<li><a href="/book/85467/\d+.html">(.*?)</a></li>'
    chapter = re.findall(pat,html,re.S)
    print(chapter)


# In[4]:


urls = ['https://www.jx.la/book/85467/index_{}.html'.format(i) for i in range(1,5)]
for url in urls:
    html = Get_Html(url)
    Get_Info(html)
    time.sleep(1)

