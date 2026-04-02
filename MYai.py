avgchangeinpercentone=0
avgchangeinpercenttwo=0
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

for k in range(0,34):
    errorrateB=0
    errorrateA=0
    for i in range(0,34):
        x=m(0.2,0.4,0.23,0.45,0.34,0.67,0.1,7)
        avgchangeinpercentone=x[0]
        avgchangeinpercenttwo=x[1]
        x=m(0.2,0.4,0.23,0.45,0.34,0.67,0.1,7)
        avgchangeinpercentone=x[0]-avgchangeinpercentone
        avgchangeinpercenttwo=x[1]-avgchangeinpercenttwo
    errorrateB=(avgchangeinpercentone/34)
    errorrateA=(avgchangeinpercenttwo/34)
    print("Test number",k,":")
    print("average error rate for B:",errorrateB)
    print("average error rate for A:",errorrateA)
