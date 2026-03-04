
f=9
t=-3
op=5
def g(y,x,l):
    for i in range(0,l):

        y=y+complex(1,i)
        
    for s in range(0,l):

        x=x-complex(-1,s)
    return(x*y)
def opi(lo,ol,piu,lp):
    return lo*lp*lp+ol*lp+piu
p=g(f,t,op)
print(p)
o=p.real+p.imag+1
f=p.real+p.imag-(op*2)-1
io=p.real+p.imag-1
oi=p.real+p.imag+(op/2)+1
print("f=",int(o),"t=",int(f), "ta=",int(io), "fa=",int(oi))
print("f(x)="+str(int(o))+"x^2+"+str(int(io-f))+"x+"+str(int(oi)))
k=int(o)*2
print("derivative of f(x) when y=0 f(x)="+str(int(k))+"x"+str(int(f-io)))
print("derivative of f(x) when y=0 x="+str((-(io-f)/(2*k))))
xi=(-(io-f)/(2*k))
print("find y while x="+str((-(io-f)/(2*k))))
print("y="+str(float(opi(f,(io-f),oi,xi))))
