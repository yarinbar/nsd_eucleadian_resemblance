
import sys
import os
import numpy as np
from numpy.random import randint
import PIL
from PIL import Image
import time
import random



"""
DATASET DIRECTORY STRUCTURE

dataset
    cat1
        img1
        img2
        .
        .
        .
        imgk
        
    cat2
    cat3
    .
    .
    .
    catk
"""

class Dataset:
    
    def _extract(self):
        """
        returns a list of lists. each list contain images of the same category
        """
        
        category_list  = []
        category_names = os.listdir(self.ds_path)
        
        for category_name in category_names:
            category_path = os.path.join(self.ds_path, category_name)
            
            # we cant iterate files
            if os.path.isfile(category_path):
                continue
            
            category = [] 
            img_list = os.listdir(category_path)

            for img_name in img_list:
                img_path = os.path.join(category_path, img_name)
                img = Image.open(img_path)
                img = np.asarray(img)
                
                category.append(img)
            
            category_list.append(category)
            
        return category_list
    
    @staticmethod
    def generate_questions(question_cat, wrong_cat):
        """
        takes a list of images from the same category for the question and the right answer
        and also takes other categories list to add a wrong answer
        """
        
        questions = []
        y_true    = []
        
        for i in range(len(question_cat)):
            q_img = question_cat[i]
            
            for category in wrong_cat:
                for wrong_img in category:
                    
                    # we avoid choosing the same image as the question
                    right_img_index = random.choice(list(range(0, i)) + list(range(i + 1, len(question_cat))))
                    right_img = question_cat[right_img_index]
                    
                    if randint(0, 2) % 2 == 0:
                        questions.append((q_img, right_img, wrong_img))
                        y_true.append(0)
                    else:
                        questions.append((q_img, wrong_img, right_img))
                        y_true.append(1)
        
        return questions, y_true
                
    
    @staticmethod
    def create_ds(category_list):
        """
        returns a list of questions (X) that are composed of (q_img, a_img, b_img) either a 
        or b are the correct answer.
        also returns y_true which tells the model which one was the right answer
        """
        
        X      = []
        y_true = []
        
        for i in range(len(category_list)):
            
            right_cat = category_list[i]
            wrong_cat = category_list[:i] + category_list[i + 1:]
            
            X_cat, y_true_cat = Dataset.generate_questions(right_cat, wrong_cat)
            
            X      += X_cat
            y_true += y_true_cat
        
        # seed is 1024 for same shuffling
        random.Random(1024).shuffle(X)
        random.Random(1024).shuffle(y_true)
        
        return X, y_true
    
    def __init__(self, ds_path):
        
        self.ds_path = ds_path
        
        category_list = self._extract()
        self.X, self.y_true = self.create_ds(category_list)
        
        # self.X[0][0] is q_img of the first question
        # self.X[0][1] is a_img of the first question
        # self.X[0][2] is b_img of the first question




