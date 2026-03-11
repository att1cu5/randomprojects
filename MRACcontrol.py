import numpy as np
time=0.1
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

print("Polynomial Coefficients:", coeffs)
# To evaluate the polynomial function at a value (e.g., x=2):
print("P(",time,") =", np.polyval(coeffs, time))
