import math
ra=complex(0,0)
for i in range(0,5):
    f=complex(math.e,0)

    t=f**complex(0,1)*i
    ra=+t*complex(0,-1)
print(ra)
