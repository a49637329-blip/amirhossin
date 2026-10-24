
import random 

n  =  10  

a  =  []

for i in range (n)  : 
    
    a  +=  [random.random()] 
    
    
total = 0.0 

for v in a : total += v 

avrage = total / len(a)

