import numpy as np

def gradient_descent(x1, x2, y): 
    w0 = 0                      
    w1 = w2 = 1                     
    iterations  = 3
    
    n = len(x1)
    learning_rate = 0.0002
    
    for i in range(iterations):
        y_predicted =  w0 + (w1 * x1) + (w2 * x2)                
        cost_1 = (1 /n ) * sum([val ** 2 for val in (y - y_predicted)])
        w0_d = - (2/n) * sum (y - y_predicted)  # bd
        
        w1_d = - (2/n) * sum (x1 * (y - y_predicted)) # md  
        w2_d = - (2/n) * sum (x2 * (y - y_predicted)) # md         
        
        w0 = w0 - learning_rate * w0_d
        w1 = w1 - learning_rate * w1_d
        w2 = w2 - learning_rate * w2_d       
        
        y_predicted =  w0 + (w1 * x1) + (w2 * x2)
        cost_2 = (1 /n ) * sum([val ** 2 for val in (y - y_predicted)])
             
        print("w0: {}, w1: {}, w2: {}, cost1: {}, cost2: {}, iterations {} ".format(w0, w1, w2, cost_1, cost_2, i))


x1 = np.array([60,67,71,75,78])
x2 = np.array([22,24,15,20,16])
y = np.array([140,159,192,200,212])

gradient_descent(x1,x2,y)
