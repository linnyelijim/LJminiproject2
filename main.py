# INF601 - Advanced Programming in Python
# Lindsey Jimenez
# Mini Project 2

import pandas as pd
import requests
import matplotlib.pyplot as plt


query = 'Chickpea, Sweet Potato, Quinoa, Yellow Onion, Red Pepper, Hummus, and Kale'
api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
response = requests.get(api_url, headers={'X-Api-Key': 'AhHrFOWAF95xn1IcbTAkpw==cl8yizGZUtZHtWLL'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)

df = pd.read_json(response.text)
print(df)

