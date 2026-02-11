d=0
f=0
g=0
h=1
k=0.001
p=0
print("minimum x: ")
xmin=float(input())
print("maximum x: ")
xmax=float(input())
delta=0
average=0
print("a value:")
a=float(input())
print("b value:")
b=float(input())
print("c value:")
c=float(input())
##
def f(a,i,b,c): 
    return float (a*i*i+b*i+c)
i=xmin
while(i<xmax):
    d=f(a,i-k,b,c)
    g=f(a,i+k,b,c)
    delta=(delta+((d*d)-(g*g)))
    i=i+k
    time=time+k
print("rate of change:")
print(delta/time)




