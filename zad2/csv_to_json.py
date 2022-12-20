import matplotlib.colors as colors
import csv
import json
import os
import pandas as pd


main_df = pd.DataFrame()

for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        main_df = main_df.append(pd.read_csv(file))

main_df.to_csv('colors.csv', index=False)

df = pd.read_csv('colors.csv')
colors_rgb = []
hex_value = df['value'].tolist()

for i in hex_value:
    new_i = colors.hex2color(i)
    colors_rgb.append(new_i)

df['rgb'] = colors_rgb 

df.to_csv('colors.csv') 

with open ("colors.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    data = {"color": []}
    for row in reader:
        data["color"].append({"color name": row[1], "Hex": row[2], "RGB": row[3]})

with open ("colors.json", "w") as file:
    json.dump(data, file, indent=4)

file = 'colors.csv' 

if(os.path.exists(file) and os.path.isfile(file)):
    os.remove(file)