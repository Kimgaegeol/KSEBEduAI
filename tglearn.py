import numpy as np

def quick_sort(l):
    n = len(l)
    if n <= 1: return l

    x_l = [(value[0], i) for i, value in enumerate(l)]

    pivot = x_l[n // 2][0]

    left, mid, right = [], [], []

    for value, index in x_l:
        if value < pivot:
            left.append(l[index])
        elif value > pivot:
            right.append(l[index])
        else:
            mid.append(l[index])

    return quick_sort(left) + mid + quick_sort(right)

    return quick_sort(left)+mid+quick_sort(right)

class MyKNeighborsRegressor:
    def __init__(self, n_neighbors = 5):
        self.n_neighbors = n_neighbors
        self.list = []

    def fit(self,x,y):
        for _ in range(len(x)):
            self.list.append([float(x[_][0]),float(y[_][0])])
        self.list = quick_sort(self.list)

    def predict(self, new_x):
        self.list.append([new_x,None])
        self.list = quick_sort(self.list)
        head = 0
        for i in range(len(self.list)):
            if self.list[i][0] == new_x:
                head = i
                break
        l = []



class MyLinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None

    def fit(self, x, y):
        """
        learning fucntion
        :param x: independt variable (2d array format)
        :param y: dependent variable (2d array format)
        :return: void
        """
        x_mean = np.mean(x)
        y_mean = np.mean(y)

        denominator = np.sum(pow(x-x_mean,2))
        numerator = np.sum((x-x_mean)*(y-y_mean))

        self.slope = numerator/denominator
        self.intercept = y_mean-self.slope*x_mean

    def predict(self, new_x) -> np.ndarray:
        """
        predict value for input
        :param new_x: new indepent variable
        :return: predict value for input (2d array format)
        """
        return self.slope*np.array(new_x) + self.intercept