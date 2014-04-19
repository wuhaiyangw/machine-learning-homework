#!/usr/bin/env python
#-*-coding:utf8-*-
'''
Created on 2014-4-20

@author: wuhaiyangw@gmail.com

@brief: for file process
'''


import sys

def split_data(splits, test_split, data):
    """Split data into 'splits' different sub-blocks,
    returning theblock indexed by 'test_split'
    plus the rest of the data."""

    assert test_split >= 0 and test_split < splits
    assert splits <= len(data)

    split_size = len(data) / int(splits)
    test_start = split_size*test_split
    test_end   = test_start + split_size

    test  = data[test_start:test_end]
    train = numpy.concatenate([data[0:test_start],data[test_end:]])

    return (train,test)
