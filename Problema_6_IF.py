n1=int(input("prima nota este-"))
n2=int(input("a doua nota este-"))
n3=int(input("a treia nota este-"))
if(n3>=8):
    print(n1,n2,n3)
if(n3<8):
    if(n1>n2):
        print(n1)
    if(n2>n1):
        print(n2)