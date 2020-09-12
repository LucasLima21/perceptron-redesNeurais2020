import numpy as np
class Neuron():
    def __init__(self, lr=0.1, low_limit=-0.5, high_limit=0.5):
        self.weightArray = weightArray=np.random.uniform(low_limit, high_limit, 3)
        self.learningRate = lr
        self.epoch = 0
        self.fitCountWeight = 0
        self.changedWeight = 1
        
    
    def updateWeightArray(self, expectValue, obtainedValue, input_):
        if(expectValue != obtainedValue):
            self.fitCountWeight+=1
            self.changedWeight = 1
            auxData = (self.learningRate*(expectValue - obtainedValue))*input_
            self.weightArray = self.weightArray + auxData
            
    def calculateActivation(self, input_):
        u = np.sum(input_ * self.weightArray)
        return 1 if u > 0 else 0
        
        
    def fit(self, arrayX, arrayY):
        while(self.changedWeight == 1):
            self.changedWeight = 0
            for i in range(len(arrayX)):
                self.updateWeightArray(arrayY[i], self.calculateActivation(arrayX[i]), arrayX[i])
            self.epoch += 1
            
    def predict(self,X):
        ret = []
        X = np.insert(X, 2, 1, axis=1)
        for x in X:
            ret.append(self.calculateActivation(x))
        return ret
