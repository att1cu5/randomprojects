import random
import math
import numpy as np

          


def calculate_steady_state(matrix):
    
    """
    Calculates the long-term equilibrium (steady-state) vector 
    for a given Markov chain transition matrix.
    """
    # Convert input to a NumPy array
    P = np.array(matrix, dtype=float)
    
    # Get the number of states (matrix dimensions)
    n = P.shape[0]
    
    # Transpose P and subtract the Identity matrix: (P^T - I)
    # This sets up the equation: (P^T - I) * pi = 0
    Q = P.T - np.eye(n)
    
    # Replace the last row with 1s to enforce the sum-to-1 constraint
    Q[-1] = np.ones(n)
    
    # Create target vector: all zeros except the last element which is 1
    b = np.zeros(n)
    b[-1] = 1.0
    
    # Solve the system of linear equations
    try:
        steady_state = np.linalg.solve(Q, b)
        return steady_state
    except np.linalg.LinAlgError:
        raise ValueError("The matrix does not have a unique steady state.")
def m(LR,IVA,IVB,WVA,WVB,WVC,WVD,HB):

                import math
                import re
                import numpy as np
                input_vector = [IVA, IVB]
                weights_1 = [WVA, WVB]
                weights_2 = [WVC, WVD]
              
                # Computing the dot product of input_vector and weights_1
                first_indexes_mult = input_vector[0] * weights_1[0]
                second_indexes_mult = input_vector[1] * weights_1[1]
                dot_product_1 = first_indexes_mult + second_indexes_mult
              
                #print(f"The dot product is: {dot_product_1}")
              
                dot_product_1 = np.dot(input_vector, weights_1)
                #print(f"The dot product is: {dot_product_1}")
                dot_product_2 = np.dot(input_vector, weights_2)
                #print(f"The dot product is: {dot_product_2}")
                def sigmoid(x):
                      return 1 / (1 + np.exp(-x))
              
                def make_prediction(input_vector, weights, bias):
                      layer_1 = np.dot(input_vector, weights) + bias
                      layer_2 = sigmoid(layer_1)
                      return layer_2
                bias=1
                prediction = make_prediction(input_vector, weights_1, bias)
                #print(f"The prediction result is: {prediction}")
                input_vector = np.array([2, 1.5])
                prediction = make_prediction(input_vector, weights_1, bias)
                #print(f"The prediction result is: {prediction}")
                target = 0
              
                mse = np.square(prediction - target)
              
                #print(f"Prediction: {prediction}; Error: {mse}")
                derivative = 2 * (prediction - target)
                #print(f"The derivative is {derivative}")
                weights_1 = weights_1 - derivative
                prediction = make_prediction(input_vector, weights_1, bias)
                error = (prediction - target) ** 2
                #print(f"Prediction: {prediction}; Error: {error}")
              
                def sigmoid_deriv(x):
                      return sigmoid(x) * (1-sigmoid(x))
              
                derror_dprediction = 2 * (prediction - target)
                layer_1 = np.dot(input_vector, weights_1) + bias
                dprediction_dlayer1 = sigmoid_deriv(layer_1)
                dlayer1_dbias = 1
              
                derror_dbias = (derror_dprediction * dprediction_dlayer1 * dlayer1_dbias)
                class NeuralNetwork:
                    def __init__(self, learning_rate):
                        self.weights = np.array([np.random.randn(), np.random.randn()])
                        self.bias = np.random.randn()
                        self.learning_rate = learning_rate
              
                    def _sigmoid(self, x):
                        return 1 / (1 + np.exp(-x))
              
                    def _sigmoid_deriv(self, x):
                        return self._sigmoid(x) * (1 - self._sigmoid(x))
              
                    def predict(self, input_vector):
                        layer_1 = np.dot(input_vector, self.weights) + self.bias
                        layer_2 = self._sigmoid(layer_1)
                        prediction = layer_2
                        return prediction
              
                    def _compute_gradients(self, input_vector, target):
                        layer_1 = np.dot(input_vector, self.weights) + self.bias
                        layer_2 = self._sigmoid(layer_1)
                        prediction = layer_2
              
                        derror_dprediction = 2 * (prediction - target)
                        dprediction_dlayer1 = self._sigmoid_deriv(layer_1)
                        dlayer1_dbias = 1
                        dlayer1_dweights = (0 * self.weights) + (1 * input_vector)
              
                        derror_dbias = (
                            derror_dprediction * dprediction_dlayer1 * dlayer1_dbias
                        )
                        derror_dweights = (
                            derror_dprediction * dprediction_dlayer1 * dlayer1_dweights
                        )
              
                        return derror_dbias, derror_dweights
              
                    def _update_parameters(self, derror_dbias, derror_dweights):
                        self.bias = self.bias - (derror_dbias * self.learning_rate)
                        self.weights = self.weights - (
                            derror_dweights * self.learning_rate
                        )
              
                    # ...
                class Neural_Network:
                    def train( self,input_vectors, targets, iterations):
                        cumulative_errors = []
                        for current_iteration in range(iterations):
                            # Pick a data instance at random
                            random_data_index = np.random.randint(len(input_vectors))
              
                            input_vector = input_vectors[random_data_index]
                            target = targets[random_data_index]
              
                            # Compute the gradients and update the weights
                            derror_dbias, derror_dweights = self._compute_gradients(
                                input_vector, target
                            )
              
                            self._update_parameters(derror_dbias, derror_dweights)
              
                            # Measure the cumulative error for all the instances
                            if current_iteration % 100 == 0:
                                cumulative_error = 0
                                # Loop through all the instances to measure the error
                                for data_instance_index in range(len(input_vectors)):
                                    data_point = input_vectors[data_instance_index]
                                    target = targets[data_instance_index]
              
                                    prediction = self.predict(data_point)
                                    error = np.square(prediction - target)
              
                                    cumulative_error = cumulative_error + error
                                cumulative_errors.append(cumulative_error)
              
                        return cumulative_errors
              
              
              
              
                
                learningRate=LR
                hexB=HB
                hexA=0
                u=0
              
                    #print(newB)
                neural_networkA = str(NeuralNetwork(learningRate))
                newA = re.sub(r'[^a-zA-Z0-9 ]', '',neural_networkA  )
                hexA=newA.replace("mainmlocalsNeuralNetwork object at ","")
              
                neural_networkB =str(NeuralNetwork(learningRate))
                newB = re.sub(r'[^a-zA-Z0-9 ]', '',neural_networkB  )
                      
                hexB=newB.replace("mainmlocalsNeuralNetwork object at ","")
                neural_networkB =str(NeuralNetwork(learningRate))
                u = re.sub(r'[^a-zA-Z0-9 ]', '',neural_networkB  )
                      
                hexC=u.replace("mainmlocalsNeuralNetwork object at ","")    
              
                hexA=int(hexA,16)
                hexB=int(hexB,16)
                hexC=hexA-hexB
              
                MAtrixA=[[hexA,hexB/2],[hexB/2,hexC]]
                VectorAc=complex(MAtrixA[0][0],MAtrixA[1][0])
                VectorAB=complex(MAtrixA[1][0],MAtrixA[1][1])
                vectrd=math.sqrt(abs(pow(VectorAc,2))+abs(pow(VectorAB,2)))
              
                VectorAcd=complex(MAtrixA[0][0],MAtrixA[1][0])/vectrd
                VectorABd=complex(MAtrixA[1][0],MAtrixA[1][1])/vectrd
                vectrr=math.sqrt(abs(pow(VectorAcd,2))+abs(pow(VectorABd,2)))
                ProbA=pow(abs(VectorAcd),2)/(pow(abs(VectorAcd),2)+pow(abs(VectorABd),2))
                ProbB=pow(abs(VectorABd),2)/(pow(abs(VectorABd),2)+pow(abs(VectorAcd),2))
              
                #print("state one: ",ProbA*100,"%","state two: ",ProbB*100,"%")
                return [ProbA*100,ProbB*100]
