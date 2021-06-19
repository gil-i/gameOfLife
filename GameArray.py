import numpy as np
import random 

from numpy.lib.histograms import _histogram_bin_edges_dispatcher


class LifeArray:
    """ This class represent the matrix array of the game of life and can be initialized at random or with a numpy array."""
    def ini_at_random(self):
        
        for p in np.ndenumerate(self.LifeArr):
            random.seed(p)
            rand = random.random()
            if rand> .8:
                self.LifeArr[p[0]] = 1
    
    def __init__(self, height, width, initiate=None):
        self.LifeArr = np.zeros((height,width))
        self.width = width 
        self.height = height
        if initiate:
            self.ini_at_random()

    def update(self):
        temp = np.zeros(self.LifeArr.shape)
        for p in np.ndenumerate(self.LifeArr):
            i,j = p[0]
            neighbors  = self.LifeArr[max(0, i-1) : min(i+2,self.height),
                    max(0, j-1) : min(j+2,self.width)]

            suma = np.sum(neighbors)
            if  suma == 3 and p[1] == 0:
                temp[p[0]] = 1
            elif p[1] == 1 and suma in range(3,5):
                temp[p[0]] = 1
            else: 
                temp[p[0]] = 0
        self.LifeArr = temp    

    def print(self):
        print(self.LifeArr)
        print("")
    
    def born(self, x, y):
        self.LifeArr[x,y] = 1

if __name__ == '__main__':
    arry = LifeArray(10,9,True)
    arry.print()
    arry.update()
    arry.print()
    arry.update()