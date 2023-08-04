# Pandas Series

A pandas.Series is a one-dimensional labeled array in pandas, which is a fundamental data structure that represents a column of data in a tabular format. Each element in a Series has an associated label, known as the index.

## Creating a Series
You can create a Series using various data sources, such as a Python list, NumPy array, or even a dictionary.

```python
import pandas as pd

# Creating a Series from a list
data = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data)

# Creating a Series from a dictionary
data_dict = {'A': 100, 'B': 200, 'C': 300}
series_from_dict = pd.Series(data_dict)
```

## Accessing Data in a Series
You can access elements in a Series using the index label.

```python
# Accessing elements by index label
print(series_from_list[2])  # Output: 30

# Accessing elements by index label from a dictionary-based Series
print(series_from_dict['B'])  # Output: 200
```