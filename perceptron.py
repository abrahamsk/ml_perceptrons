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
        self.prev_bias = self.bias.copy() # store prev bias when you update bias
        self.bias = self.bias + eta * 1 * target # bias input is always +1
        #self.weights = self.weights + eta * inputs * target
        # for w in np.nditer(self.weights, order='C'):
        #     print w
        #w = w + eta * input[w] * target
        self.prev_weights = self.weights.copy()
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


    def revert_weights(self):
        """
        reset weights to previous values if results
        of stochastic descent changes are getting worse
        """
        self.weight = self.prev_weights.copy()
        return


# compute accuracy of perceptron
def compute_accuracy(perceptron, letters_list_training):
    for letter in letters_list_training:
            #print letter.value
            if m in letter.value:
                # test perceptrons that contain the letter matching m in perceptron[mn]
                output = perceptron.test(perceptrons[m + n], letter.attributes)
                # if perceptron output is true, sgn((dot product(w,x))) is positive
##                print "output: ", output
                if output == True:
                    correct_output = correct_output + 1 # increment correct counter if input matches target
#                    print "+ Input m: ", m, " from perceptron ", m,n, " result: ", m
                else:
                    incorrect_output = incorrect_output + 1
                    # set t = 1 for input m in perceptron[mn]
                    perceptron.train(perceptrons[m + n], letter.attributes, 1.0)
#                    print "- Input m: ", m, " from perceptron ", m,n, " result: ", n
            if n in letter.value:
                # test perceptrons that contain the letter matching m in perceptron[mn]
                output = perceptron.test(perceptrons[m + n], letter.attributes)
##                print "output: ", output
                if output == True:
                    correct_output = correct_output + 1 # increment correct counter if input matches target
#                    print ">>> + Input n: ", n, " from perceptron ", m,n, " result: ", n
                else:
                    incorrect_output = incorrect_output + 1
                    # set t = -1 for input n in perceptron[mn]
                    perceptron.train(perceptrons[m + n], letter.attributes, -1.0)
#                    print ">>> - Input n: ", n, " from perceptron ", m,n, " result: ", m