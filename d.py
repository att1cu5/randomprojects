#bra vectors
f=complex(2,5)
ok=complex(2,5)
ik=complex(2,3)
ki=complex(2,3)
#ket vecotrs
fa=complex(2,3)
oka=complex(2,6)
ika=complex(2,5)
kia=complex(2,4)
iko=[0,0,0,0]
def u(r,g,h,j,k,o,l,p):
    
    return r*k,g*l,h*o,j*p
print(u(f,ok,ik,ki,fa,oka,ika,kia))
iko=u(f,ok,ik,ki,fa,oka,ika,kia)
u=(iko[0]*iko[1]*iko[2]*iko[3])
hk=u.real
io=u.imag
print((hk+io)*(hk-io))
