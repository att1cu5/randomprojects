def getgrades(g,h):
    def gradecompare(l,grade):
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
        
        #print("predicted grade",,"%")
        return round((futuregradeA+futuregradeB)/2,2)
    class Node:
        def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
            self.feature = feature
            self.threshold = threshold
            self.left = left
            self.right = right
            self.value = value
    
    def mean(values):
        return sum(values) / len(values)
    
    def build_tree(X, y):
        if len(set(y)) == 1:
            return Node(value=y[0])
            
        best_feature = 0
        # FIXED: Wrapped in square brackets to make it a list instead of a generator
        best_threshold = mean([row[0] for row in X])
        
        left_X, left_y = [], []
        right_X, right_y = [], []
        
        for i in range(len(X)):
            if X[i][best_feature] <= best_threshold:
                left_X.append(X[i])
                left_y.append(y[i])
            else:
                right_X.append(X[i])
                right_y.append(y[i])
                
        # Safety check: prevents infinite recursion if data stops splitting
        if not left_y or not right_y:
            return Node(value=mean(y))
            
        return Node(
            feature=best_feature,
            threshold=best_threshold,
            left=build_tree(left_X, left_y),
            right=build_tree(right_X, right_y)
        )
    
    def predict(tree, x):
        if tree.value is not None:
            return tree.value
        if x[tree.feature] <= tree.threshold:
            return predict(tree.left, x)
        else:
            return predict(tree.right, x)
    
    # Example data
    X = [[g]]
    y = [h]
    
    tree = build_tree(X, y)
    treeout=predict(tree, [82]) # Expected Output: 89.0
    
    grades=gradecompare(1,2)
    
    print("perecnt expected: ",(abs(treeout+grades))/2,"%")
    return abs(treeout+grades)/2
getgrades(30,50)
