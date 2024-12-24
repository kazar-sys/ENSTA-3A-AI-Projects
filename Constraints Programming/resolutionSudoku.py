from sys import exit, argv
import time

# teste si la grille contient une erreur
def estContradictoire(liste):
    chiffres = set(liste) - {0}
    for c in chiffres:
        if liste.count(c) != 1:
            return True
    return False

# renvoie la liste des valeurs possibles pour une case
def casePossibles(case, sudoku):
    chiffres = set(sudoku[case[0]])
    chiffres |= {sudoku[i][case[1]] for i in range(9)}
    cellule = case[0] // 3, case[1] // 3
    for i in range(3):
        chiffres |= set(sudoku[cellule[0]*3 + i][cellule[1]*3:(cellule[1]+1)*3])
    return list(set(range(1, 10)) - chiffres)

try:
    fichier = argv[1]
except IndexError:
    print("Usage : " + argv[0] + " fichier.txt")
    exit(0)

sudoku = []
trous = []

# Temps de début d'algorithme
t_start = time.time()
try:
    with open(fichier, "r") as f:
        for nl, ligne in enumerate(f):
            try:
                nouvelle = [int(i) for i in list(ligne.strip())]
            except ValueError:
                print("La ligne " + str(nl+1) + " contient autre chose qu'un chiffre.")
                exit(1)
            if len(nouvelle) != 9:
                print("La ligne " + str(nl+1) + " ne contient pas 9 chiffres.")
                exit(1)
            trous += [[nl, i] for i in range(9) if nouvelle[i] == 0]
            sudoku.append(nouvelle)

except FileNotFoundError:
    print("Fichier " + fichier + " non trouvé.")
    exit(1)
except PermissionError:
    print("Vous n'avez pas le droit de lire le fichier " + fichier + ".")
    exit(1)

if nl != 8:
    print("Le jeu contient " + str(nl+1) + " lignes au lieu de 9.")
    exit(1)

for l in range(9):
    if estContradictoire(sudoku[l]):
        print("La ligne " + str(l+1) + " est contradictoire.")
        exit(1)

for c in range(9):
    colonne = [sudoku[l][c] for l in range(9)]
    if estContradictoire(colonne):
        print("La colonne " + str(c+1) + " est contradictoire.")
        exit(1)

for l in range(3):
    for c in range(3):
        cellule = []
        for i in range(3):
            cellule += sudoku[l*3 + i][c*3:(c+1)*3]
        if estContradictoire(cellule):
            print("La cellule (" + str(l+1) + " ; " + str(c+1) + ") est contradictoire.")
            exit(1)

# Affichage de la grille initiale
print("\nVoici la grille initiale : \n")
for l in sudoku:
    ch = ""
    for c in l:
        ch += str(c)
    print(ch)

# Résolution
possibles = [[] for i in trous]
caseAremplir = 0

while caseAremplir < len(trous):
    # FILL HERE
    possibles[caseAremplir] = casePossibles(trous[caseAremplir], sudoku)
    try:
        while not possibles[caseAremplir]:
            sudoku[trous[caseAremplir][0]][trous[caseAremplir][1]] = 0
            caseAremplir -= 1
    except IndexError:
        print("\nLa grille de sudoku n'a pas de solution\n")
        exit(1)

    sudoku[trous[caseAremplir][0]][trous[caseAremplir][1]] = possibles[caseAremplir].pop()
    caseAremplir += 1

# Temps de fin d'algorithme
t_end = time.time()


print(f"\nVoici la grille résolue en {round((t_end - t_start), 4)} secondes :\n")
# affichage de la grille remplie
for l in sudoku:
    ch = ""
    for c in l:
        ch += str(c)
    print(ch)