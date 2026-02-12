delta=0
f=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

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
for i in range(-11,12):
    
    z=((j(i,i+1,i+2)+h(i,i+1,i+2)))
    deltaA=deltaA-z
    delta=delta+z
    print("(",z,",",i,")")
    print("rate of change:",((delta*deltaA)/(deltaA-delta))) 
    f[i+11]=(delta*deltaA)/(deltaA-delta)
    
    
for u in range(0,23):
    print(f[u])