def MAIN():
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    digits = [char for char in local_ip if char.isdigit()]
    for i in range(0,len(digits)):
        digits[i]=int(digits[i])
    live=0
    for i in range(0,len(digits)):
        if(digits[i]>0):
            live*=digits[i]
    while(0==0):
        askonobserver=input("do you want to see the results as a observer: ")
        if(askonobserver=="yes"):
           live=live
           break
        if(askonobserver=="no"):
           live=1
           break
    listofdensity=[0,0,0,0,0,0,0,0,0,0]
    probalityamplitude=[0,0,0,0,0,0,0,0,0,0]
    Xpos=[0,0,0,0,0,0,0,0,0,0]
    Ypos=[0,0,0,0,0,0,0,0,0,0]
    angle=[0,0,0,0,0,0,0,0,0,0]
    magnitude=[0,0,0,0,0,0,0,0,0,0]
    prob=[0,0,0,0,0,0,0,0,0,0]
    per=[0,0,0,0,0,0,0,0,0,0]
    giol=10
    def jk(g,kl,a,b):
        return (g**4*(180*kl))/((b-a)**5)
    for idf in range(0,giol):
        #LENGTH=float(input("What is the length of the box: "))
        LENGTH=32
        Biasofdown=0   
        Biasofup=0
        LOP=0
        cv=0
        cvA=0
        cvB=0
        Biasofnothing=0
        Cspeed=3.00*10**8
        #Vfreq=float(input("What is the frequency of the photon: "))
        Vfreq=32
        Lambdas=Cspeed/Vfreq
        
        
        def simpsons_quad(func, a, b, n):
            import numpy as np
            """
            Approximates the integral of func from a to b using Composite Simpson's Rule.
            Returns: (result, estimated_error)
            """
            if n % 2 != 0:
                n += 1  # n must be even for Simpson's Rule
            
            x = np.linspace(a, b, n + 1)
            y = func(x)
            dx = (b - a) / n
            
            # Simpson's Rule Formula: (dx/3) * [f(x0) + 4*sum(f_odd) + 2*sum(f_even) + f(xn)]
            result = (dx / 3) * (y[0] + y[-1] + 
                                 4 * np.sum(y[1:-1:2]) + 
                                 2 * np.sum(y[2:-2:2]))
            
            # Simple error estimation comparing n and n/2 steps
            result_half = (dx * 2 / 3) * (y[0] + y[-1] + 
                                          4 * np.sum(y[2:-2:4]) + 
                                          2 * np.sum(y[4:-4:4])) if n >= 4 else 0
            error = abs(result - result_half)
            
            return result, error
            
            
            # Example: PDF function (e.g., Normal Distribution)
            
        def pdf(x):
                import numpy as np
                return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
            
          
        from decimal import Decimal, getcontext
        
        def get_tiny_square_string(valueA,valueB,op):
            # 1. Set precision high enough to capture the result
            getcontext().prec = 50
            
            # 2. Convert input to Decimal and calculate
            # (Works if value is already a string or a Decimal object)
            if(op==1):
                result = Decimal(str(valueA)) * Decimal(str(valueB))
                
            # 3. Format as a string in scientific notation
                return f"{result:E}"
            if(op==2):
                result = Decimal(str(valueA)) + Decimal(str(valueB)) 
            
            # 3. Format as a string in scientific notation
                return f"{result:E}"
            if(op==3):
                result = Decimal(str(valueA)) - Decimal(str(valueB)) 
            
            # 3. Format as a string in scientific notation
                return f"{result:E}"
            if(op==4):
                result = Decimal(str(valueA)) / Decimal(str(valueB))
            
            # 3. Format as a string in scientific notation
                return f"{result:E}"  
            if(op==5):
                
                result = pow(Decimal(str(valueA)),Decimal(str(valueB)))
                return f"{result:E}"
            if(op==6):
                
                result = abs(Decimal(str(valueA)))
                
            # 3. Format as a string in scientific notation
                return f"{result:E}"  
        def randomG(a,c,limit,seed):
            return (a*seed+c)%limit
        def fgh(uoijd,lijk,urei):
            return uoijd
        DOWNLIST=[0]
        UPLIST=[0]
        NOLIST=[0]
        for i in range(0,giol):  
            spinDOWN=0
            spinUP=0
            nothing=0
            DATA=[0]
        
            for i in range(0,1):
                DATA[i]=DATA.insert(i,0)
                DOWNLIST[i]=DOWNLIST.insert(i,0)
                UPLIST[i]=UPLIST.insert(i,0)
                NOLIST[i]=NOLIST.insert(i,0)
            for ikol in range(0,2):
            
            
            
            
                import math
                import time
                #import random
                start = time.perf_counter()
                Astart = time.process_time()
                avgchangeinpercentone=0
                avgchangeinpercenttwo=0
                rateon=0
                P=0
                rateoff=0
                ratei=0
                weightA=0
                weightB=0
                avgpositivedisplacement=0
                avgnegativedisplacement=0
                avg=[0]
                klo=[0]
                K=[0]
                for i in range(1,33):
                    klo[i]=klo.insert(i,0)
                for i in range(1,33):
                    K[i]=K.insert(i,0)
                
                
                
                
                for i in range(1,35):
                    avg[i]=avg.insert(i,0)
                def O(re,ty,ui,ok,O):
                    return re*(O**ty)+(ui*O)+ok
                
                
                
                
    
                accuracy=0
                accuracya=0
                accuracyb=0
                for k in range(1,35):
                  
                    errorrateB=0
                    errorrateA=0
                    for i in range(1,35):
                        x=m(0.2,0.4,0.23,0.45,0.34,0.67,9,7)
                        avgchangeinpercentone=x[0]*live
                        avgchangeinpercenttwo=x[1]*live
                        x=m(0.2,0.4,0.23,0.45,0.34,0.67,9,7)
                        avgchangeinpercentone=x[0]-avgchangeinpercentone*live
                        avgchangeinpercenttwo=x[1]-avgchangeinpercenttwo*live
                    errorrateB=(avgchangeinpercentone/k)
                    errorrateA=(avgchangeinpercenttwo/k)
                
                
                
                
                    if((errorrateB)>0):
                        accuracyb+=1
                        avgpositivedisplacement+=errorrateB
                      
                    if((errorrateA)>0):
                        accuracyb+=1
                        avgpositivedisplacement+=errorrateA
                    if((errorrateB)<0):
                        accuracya+=1
                        avgnegativedisplacement+=errorrateB
                    if((errorrateA)<0):
                        accuracya+=1
                        avgnegativedisplacement+=errorrateA
                    if((errorrateB)==0 or (errorrateA)==0):
                        accuracy+=1
                    rateon=round(abs(((accuracyb/k))*100))
                    rateoff=round(abs(((accuracya/k))*100))
                    ratei=100-(rateon+rateoff)
                  
                    xi=avgpositivedisplacement/k
                    xf=avgnegativedisplacement/k
                    kl=[abs(round((rateoff/100)*k)),abs(round((ratei/100)*k)),abs(round((rateon/100)*k))]
                    #print(kl)
                  
                    def hj(lo,po,ikl,low,high):
                        
                        import random
                        
                        ui=randomG(randomG(random.uniform(-1,1),random.uniform(-1,1),random.uniform(-pow(2,32),pow(2,32)),random.uniform(-1,1)),randomG(random.uniform(-1,1),random.uniform(-1,1),random.uniform(-pow(2,32),pow(2,32)),random.uniform(-1,1)),(lo+po+ikl)*100,randomG(random.uniform(-1,1),random.uniform(-1,1),random.uniform(-pow(2,32),pow(2,32)),random.uniform(-1,1)))
                        
                      
                      
                        if(ui<=lo*100):
                            x=low
                            #print(x)
                          
                        if(ui<=(lo+po)*100 and ui>(lo*100) ):
                            x=0
                            #print(x)
                
                
                
                
                        if(ui<=(lo+po+ikl)*100 and ui>(lo+po)*100 ):
                            x=high
                          
                            #print(x)
                
                
                
                
                        return x
                    avg[k]=hj(kl[0],kl[1],kl[2],xi,xf)
                del avg[0]
                #print(avg)
                def deriveA(ERio,k,l):
                    import numpy as np
                    dx=k
                    dy=l
                    ans=np.gradient(ERio, dx, dy)
                
                
                
                
                  
                    return ans
                def derive(E,s):
                    import numpy as np
                    dx=s
                    dy=np.gradient(E, dx)
                
                
                
                
                  
                    return dy
                h=derive(avg,1)
                #print(h)
                h=derive(h,1)
                #print(h)
                def createM(arr,col,row):
                    import numpy as np
                  
                    matrix = np.array(arr).reshape(col, row)
                    return matrix
                def eval(JK):
                    import numpy as np
                    j,k=np.linalg.eig(JK)
                    return j,k
                
                
                
                
                Am=createM(h,17,2)@createM(h,2,17)
                Bm=createM(h,2,17)@createM(h,17,2)
                def kronm(AG,KG):
                    import numpy as np
                    res=np.kron(AG,KG)
                    return res
                def find_D(XCA):
                    import numpy as np
                    return np.linalg.det(XCA)
                endMa=kronm(Am,Bm)@kronm(Bm,Am)
                endMb=kronm(Bm,Am)@kronm(Am,Bm)
                hadmard=endMa*endMb
                def hadmard(NM,LM):
                    import numpy as np
                    NOP=NM/np.abs(LM+1)
                    return NOP
                def state(lo):
                    import numpy as np
                    ol=np.zeros((1,34),dtype=int)
                    ol[0, ::2] = 1e-50 # Every second element starting at index 0
                    ol[0, 1::2] = 1
                    return ol
                  
                def phase(ML,mk):
                    import numpy as np
                    phi=np.pi/mk
                    return np.exp(1j*phi)*ML
                def transpose(AKL):
                    import numpy as np
                    return AKL.conj().T
                phaseshiftA=phase(endMa,3)
                phaseshiftB=phase(endMb,3)
                endhadmardA=hadmard(endMa,endMa)
                endhadmardB=hadmard(endMb,endMb)
                StatesA=state(klo)*phaseshiftA*endhadmardA*(1/math.sqrt(2))
                po=float((6.2607015*math.pow(10,-34))/(2*math.pi))*-1j
                po=po.imag
                xcv=po/float((6.2607015*math.pow(10,-34))/(2*math.pi))
                
                
                
                
                
                
                
                
                StatesB=state(klo)*phaseshiftB*endhadmardB*(1/math.sqrt(2))
                Fb=StatesB*find_D(Bm)
                Fa=StatesA*find_D(Am)
                uio=Fb+Fa
                
                
                
                
                SUMA=0
                #print(eval(uio))
                endF=transpose(eval(uio)[0])*state(klo)
                #print(endF)
                for i in range(0,len(endF[0])):
                    SUMA+=complex(endF[-1,i].real,endF[-1,i].imag)
                for i in range(0,len(endF[0])):
                    SUMA+=complex(endF[0,i].real,endF[0,i].imag)
                
                
                
                
                end = time.perf_counter()
                endA= time.process_time()
                t=end - start
                tA=endA-Astart
                hiuo=(6.2607015*math.pow(10,-34))/(2*math.pi)
                Uans=SUMA*math.e**(complex(0,-1)*(t/hiuo))*endF
                UansB=SUMA*math.e**(complex(0,-1)*(tA/hiuo))*endF
                #print("time: ",t,"seconds", tA, "seconds")
                #print("Output A:")
                #print(Uans)
                #print("Output B:")
                #print(UansB)
                CombinedM=createM(UansB,2,17)**createM(Uans,2,17)
                CombinedMA=createM(UansB,17,2)**createM(Uans,17,2)
                CombinedME=createM(UansB,1,34)**createM(Uans,1,34)
                CombinedMAE=createM(UansB,34,1)**createM(Uans,34,1)
                
                
                
                
                #print("Combined Matrix A:")
                #print(CombinedM)
                #print("Combined Matrix B:")
                #print(CombinedMA)
                #print("Combined Matrix C:")
                #print(CombinedME)
                #print("Combined Matrix D:")
                #print(CombinedMAE)
                #print("fully combined Matrix A and B one:")
                #print(CombinedM@CombinedMA)
                MAA=CombinedM@CombinedMA
                #print("fully combined Matrix A and B two:")
                #print(CombinedMA@CombinedM)
                MAB=CombinedMA@CombinedM
                #print("combined A and B:")
                #print(kronm(MAA,MAB)-33)
                CombinedA=kronm(MAA,MAB)-33
                #print("fully combined Matrix C and D one:")
                #print(CombinedME@CombinedMAE)
                MAC=CombinedME@CombinedMAE
                #print("fully combined Matrix D and C two:")
                #print(CombinedMAE@CombinedME)
                MAD=CombinedMAE@CombinedME
                #print("combined C and D:")
                #print(kronm(MAC,MAD)-33)
                CombinedB=kronm(MAC,MAD)-33
                #print("all matrices combined A: ")
                #print(CombinedA*CombinedB)
                FinalM=CombinedA*CombinedB
                FinalMA=CombinedB*CombinedA
                #print("all matrices combined B: ")
                #print(CombinedB*CombinedA)
                FinalMB=FinalM*FinalMA
                #print("all matrices combined: ")
                #print(FinalMB)
                for i in range(-16,17):
                    if(O(1,3,1,2,i)!=0 and O(1,3,1,2,i)<16 and O(1,3,1,2,i)>-16):
                        K[i]=O(1,3,1,2,i)+17
                        klo[i]=i+17
                    else:
                        K[i]=0
                        klo[i]=0
                
                
                
                
                G=0
                for i in range(1,33):
                  G+=FinalMB[K[i]][klo[i]]
                #print("Values: ",G-G.real)
                
                if(G.imag>0):
                    spinUP+=1
                    G=complex(G.real*G.imag,G.imag)
                    LOP=complex(G.real,G.imag)
                    #print(LOP)
                    UPLIST[ikol]=fgh(LOP,1,-1)
                    NOLIST[ikol]=0
                    DOWNLIST[ikol]=0
                    DATA[ikol]=1
                if(G.imag<0):
                    spinDOWN+=1
                    G=complex(G.real*G.imag,G.imag)
                    LOP=complex(G.real,G.imag)
                    #print(LOP)
                    DOWNLIST[ikol]=fgh(LOP,-1,1)
                    NOLIST[ikol]=0
                    UPLIST[ikol]=0
                    DATA[ikol]=-1
                if(G.imag==0):
                    nothing+=1
                    LOP=complex(0,0)
                    NOLIST[ikol]=fgh(LOP,1,1)
                    DOWNLIST[ikol]=0
                    UPLIST[ikol]=0
                    #print(LOP)
                    DATA[ikol]=0
           
            #print("amount of times spinUP: ", spinUP)
            #print("amount of times spinDOWN: ", spinDOWN)
            #print("amount of times Nothing: ", nothing)
            #print(DATA)
            if(sum(DATA)>0):
        
                 #print("data is trending positive")
                 #print("probality of positive spin:",round((spinUP/(spinUP+spinDOWN+nothing)*100)),"%")
                 #print("probality of negative spin:",round((spinDOWN/(spinUP+spinDOWN+nothing)*100)),"%")
                 #print("probality of no spin:",round((nothing/(spinUP+spinDOWN+nothing)*100)),"%")
                 cvB+=1
            if(sum(DATA)<0):
                 
                 #print("data is trending negative")
                 #print("probality of positive spin:",round((spinUP/(spinUP+spinDOWN+nothing)*100)),"%")
                 #print("probality of negative spin:",round((spinDOWN/(spinUP+spinDOWN+nothing)*100)),"%")
                 #print("probality of no spin:",round((nothing/(spinUP+spinDOWN+nothing)*100)),"%")
                 cvA+=1
            if(sum(DATA)==0):
                 #print(0)
                 #print("data is not biased")
                 #print("probality of positive spin:",round((spinUP/(spinUP+spinDOWN+nothing)*100)),"%")
                 #print("probality of negative spin:",round((spinDOWN/(spinUP+spinDOWN+nothing)*100)),"%")
                 #print("probality of no spin:",round((nothing/(spinUP+spinDOWN+nothing)*100)),"%")
                 cv+=1
            Biasofdown+=round((spinDOWN/(spinUP+spinDOWN+nothing)*100))
            Biasofup+=round((spinUP/(spinUP+spinDOWN+nothing)*100))
            Biasofnothing+=round((nothing/(spinUP+spinDOWN+nothing)*100))
             
        #print("Percent of the spin being negative:",round((Biasofdown/(Biasofnothing+Biasofup+Biasofdown))*100),"%")   
        
        #print("Percent of the spin being positive:",round((Biasofup/(Biasofnothing+Biasofup+Biasofdown))*100),"%") 
        #print("Percent of the spin being nothing:",round((Biasofnothing/(Biasofnothing+Biasofup+Biasofdown))*100),"%")     
        #print("when spin is 1 :",UPLIST)
        #print("when spin is -1 :",DOWNLIST)
        #print("when spin is 0 :",NOLIST)
        ketA=0
        ketB=0
        for i in range(0,len(UPLIST)):
            ketA+=UPLIST[i]
        for i in range(0,len(DOWNLIST)):
            ketB+=DOWNLIST[i]
        braA=ketA.conjugate()
        braB=ketB.conjugate()  
        
        KETstate=[ketA,ketB]
        BRAstate=[ketA.conjugate(),ketB.conjugate()]
        
        
        #BRAans=pow(abs(BRAstate[0]),2)+pow(abs(BRAstate[1]),2)
        #KETans=pow(abs(KETstate[0]),2)+pow(abs(KETstate[1]),2)
        #BRAKETA=BRAans*KETans
        #print(BRAKET)
        Xcd=str(KETstate[0].imag) #a
        Xdd=str(BRAstate[1].imag) #d
        Xc=str(KETstate[1].real) #b
        Xd=str(BRAstate[0].real) #c
        BC=get_tiny_square_string(Xc,Xd,1) #3
        AC=get_tiny_square_string(Xcd,Xd,1) #1
        AD=get_tiny_square_string(Xcd,Xdd,1) #2
        BD=get_tiny_square_string(Xc,Xdd,1) #4 
        outputAd=get_tiny_square_string(AC,BD,3)
        outputAdd=get_tiny_square_string(AD,BC,2)
        
        z=outputAd+""+outputAdd+"j"
        
        #print("probality amplitude: ")
        probalityamplitude[idf]=z
       
        #print(z)
        output = get_tiny_square_string(Xc,Xcd,1)
        #print("a squared:",output)
        
        outputs = get_tiny_square_string(Xd,Xdd,1)
        #print("b squared:",outputs)
        outputsa = get_tiny_square_string(output,outputs,2)
        #print("c squared length of the vector:",outputsa)
        OUput=get_tiny_square_string(outputAd,outputAd,1)
        OIput=get_tiny_square_string(outputAdd,outputAdd,1)
        SUMK=get_tiny_square_string(OUput,OIput,2)
        probailitydensity=get_tiny_square_string(SUMK,0.5,5)
        #print("probaility density: ")
        #print(probailitydensity)
        realval=get_tiny_square_string(outputAd,outputAd,1)
        imagval=get_tiny_square_string(outputAdd,outputAdd,1)
        prob[idf]=get_tiny_square_string(realval,imagval,2)
        listofdensity[idf]=probailitydensity
        maxA=math.sqrt(2)/math.sqrt(LENGTH)
        #print(maxA)
        Ktimes=(2*math.pi)/Lambdas
        import random
        #N=randomG(random.uniform(-1,1),random.uniform(-1,1),random.uniform(-pow(2,32),pow(2,32)),random.uniform(-1,1))
        N=idf
        #print(Ktimes)
        X=(((2*N)+1)*math.pi)/(2*Ktimes)
        Y=(((2*Ktimes*X)/math.pi)-1)/2
        Xl=(((2*Y)+1)*math.pi)/(2*Ktimes)
        Yl=(((2*Ktimes*Xl)/math.pi)-1)/2
        
        angle[idf]=(math.atan2(Yl,Xl))*(180/math.pi)
        magnitude[idf]=math.sqrt(math.pow(Yl,2)+math.pow(Xl,2))
        Xpos[idf]=Xl
        Ypos[idf]=Yl
        #print("Psi x:",X)
    ukl=get_tiny_square_string(prob[0],prob[1],2)
    klo=get_tiny_square_string(prob[2],prob[3],2)
    ople=get_tiny_square_string(prob[4],prob[5],2)
    ilehj=get_tiny_square_string(prob[6],prob[7],2)
    ilko=get_tiny_square_string(prob[8],prob[9],2)
    lopej=get_tiny_square_string(ukl,klo,2)
    oper=get_tiny_square_string(ople,ilehj,2)
    
    ilkope=get_tiny_square_string(lopej,oper,2)
    finalsumofprob=get_tiny_square_string(ilkope,ilko,2)
    wavefunction=get_tiny_square_string(finalsumofprob,2,5)
    C=get_tiny_square_string(get_tiny_square_string(finalsumofprob,2,5),0.5,5)
    #print("list of probaility densities:")
    #print(listofdensity)
    #print("list of psi of y:")
    #print(Ypos)
    #print("list of psi of x:")
    #print(Xpos)
    #print("list of probability amplitudes:")
    #print(probalityamplitude)
    #print("list of angles:")
    #print(angle)
    #print("list of magnitudes:")
    #print(magnitude)
    #print("list of probability:")
    #print(prob)
    
    #print("total probability")
    
    
    #print(wavefunction)
    
    #print("total norm: ")
    #print(C)
    #print("normalizing factor: ")
    N=get_tiny_square_string(get_tiny_square_string(1,C,4),get_tiny_square_string(1,C,4),1)
    for i in range(0,len(prob)):
        prob[i]=get_tiny_square_string(N,prob[i],1)
    #print(N)
    #print(normalize(probalityamplitude))
    #print("prob list normalized: ")
    #print(prob)
    ukl=get_tiny_square_string(prob[0],prob[1],2)
    klo=get_tiny_square_string(prob[2],prob[3],2)
    ople=get_tiny_square_string(prob[4],prob[5],2)
    ilehj=get_tiny_square_string(prob[6],prob[7],2)
    ilko=get_tiny_square_string(prob[8],prob[9],2)
    lopej=get_tiny_square_string(ukl,klo,2)
    oper=get_tiny_square_string(ople,ilehj,2)
    
    ilkope=get_tiny_square_string(lopej,oper,2)
    finalsumofprobA=get_tiny_square_string(ilkope,ilko,2)
    #print("total sum of normalized :")
    #print(finalsumofprobA)
    normalizedproduct=get_tiny_square_string(wavefunction,N,1)
    for i in range(0,len(prob)):
        #print("Probability of "+str(i+1)+" item is equal to percent: ")
        jlplp=get_tiny_square_string(prob[i],finalsumofprobA,4)
        
        per[i]=get_tiny_square_string(jlplp,100,1)
        #print(per[i],"%")
    #print("normalize probability: ")
    
    #print(normalizedproduct)
    
    txt=random.choice(prob)
    DATAencrypt=''.join(format(ord(char), '08b') for char in txt)
    
    
    
    #print("key")
    #print(DATAencrypt)
    key=int(DATAencrypt,2)
    
    txtA=random.choice(prob)
    DATAencryptA=''.join(format(ord(char), '08b') for char in txtA)
    #print("key")
    #print(DATAencrypt)
    #print(DATAencrypt)
    keyA=int(DATAencryptA,2)
    
    lstate=159508576913954845180612982391718185118169205577160977874080339596104103895262091379231784642186123052583829943829114233517318692221751 
    Astate=139633821288291447314342521502729566484678743216628016127416602976725176179183876897984161943236839463687991727983992051777723228894007
    bhjl=[[0,0,0],[0,0,0],[0,0,0]]
    Xposition=0
    Yposition=0
    if(key==lstate):
        Xposition=1
    if(key>lstate):
        Xposition=2
    if(key<lstate):
        Xposition=0
    if(keyA==Astate):
        Yposition=1
    if(keyA>Astate):
        Yposition=2
    if(keyA<Astate):
        Yposition=0
    bhjl[Xposition][Yposition]=1
    bhjl[Yposition][Xposition]=1
    
    #print("keyA: ",keyA)
    #print("key: ",key)
    
    return bhjl,angle,magnitude
