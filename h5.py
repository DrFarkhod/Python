#5
from functools import reduce
new_list = [i for i in range(100,1000) if i % 2 == 0]
summa = reduce((lambda x, y: x * y), new_list)
print(summa)