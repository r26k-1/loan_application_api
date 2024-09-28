import pandas as pd
import numpy as np

from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

import joblib
from prediction_model.processing.datahandling import load_dataset,load_pipeline
from prediction_model.config import config

classification_pipeline = load_pipeline(config.MODEL_NAME)


def generate_prediction(data_input):
    data = pd.DataFrame(data_input)
    pred = classification_pipeline.predict(data[config.FEATURES])
    output = np.where(pred == 1, "Y" , "N")
    result = {"prediction" : output}
    return result


'''
def generate_prediction():
    test_data = load_dataset(config.TEST_FILE)
    pred = classification_pipeline.predict(test_data[config.FEATURES])
    output = np.where(pred == 1, "Y" , "N")
    print(output)
    #result = {"prediction" : output}
    #return result
'''

if __name__=='__main__':
    generate_prediction()