from decimal import Decimal, getcontext
        
def get_tiny_square_string(valueA,valueB,op):
            # 1. Set precision high enough to capture the result
            import math
            getcontext().prec = 50
            
            # 2. Convert input to Decimal and calculate
            # (Works if value is already a string or a Decimal object)
            if(op==1):
                result = Decimal(str(valueA)) * Decimal(str(valueB))
                
            # 3. Format as a string in scientific notation
                return f"{result:E}"
            if(op==2):
                result = Decimal(str(valueA)) + Decimal(str(valueB)) 
            
            # 3. Format as a string in scientific notation
                return f"{result:E}"
            if(op==3):
                result = Decimal(str(valueA)) - Decimal(str(valueB)) 
            
            # 3. Format as a string in scientific notation
                return f"{result:E}"
            if(op==4):
                result = Decimal(str(valueA)) / Decimal(str(valueB))
            
            # 3. Format as a string in scientific notation
                return f"{result:E}"  
            if(op==5):
                
                result = pow(Decimal(str(valueA)),Decimal(str(valueB)))
                return f"{result:E}"
            if(op==6):
                
                result = abs(Decimal(str(valueA)))
                
            # 3. Format as a string in scientific notation
                return f"{result:E}"  
            if(op==7):
                
                result = math.sin(Decimal(str(valueA)))
                
            # 3. Format as a string in scientific notation
                return f"{result:E}"  
            if(op==8):
                
                result = math.cos(Decimal(str(valueA)))
                
            # 3. Format as a string in scientific notation
                return f"{result:E}"  
