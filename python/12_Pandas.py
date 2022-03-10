dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

iris = pd.read_csv("Iris.csv", index_col = 0)
print(iris)

print(iris[['SepalLengthCm']])

print(iris[0:4])

print(iris.loc[iris.SepalLengthCm == 5.1])

