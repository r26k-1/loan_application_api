from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from sklearn.pipeline import Pipeline
from prediction_model.config import config
import prediction_model.processing.preprocessing as pp
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

classification_pipeline = Pipeline([
    ('MeanImputation', pp.MeanImputer(variables = config.NUM_FEATURES)),
    ('ModeImputation', pp.ModeImputer(variables = config.CAT_FEATURES)),
    ('DomainProcessing', pp.DomainProcessing(config.FEATURE_TO_MODIFY,config.FEATURE_TO_ADD)),
    ('DropFeatures', pp.DropColumns(variables_to_drop=config.DROP_FEATURES)),
    ('LabelEncoder',pp.CustomLabelEncoder(variables=config.FEATURES_TO_ENCODE)),
    ('LogTransform',pp.LogTransform(variables=config.LOG_FEATURES)),
    ('MinMaxScale',MinMaxScaler()),
    ('LogisticClassifier',LogisticRegression(random_state=0))
    ])

