# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
#http://py4e-data.dr-chuck.net/comments_840971.html here is the html page
#  with fromm where we will count number of comments from html fiel

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
l=[]
tags = soup('tr')   #collect all the <tr> tags
for tag in tags:
    tag=str(tag)    #tags must be converted into string to use regular expression library re
    #print(tag)
    x=re.findall('<span.*>([0-9]+)',tag)  # sees the line containing <span followed by any character any number of times followed by >
                                            #and collect numbers occuring one or more number of times only
    #print(x)
    l.extend(x)
sum=0
for y in l:
    y=int(y)
    sum=sum+y
print(sum)
