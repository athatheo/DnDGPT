import os

import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle


app = Flask(__name__)
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(max_depth=2, random_state=0)
#model = pickle.load(open('randomForestRegressor.pkl','rb'))
# OPENAI_KEY = os.environ['OPENAI_KEY']
from gpt3 import call_gpt


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods = ['POST'])
def predict():
    text = [x for x in request.form.values()]
    prediction = call_gpt(text[0])
    return render_template('result.html', prediction_text=prediction)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)



if __name__ == '__main__':
    app.run(debug=True)