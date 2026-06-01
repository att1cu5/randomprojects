a=1
fg=0
def ran(v,kl,lo,h):
    
    return (kl**2)-(h+lo)%v
def f(x):
    return x+1
def g(a):
    import math
    output=0
    k=0
    for i in range(1,10):
        
        output+=(f(i)+a-f(i)*a)
        try: 
            k+=(output-a)/a
        except ZeroDivisionError:
            k=math.inf
    return k,output
def ranged(ih):
    hj=g(ih)
    ol=g(-ih)
    jio=ol[0]/ol[1]
    jok=hj[0]/hj[1]
    return jio,jok
def weight(xd,fg,fgo):
    if(xd<0):
        for i in range(xd,-1):
            klo=ranged(i/(10**i))[0]

            fg+=(klo[0]+klo[1])
        for i in range(xd,-1):
            klo=ranged(i/(10**i))[1]

            fgo+=(klo[0]+klo[1])
    #print(fg)
    else:
        for i in range(1,xd):
            klo=ranged(i/(10**i))

            fg+=(klo[0]+klo[1])
        for i in range(1,xd):
            klo=ranged(i/(10**i))

            fgo+=(klo[0]+klo[1])
    return fg,fgo
def matrix(x,y,kl,lp):
    import numpy as np
    #import random
    h=0
    mat=np.array([[0,0],[0,0]])
    #h=random.choice([-1,1])
    for i in range(kl,lp):
        if(i%2==0):
            h=1
        else:
            h=-1
    if(h==1):
            mat=np.array([[x,-y],[-y,x]])
    if(h==-1):
            mat=np.array([[-x,y],[y,-x]])
    return mat
def nmartrix(l,o,d,k,lo,kl,op,dpi):
    
    return matrix(l,o,op,dpi)*weight(d,k,lo)[kl]

def j(v,vf,k,l,p,o,pl,ok,plk,plkl,okl): 
    ko=ran(3,2,-1,4)
    kop=ran(5,6,-1,8)
    for i in range(v,vf):
        ko+=nmartrix(k,l,p,o,pl,0,plk,ok)
        kop+=nmartrix(k,l,p,o,pl,1,plkl,okl)
    return ko,kop
def hu():
    #import random
    #h=random.choice([0,1])
    #j(-4,3,0.6,0.2,3,4,3,-4,6,-2,7)[1]
    return j(-4,3,2,-0.2,3,4,3,-2,2,3,-3)[0]*j(-4,3,-0.2,2,3,4,3,-2,2,5,-3)[1]
print(hu())
