import numpy as np

class LinearRegression:
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