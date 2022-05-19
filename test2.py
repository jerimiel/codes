def hat(**kwargs):
    for i,j in kwargs.items():
        print(type(i),type(j))
    


hat(red=33,blue=45)
a=[1,2,3,4,5,6]
import random
b=random.sample(a,6)
print(b)
print(a.count(23))
