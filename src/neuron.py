"""
Alunos:
    David Cardoso Yonekura
    Lucas da Silva Lima
    Rafael Barbosa de Carvalho

"""

import numpy as np

class Neuron():
    def __init__(self, lr=0, low_limit=0, high_limit=0):
        # o ultimo valor aleatorio gerado será o Bias,
        # visto que x_0, de valor 1, será adicionado na ultima coluna
        self.weightArray = np.random.uniform(low_limit, high_limit, 3)
        self.learningRate = lr
        self.low_limit = low_limit
        self.high_limit = high_limit
        self.epoch = 0
        self.fitCountWeight = 0
        self.changedWeight = 1
        self.fitCountEpoch = []
        self.auxCountWeight = 0
        
    def updateWeightArray_print(self, expectValue, obtainedValue, input_):
        # função adicionada para que seja mostrada cada alteração do vetor
        # na parte 1 do projeto, feito desta maneira para nao interferir no resultado da parte 2
        # que utiliza da função updateWeightArray
        if(expectValue != obtainedValue):
            self.fitCountWeight+=1
            self.auxCountWeight+=1
            self.changedWeight = 1
            auxData = (self.learningRate*(expectValue - obtainedValue))*input_
            self.weightArray = self.weightArray + auxData
            print("Vetor de pesos Alterado: ", self.weightArray)
    
        
    
    def updateWeightArray(self, expectValue, obtainedValue, input_):
        if(expectValue != obtainedValue):
            self.fitCountWeight+=1
            self.changedWeight = 1
            auxData = (self.learningRate*(expectValue - obtainedValue))*input_
            self.weightArray = self.weightArray + auxData
            
    def calculateActivation(self, input_):
        u = np.sum(input_ * self.weightArray)
        return 1 if u > 0 else 0
        
        
    def fit_print(self, arrayX, arrayY):
        # função adicionada para que seja mostrada cada alteração do vetor
        # na parte 1 do projeto, feito desta maneira para nao interferir no resultado da questão 2
        # que utiliza da função fit
        while(self.changedWeight == 1):
            self.changedWeight = 0
            for i in range(len(arrayX)):
                self.updateWeightArray_print(arrayY[i], self.calculateActivation(arrayX[i]), arrayX[i])
            self.fitCountEpoch.append(self.auxCountWeight)
            self.auxCountWeight = 0
            self.epoch += 1
        
    def fit(self, arrayX, arrayY):
        while(self.changedWeight == 1):
            self.changedWeight = 0
            for i in range(len(arrayX)):
                self.updateWeightArray(arrayY[i], self.calculateActivation(arrayX[i]), arrayX[i])
            self.epoch += 1
            
            
    def iteratedFit(self, arrayX, arrayY, iteration):
        epochArray = []
        fitArray = []
        for i in range(iteration):
            self.weightArray = np.random.uniform(self.low_limit, self.high_limit, 3)
            self.fit(arrayX, arrayY)
            self.changedWeight = 1
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