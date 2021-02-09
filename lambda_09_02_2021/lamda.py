def identity(x):
    return x


data = identity(5)
print(data)

print((lambda x:x +x) (5))

lamda_cust_fun = lambda x:x +x
print(lamda_cust_fun(5))

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)


my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

pairs.sort(key=lambda pair: pair[1])
print(pairs)

sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter (lambda x: x > 4, sequences) 
print(list(filtered_result))


sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map (lambda x: x*x, sequences) 
print(list(filtered_result))

from functools import reduce
sequences = [1,2,3,4,5]
product = reduce (lambda x, y: x*y, sequences)
print(product)


C = [39.2, 36.5, 37.3, 38, 37.8] 
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)
C = list(map(lambda x: (float(5)/9)*(x-32), F))
print(C)

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9] 

print(list(map(lambda x, y, z : x+y+z, a, b, c)))


from math import sin, cos, tan, pi

def map_functions(x, functions):
     """ map an iterable of functions on the the object x """
     res = []
     for func in functions:
         res.append(func(x))
     return res

family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))


fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)


even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)


even_numbers = list(filter(lambda x: x % 2 -1, fibonacci))
print(even_numbers)

import functools
print(functools.reduce(lambda x,y: x+y, [47,11,42,13]))

from functools import reduce
f = lambda a,b: a if (a > b) else b
print(reduce(f, [47,11,42,102,13]))

from functools import reduce
print(reduce(lambda x, y: x+y, range(1,101)))


print(reduce(lambda x, y: x*y, range(1,49)))
print(reduce(lambda x, y: x*y, range(44,50))/reduce(lambda x, y: x*y, range(1,7)))




# 1) Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this:

# Order Number    Book Title and Author              Quantity     Price per Item
# 34587           Learning Python, Mark Lutz             4          40.95
# 98762           Programming Python, Mark Lutz          5          56.80
# 77226           Head First Python, Paul Barry          3          32.95
# 88112           Einführung in Python3, Bernd Klein     3          24.99


# Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number and the product of the price per items and the quantity. The product should be increased by 10,- € if the value of the order is smaller than 100,00 €.
# Write a Python program using lambda and map.


# 2) The same bookshop, but this time we work on a different list. The sublists of our lists look like this: [ordernumber, (article number, quantity, price per unit), ... (article number, quantity, price per unit) ] Write a program which returns a list of two tuples with (order number, total amount of order).




orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
           ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 	3, 24.99]]

min_order = 100
# print(list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10),map(lambda x: (x[0],x[2] * x[3]), orders))))
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), 
                  map(lambda x: (x[0],x[2] * x[3]), orders)))

# print(invoice_totals)
# [('34587', 163.8), ('98762', 284.0), ('77226', 108.85000000000001), ('88112', 84.97)]
from functools import reduce

orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
           [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
           [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

min_order = 100
print(list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), orders)))
invoice_totals = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), orders))
print(list(map(lambda x: [x[0]] + [reduce(lambda a,b: a + b, x[1:])], invoice_totals)))
invoice_totals = list(map(lambda x: [x[0]] + [reduce(lambda a,b: a + b, x[1:])], invoice_totals))
print(list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), invoice_totals)))
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), invoice_totals))

# print(invoice_totals)
# [[1, 678.3299999999999], [2, 494.46000000000004], [3, 364.79999999999995], [4, 492.57]]