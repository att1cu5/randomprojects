def gradecompare(l,grade):
    g=30
    h=50
    rate=h/g
    Totalerror=0
    for i in range(0,l):
        #g=float(input("What grade did you get? "))
        #h=float(input("What grade got predicted? "))
        diff=g-h
        Totalerror+=diff
    #print("error:")
    #print(Totalerror/l)
    futuregradeA=grade-Totalerror
    futuregradeB=grade*rate
    if(futuregradeA>100):
        futuregradeA=100
    if(futuregradeB>100):
        futuregradeB=100
    print("predicted grade",round((futuregradeA+futuregradeB)/2,2),"%")
    return Totalerror/l
gradecompare(1,8)
