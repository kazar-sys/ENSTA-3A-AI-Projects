# Bibliothèques
import time

# Données

# Parcours du cavalier
parcours = [
    (0, 0, 42), (2, 1, 13), (4, 0, 35), (6, 1, 28), (4, 2, 14), (6, 3, 39), (7, 1, 19), (5, 0, 29), 
    (6, 2, 33), (7, 0, 55), (5, 1, 41), (3, 0, 18), (1, 1, 34), (0, 3, 17), (2, 2, 40), (4, 3, 26), 
    (3, 1, 56), (1, 0, 38), (0, 2, 53), (2, 3, 36), (0, 4, 8), (2, 5, 49), (1, 7, 23), (0, 5, 4), 
    (1, 3, 15), (0, 1, 32), (2, 0, 27), (3, 2, 31), (2, 4, 21), (3, 6, 5), (4, 4, 63), (6, 5, 22), 
    (7, 7, 6), (5, 6, 60), (3, 7, 3), (1, 6, 51), (3, 5, 58), (1, 4, 12), (0, 6, 45), (2, 7, 10), 
    (1, 5, 62), (0, 7, 59), (2, 6, 64), (4, 7, 50), (6, 6, 9), (7, 4, 57), (5, 5, 7), (3, 4, 46), 
    (4, 6, 24), (6, 7, 61), (7, 5, 47), (5, 4, 1), (7, 3, 30), (5, 2, 20), (6, 0, 16), (7, 2, 44), 
    (6, 4, 52), (7, 6, 2), (5, 7, 48), (4, 5, 11), (5, 3, 54), (4, 1, 37), (3, 3, 43), (1, 2, 25)
]

# Taille de la grille
n = 8

# Somme demandée pour chaque colonne et chaque ligne
target = 1442

# Génération de la grille avec les valeurs
grid = [element[2] for element in sorted(parcours, key=lambda x: (x[0], x[1]))]
grid = [grid[i:(i+n)] for i in range(0, len(grid), n)]


# Fonctions utiles

# Effectuer les sommes des lignes et des colonnes et les ajouter à la grille en fin de ligne et en fin de colonne
def sums(grid):

    sommes = list()

    # Sommes des lignes
    for i in range(n):
        sommes.append(sum(grid[i]))
    
    # Sommes des colonnes
    for j in range(n):
        to_append = 0
        for i in range(n):
            to_append += grid[i][j]
        sommes.append(to_append)
    
    for i in range(n):
        grid[i].append(sommes[i])

    new_line = list()
    for i in range(n):
        new_line.append(sommes[n+i])
    
    grid.append(new_line)
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = str(grid[i][j]) 

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += " " * (len(grid[i][-1]) - len(grid[i][j]) + 1)

    return grid

# Compléter la grille avec les bonnes valeurs
def completeGrid(target, grid, n):
    
    all_cases = int((target - 260) / n)
    diag_cases = (target - 260) % n

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += all_cases
            if i == j:
                grid[i][j] += diag_cases
    
    return grid

# Applications

# Complétion de la grille
grid = completeGrid(target, grid, n)

# Génération de la nouvelle grille aveec les sommes
new_grid = sums(grid)

# Affichages

# Affichages de chaque case remplie successivement
empty_grid = [[("X" + " " * (len(str(target))-1)) for _ in range(n)] for _ in range(n)]
for i in range(n**2):
    empty_grid[parcours[i][0]][parcours[i][1]] = str(grid[parcours[i][0]][parcours[i][1]]) 
    for line in empty_grid:
        print(" ".join(line))
    print("\n")
    time.sleep(2)

# Affichage de la grille finale avec les sommes
for line in new_grid:
    print("".join(line))
