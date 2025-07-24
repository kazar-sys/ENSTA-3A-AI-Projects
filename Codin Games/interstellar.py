# Importation des bibliothèques
import re
from math import sqrt

# Fonctions utiles

# Fonction pour extraire les coefficients des vecteurs
def extraireCoefficients(vecteur_str):
    # Expression régulière modifiée pour capturer les coefficients (y compris les cas +i, -j)
    vecteur_str.replace(" ", "")
    matches = re.findall(r'([+-]?\d*)([ijk])', vecteur_str)
    
    # Dictionnaire pour stocker les coefficients de i, j, k
    coefficients = {'i': 0, 'j': 0, 'k': 0}

    # Boucle pour chaque match trouvé
    for coef, variable in matches:
        # Si le coefficient est vide (ex: +i ou -j), il est égal à 1 ou -1
        if coef == '' or coef == '+':
            coef = 1
        elif coef == '-':
            coef = -1
        else:
            coef = int(coef)
        
        # On met à jour le dictionnaire des coefficients
        coefficients[variable] = coef

    # Retourne les coefficients dans l'ordre (i, j, k)
    return (coefficients['i'], coefficients['j'], coefficients['k'])

# Fonction direction
def direction(a, b):
    return ((b[0] - a[0], b[1] - a[1], b[2] - a[2]))

# Fonction distance
def distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

# Entrées
a = "133i - 6 j -8k"
b = "4i +8j -44 k"

# Application des fonctions
coef_a, coef_b = extraireCoefficients(a), extraireCoefficients(b)
distance = distance(coef_b, coef_a)
direction = direction(coef_a, coef_b)

# Affichages
direction_string = ["-" * (direction[2]<0) + str(direction[0]) + "i", "+" * (direction[1]>0) + "-" * (direction[1]<0) + str(direction[1]) + "j", "+" * (direction[2]>0) + "-" * (direction[2]<0) + str(direction[2]) + "k"]


display_direction = "Direction: " + "".join(direction_string)
display_distance = "Distance: " + str(round(distance, 2))
print(coef_a, coef_b)
print(display_direction)
print(display_distance)