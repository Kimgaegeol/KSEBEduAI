import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from tglearn import MyLinearRegression, MyKNeighborsRegressor

ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
x = ls[["GDP per capita (USD)"]].values
print(x)
y = ls[["Life satisfaction"]].values
print(y)

# ls.plot(kind="scatter", grid=True, x="GDP per capita (USD)", y="Life satisfaction")
# plt.axis([23500,62500,4,9])
# plt.show()
#
# model = LinearRegression()
# model2 = KNeighborsRegressor(n_neighbors=3)
# model3 = MyLinearRegression()
# model.fit(x,y)
# model2.fit(x,y)
# model3.fit(x,y)
#
# x_new = [[31721.3]] #ROK 2020
# print(model.predict(x_new))
# print(model2.predict(x_new))
# print(model3.predict(x_new))

model = MyKNeighborsRegressor()
model.fit(x,y)
model.predict(30000)