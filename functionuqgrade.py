def f(x):
    import math
    return math.pow(x,(1/x))
def fa(x):
    import math
    return math.pow(x,(1/(x+1)))
lo=0
ol=0
for i in range(1,100):
    print("first input:",f(i),end=" ")
    print("second input:",fa(i))
    lo+=f(i)
    ol+=fa(i)
print("first avg: ",lo/100,"second avg:",ol/100)
print("difference: ",(lo/100)-(ol/100))
