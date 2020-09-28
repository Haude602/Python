
#Find the link at position 18 (the first name is 1).
#  Follow that link. Repeat this process 7 times. 
# The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: R
#The answer is rosina



#http://py4e-data.dr-chuck.net/known_by_Aara.html is the link to get started
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count=int(input("Enter count"))
position =int(input("Enter position"))


for i in range(count):
    c=0
    url = input('Enter - ')
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
    tags = soup('a')   #collect all the <a> tag
    for tag in tags:
        c=c+1
        if c==position:
            
            print(tag)
