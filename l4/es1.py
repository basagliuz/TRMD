import numpy as np


array_1 = np.arange(0, 5, 0.5)
array_2 = np.arange(0, 3, 0.3)
result = array_2 - array_2

zeros = np.where(array_2 != 0)[0]
result = array_1[zeros]/array_2[zeros]
print(result)

array_2 = np.where(array_2 == 0, )
