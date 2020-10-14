e1=int(input("nr crt="))
e2=int(input("nr crt="))
e3=int(input("nr crt="))
p1=int(input("punctaj="))
p2=int(input("punctaj="))
p3=int(input("punctaj="))
if ((p1>p2)and(p1>p3)):
    print(e1)
if ((p2>p1)and(p2>p3)):
    print(e2)
if ((p3>p1)and(p3>p2)):
    print(e3)