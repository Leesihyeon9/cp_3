num = int(input("몇단까지 출력할까요:"))
for x in range(1,num+1):
    print("-"*3,"[",x,"단]","-"*3)
    for y in range(1,20):
        print(x,"*",y,"=",x*y )