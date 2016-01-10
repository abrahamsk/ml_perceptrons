#!/usr/bin/env python

# Machine Learning 445
# HW 1: Perceptrons
# Katie Abrahams, abrahake@pdx.edu
# 1/19/16

class letter:
    """Letter entity class"""
    letter = None
    attributes = []  # 16 numerical attributes for a letter from the dataset

    def __init__(self, input):
        self.letter = input[0]
        self.attributes = input[1-15]
