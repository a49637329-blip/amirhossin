
import random 

n  =  10  

a  =  []

for i in range (n)  : 
    
    a  +=  [random.random()] 
    
    
n  = len  (a)  

for i in range (n//2):
    
    temp = a[i]
    a[i] = a[n-1-i]
    a[n-1-i] = temp
    

