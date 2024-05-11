
import requests
import json
import pandas as pd

data = pd.read_csv('IndianHealthyRecipe.csv')

for i in range(len(data['Dish Name'])):
    dish = data['Dish Name'][i]
    spice = data['Spice'][i]
    if spice == 'medium' and 'VEGETARIAN' in data['Dietary Info'][i]:
        # Prep 10 mins
        # to thiis: 10 (int)
        prep_time = data['Prep Time'][i].replace('mins','').replace('Prep','').strip()
        
        # convert to integer
        prep_time = int(prep_time)
        print(f"[🕒 {prep_time}] 🍔 {dish} {spice.replace('medium','🌶️')} {data['Dietary Info'][i]}")
