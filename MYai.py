import math
avgchangeinpercentone=0
avgchangeinpercenttwo=0
rateon=0
rateoff=0
ratei=0
weightA=0
weightB=0
avgpositivedisplacement=0
avgnegativedisplacement=0
avg=[0]
klo=[0]
for i in range(1,35):
    avg[i]=avg.insert(i,0)

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
accuracy=0
accuracya=0
accuracyb=0
for k in range(1,35):
    
    errorrateB=0
    errorrateA=0
    for i in range(1,35):
        x=m(0.2,0.4,0.23,0.45,0.34,0.67,9,7)
        avgchangeinpercentone=x[0]
        avgchangeinpercenttwo=x[1]
        x=m(0.2,0.4,0.23,0.45,0.34,0.67,9,7)
        avgchangeinpercentone=x[0]-avgchangeinpercentone
        avgchangeinpercenttwo=x[1]-avgchangeinpercenttwo
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
        ui=random.randint(0,(lo+po+ikl)*100)
        
        
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
def derive(E):
    import numpy as np
    dx=1
    dy=np.gradient(E, dx)

    
    return dy
h=derive(avg)
#print(h)
h=derive(h)
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
    NOP=NM/np.abs(LM)
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
phaseshiftA=phase(endMa,3)
phaseshiftB=phase(endMb,3)
endhadmardA=hadmard(endMa,endMa)
endhadmardB=hadmard(endMb,endMb)
StatesA=state(klo)*phaseshiftA*endhadmardA*(1/math.sqrt(2))
print(StatesA*find_D(Am))
StatesB=state(klo)*phaseshiftB*endhadmardB*(1/math.sqrt(2))
print(StatesB*find_D(Bm))

