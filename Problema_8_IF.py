n1=int(input("primul numar-"))
n2=int(input("al doilea numar-"))
if((n1//2==0)and(n2//2==0)):
    if(n1>n2):
        print(n1)
    else:
        print(n2)
if((n1//2==0)and(n2//2!=0)):
    print(n1)
if((n1//2!=0)and(n2//2==0)):
    print(n2) 
if((n1//2!=0)and(n2//2!=0)):
    print("nu exista numere pare")   