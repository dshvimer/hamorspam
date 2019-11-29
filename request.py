import requests
url = 'http://localhost:5000/predict'

j = {
    'inputs': [
        'yo dude',
        'free porn'
    ]
}
r = requests.post(url,json=j)
print(r.json())