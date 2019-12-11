from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.layers import concatenate, Dense, Input, Dropout
from tensorflow.keras.applications.vgg19 import VGG19

import sys
import os
import numpy as np
import pandas as pd
from numpy.random import randint
import PIL
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
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
		
def get_testing_data(img_path, csv_path):
    
    data   = []
    y_true = []
    
    print("fetching data")
    
    df = pd.read_csv(csv_path, header=None)
    
    for i in range(4096): 
            
        question = df.iloc[i * 9:(i + 1) * 9]
        target = question.iloc[0][0]
        
        q_img  = Image.open(os.path.join(img_path, "{}.png".format(target)))
        q_img  = np.asarray(q_img)
        q_img  = np.expand_dims(q_img, axis=0)
        q_tag  = target[:8]
        
        same_imgs = question[question[1].str.contains(q_tag)].values
        diff_imgs = question[~question[1].str.contains(q_tag)].values
        
        for j in range(min(len(same_imgs), len(diff_imgs))):
            
            right_ans = Image.open(os.path.join(img_path, "{}.png".format(same_imgs[j][0])))
            right_ans = np.asarray(right_ans)
            right_ans = np.expand_dims(right_ans, axis=0)
            
            wrong_ans = Image.open(os.path.join(img_path, "{}.png".format(diff_imgs[j][0])))
            wrong_ans = np.asarray(wrong_ans)
            wrong_ans = np.expand_dims(wrong_ans, axis=0)
            
            order = randint(0, 2)
            
            if order % 2 == 0:
                data.append((q_img, right_ans, wrong_ans))
                y_true.append(0)
            
            else:
                data.append((q_img, wrong_ans, right_ans))
                y_true.append(1)

    
    # seed is 1024 for same shuffling
    random.Random(1024).shuffle(data)
    random.Random(1024).shuffle(y_true)
    
    return data, y_true

	
