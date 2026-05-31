
output=0
inputs=0
a=1
fg=0
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
def weight(xd):
    fg=0
    for i in range(xd,-1):
        klo=ranged(i/(10**i))

        fg+=(klo[0]+klo[1])
    return fg
