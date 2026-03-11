import numpy as np
time=0.1
Aavg=0
Bavg=0
Cavg=0
Davg=0
errorA=0
errorB=0
errorC=0

while(time<=1):
            AMatrix=[[4,10,0],[1,9,0],[0,4,10]]
            BMatrix=[[0,0,0],[0,0,0],[0,0,0]]
            np.NMatrix=[[0,0,0],[0,0,0],[0,0,0]]
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
            for i in range(0,2):
                np.NMatrix[i][0]=AMatrix[i][0]*Xm(time)+BMatrix[i][0]*r(time)
            for i in range(0,2):
                np.NMatrix[i][1]=AMatrix[i][1]*Xm(time)+BMatrix[i][1]*r(time)
            for i in range(0,2):
                np.NMatrix[i][2]=AMatrix[i][2]*Xm(time)+BMatrix[i][2]*r(time)
            
            
            
            # Define a 3x3 matrix
            A = np.NMatrix
            
            # Calculate eigenvalues
            eigenvalues = np.linalg.eigvals(A)
            
            # Convert eigenvalues to polynomial coefficients (p(x) = x^3 + c2*x^2 + c1*x + c0)
            coeffs = np.poly(eigenvalues)
            
            #print("Polynomial Coefficients:", coeffs)
            coeffsA=coeffs[0]
            coeffsB=coeffs[1]
            coeffsC=coeffs[2]
            coeffsD=coeffs[3]
            #print(str(coeffsD)+"x^3+"+str(coeffsC)+"x^2"+str(coeffsB)+"x+"+str(coeffsA))
            # To evaluate the polynomial function at a value (e.g., x=2):
            #print("P(",time,") =", np.polyval(coeffs, time))
            time=time+0.1
            Aavg=Aavg+coeffsA
            Bavg=Bavg+coeffsB
            Cavg=Cavg+coeffsC
            Davg=Davg+coeffsD
print("average A: ",Aavg/((time-0.9)/0.1))
print("average B: ",Bavg/((time-0.9)/0.1))
print("average C: ",Cavg/((time-0.9)/0.1))
print("average D: ",Davg/((time-0.9)/0.1))
Aavg=Aavg/((time-0.1)/0.1)
Bavg=Bavg/((time-0.1)/0.1)
Cavg=Cavg/((time-0.1)/0.1)
Davg=Davg/((time-0.1)/0.1)
realA=coeffsA
realB=coeffsB
realC=coeffsC
realD=coeffsD
errorA=abs(Aavg-realA)/realA
errorB=abs(Bavg-realB)/realB
errorC=abs(Cavg-realC)/realC
print("errorA percentage: ",errorA*100,"%")
print("errorB percentage: ",errorB*100,"%")
print("errorC percentage: ",errorC*100,"%")
time=0.1


while(time<=5):
            AMatrix=[[4,10,0],[1,9,0],[0,4,10]]
            BMatrix=[[0,0,0],[0,0,0],[0,0,0]]
            np.NMatrix=[[0,0,0],[0,0,0],[0,0,0]]
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
            for i in range(0,2):
                np.NMatrix[i][0]=AMatrix[i][0]*Xm(time)+BMatrix[i][0]*r(time)
            for i in range(0,2):
                np.NMatrix[i][1]=AMatrix[i][1]*Xm(time)+BMatrix[i][1]*r(time)
            for i in range(0,2):
                np.NMatrix[i][2]=AMatrix[i][2]*Xm(time)+BMatrix[i][2]*r(time)
            
            
            
            # Define a 3x3 matrix
            A = np.NMatrix
            
            # Calculate eigenvalues
            eigenvalues = np.linalg.eigvals(A)
            
            # Convert eigenvalues to polynomial coefficients (p(x) = x^3 + c2*x^2 + c1*x + c0)
            coeffs = np.poly(eigenvalues)
            
            #print("Polynomial Coefficients:", coeffs)
            coeffsA=coeffs[0]
            coeffsB=coeffs[1]
            coeffsC=coeffs[2]
            coeffsD=coeffs[3]
            #print(str(coeffsD)+"x^3+"+str(coeffsC)+"x^2"+str(coeffsB)+"x+"+str(coeffsA))
            # To evaluate the polynomial function at a value (e.g., x=2):
            #print("P(",time,") =", np.polyval(coeffs, time))
            time=time+0.1
            Aavg=Aavg+coeffsA
            Bavg=Bavg+coeffsB
            Cavg=Cavg+coeffsC
            Davg=Davg+coeffsD
fa=time+1
fb=time**2+time
print("time functionA: ",fa)
print("time functionB: ",fb)
Aavg=Aavg/((time-0.1)/0.1)
Bavg=Bavg/((time-0.1)/0.1)
Cavg=Cavg/((time-0.1)/0.1)
Davg=Davg/((time-0.1)/0.1)
print("average A: ",Aavg)
print("average B: ",Bavg)
print("average C: ",Cavg)
print("average D: ",Davg)
LOWa=realA-(Aavg*errorA)
HIGHa=realA+(Aavg*errorA)
LOWb=realB-(Bavg*errorB)
HIGHb=realB+(Bavg*errorB)
LOWc=realC-(Cavg*errorC)
HIGHc=realC+(Cavg*errorC)
print("predicted real value of coefficient C low value:",realC-(Cavg*errorC))
print("predicted real value of coefficient C high value:",realC+(Cavg*errorC))
preC=(HIGHc+LOWc)/2
print("predicted value: ",preC)

print("real value: ",coeffsC)
print("predicted real value of coefficient A low value:",realA-(Aavg*errorA))
print("predicted real value of coefficient A high value:",realA+(Aavg*errorA))
print("predicted value: ",(HIGHa+LOWa)/2)
preA=(HIGHa+LOWa)/2
print("real value: ",coeffsA)
print("predicted real value of coefficient B low value:",realB-(Bavg*errorB))
print("predicted real value of coefficient B high value:",realB+(Bavg*errorB))
preB=(HIGHb+LOWb)/2
print("predicted value: ",preB)
print("real value: ",coeffsB)
