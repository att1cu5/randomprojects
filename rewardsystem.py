a=1
fg=0
def ran(v,kl,lo,h):
    
    return (((kl**2))%v)-h*lo
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

   
    ko=nmartrix(k,l,p,o,pl,0,plk,ok)+ran(3,2,1,4)
    kop=nmartrix(k,l,p,o,pl,1,plkl,okl)-ran(7,9,2,8)
    return ko,kop
def hu(h,k,l,o):
    import numpy as np
    #import random
    #h=random.choice([0,1])
    #j(-4,3,0.6,0.2,3,4,3,-4,6,-2,7)[1]
    g=j(-2,3,-0.2,2,3,5,3,-2,2,5,-3)[1]*np.array([[-h,k],[l,-o]])
    return j(-4,3,2,-0.2,3,4,3,-2,2,3,-3)[0]*g
def r(xv,kl):
    return float(xv**kl)
def k(v,s):
    return float(v*s)
def ld(k):
    jkl=0
    for i in range(0,k):
        hk=float(i)
        ui=float((hk+2)/3)
        ki=float((hk-2)/-3)
        kl=float((hk+5)/4)
        okd=float((hk-5)/-4)
        print(ui)
        
ld(3)
