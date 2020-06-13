from flask import Flask
import os
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

@app.route("/")
def result():
    # Loading model to predict the results
   model = pickle.load(open("model.pkl", "rb")) 
   #the value 1.8 is hard-coded so simply capture any other numeric value or leave it the way it is
   return str(model.predict([[1.8]]))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    app.debug = True
    app.run()   