#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16
import numpy as np
import random as random

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

    def __init__(self, inputs):
        self.inputs = inputs
        return

    def train(self):
        return

    def test(self, inputs):
        # return true if bias + the dot product of weights and inputs is geq 0
        return self.bias + np.dot(self.weights, inputs) >= 0
