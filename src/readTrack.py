import json
coord = []
with open('data.json') as json_file:  

    data = json.load(json_file)
    for p in data['coordinates']:
    	coord.append(p)
        # print('X: ' + str(p['x']))
        # print('Y: ' + str(p['y']))
        # print('')
print(coord)