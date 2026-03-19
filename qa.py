import math 
uio=[0,0,0,0,0,0,0,0,0,0,0]
uiop=[0,0,0,0,0,0,0,0,0,0,0]
x=complex(0,0)
o=[0,0,0,0,0,0,0,0,0,0,0]
p=[0,0,0,0,0,0,0,0,0,0,0]
u=[0,0,0,0,0,0,0,0,0,0,0]
O=[0,2,4,2,3,5,6,4,7,5,4]
OI=[0,5,4,6,3,5,7,4,9,2,3]
OU=[2,3,4,6,3,8,9,3,8,7,8]
OOP=[2,3,7,8,4,5,3,7,4,5,9]
OPL=[0,0,0,0,0,0,0,0,0,0,0]
PT=[O,OI,OU,OOP,OU,OI,O,OI,OOP,OU]
for i in range(0,10):
    x=(complex(complex(0,-1)*math.e**complex(0,1)*i))
    o[i]=x
    u[i]=x.real
    p[i]=x.imag
for uiol in range(0,10):
    for ui in range(0,10):
        uio[ui]=(PT[ui][uiol]*u[ui])
       
        uiop[ui]=(PT[ui][uiol]*p[ui])
        
        


for oler in range(0,10):
    print(round(uiop[oler])*round(uio[oler]))
