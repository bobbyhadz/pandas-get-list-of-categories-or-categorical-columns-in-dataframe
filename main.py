# Pandas: Get a List of Categories or Categorical Columns

import pandas as pd

df = pd.DataFrame({
    'id': pd.Categorical(['a', 'b', 'c', 'd']),
    'name': pd.Categorical(['Alice', 'Bobby', 'Carl', 'Dan']),
    'experience': [1, 5, 3, 8],
    'salary': [189.1, 180.2, 190.3, 205.4],
})

print(df.select_dtypes(include=['category']))

print('-' * 50)

print(df['name'].cat.categories)