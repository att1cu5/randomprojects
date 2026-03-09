uio=[3,4,56,7,34,9,20,23]
k=complex(8,3)
deltau=1
Q=1
R=2
r=0
iop=0
for i in range(0,5):
    iop+=(uio[i]-uio[i-1])**2
fgo=abs(deltau*k)**2
print(Q*(iop)+R*(fgo))
J=Q*(iop)+R*(fgo)
