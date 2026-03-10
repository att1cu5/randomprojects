def check(x,y,Rx,L,Qy):
    L=Rx*x+y*Qy
    return 0
uio=[3,4,56,7,34,8]
k=[complex(8,3),complex(4,6),complex(3,6),complex(3,5),complex(6,1),complex(5,7)]
deltau=1
Q=0
BM=0
Bexpected=3
OP=5
LO=[0,0,0,0,0,0,0,0,0,0,0]
OL=[0,0,0,0,0,0,0,0,0,0,0]
R=0
r=0
iop=0
fgo=0
times=5
for i in range(0,times):
    iop+=((uio[i])-(uio[i-1]))**2
    LO[i]=iop
    fgo+=(deltau*k[i])**2
    OL[i]=fgo
        
    BM+=uio[i]*((1)/(times+1))

uiol=fgo.real+fgo.imag
uoil=fgo.real-fgo.imag
print(5,"=","R(",iop,")+Q(",uoil*uiol,")")
JK=uoil*uiol
JL=iop
R=BM/Bexpected
print("numbers:",JL," and ",JK)
print("R=",R)
print(5,"=",R*iop,"+Q(",uoil*uiol,")")
print("find Q")
print("Q=",(5-(R*iop))/(uoil*uiol))
Q=(5-(R*iop))/(uoil*uiol)
J=R*JL+JK*Q
print("J=",J)
