import re

def matchcheck():
    count=0
    search=input("enter word which you want to search")
    pattern =re.compile(search)
    filename=input("enter filename")
    f=open(filename,"r")
    c=f.read()
    matcher=pattern.finditer(c)

    for match in matcher:
        count = count+1
    print("number of occurance ", count)
    if count>0:
        f=open("hello.txt","w")
        s=input("enter which word you want to replace") 
        f.write(c.replace(search,s))
        f.close()
        print("replacement has been done")
    else:
        print("No match found")

matchcheck()




