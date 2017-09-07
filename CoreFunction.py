import random

class CoreFunction:
    def __init__(self):
        self.all_output = {}
        self.x = []
        self.y = []

    def Linear(self, input_value, k):
        b = input_value
        if b:
            x = [random.uniform(0, b) for i in range(b)]
            for i in x:
                y[i] = -k*(x - (b/2))
            
            return y
        else:
            print "input error"

    def simgoid(self, input_value, k):
        b = input_value
        if b:
            x = [random.uniform(0, b) for i in range(b)]
            for j in x:
                y[j] = -k*((x-(b/2))/(1+abs(x-(b/2))))
            print y
            return y
        else:
            print "input error"
    def combination(self,input_value, y):
        for k in all_output:
            all_output[k] = y
        print all_output
