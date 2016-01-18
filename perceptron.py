#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16

import numpy as np
import random as random

eta = 0.2 # learning rate is 0.2 for training perceptrons

class perceptron:
    """ Perceptron entity class
     contains bias and weights """
    bias =  np.array([random.uniform(-.999999999999, .999999999999)])  # weight0 is the bias, 1 bias per perceptron
    prev_bias = np.array([]) # store prev bias when you update bias
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
    prev_weights = np.array([]) # store prev weights when you update weights

    # bool to mark whether output from perceptron is correct during training
    is_result_correct = None

    def __init__(self):
        """ init perceptron """
        return

    def test_accuracy(self, instances):
        """
        Test the accuracy of a perceptron for a given set of inputs
        :param inputs:
        :return: the number of accurate results for a given data set
        """
        num_accurate = 0

        # run test function for all instances in training set
        # that match the letters in perceptron name
        for i in range(len(instances)):
            #print instances[i].attributes
            if perceptron.test(self, instances[i].attributes) == True:
               num_accurate += 1

        return num_accurate

    def train(self, inputs, target):

        """
        :param inputs:
        :param target:
        :return perceptron output y = sgn(dot product(w,x)):
        train perceptron using weight changes
        for use with stochastic gradient descent
        """
        # x, expected = choice(training_data)
        # result = dot(w, x)
        # error = expected - unit_step(result)
        # errors.append(error)
        # w += eta * error * x

        # update weights after storing previous weight values
        ####print "bias + " + self.bias + "eta * 1 * target " + target
    #    self.prev_bias = self.bias.copy() # store prev bias when you update bias
        self.bias = self.bias + eta * 1 * target # bias input is always +1
        #self.weights = self.weights + eta * inputs * target
        # for w in np.nditer(self.weights, order='C'):
        #     print w
        #w = w + eta * input[w] * target
    #    self.prev_weights = self.weights.copy()
        # update all weight values using gradient descent
        for i in range(len(self.weights)):
            #print i
            self.weights[i] = self.weights[i] + eta * inputs[i] * target
            #print self.weights[i]

        # for w in self.weights:
        #     print self.weights[w]
            #w = w + eta * input[w] * target
        ####return self.bias + np.dot(self.weights, inputs) >= 0
        return

    def save_bias(self):
        """
        Preserve the bias to revert if need be after epoch
        :return: bias
        """
        return self.bias

    def save_weights(self):
        """
        Preserve the weights to revert if need be after epoch
        :return: weights
        """
        return self.weights

    def test(self, inputs):
        """
        :param inputs:
        return output y from perceptron
        y = sgn(dot product(w,x))
        """
        # run test on perceptron and return the output from the perceptron
        # return true if bias + the dot product of weights and inputs is geq 0
        # signum function, tells if the sign of the test is correct
        return self.bias + np.dot(self.weights, inputs) >= 0

    def set_incorrect_result(self):
        """
        record that perceptron returned an incorrect result
        such that output  y neq target t
        """
        self.is_result_correct = False
        return

    def check_result(self):
        """
        :return whether perceptron was marked as having incorrect results:
        """
        return self.is_result_correct


    def revert_weights(self, saved_bias, saved_weights):
        """
        reset weights to previous values if results
        of stochastic descent changes are getting worse
        """
        self.bias = self.saved_bias.copy()
        self.weight = self.saved_weights.copy()
        return