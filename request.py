import requests
url = 'http://localhost:5000/predict'

inputs= [
        'yo dude',
        'free porn',
        'hot xxx'
    ]
j = {
    'inputs': inputs
}
print("Inputs: ", inputs)
r = requests.post(url,json=j)
print(r.json())