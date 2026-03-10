uio=[3,4,56,7,34,9,20,23]
k=[complex(8,3),complex(4,6),complex(3,6),complex(3,5),complex(0,1)]
deltau=1
Q=1
OP=5
LO=[0,0,0,0,0,0,0,0,0,0,0]
R=2
r=0
iop=0
for i in range(0,5):
    iop+=(uio[i]*k[i]-uio[i-1]*k[i])**2
    LO[i]=iop
fgo=abs(deltau*k)**2
print(Q*(iop)+R*(fgo))
J=Q*(iop)+R*(fgo)
