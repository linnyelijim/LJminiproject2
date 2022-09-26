# INF601 - Advanced Programming in Python
# Lindsey Jimenez
# Mini Project 2

import pandas as pd
import requests
import matplotlib.pyplot as plt

# Pulling the API data set from api-ninjas
query = 'Chickpea, Sweet Potato, Quinoa, Yellow Onion, Red Pepper, Hummus, and Kale'
api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
response = requests.get(api_url, headers={'X-Api-Key': 'AhHrFOWAF95xn1IcbTAkpw==cl8yizGZUtZHtWLL'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)

# Stores information in Pandas dataframe and assigns it to var df
df = pd.read_json(response.text)

# Prints entire specified data set
print(df)

# Creates Pie Chart for calories
df["calories"].plot.pie(
    subplots=True,
    legend=True,
    labels=None,
    colors=["#003f5c", "#444e86", "#955196", "#dd5182", "#ff6e54", "#ffa600"],    autopct="%.0f%%",
    fontsize=15,
    figsize=(7.5, 6),
    shadow=True,
    explode=(0.15, 0, 0, 0, 0, 0),
    textprops={'color': "w"}
)
# Adjusts plot positioning
plt.subplots_adjust(
    left=0.1,
    bottom=0.1,
    right=0.7
)
# Modifies the legend placement and information
plt.legend(
    title="Food Item:",
    fontsize=11,
    labels=df["name"],
    bbox_to_anchor=(0.95, 0.95),
    loc="upper right",
    bbox_transform=plt.gcf().transFigure
)
# Creates title for the graph
plt.title("Calories", fontsize=25)
# Shows the graph
plt.show()

# Creates Pie Chart for total fat
df["fat_total_g"].plot.pie(
    subplots=True,
    legend=True,
    labels=None,
    colors=["#003f5c", "#444e86", "#955196", "#dd5182", "#ff6e54", "#ffa600"],
    autopct="%.0f%%",
    fontsize=15,
    figsize=(7.5, 6),
    shadow=True,
    explode=(0, 0, 0, 0, 0.15, 0),
    textprops={'color': "w"}
)
# Adjusts plot positioning
plt.subplots_adjust(
    left=0.1,
    bottom=0.1,
    right=0.7
)
# Modifies the legend placement and information
plt.legend(
    title="Food Item:",
    fontsize=11,
    labels=df["name"],
    bbox_to_anchor=(0.95, 0.95),
    loc="upper right",
    bbox_transform=plt.gcf().transFigure
)
# Creates title for the graph
plt.title("Total Fat", fontsize=25)
# Shows the graph
plt.show()

# Creates Pie Chart for protein
df["protein_g"].plot.pie(
    subplots=True,
    legend=True,
    labels=None,
    colors=["#003f5c", "#444e86", "#955196", "#dd5182", "#ff6e54", "#ffa600"],    autopct="%.0f%%",
    fontsize=15,
    figsize=(7.5, 6),
    shadow=True,
    explode=(0.15, 0, 0, 0, 0, 0),
    textprops={'color': "w"}
)
# Adjusts plot positioning
plt.subplots_adjust(
    left=0.1,
    bottom=0.1,
    right=0.7
)
# Modifies the legend placement and information
plt.legend(
    title="Food Item:",
    fontsize=11,
    labels=df["name"],
    bbox_to_anchor=(0.95, 0.95),
    loc="upper right",
    bbox_transform=plt.gcf().transFigure
)
# Creates title for the graph
plt.title("Protein", fontsize=25)
# Shows the graph
plt.show()

# Creates Pie Chart for fiber
fiber = df["fiber_g"].plot.pie(
    subplots=True,
    legend=True,
    labels=None,
    colors=["#003f5c", "#444e86", "#955196", "#dd5182", "#ff6e54", "#ffa600"],    autopct="%.0f%%",
    fontsize=15,
    figsize=(7.5, 6),
    shadow=True,
    explode=(0.15, 0, 0, 0, 0, 0),
    textprops={'color': "w"}
)
# Adjusts plot positioning
plt.subplots_adjust(
    left=0.1,
    bottom=0.1,
    right=0.7
)
# Modifies the legend placement and information
plt.legend(
    title="Food Item:",
    fontsize=11,
    labels=df["name"],
    bbox_to_anchor=(0.95, 0.95),
    loc="upper right",
    bbox_transform=plt.gcf().transFigure
)
# Creates title for the graph
plt.title("Fiber", fontsize=25)
# Shows the graph
plt.show()

# Creates Pie Chart for sugar
df["sugar_g"].plot.pie(
    subplots=True,
    legend=True,
    labels=None,
    colors=["#003f5c", "#444e86", "#955196", "#dd5182", "#ff6e54", "#ffa600"],    autopct="%.0f%%",
    fontsize=15,
    figsize=(7.5, 6),
    shadow=True,
    explode=(0, 0.15, 0, 0, 0, 0),
    textprops={'color': "w"}
)
# Adjusts plot positioning
plt.subplots_adjust(
    left=0.1,
    bottom=0.1,
    right=0.7
)
# Modifies the legend placement and information
plt.legend(
    title="Food Item:",
    fontsize=11,
    labels=df["name"],
    bbox_to_anchor=(0.95, 0.95),
    loc="upper right",
    bbox_transform=plt.gcf().transFigure)
# Creates title for the graph
plt.title("Sugar", fontsize=25)
# Shows the graph
plt.show()
