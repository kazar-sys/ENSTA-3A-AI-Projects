# But du puzzle : faire exploser les bombes A, B et H en mettant la force d'explosion maximum que chaque case de l'espace encaisse.
# Pour la bombe A : force 3 une case autour d'elle, force 2 deux cases autour d'elle, force 1 trois cases autour d'elle.
# Pour la bombe H : force 5 pour toutes les cases situées autour à trois cases.
# Pour la bombe B : force 3 puis 2 puis 1 au-dessus, en-dessous, à gauche et à droite. N'explose que si une autre bombe la fait exploser.

# Entrées
n = 15
space = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, "A", 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, "B", 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# On parcourt l'espace pour changer la bombe B en B0, on mettra B1 au fur et à mesure si elle est touchée et donc si elle explose.
for i in range(n):
    for j in range(n):
        if space[i][j] == "B":
            space[i][j] = "B0"


### Fonctions utiles 

def isValid(i, j, n): # Définit si une position rentre dans la taille de l'espace
    return (0 <= i < n) and (0 <= j < n)


### Coeur du programme

# Double boucle pour parcourir tout l'espace, changer les valeurs autour de chaque case munie d'une bombe
for i in range(n):
    for j in range(n):
        if space[i][j] == "H":
            for k in range(-3, 4):
                for l in range(-3, 4):
                    if isValid(i+l, j+k, n) and isinstance(space[i+l][j+k], int):
                        space[i+l][j+k] = max(5, space[i+l][j+k])
                    elif isValid(i+l, j+k, n) and space[i+l][j+k] == "B0":
                        space[i+l][j+k] = "B1"
        elif space[i][j] == "A":
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if isValid(i+l, j+k, n) and isinstance(space[i+l][j+k], int):
                        space[i+l][j+k] = max(3, space[i+l][j+k])
                    elif isValid(i+l, j+k, n) and space[i+l][j+k] == "B0":
                        space[i+l][j+k] = "B1"
            for k in range(-2, 3, 4):
                for l in range(-2, 3):
                    if isValid(i+l, j+k, n) and isinstance(space[i+l][j+k], int):
                        space[i+l][j+k] = max(2, space[i+l][j+k])
                    elif isValid(i+l, j+k, n) and space[i+l][j+k] == "B0":
                        space[i+l][j+k] = "B1"
            for k in range(-2, 3):
                for l in range(-2, 3, 4):
                    if isValid(i+l, j+k, n) and isinstance(space[i+l][j+k], int):
                        space[i+l][j+k] = max(2, space[i+l][j+k])
                    elif isValid(i+l, j+k, n) and space[i+l][j+k] == "B0":
                        space[i+l][j+k] = "B1"
            for k in range(-3, 4, 6):
                for l in range(-3, 4):
                    if isValid(i+l, j+k, n) and isinstance(space[i+l][j+k], int):
                        space[i+l][j+k] = max(1, space[i+l][j+k])
                    elif isValid(i+l, j+k, n) and space[i+l][j+k] == "B0":
                        space[i+l][j+k] = "B1"
            for k in range(-3, 4):
                for l in range(-3, 4, 6):
                    if isValid(i+l, j+k, n) and isinstance(space[i+l][j+k], int):
                        space[i+l][j+k] = max(1, space[i+l][j+k])
                    elif isValid(i+l, j+k, n) and space[i+l][j+k] == "B0":
                        space[i+l][j+k] = "B1"

# On reparcourt pour transformer les bombes B0 en B qui n'ont pas explosé, et pour gérer les bombes B1 qui ont explosé.
for i in range(n):
    for j in range(n):
        if space[i][j] == "B1":
            for k in range(1, 4):
                if isValid(i-k, j, n) and isinstance(space[i-k][j], int):
                        space[i-k][j] = max(4-k, space[i-k][j])
            for k in range(1, 4):
                if isValid(i+k, j, n) and isinstance(space[i+k][j], int):
                        space[i+k][j] = max(4-k, space[i+k][j])
            for k in range(1, 4):
                if isValid(i, j-k, n) and isinstance(space[i][j-k], int):
                        space[i][j-k] = max(4-k, space[i][j-k])
            for k in range(1, 4):
                if isValid(i, j+k, n) and isinstance(space[i][j+k], int):
                        space[i][j+k] = max(4-k, space[i][j+k])
            space[i][j] = "B"
        elif space[i][j] == "B0":
            space[i][j] = "B"

### Print final
for i in range(n):
    for j in range(n):
        space[i][j] = str(space[i][j])

for line in space:
    print("".join(line))