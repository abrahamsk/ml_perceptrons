#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16

max_letter_attribute_val = 15

class letter:
    """Letter entity class"""
    value = None # alphabet letter
    attributes = []  # 16 numerical attributes for a letter from the data set

    def __init__(self, input):
        self.value = input[:1]
        self.attributes = map(float, input[1:])
        # scale each data value to be between 0 and 1 by dividing by 15 (max val = 15)
        self.attributes = [i/max_letter_attribute_val for i in self.attributes]