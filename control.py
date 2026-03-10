uio=[3,4,56,7,34,9,20,23]
k=[complex(8,3),complex(4,6),complex(3,6),complex(3,5),complex(0,1)]
deltau=1
Q=0
OP=5
LO=[0,0,0,0,0,0,0,0,0,0,0]
OL=[0,0,0,0,0,0,0,0,0,0,0]
R=0
r=0
iop=0
fgo=0
for i in range(0,5):
    iop+=((uio[i]*k[i])-(uio[i-1]*k[i]))**2
    LO[i]=iop
    fgo+=(deltau*k[i])**2
    OL[i]=fgo
print((iop)+((-fgo.real-fgo.imag)*(fgo.real+fgo.imag)))
J=(iop)+(fgo)
