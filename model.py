from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.layers import concatenate, Dense, Input, Dropout
from tensorflow.keras.applications.vgg19 import VGG19

import sys
import os
import numpy as np
from numpy.random import randint
import time
import random


class FVModel():

    def __init__(self, pred_func, layers_to_omit=5):
                
        initial_model = VGG19()
        initial_model = Model(initial_model.input, initial_model.layers[-layers_to_omit].output)
        output = tf.keras.layers.Flatten()(initial_model.output)

        model = Model(initial_model.input, output)

        self.model     = model
        self.pred_func = pred_func

    def predict(self, q, a, b):

        q_fv = self.model.predict(q)
        a_fv = self.model.predict(a)
        b_fv = self.model.predict(b)
        
        return self.pred_func(q_fv, a_fv, b_fv)
    
    def test(self, X, y_true):
        
        right = 0
        total = len(y_true)
                
        for i in range(len(X)):
                
            q = X[i][0]
            a = X[i][1]
            b = X[i][2]
            
            ans = self.predict(q, a, b)
            
            if y_true[i] == ans:
                right += 1
      
        return 100 * (float(right / total))
		
