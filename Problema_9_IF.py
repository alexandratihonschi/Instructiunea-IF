a1a=int(input("albe mici="))
a1r=int(input("rosii mici="))
a1v=int(input("verzi mici="))
b1a=int(input("albe mari="))
b1r=int(input("rosii mari="))
b1v=int(input("verzi mari="))
print("bile in total=",a1a+b1a+a1r+b1r+a1v+b1v)
if a1a+a1r+a1v>b1a+b1r+b1v:
    print("mari:",b1a+b1r+b1v,"bile")
else:
    print("mici:",a1a+b1a+a1v,"bile")
if (a1a+b1a>a1r+b1r) and (a1a+b1a>a1v+b1v):
    print("albe:",a1a+b1a,"bile")
elif (a1r+b1r>a1a+b1a) and (a1r+b1r>a1v+b1v):
    print("rosii:",a1r+b1r,"bile")
else:
    print("verzi:",a1v+b1v,"bile")