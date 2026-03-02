d=[{0,0,0},{0,0,0},{0,0,0},{0,0,0}]
while(0==0):
    i=int(input("pick a number that is not 1 or 2 or -1 or -2 or 0:"))
    if(i!=1 and i!=2 and i!=-1 and i!=-2 and i!=0):
        break
    elif(i==1 or i==2 or i==-1 or i==-2 or i==0):
        i=complex(i,i)
        break
d[2]={0,-i,-i+1}
d[1]={-i-1,-i,0}
d[0]={-i,0,-i-2}
d[3]={-i+2,0,-i}
g=list(d[1])
z=complex(g[1],g[2])
g=list(d[0])
h=complex(g[1],g[2])
g=list(d[2])
y=complex(g[1],g[2])
g=list(d[3])
o=complex(g[1],g[2])
print(z)
print(h)
print(y)
print(o)
u=(z*o*h*y)
ea=u.real*-u.real+(u.imag*-u.imag)
print(ea)
d[2]={0,i,i+1}
d[1]={i-1,0,i}
d[0]={i,0,i-2}
d[3]={i+2,0,i}
g=list(d[1])
z=complex(g[1],g[2])
g=list(d[0])
h=complex(g[1],g[2])
g=list(d[2])
y=complex(g[1],g[2])
g=list(d[3])
o=complex(g[1],g[2])
print(z)
print(h)
print(y)
print(o)
u=(z*o*h*y)
e=u.real*-u.real+(u.imag*-u.imag)
print(e)
print("difference of values: " , e-ea)
