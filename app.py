from flask import Flask, jsonify
#import os
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

 # Loading model to predict the results
model = pickle.load(open("model.pkl", "rb")) 

@app.route('/')
def result():
   
   #the value 1.8 is hard-coded so simply capture any other numeric value or leave it the way it is
   return jsonify(float(model.predict([[1.8]])))

if __name__ == '__main__':
    app.debug = True
    #port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0')
