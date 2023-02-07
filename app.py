import os

import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle


app = Flask(__name__)
#model = pickle.load(open('randomForestRegressor.pkl','rb'))
# OPENAI_KEY = os.environ['OPENAI_KEY']
from gpt3 import call_gpt


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods = ['POST'])
def predict():
    #actual_secret2 = os.environ['OPENAI_KEY']
    #actual_secret3 = os.getenv('OPENAI_KEY')
    #text = [x for x in request.form.values()]
#    prediction = call_gpt(text[0])
    return render_template('result.html', prediction_text=call_gpt())

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
