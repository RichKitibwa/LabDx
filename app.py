from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

 # Loading model to predict the results
model = pickle.load(open("model.pkl", "rb")) 

@app.route('/result', methods = [ 'POST'])
def result():
    
    if request.method == 'POST':
         req_data = request.get_json()
         value= req_data['value']
         prediction = float(model.predict([[float(value)]]))
         if  value :
             return jsonify(result = prediction)
             
         return "No value entered"

if __name__ == '__main__':
    app.debug = True
    app.run()
