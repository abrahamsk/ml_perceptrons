#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16
from __future__ import division # want float and not int division
import numpy as np
import random as random
from input import letters_list_training

eta = 0.2 # learning rate is 0.2 for training perceptrons

class perceptron:

    def __init__(self):
        """ Perceptron entity class
        contains bias and weights """
        self.bias =  np.array([random.uniform(-.999999999999, .999999999999)])  # weight0 is the bias, 1 bias per perceptron
        # 16 weights for perceptron, seeded randomly with values from 0-1
        # Total of 17 weights, including the bias
        self.weights = np.array([random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999),
                        random.uniform(-.999999999999, .999999999999), random.uniform(-.999999999999, .999999999999)])

    def test_accuracy(self, p_id):
        """
        Test the accuracy of a perceptron for a given set of inputs
        :param id of perceptron:
        :return: the number of accurate results for a given data set
        """
        num_accurate = 0
        total = 0
        choice_alpha = ""

        # iterate through training data
        for instance in letters_list_training:
            if instance.value in p_id:
                # if instance letter value is in perceptron ID, run test on perceptron using instance
                choice_num = self.test_instance(instance.attributes)

                # choose targets for return from perceptron function
                if choice_num == -1:
                    # perceptron chose p_id[0], map -1 from perceptron to choice 0 in p_id
                    # anytime perceptron returns -1, it chose choice p_id[0]
                    choice_alpha = p_id[0]
                else:
                    # mapping p_id[1] to choice 1
                    choice_alpha = p_id[1]

                # choice matches letter target, test is correct
                if choice_alpha == instance.value:
                    num_accurate += 1
                total += 1
        return num_accurate/total

    def adjust_weights(self, p_id):

        """
        :param p_id:
        :param target:
        :return perceptron output y = sgn(dot product(w,x)):
        train perceptron using weight changes
        for use with stochastic gradient descent
        """
        #print "---Adjust weights---"

        # iterate over the set of instances to find matching values
        for instance in letters_list_training:
            # declare target for instance
            target = int
            if instance.value in p_id:
                # if instance letter value is in perceptron ID, run test on perceptron using instance
                choice_num = self.test_instance(instance.attributes)

                # if instance value is found in p_id[0], target is -1
                # else target is 1
                if instance.value == p_id[0]:
                    target = -1
                else:
                    target = 1

                # choice matches doesn't match target, change weights
                if choice_num != target:
                    self.bias[0] = self.bias[0] + eta * 1 * target # bias input is always +1
                    for i in range(len(self.weights)):
                        self.weights[i] = self.weights[i] + eta * instance.attributes[i] * target
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

    def test_instance(self, inputs):
        """
        :param inputs:
        return output y from perceptron
        y = sgn(dot product(w,x))
        """
        # required to return -1 or 1

        # run test on perceptron and return the output from the perceptron
        # return true if bias + the dot product of weights and inputs is geq 0
        # signum function, tells if the sign of the test is correct
        # print self.bias[0]
        # print np.dot(self.weights, inputs)
        # print len(inputs)
        # print inputs
        result = (self.bias[0] + np.dot(self.weights, inputs) >= 0)
        #np.sign(self.bias[0] + np.dot(self.weights, inputs))
        if(result == True):
            return 1
        else:
            return -1


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
        self.bias = saved_bias.copy()
        self.weights = saved_weights.copy()
        # print dir(saved_bias)
        # print type(saved_bias)
        # print type(saved_weights)
        # # self.weights = saved_weights.copy()
        # # print len(saved_weights)
        # for i in range(0, len(saved_weights)-1):
        #     self.weights[i] = saved_weights[i]
        #print dir(saved_weights)

        return

    def update_weights(self, perceptron):
        """
        set weights if results
        of stochastic descent changes are improving
        """
        self.bias = perceptron.bias.copy()
        self.weights = perceptron.weights.copy()


        return