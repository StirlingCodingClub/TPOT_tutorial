from tpot import TPOTClassifier
import pandas as pd
import os
from sklearn import preprocessing

# Set project folder as working folder
os.chdir('/home/thiago/Projects/TPOT_tutorial/')

# Read in csv data using pandas, letting it know there are no variable names
covtype = pd.read_csv('./data/cov_type/covtype.data', header=None)

covtype.head()

covtype.tail()

covtype.shape

covtype.dtypes

# Indexing in pandas is a little different from R
# df[] only takes column names
# df.loc[] only takes row names
# REMEMBER THE ZERO INDEXING!

# We use .values to get an array instead of a series
covtype_pred = covtype.iloc[:,0:53].values

covtype_pred.shape

covtype_target = covtype.iloc[:,54].values

covtype_target.shape

