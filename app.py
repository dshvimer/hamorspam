import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    x = vectorizer.transform(data['inputs'])
    predictions = model.predict(x)
    output = predictions
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)