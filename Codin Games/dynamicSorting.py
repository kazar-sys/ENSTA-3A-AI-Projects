expression = '+age-name'
types = 'int,string'
n = 6
rows = [
    'id:1,name:hugo,age:1',
    'id:2,name:maria,age:12',
    'id:3,name:jason,age:2',
    'id:4,name:amit,age:15',
    'id:5,name:maria,age:6',
    'id:6,name:robert,age:12'
]

import re

matches = re.findall(r'([-+])(\w+)', expression)

order = [[match[0], match[1]] for match in matches]

for key in order:
    if key[0] == '+':
        key[0] = False
    else:
        key[0] = True

data = list()
for row in rows:
    # Diviser la chaîne par les virgules pour séparer les paires clé-valeur
    pairs = row.split(',')
    
    # Initialiser un dictionnaire pour stocker les données de la ligne actuelle
    row_dict = {}
    
    for pair in pairs:
        # Diviser chaque paire clé-valeur par les deux-points
        key, value = pair.split(':')
        
        # Convertir l'ID en entier
        if value.isdigit():
            value = int(value)
        
        # Ajouter la paire clé-valeur au dictionnaire
        row_dict[key] = value
    
    # Ajouter le dictionnaire résultant à la liste des résultats
    data.append(row_dict)

from operator import itemgetter

def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=itemgetter(key), reverse=reverse)
    return xs


sorted_data = multisort(data, order)

print(sorted_data)

for people in sorted_data:
    print(people['id'])

