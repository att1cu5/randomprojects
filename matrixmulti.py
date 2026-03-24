import math
p=[[2,1],[3,4]]
pa=p[0][0]
pb=p[1][1]
a=pa*pb
b=-pa
c=-pb
A=b*c/a
u=0
i=0
B=p[1][0]*p[0][1]
print(str(int(a))+str(int(b+c))+"x+"+str(int(A))+"x^2"+"="+str(int(u)))
u=-a
print(str(int(b+c))+"x+"+str(int(A))+"x^2"+"="+str(int(u)))
print(str(int((b+c)/-1))+"x+"+str(int(A/-1))+"x^2"+"="+str(int(u/-1)))
i=float(math.sqrt(abs(b+c)))
print("("+str(i)+"-x)"+"("+str(i)+"+x)"+"="+str(int(u/-1)))
