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

df['calories'].plot.pie(
    ylabel=None,
    subplots=True,
    legend=True,
    labels=df['name'],
    colors=["pink", "goldenrod", "tan", "bisque", "lemonchiffon", "darkolivegreen"],
    autopct="%.2f",
    fontsize=15,
    figsize=(9, 5),
    shadow=True,
    explode=(0.15, 0, 0, 0, 0, 0)
)
plt.subplots_adjust(
    left=0.1,
    bottom=0.1,
    right=0.7)
plt.legend(
    title="Food Item:",
    fontsize=11,
    bbox_to_anchor=(0.95, 0.95),
    loc="upper right",
    bbox_transform=plt.gcf().transFigure)
plt.title("Calories", fontsize=25)
plt.show()
