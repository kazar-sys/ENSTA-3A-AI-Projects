# But du puzzle : en entrée on dispose d'une grille de morpion, on doit retourner 
# la grille avec le mouvement gagnant pour le joueur O, false si aucune grille n'est gagnante.

# Entrée
grid = [
    ['O', 'O', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]


### Définition des fonctions utiles

# Fonction déterminant si une grille est gagnante
def isWinning(grid, player):
    
    # Vérification par lignes
    for i in range(3):
        if "".join(grid[i]) == 3*player:
            return True
    
    # Vérification par colonnes
    for j in range(3):
        col = ""
        for i in range(3):
            col += grid[i][j]
        if col == 3*player:
            return True
    
    # Vérification de la diagonale nord-ouest / sud-est
    diag_no_se = grid[0][0] + grid[1][1] + grid[2][2]
    if diag_no_se == 3*player:
        return True

    # Vérification de la diagonale sud-ouest / nord-est
    diag_so_ne = grid[2][0] + grid[1][1] + grid[0][2]
    if diag_so_ne == 3*player:
        return True
    
    # La fonction retourne False si la grille n'est pas gagnante
    return False


### Coeur du programme

# Double boucle pour tester chaque case vide remplie par le joueur 
player = 'O' # Définition de quel joueur on doit faire gagner
win = False # Initialisation de la variable à False, le joueur n'a pas encore gagné

for i in range(3):
    if win:
        break
    for j in range(3):
        if grid[i][j] == '.':
            grid[i][j] = player
            if isWinning(grid, player):
                win = True
                break
            else:
                grid[i][j] = '.'

# Gérer la sortie : dessin de la grille si win, string "false" sinon
if win:
    for line in grid:
        print("".join(line))
else:
    print("false")