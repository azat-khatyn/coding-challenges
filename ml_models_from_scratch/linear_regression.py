import numpy as np
from numpy import random


class LinearRegressionGD:

    def __init__(self, alpha: float, lmbd: float, n_iter: int):
        self.theta_final = None
        self.costs = []
        self.alpha = alpha
        self.lmbd = lmbd
        self.n_iter = n_iter

    def fit(self, X: np.ndarray, Y: np.ndarray):
        ones = np.ones(X.shape[0]).reshape(X.shape[0], 1)
        X_good = np.concatenate((ones, X), axis=1)
        theta = random.randn(X_good.shape[1])
        m = X_good.shape[0]
        self.costs = []
        for k in range(self.n_iter):
            theta = theta - self.alpha * (1.0 / m * ((X_good @ theta - Y) @ X) + self.lmbd * theta)
            cost = 1.0 / (2 * m) * np.sum(np.square(X_good @ theta - Y)) + self.lmbd / 2 * np.sum(np.square(theta))
            self.costs.append(cost)
        self.theta_final = theta

    def get_theta(self):
        return self.theta_final

    def get_costs(self):
        return self.costs

    def predict(self, x: np.ndarray):
        return np.dot(self.theta_final, x)