loaded=1

for i in range(0,loaded):
    
    mjk,klopio,oplut=MAIN()
    #print(mjk[0])
    #print(mjk[1])
    #print(mjk[2])
    
    flattened_list = [bit for row in mjk for bit in row]
    
    #print(flattened_list)
    bit_string = "".join(map(str, flattened_list))
    #print("data in bin: ",bit_string)
    #print("data in dec: ",int(bit_string,2))
    #print("state : ",round((int(bit_string,2)/256)*100))
    probalityweight=(int(bit_string,2)/256)/100
    MagnitudeA=klopio[i]
    angleA=oplut[i]
    magprob=get_tiny_square_string(MagnitudeA,probalityweight,1)
    X=get_tiny_square_string(magprob,get_tiny_square_string(angleA,0,8),1)
    Y=get_tiny_square_string(magprob,get_tiny_square_string(angleA,0,7),1)
    #print("X: ",X)
    binary_strX = ' '.join(format(ord(c), '08b') for c in X)
    int_valuesX = [int(binary, 2) for binary in binary_strX.split()]
    #print("Y: ",Y)
    binary_strY = ' '.join(format(ord(c), '08b') for c in Y)
    int_valuesY = [int(binary, 2) for binary in binary_strY.split()]
    current_state = '0'
    print(f"Start: {current_state}")
    matrixoutA=[]
    matrixoutB=[]
    matrixoutC=[]
    matrix_out_list=[]
    #print("Y",binary_strY,"X",binary_strX)
    #print(len(int_valuesY))
    states=[]
    if(len(int_valuesY)<len(int_valuesX)):
        for ik in range(0,len(int_valuesY)):
            matrixoutB.append(int_valuesY[ik]/sum(int_valuesY))
        for ik in range(0,len(int_valuesY)):
            matrixoutA.append(int_valuesX[ik]/sum(int_valuesX))
        for ik in range(0,len(int_valuesY)):
            matrixoutC.append(math.sqrt(math.pow(int_valuesX[ik],2)+math.pow(int_valuesY[ik],2)))
        for i in range(0,len(int_valuesY)):
          states.append(str(i))
        for i in range(0,len(int_valuesY)):
          if(i%3==0):
            matrix_out_list.append(matrixoutA)
          if(i%3==1):
            matrix_out_list.append(matrixoutB)
          if(i%3==2):
            matrix_out_list.append(matrixoutC)
    else:
        for ik in range(0,len(int_valuesX)):
            matrixoutB.append(int_valuesY[ik]/sum(int_valuesY))
        for ik in range(0,len(int_valuesX)):
            matrixoutA.append(int_valuesX[ik]/sum(int_valuesX))
        for ik in range(0,len(int_valuesX)):
            matrixoutC.append(math.sqrt(math.pow(int_valuesX[ik],2)+math.pow(int_valuesY[ik],2)))
        for i in range(0,len(int_valuesX)):
          states.append(str(i))
        for i in range(0,len(int_valuesX)):
          if(i%3==0):
            matrix_out_list.append(matrixoutA)
          if(i%3==1):
            matrix_out_list.append(matrixoutB)
          if(i%3==2):
            matrix_out_list.append(matrixoutC)
    length=len(matrix_out_list)
    
    transition_matrix = {states[i]: matrix_out_list[i] for i in range(len(states))}
    
    #print("matrix selected: ",transition_matrix)
    for day in range(length):
    # Choose the next state based on the current state's probabilities
        
        next_state = random.choices(states, weights=transition_matrix[current_state])[0]
        hlkop=int(next_state)
        #print(hlkop)
        res=calculate_steady_state(matrix_out_list[hlkop])
        print("Steady-State Vector:", res)
        magnitudeK=0
        for i in range(0,len(matrix_out_list[hlkop])):
            magnitudeK+=math.pow(res[i],2)
        print("Magnitude: ",math.sqrt(magnitudeK))
        #print(transition_matrix[current_state][hlkop])
        print(f"term {day + 1}: {next_state}")
        current_state = next_state
        
    
    #if(round((int(bit_string,2)/256)*100)==100):
     #   print("state sucessfully reached!")
     #   break






