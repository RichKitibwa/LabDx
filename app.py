from flask import Flask
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
    app.debug = True
    app.run()   