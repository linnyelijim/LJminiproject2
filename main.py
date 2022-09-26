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

df["calories"].plot.pie(
    subplots=True,
    legend=True,
    labels=None,
    colors=["pink", "goldenrod", "tan", "bisque", "lemonchiffon", "darkolivegreen"],
    autopct="%.0f%%",
    fontsize=15,
    figsize=(7.5, 6),
    shadow=True,
    explode=(0.15, 0, 0, 0, 0, 0)
)
plt.subplots_adjust(
    left=0.1,
    bottom=0.1,
    right=0.7
)
plt.legend(
    title="Food Item:",
    fontsize=11,
    labels=df["name"],
    bbox_to_anchor=(0.95, 0.95),
    loc="upper right",
    bbox_transform=plt.gcf().transFigure)
plt.title("Calories", fontsize=25)
plt.show()


df["fat_total_g"].plot.pie(
    subplots=True,
    legend=True,
    labels=None,
    colors=["pink", "goldenrod", "tan", "bisque", "lemonchiffon", "darkolivegreen"],
    autopct="%.0f%%",
    fontsize=15,
    figsize=(7.5, 6),
    shadow=True,
    explode=(0.15, 0, 0, 0, 0, 0)
)
plt.subplots_adjust(
    left=0.1,
    bottom=0.1,
    right=0.7
)
plt.legend(
    title="Food Item:",
    fontsize=11,
    labels=df["name"],
    bbox_to_anchor=(0.95, 0.95),
    loc="upper right",
    bbox_transform=plt.gcf().transFigure)
plt.title("Total Fat", fontsize=25)
plt.show()

df["protein_g"].plot.pie(
    subplots=True,
    legend=True,
    labels=None,
    colors=["pink", "goldenrod", "tan", "bisque", "lemonchiffon", "darkolivegreen"],
    autopct="%.0f%%",
    fontsize=15,
    figsize=(7.5, 6),
    shadow=True,
    explode=(0.15, 0, 0, 0, 0, 0)
)
plt.subplots_adjust(
    left=0.1,
    bottom=0.1,
    right=0.7
)
plt.legend(
    title="Food Item:",
    fontsize=11,
    labels=df["name"],
    bbox_to_anchor=(0.95, 0.95),
    loc="upper right",
    bbox_transform=plt.gcf().transFigure)
plt.title("Protein", fontsize=25)
plt.show()

df["fiber_g"].plot.pie(
    subplots=True,
    legend=True,
    labels=None,
    colors=["pink", "goldenrod", "tan", "bisque", "lemonchiffon", "darkolivegreen"],
    autopct="%.0f%%",
    fontsize=15,
    figsize=(7.5, 6),
    shadow=True,
    explode=(0.15, 0, 0, 0, 0, 0)
)
plt.subplots_adjust(
    left=0.1,
    bottom=0.1,
    right=0.7
)
plt.legend(
    title="Food Item:",
    fontsize=11,
    labels=df["name"],
    bbox_to_anchor=(0.95, 0.95),
    loc="upper right",
    bbox_transform=plt.gcf().transFigure)
plt.title("Fiber", fontsize=25)
plt.show()

df["sugar_g"].plot.pie(
    subplots=True,
    legend=True,
    labels=None,
    colors=["pink", "goldenrod", "tan", "bisque", "lemonchiffon", "darkolivegreen"],
    autopct="%.0f%%",
    fontsize=15,
    figsize=(7.5, 6),
    shadow=True,
    explode=(0.15, 0, 0, 0, 0, 0)
)
plt.subplots_adjust(
    left=0.1,
    bottom=0.1,
    right=0.7
)
plt.legend(
    title="Food Item:",
    fontsize=11,
    labels=df["name"],
    bbox_to_anchor=(0.95, 0.95),
    loc="upper right",
    bbox_transform=plt.gcf().transFigure)
plt.title("Sugar", fontsize=25)
plt.show()