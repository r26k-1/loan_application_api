from flask import Flask, render_template, request
from util import load_artifacts, predict

app = Flask(__name__)

# Load your artifacts (model, scaler, etc.)
artifacts_dir = "C:/Users/OWNER/Documents/complete mlops"  # Update to your path
_model, _scaling, _data_columns = load_artifacts(artifacts_dir)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method == 'POST':
        # Get form data
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        selfemployed = request.form['selfemployed']
        applicantincome = float(request.form['applicantincome'])
        loanamount = float(request.form['loanamount'])
        loanamountterm = float(request.form['loanamountterm'])
        credithistory = float(request.form['credithistory'])
        propertyarea = request.form['propertyarea']

        # Call the predict function with model and scaler
        prediction = predict(gender, married, dependents, education, selfemployed,
                             applicantincome, loanamount, loanamountterm, 
                             credithistory, propertyarea, _model, _scaling)

        result = 'Approved' if prediction[0] == 1 else 'Not Approved'
        return render_template('result.html', prediction=result)

@app.route('/features')
def features():
    feature_list = [
        "1. Gender: Male or Female",
        "2. Married: Yes or No",
        "3. Dependents: Number of dependents",
        "4. Education: Graduate or Not Graduate",
        "5. Self Employed: Yes or No",
        "6. Applicant Income: Income of the applicant",
        "7. Loan Amount: Amount of loan requested",
        "8. Loan Amount Term: Duration of the loan in months",
        "9. Credit History: 1.0 for good credit history, 0.0 for bad credit history",
        "10. Property Area: Urban, Semiurban, or Rural"
    ]
    return render_template('features.html', features=feature_list)

@app.route('/loan-status')
def loan_status():
    return render_template('loan_status.html')

if __name__ == '__main__':
    app.run(debug=True)
