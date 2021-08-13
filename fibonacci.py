a = int(input("Enter the number of terms:"))  
  
n1 = 0  
n2 = 1  
count = 2  
 
if a <= 0:  
   print("Plese enter a positive integer")  
elif a == 1:  
   print("Fibonacci sequence is:")  
   print(n1)  
else:  
   print("Fibonacci sequence:")  
   print(n1,",",n2,end=', ')  
   while count < a:  
       nth = n1 + n2  
       print(nth,end=' , ')  
        
       n1 = n2  
       n2 = nth  
       count += 1  
