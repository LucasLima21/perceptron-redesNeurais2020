"""
Alunos:
    David Cardoso Yonekura
    Lucas da Silva Lima
    Rafael Barbosa de Carvalho

"""

import numpy as np
class Neuron():
    def __init__(self, lr, low_limit, high_limit):
        # o ultimo valor aleatorio gerado será o Bias,
        # visto que x_0, de valor 1, será adicionado na ultima coluna
        self.weightArray = np.random.uniform(low_limit, high_limit, 3)
        self.learningRate = lr
        self.low_limit = low_limit
        self.high_limit = high_limit
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
            
            
    def iteratedFit(self, arrayX, arrayY, iteration):
        epochArray = []
        fitArray = []
        for i in range(2):
            self.fit(arrayX, arrayY)
            self.weightArray = np.random.uniform(self.low_limit, self.high_limit, 3)
            epochArray.append(self.epoch)
            fitArray.append(self.fitCountWeight)
            self.epoch = 0
            self.fitCountWeight = 0
                
        return (epochArray, fitArray)
        
            
    def run100epochs(self, arrayX, arrayY):
        p = np.random.permutation(len(arrayX))
        arrayX, arrayY = arrayX[p], arrayY[p]
        while(self.epoch < 100):
            for i in range(len(arrayX)):
                self.updateWeightArray(arrayY[i], self.calculateActivation(arrayX[i]), arrayX[i])
            self.epoch += 1
     
    def predict(self,X):
        ret = []
        X = np.insert(X, 2, 1, axis=1)
        for x in X:
            ret.append(self.calculateActivation(x))
        return ret
    