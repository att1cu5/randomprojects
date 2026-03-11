time=0.1
AMatrix=[[4,10,0],[1,9,0],[0,4,10]]
BMatrix=[[0,0,0],[0,0,0],[0,0,0]]
def Xm(t):
    return t+1
def r(t):
    return (t*t)+t
for i in range(0,2):
    BMatrix[i][0]=(Xm(time)-(AMatrix[i][0]*Xm(time)))/r(time)
for i in range(0,2):
    BMatrix[i][1]=(Xm(time)-(AMatrix[i][1]*Xm(time)))/r(time)    
for i in range(0,2):
    BMatrix[i][2]=(Xm(time)-(AMatrix[i][2]*Xm(time)))/r(time)    
print(BMatrix)
