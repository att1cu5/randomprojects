import math
e=-1
i=1
while(e!=0):
     
    
    cg=i
    
    def f(x):
        return math.pi*x
    #print("output:")
    #print(int(f(i)))
    g=int(f(i))
    #print("ratio:")
    #print(g/i)
    #print("error rate:")
    k=100
    e=((g/i)-math.pi)*k
    
    for h in range(0,int(abs(e))):
        print("|",end="")
    print("|")    
    
    i=i+1
