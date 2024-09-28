import os
import pathlib

#import sys
#print(sys.path)
#sys.path.append('D:\\MLModelPackaging\\pack-ml-model')

#in cmd -
#set PYTHONPATH=%PYTHONPATH%;D:\MLModelPackaging\pack-ml-model

import prediction_model
PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent
#print(PACKAGE_ROOT)

DATAPATH = os.path.join(PACKAGE_ROOT,"datasets")
#print(DATAPATH)

TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'

MODEL_NAME = 'classification.pkl'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,"trained_models")
#print(SAVE_MODEL_PATH)

TARGET = 'Loan_Status'

FEATURES = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']

NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']
CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Credit_History','Property_Area']

#in our case its same as categorical features
FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed','Credit_History', 'Property_Area']

FEATURE_TO_MODIFY = 'ApplicantIncome'
FEATURE_TO_ADD = 'CoapplicantIncome'
DROP_FEATURES = ['CoapplicantIncome']

LOG_FEATURES = ['ApplicantIncome', 'LoanAmount']




