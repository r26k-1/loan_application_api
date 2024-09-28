import pickle
import json
import os
import numpy as np

# Define the function to load artifacts
def load_artifacts(artifacts_dir):
    # List of files
    model_file = os.path.join(artifacts_dir, 'modellog.pkl')
    scaling_file = os.path.join(artifacts_dir, 'minmaxscaler.pkl')
    columns_file = os.path.join(artifacts_dir, 'columns.json')

    # Load the model
    with open(model_file, 'rb') as f:
        model = pickle.load(f)
    
    # Load the scaling object
    with open(scaling_file, 'rb') as f:
        scaling = pickle.load(f)

    # Load data columns
    with open(columns_file) as f:
        data_columns = json.load(f)['features']
    
    return model, scaling, data_columns

# Define the prediction function
def predict(gender, married, dependents, education, selfemployed, 
            applicantincome, loanamount, loanamountterm, 
            credithistory, propertyarea, _model, _scaling):
    
    # Encode categorical features
    gender_encode = lambda x: 0 if x == 'Female' else 1
    married_encode = lambda x: 0 if x == 'No' else 1
    dependents_encode = lambda x: 0 if x == '0' else 1 if x == '1' else 2 if x == '2' else 3
    education_encode = lambda x: 0 if x == 'Graduate' else 1
    self_employed_encode = lambda x: 0 if x == 'No' else 1
    property_area_encode = lambda x: 0 if x == 'Rural' else 1 if x == 'Semiurban' else 2
    
    gender = gender_encode(gender)
    married = married_encode(married)
    dependents = dependents_encode(dependents)
    education = education_encode(education)
    selfemployed = self_employed_encode(selfemployed)
    credithistory = credithistory
    propertyarea = property_area_encode(propertyarea)
    
    # Log transform numerical features
    applicantincome_log = np.log(applicantincome)
    loanamount_log = np.log(loanamount)
    loanamountterm_log = np.log(loanamountterm)
    
    # Combine all features into a single array
    input_data = np.array([[gender, married, dependents, education, selfemployed, 
                            applicantincome_log, loanamount_log, loanamountterm_log, 
                            credithistory, propertyarea]])

    # Apply scaling to the entire input data
    input_data_scaled = _scaling.transform(input_data)

    # Predict using the loaded model
    prediction = _model.predict(input_data_scaled)
    
    return prediction
