#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16
import numpy as np
import random as random

learning_rate = 0.2 # eta is 0.2 for training perceptrons

class perceptron:
    """Perceptron entity class"""
    bias =  random.uniform(-.999999999999, .999999999999)  # weight0 is the bias, 1 bias per perceptron
    # 16 weights for perceptron, seeded randomly with values from 0-1
    # Total of 17 weights, including the bias
    weights = np.array([random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999)])
    # 16 inputs
    inputs = []

    def __init__(self):
        return

    # train perceptron
    def train(self, target):
        # x, expected = choice(training_data)
        # result = dot(w, x)
        # error = expected - unit_step(result)
        # errors.append(error)
        # w += eta * error * x

        self.bias = self.bias + learning_rate * self.inputs * target
        self.weights = self.weights + learning_rate * self.inputs * target

        return

    # run test on perceptron
    def test(self, inputs):
        # return true if bias + the dot product of weights and inputs is geq 0
        # signum function, tells if the sign of the test is correct
        return self.bias + np.dot(self.weights, inputs) >= 0
