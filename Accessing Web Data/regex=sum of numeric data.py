#to find sum of all data(numbers) present in text file actual.txt

import re
fname=input('enter filename')
while True:
    try:
        fh=open(fname)
        break
    except:
        print('Enter valid filename')
        continue
l=list()
lines=fh.readlines()
for line in lines:
    line=line.rstrip()
    x=re.findall('[0-9]+',line)
    l.extend(x)
sum=0
for y in l:
    y=int(y)
    sum=sum+y
print(sum)
