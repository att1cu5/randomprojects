delta=0
f=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

deltaA=0
def j(i,o,l):
    d=i+o+l
    g=i*(o+l)
    h=o*(i+l)
    y=l*(i+o)
    return d+g+h+y
def h(i,o,l):
    d=i-o-l
    g=i/(o-l)
    h=o/(i-l)
    y=l/(i-o)
    return d-g-h-y
for i in range(-15,12):
    
    z=((j(i,i+1,i+5)+h(i,i+4,i+1)))
    deltaA=deltaA-z
    delta=delta+z
    print("(",z,",",i,")")
    print("rate of change:",((delta*deltaA)/(deltaA-delta))) 
    f[i+15]=(delta*deltaA)/(deltaA-delta)
    
    
for u in range(0,27):
    for k in range(0,round(f[u]/100)):
        print(" ",end="")
    print("|",end="")
    for k in range(0,20):
        print("|",end="")
    print()
