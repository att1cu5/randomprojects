Qavg=0
Ravg=0
RatioAvg=0
RatioAvga=0
uio=[3,4,9,7,34,8]
k=[complex(3,8),complex(9,4),complex(12,5),complex(9,5),complex(6,1),complex(5,7)]
deltau=1
Q=0
BM=0
Bexpected=3
OP=1
previousuio=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
LO=[0,0,0,0,0,0,0,0,0,0,0]
OL=[0,0,0,0,0,0,0,0,0,0,0]
def has_duplicates(seq):
    return len(seq) != len(set(seq)) #

# Example:
R=0
r=0
iop=0
fgo=0
times=6
for i in range(0,times):
    iop+=((uio[i])-(uio[i-1]))**2
    LO[i]=iop
    
    fgo+=(deltau*k[i])**2
    OL[i]=fgo
    #print(OP,"=","R(",iop,")+Q(",(fgo.real+fgo.imag)*(fgo.real-fgo.imag),")")
    count=0
    if(has_duplicates(uio)!=True):
        count=1
        BM+=uio[i]*((count)/(times+1))
    elif(has_duplicates(uio)==True):
        previousuio[i]=uio[i]
        count=uio.count(uio[i])
        BM+=uio[i]*((count)/(times+1))
    uiol=fgo.real+fgo.imag
    uoil=fgo.real-fgo.imag
#print(OP,"=","R(",iop,")+Q(",uoil*uiol,")")
    JK=uoil*uiol
    JL=iop
    R=BM/Bexpected
    #print("numbers:",JL," and ",JK)
    #print("R=",R)
    #print(OP,"=",R*iop,"+Q(",uoil*uiol,")")
    #print("find Q")
    #print("Q=",(OP-(R*iop))/(uoil*uiol))
    Q=(OP-(R*iop))/(uoil*uiol)
    J=R*JL+JK*Q
    #print("J=",J)
    Ravg+=R
    Qavg+=Q
    RatioAvg+=(R/Q)
    RatioAvga+=(Q/R)
print("average R: ",Ravg/(times+1))
print("average Q: ",Qavg/(times+1))
print("average RatioAvg: ",RatioAvg/(times+1))
print("average RatioAvga: ",RatioAvga/(times+1))
