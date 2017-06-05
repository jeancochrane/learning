import numpy as np


class Adaline(object):

    def __init__(self, bias=0, eta=0.01, epoch=10, stochastic=False,
                 shuffle=True):

        self.bias = bias
        self.eta = eta
        self.epoch = epoch
        self.stochastic = stochastic
        self.shuffle = shuffle

    def net_input(self, x):

        return self.weights[0] + np.dot(x, self.weights[1:])

    def _initialize_weights(self, X):

        self.weights = np.zeros(1 + X.shape[1])
        self.weights[0] = -self.bias

        return self

    def fit(self, X, y):

        self._initialize_weights(X)
        self.cost = []

        for _ in range(self.epoch):

            if self.shuffle:
                X, y = self._shuffle(X, y)

            if self.stochastic:

                cost = []
                for xi, yi in zip(X, y):
                    error = yi - self.activation(xi)
                    self.weights[0] += self.eta * error
                    self.weights[1:] += self.eta * xi.dot(error)
                    cost.append(error**2 / 2)
                self.cost.append(sum(cost) / len(cost))

            else:

                errors = y - self.activation(X)
                self.weights[0] += self.eta * errors.sum()
                self.weights[1:] += self.eta * X.T.dot(errors)

                cost = (errors**2).sum() / 2
                self.cost.append(cost)

        return self

    def partial_fit(self, X, y):

        try:
            assert len(self.weights)
        except AttributeError:
            self._initialize_weights(X)

        error = y - self.activation(X)
        self.weights[0] += self.eta * error
        self.weights[1:] += self.eta * X.dot(error)

        return self

    def activation(self, x):

        return self.net_input(x)

    def predict(self, x):

        return np.where(self.activation(x) >= 0, 1, -1)

    def _shuffle(self, X, y):

        order = np.random.permutation(len(y))
        return X[order], y[order]
