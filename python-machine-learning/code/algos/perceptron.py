import numpy as np


class Perceptron(object):

    def __init__(self, bias=0, eta=0.1, epoch=10):

        self.bias = bias
        self.eta = eta
        self.epoch = epoch

    def net_input(self, x):

        return self.weights[0] + np.dot(x, self.weights[1:])

    def fit(self, X, y):

        self.weights = np.zeros(1 + X.shape[1])
        self.weights[0] = -self.bias
        self.errors = []

        for _ in range(self.epoch):
            errors = 0
            for xi, yi in zip(X, y):
                # compute error and delta_w
                error = yi - self.predict(xi)
                delta_w = self.eta * error * xi

                # update weights
                self.weights[1:] += delta_w
                self.weights[0] += error

                # append to error count
                errors += int(error != 0)

            self.errors.append(errors)

        return self

    def predict(self, x):

        return np.where(self.net_input(x) >= 0, 1, -1)
