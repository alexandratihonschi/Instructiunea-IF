zc=int(input("ziua curenta-"))
lc=int(input("luna curenta-"))
ac=int(input("anul curent-"))
zn=int(input("ziua nasterii-"))
ln=int(input("luna nasterii-"))
an=int(input("anul nasterii-"))
if((lc<12)and(zc<31)and(an<ac)):
    if(lc>ln):
        print(ac-an)
    else:
        print((ac-an)+1)
