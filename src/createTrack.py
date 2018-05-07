import json
import random

data = {}  
data['coordinates'] = [] 
for i in range(10): 
    x= random.randint(10, 100)
    y= random.randint(10, 100)
    data['coordinates'].append({  
        'x': x,
        'y': y,
    })


with open('data.json', 'w') as outfile:  
    json.dump(data, outfile, indent=4)
