#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

while True:
    fname=input('Enter filename')
    try:
        fh=open(fname)
        break
    except:
        print('Enter valid name of file')
    continue
lines=fh.readlines()
count=dict()
for line in lines:
    line=line.rstrip()
    if line.startswith('From '):
        words=line.split()
        for word in words:
            if word==words[5]:
                word=word.split(":")
                hour=word[0]
                count[hour]=count.get(hour,0)+1
l=list()
for k,v in count.items():
    newl=(k,v)
    l.append(newl)
    l=sorted(l)
for x,y in l:
    print(x,y)









