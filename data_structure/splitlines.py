
while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
        break
    except:
        print('Filename is wrong')
    continue


l = []
#print(type(l))
lines=fh.readlines()
for line in lines:
    x = line.split()
    for y in x:
        if y not in l:
            l.append(y)



l.sort()
print(l)
