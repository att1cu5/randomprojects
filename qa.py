import math 
uio=[0,0,0,0,0,0,0]
uiop=[0,0,0,0,0,0,0]
x=complex(0,0)
o=[0,0,0,0,0,0,0]
p=[0,0,0,0,0,0,0]
u=[0,0,0,0,0,0,0]
O=[0,2,4,2,3,5,6]
OI=[0,5,4,6,3,5,7]
OU=[2,3,4,6,3,8,9]
OOP=[2,3,7,8,4,5,3]
OPL=[0,0,0,0,0,0,0]
PT=[O,OI,OU,OOP,OU,OI,O]
for i in range(0,7):
    x=(complex(complex(0,-1)*math.e**complex(0,1)*i))
    o[i]=x
    u[i]=x.real
    p[i]=x.imag
for uiol in range(0,7):
    for ui in range(0,7):
        uio[ui]=(PT[ui][uiol]*u[ui])
        uiop[ui]=(PT[ui][uiol]*p[ui])
