# Python code to demonstrate the working of gcd() 
    
# importing "math" for mathematical operations  
import math  
    
# prints 12  
print ("The gcd of 28 and 21 is : ", end ="")  
print (math.gcd(28, 21))  
print("35:54*101",(54*101))
print("39:99*42",(99*42))
print("37:67*63",(67*63))
# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 28
num2 = 21

print("The L.C.M. is", compute_lcm(num1, num2))
# Python3 program to demonstrate the  
# sqrt() method  
  
  # import the math module  
import math  
# print the square root of 784
print(math.sqrt(784))
print("25:63/3",(63/3))
print("26:26E-3",(1.444E-3))
print("32:65**2",(65**2))
print("41:32**2-21**2",(32**2-21**2))
print("43:458%11",(458%11))
print("44:2**9",(2**9))
print("79:16*22*15",(16*22*15))
print("73:396*394",(396*394))
# Python program to demonstrate mean() 
# function from the statistics module 
  
# Importing the statistics module 
import statistics 
  
# list of positive integer numbers 
data1 = [9, 21, 20, 22, 23, ]
  
x = statistics.mean(data1) 
  
# Printing the mean 
print("Mean is :", x) 
print("62:241*111",(241*111))
 

# Python3 program to demonstrate the  
# sqrt() method  
  
# import the math module  
import math  
  
# print the square root of  7056 
print(math.sqrt(7056))  
print("55: 92*92", (92*92))

       
 
 

  

 
  

  

 