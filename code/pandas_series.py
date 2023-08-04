import pandas as pd
import numpy as np

# Pandas Series
# Like a table column, 1D array with any type of data

py_list = [5,9,12,27]

pd1 = pd.Series(py_list)
"""
0     5
1     9
2    12
3    27
dtype: int64
"""

# print specific value
pd1[2]
# pd1[2] is 12

# Labels using the index argument
pd_data = [1,2,3,4,5]
pd_index = ["A", "B", "C", "D", "X"]
pd2= pd.Series(pd_data, pd_index)
"""
A    1
B    2
C    3
D    4
X    5
dtype: int64
"""

pd3= pd.Series(pd_data, index=pd_index)
el = pd3["B"]
# el is 2
el2 = pd3[3]
# el2 is 3

# Key Value Dictionary
# Dictionaries are key-value-pairs
cars = {"Tesla": 12, "Mercedes": 42, "BMW": 5}
pd4 = pd.Series(cars)
"""
Tesla       12
Mercedes    42
BMW          5
dtype: int64
"""
x = pd4['Tesla']
# x is 12





