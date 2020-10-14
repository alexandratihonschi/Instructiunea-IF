a=int(input("prima latura="))
b=int(input("a doua latura="))
c=int(input("a treia latura="))
if ((a<32000)and(b<32000)and(c<32000)):
    if((a<b+c)and(b<a+c)and(c<a+b)):
        print('da')
    else:
        print(nu)