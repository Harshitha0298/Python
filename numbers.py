#type to know the data type
x=3
y=3.4
z=3+4j
print(type(x))
print(type(y))
print(type(z))

#type conversion
x="10"
y=3
print(int(x))
print(float(x))
print(complex(int(x),y))

#rounding
x=7
y=8
print(abs(x-y))

import math
x=3.456475
print(math.floor(x))
print(math.ceil(x))
print(round(x,3))
print(math.trunc(x))

#random
import random
print(random.random())
print(random.randint(0,6))

#validation
x=34.0
print(x.is_integer())

x=34.40
print(x.is_integer())

x=44
print(isinstance(x,int))


x="44"
print(isinstance(x,str))

#generate the random interger between i and 100 and check if the generated value is odd or even
num=random.randint(1,100)
print(num)
if(num%2==0):
    print("even number")
else:
    print("odd number")
