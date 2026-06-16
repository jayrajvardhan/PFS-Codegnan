'''
Data analysis:
--------------
--> the process of inspecting, cleaning, transforming, and modelling data to discover
useful insights.

Types of data analysis:
-----------------------
1.Descriprtive analysis
-----------------------
--> Summarizing data

2.Diagnostic analysis
---------------------
--> Understanding causes

3.Predictive analysis
---------------------
--> Forecasting the future outcomes

4.Prescriptive analysis
------------------------
--> Suggesting actions based on data

why DA
------
--> To improve decision making
--> Detects trends and patterns
-->
Numpy(Numerical python):
-----------------------
--> This python library for numerical computing it provides support for multiple
dimensional arrays, and linear algebra operations, making it essential for data
analysis

using numpy in DA:
------------------
--> Improved performance
--> Simplifies complex operations
--> Easy data manipulation
'''
'''
import numpy as np
arr_1 = np.array([[1,2,3,4],[4,5,6,7],[5,6,7,8]])
print(arr_1)

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.shape)
reshaped = arr.reshape(3,2)
print(reshaped)

import numpy as np
arr = np.array([10,20,30,40,50])
print(arr + 5)

import numpy as np
arr1 = np.array([[1,2],[4,5]])
arr2 = np.array([[5,6],[7,8]])
print(np.dot(arr1, arr2))
'''

import numpy as np
arr1 = np.array([10,20,30])
nrm_copy = arr1.view()
arr1[0] = 100
print(nrm_copy)
print(arr1)

copy_dee = arr1.copy()
arr1[1] = 200
print(copy_dee)
print(arr1)

'''
Pandas:
------
--> Pandas is a powerful data manipulation and analysis library..
--> where it provides data strucutre like series and dataframe for efficient data
handling.
eg:
--
import pandas as pd
any = pd.Series([2999,15999,52999,4999,1999],
                index=['Earbuds', 'Smartphone', 'Laptop', 'Watch', 'Footwear'])
print(any)

methods Series
--------------
mean()
sum()
max()
min()
apply()
map()

Dataframe
---------
data = {'product':['Earbuds', 'Smartphone', 'Laptop', 'Watch', 'Footwear'],
        'Brand':['Noise', 'Motoedge', 'Acer', 'fastrack', 'Nike'],
        'Price':['1599', '25000', '50000', '2000', '1000'],
        'stock':['50', '15', '25', 40', '70']
       }
dip = pd.DataFrame(data)
print(dip)
'''

import pandas as pd
any = pd.Series([2999,15999,52999,4999,1999],
                index=['Earbuds', 'Smartphone', 'Laptop', 'Watch', 'Footwear'])
print(any)


import pandas as pd
data = {'product':['Earbuds', 'Smartphone', 'Laptop', 'Watch', 'Footwear'],
        'Brand':['Noise', 'Motoedge', 'Acer', 'fastrack', 'Nike'],
        'Price':['1599', '25000', '50000', '2000', '1000'],
        'stock':['50', '15', '25', '40', '70']
       }
dip = pd.DataFrame(data)
print(dip)

