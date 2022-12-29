# Program takes UNESCO world heritge sites and plots them on a map,
# colour coding them based on if I have visited them or not. Optional
# lines of code to colour code by "type" of UNESCO site instead.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd


COLOURS_TYPE = {"Cultural": "red", "Natural": "blue", "Mixed": "green"}
COLOURS_VISIT = {0: "red", 1: "black"}
KEY = {0: "Not visited", 1: "Visited"}

# Function for data extraction of UNESCO World Heritage Sites from CSV


def GetData(fileName):
    return pd.read_csv(fileName, header=0, usecols=["category", "longitude", "latitude", "Visit_Status", "name_en"])


# Using geopandas to load world map
countries = gpd.read_file(
    gpd.datasets.get_path("naturalearth_lowres"))


# Reading data from UNESCO file and grouping by visit status
UNESCO_Sites = GetData('visit_status_sites')
grouped_file = UNESCO_Sites.groupby("Visit_Status")

# BY TYPE: grouped_file = UNESCO_Sites.groupby("Category"")


# Initialising Graph
fig, ax = plt.subplots()


# Plotting out world map
countries.plot(color="lightgrey", ax=ax)


# Plotting UNESCO sites, colour-coded by type. Optional add-on which I don't need
# but was interesting anyway Now they are printed by if I have visited them.
# for key, status in grouped_file:
#    status.plot(ax=ax, x="longitude",
#                y="latitude", kind="scatter", label=KEY[key], color=COLOURS_TYPE[key])


for key, status in grouped_file:
    status.plot(ax=ax, x="longitude",
                y="latitude", kind="scatter", label=KEY[key], color=COLOURS_VISIT[key])

plt.title("UNESCO World Heritage Sites")
plt.show()
