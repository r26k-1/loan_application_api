import numpy as np
from prediction_model.config import config


class MeanImputer:
  def __init__(self,variables = None):
    self.variables = variables

  def fit(self,X,y=None):
    self.mean_dict = {}
    for col in self.variables:
      self.mean_dict[col] = X[col].mean()
    return self

  def transform(self,X):
    X = X.copy()
    for col in self.variables:
      X[col].fillna(self.mean_dict[col],inplace = True)
    return X


class ModeImputer:
  def __init__(self,variables = None):
    self.variables = variables

  def fit(self,X,y=None):
    self.mode_dict = {}
    for col in self.variables:
      self.mode_dict[col] = X[col].mode()[0]
    return self

  def transform(self,X):
    X = X.copy()
    for col in self.variables:
      X[col].fillna(self.mode_dict[col],inplace = True)
    return X


class DropColumns:
    def __init__(self,variables_to_drop=None):
        self.variables_to_drop = variables_to_drop

    def fit(self,X,y=None):
        return self

    def transform(self,X):
        X = X.copy()
        X = X.drop(columns =self.variables_to_drop)
        return X


class DomainProcessing:
    def __init__(self,variable_to_modify = None , variable_to_add = None):
        self.variable_to_modify = variable_to_modify
        self.variable_to_add = variable_to_add

    def fit(self,X,y=None):
        return self

    def transform(self,X):
        X = X.copy()
        X[self.variable_to_modify] = X[self.variable_to_modify] + X[self.variable_to_add]
        return X


class CustomLabelEncoder:
    def __init__(self,variables = None):
        self.variables = variables

    def fit(self,X,y=None):
        self.label_dict = {}
        for var in self.variables:
            t = X[var].value_counts().sort_values(ascending = True).index
            self.label_dict[var] = {k: i for i,k in enumerate(t,0)}
        return self

    def transform(self,X
    ):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.label_dict[feature])
        return X

#Log transformation
class LogTransform:
    def __init__(self,variables=None):
        self.variables = variables

    def fit(self,X,y=None):
        return self

    def transform(self,X):
        X = X.copy()
        for col in self.variables:
            X[col] = np.log(X[col])
        return X









