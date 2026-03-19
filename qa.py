import math 
x=complex(0,0)
o=[0,0,0,0,0,0,0]
for i in range(0,7):
    x=(complex(complex(0,-1)*math.e**complex(0,1)*i))
    o[i]=x
print(o)
