#Homogeneous Data Structures

hogeneousList = [1, 2, 3, 4, 'Hello', 6, 7, 8, 9, 10]

for i in hogeneousList:
    print(type(i))

import numpy as np
homogenousArray = np.array(['1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0', '10.0'])

#Heterogeneous Data Structures

heterogeneousList = [1, 'Hello', 3.14, True]

for i in heterogeneousList:
    print(type(i))