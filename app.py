from flask import Flask, jsonify, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

 # Loading model to predict the results
model = pickle.load(open("model.pkl", "rb")) 

@app.route('/')
@app.route('/result', methods = ['GET', 'POST'])
def result():
    
    if request.method == 'GET':
         value= request.args.get('value', None)
         prediction = float(model.predict([[float(value)]]))
         if  value :
             return jsonify(result = prediction)

   #the value 1.8 is hard-coded so simply capture any other numeric value or leave it the way it is
         return "No value entered"

if __name__ == '__main__':
    app.debug = True
    app.run()
