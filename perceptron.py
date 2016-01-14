#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16
import numpy as np
import random as random

eta = 0.2 # eta is 0.2 for training perceptrons

class perceptron:
    """Perceptron entity class"""
    bias =  np.array([random.uniform(-.999999999999, .999999999999)])  # weight0 is the bias, 1 bias per perceptron
    # 16 weights for perceptron, seeded randomly with values from 0-1
    # Total of 17 weights, including the bias
    weights = np.array([random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999)])
    # 16 inputs
    #inputs = []

    def __init__(self):
        return

    # train perceptron
    def train(self, inputs, target):
        # x, expected = choice(training_data)
        # result = dot(w, x)
        # error = expected - unit_step(result)
        # errors.append(error)
        # w += eta * error * x

        # update weights
        """
        :rtype: object
        """
        self.bias = self.bias + eta * 1 * target # bias input is always +1
        #self.weights = self.weights + eta * inputs * target
        # for w in np.nditer(self.weights, order='C'):
        #     print w
        #w = w + eta * input[w] * target
        for i in range(len(self.weights)):
            #print i
            self.weights[i] = self.weights[i] + eta * inputs[i] * target
            #print self.weights[i]

        # for w in self.weights:
        #     print self.weights[w]
            #w = w + eta * input[w] * target

        return

    # run test on perceptron
    def test(self, inputs):
        # return true if bias + the dot product of weights and inputs is geq 0
        # signum function, tells if the sign of the test is correct
        return self.bias + np.dot(self.weights, inputs) >= 0
