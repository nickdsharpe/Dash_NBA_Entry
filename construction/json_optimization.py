import pandas as pd
import json

with open(f'../game_data/team_one/Offense/Murray.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
        
df = pd.DataFrame(file).transpose()

print(df)