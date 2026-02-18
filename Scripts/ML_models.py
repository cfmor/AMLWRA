#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Feb 17 16:16:00 2026

@author: cfmor

This script is part of the PhD Project: "Application of Machine Learning to Wind Resource Assessment". 


"""



#%% Packages and functions

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns

#%% Specific sci-kit learn functions

from sklearn.preprocessing import StandardScaler, add_dummy_feature, RobustScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import (train_test_split, 
                                     RandomizedSearchCV, 
                                     ShuffleSplit, 
                                     TimeSeriesSplit)
from sklearn.ensemble import (RandomForestRegressor,
                              KNeighborsRegressor,
                              ExtraTreesRegressor,
                              AdaBoostRegressor,
                              GradientBoostingRegressor, 
                              VotingRegressor)
from sklearn.neural_network import MLPRegressor


#%% Retrieving data.

# Define the path to the data directory
data_dir = os.path.join(os.getcwd(), 'data')

