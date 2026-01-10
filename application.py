import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)
app=application


# importing ridge regressor model and standardscaler pickle files

ridge_model=pickle.load(open('model/ridge.pkl','rb'))
standard_scaler=pickle.load(open('model/scaler.pkl','rb'))

#Route for home page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/model',methods=['GET','POST'])
def model():
    if request.method=='POST':
        # Get input values from the form
        input_values = [float(x) for x in request.form.values()]
        # Scale the input values
        scaled_input = standard_scaler.transform([input_values])
        # Make prediction
        prediction = ridge_model.predict(scaled_input)
        return render_template('model.html', prediction=prediction[0])
    return render_template('model.html')
if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)