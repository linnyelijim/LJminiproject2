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

plots = [df["calories"], df["fat_total_g"], df["protein_g"], df["fiber_g"], df["sugar_g"]]
titles = ["Calories", "Total Fat", "Protein", "Fiber", "Sugar"]

# Loops through chosen dataframe index information
for index, i in enumerate(plots):
    # Creates a pie chart for each index
    i.plot.pie(
        subplots=True,
        legend=True,
        labels=None,
        colors=["#003f5c", "#444e86", "#955196", "#dd5182", "#ff6e54", "#ffa600"], autopct="%.0f%%",
        fontsize=15,
        figsize=(7.5, 6),
        shadow=True,
        explode=(0.15, 0, 0, 0, 0, 0),
        textprops={'color': "w"}
    )
    # Removes index name from graph
    plt.ylabel(
        ''
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
    plt.title(titles[index], fontsize=25)
    # Saves the image into charts
    plt.savefig("charts/"+titles[index]+".png")
    # Shows the graph
    plt.show()

