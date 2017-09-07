import random
import numpy as np

class CoreFunction:
    def __init__(self):
        self.x = []


    def Linear(self, input_value):
        k = -2
        b = input_value
        if b:
            foo = [random.randint(0, b) for col in range(b)]
            x = [map(lambda x: k*(x-(b/2)), foo)]
            #print x
            return x
        else:
            print "input error"

    def Simgoid(self, input_value):
        b = input_value
        k = -6
        if b:
            foo = [random.uniform(0, b) for i in range(b)]
            x = [map(lambda x:round(k*((x-(b/2))/(1+abs(x-(b/2)))),2), foo)]
            return x
        else:
            print "input error"
