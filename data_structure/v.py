largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n=float(num)
    except:
        print('Enter numeric value')
        continue
    if largest==None and smallest==None:
        largest=n
        smallest=n
    elif n>largest:
         largest=n
    elif n<smallest:
        smallest=n
print("smallest=",smallest)
print("largest",largest)



