# class A: 
#     def rk(self): 
#         print(" In class A") 
# class B(A): 
#     def rk(self): 
        
#         print(" In class B") 
  
# r = B() 
# r.rk() 


"""Memory Allocation"""

"""
Python optimizes memory utilization by allocation the same object reference to a new variable 
"""

x = 10
y = x
print("Value of x and y",x,y)
print("Memory Address of x and y",id(x),id(y))
if id(x) == id(y):
    print("x and y refer to the same object") 


"""Changes of X """

x = 10 
y = x
x += 1

print("Value of x and y",x,y)
print("Memory Address of x and y",id(x),id(y))

if id(x) != id(y): 
    print("x and y do not refer to the same object") 



Z = 5
print(Z)
del z
print(z)