import pickle
from flask import Flask , request , app , jsonify , url_for , render_template 
import numpy as np
import pandas as pd
import sklearn

app = Flask(__name__)
## Load the model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))#read byte mode
scaler  = pickle.load(open('scaling.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('main.html')



@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    return render_template('main.html' ,prediction_text = f"The House Price Prediction is {output}")



@app.route('/predict' , methods = ['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
    print(output)
    return jsonify(output)

if __name__ =='__main__':
    app.run(debug=True)

