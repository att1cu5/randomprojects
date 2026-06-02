a=1
fg=0

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","."]
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
    return xv**kl

def ld(k,kl,lk,kix,ifg):
    jkl=0
    for i in range(0,k):
        hk=float(i-k)
        ui=float((hk+kix)/-kl)
        ki=float((hk-kix)/kl)
        kl=float((hk+ifg)/lk)
        okd=float((hk-ifg)/-lk)
        return hu(r(ui,okd),r(ki,ui),r(ui,kl),r(okd,ui)) 
def reward(i,klo,mol,lopo,oop):
    import numpy as np        
    if(i!=0):
        #print(np.linalg.det(ld(abs(i),oop,lopo,klo,mol)))
        return np.linalg.det(ld(abs(i),oop,lopo,klo,mol))
    else:
        #print(0)
        return 0
def direction(x):
    nstate=0
    cstate=0
    rstate=0
    if(x.imag>0):
        cstate=1
    elif(x.imag<0):
        cstate=2
    else:
        cstate=0
    if(x.real>0):
        nstate=1
    elif(x.real<0):
        nstate=2
    else:
        nstate=0
    if(x.real>x.imag):
        rstate=1
    elif(x.real<x.imag):
        rstate=2
    else:
        rstate=0
    #print(cstate,nstate,rstate)
    return cstate,nstate,rstate
def io(hj,ko,pl,ol,kp,i):    
    return direction(reward(i+hj,i-ko,i-pl,i-ol,i+kp))
def wordmaker(xlo):
    word=""
    wordsa=["new","nor","..."]
    for o in range(xlo,100):
        try:
            if(o!=-1 and o!=-2 and o!=-3 and o!=0 and o!=-4):
                for i in range(1,4):
                    gh=io(100,8,3,-10,8,i+o)
                    x=2
                    val=0
                    for i in range(1,4):
                        val+=gh[i-1]*(3**(x))
                        x-=1
                    word+=alphabet[val]
                if(len(word)==3):
                    break
                print()    
        except ZeroDivisionError: 
            
            
            print(end="")
        
    if(word==wordsa[0]):
        return 1,word
    if(word==wordsa[1]):
        return 3,word
    if(word==wordsa[2]):
        return 2, word 
    else:
        return 0,"naw"
def wordchecks():
    import random
    for i in range(-100,100):   
        h=random.randint(-100,70)
        #print(h,wordmaker(h))
    return wordmaker(h)

if(wordchecks()[0]!=0):
    print(wordchecks()[1],end=" ")
    
