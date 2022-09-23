from locale import normalize
import pandas as pd
import matplotlib.pyplot as plt
import os

data_file = "_data/gdp_csv.csv"
normalizeAmount = 1_000_000_000_000

df = pd.read_csv(data_file)
print(df.head())

fix, ax = plt.subplots()
usa = df[df['Country Code'] == 'USA']
china = df[df['Country Code'] == 'CHN']
ax.plot(usa['Year'], usa['Value'] / normalizeAmount)
ax.plot(china['Year'], china['Value'] / normalizeAmount)
ax.set_title("USA and China GDP: 1960-2020")

