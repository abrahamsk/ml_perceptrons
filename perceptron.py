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
        Test the accuracy of a perceptron for instances matching the letters
         in p_id for perceptron[p_id]
        :param id of perceptron:
        :return: the number of accurate results for a given data set
        """
        num_accurate = 0
        total = 0
        choice_alpha = ""

        # iterate through training data
        for instance in letters_list_training:
            if instance.value[0] in p_id:
                # if instance letter value is in perceptron ID, run test on perceptron using instance
                choice_num = self.test_instance(instance.attributes)
                # choose targets for return from perceptron function
                if choice_num == -1:
                    # perceptron chose p_id[0], map -1 from perceptron to choice 0 in p_id
                    # anytime perceptron returns -1, it chose choice p_id[0]
                    choice_alpha = p_id[0]
                else:
                    # mapping p_id[1] to choice 1
                    # anytime perceptron returns 1, it chose choice p_id[1]
                    choice_alpha = p_id[1]

                # if choice matches letter target, test is correct
                if choice_alpha == instance.value[0]:
                    # increment counter to mark correct result from perceptron
                    num_accurate += 1
                # increment total whether perceptron was correct or not
                # to track total instances
                total += 1
        # return percent correct
        return num_accurate/total


    def adjust_weights(self, p_id):
        """
        :param p_id:
        :param target:
        train perceptron using weight changes
        for use with stochastic gradient descent

        test correctness of perceptron and adjust weights
        if output from perceptron is incorrect
        """
        #print "---Adjust weights---"

        # iterate over the set of instances to find matching values
        for instance in letters_list_training:
            # declare target for instance
            target = int
            if instance.value[0] in p_id:
                # if instance letter value is in perceptron ID, run test on perceptron using instance
                choice_num = self.test_instance(instance.attributes)

                # if instance value is found in p_id[0], target is -1
                # else target is 1
                if instance.value[0] == p_id[0]:
                    target = -1
                else:
                    target = 1

                # perceptron choice matches doesn't match target, change weights
                if choice_num != target:
                    self.bias[0] = self.bias[0] + eta * 1 * target # bias input is always +1
                    for i in range(len(self.weights)):
                        self.weights[i] = self.weights[i] + eta * instance.attributes[i] * target
        return


    def test_instance(self, inputs):
        """
        :param inputs:
        tests one instance for one perceptron
        return output y from perceptron
        y = sgn(dot product(w,x))
        """
        # required to return -1 or 1

        # run test on perceptron and return the output from the perceptron
        # return true if bias + the dot product of weights and inputs is geq 0
        # signum function, tells if the sign of the test is correct

        result = (self.bias[0] + np.dot(self.weights, inputs) >= 0)
        #np.sign(self.bias[0] + np.dot(self.weights, inputs))
        if(result == True):
            return 1
        else:
            return -1


    def update_weights(self, perceptron):
        """
        update weights if results of stochastic descent changes are improving
        (commit the changes to weights that are tested in gradient descent
        once it has been verified that new weights improve accuracy)
        """
        self.bias = perceptron.bias.copy()
        self.weights = perceptron.weights.copy()
        return