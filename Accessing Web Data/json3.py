#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
#  The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract 
# the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#the url we wl use is  http://py4e-data.dr-chuck.net/comments_840974.json
#answer is 2483
import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum=0
l=list()

while True:
    url = input('Enter location: ')
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    js = json.loads(data)
    l=js["comments"]
    sum=0
    for x in l:
        c=int(x["count"])
        sum=sum+c
    print(sum)

