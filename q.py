import math
ra=complex(0,0)
for i in range(0,5):
    f=complex(math.e,0)

    t=f**complex(0,1)*i
    ra=+(t*complex(0,-1))
print(ra)
print("magnitude: ",math.sqrt(math.pow(ra.real,2)+math.pow(ra.imag,2)))
mag=math.sqrt(math.pow(ra.real,2)+math.pow(ra.imag,2))
ang=math.atan(abs(ra.imag)/abs(ra.real))
print("Angle: ",ang)
