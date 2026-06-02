def gradecompare(l):
    g=67
    h=89
    Totalerror=0
    for i in range(0,l):
        #g=float(input("What grade did you get? "))
        #h=float(input("What grade got predicted? "))
        diff=g-h
        Totalerror+=diff
        print("error:")
        print(Totalerror/l)
    return Totalerror/l
gradecompare(2)
