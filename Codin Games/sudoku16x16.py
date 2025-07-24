from sys import exit, argv

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
    chiffres |= {sudoku[i][case[1]] for i in range(16)}
    cellule = case[0] // 4, case[1] // 4
    for i in range(4):
        chiffres |= set(sudoku[cellule[0]*4 + i][cellule[1]*4:(cellule[1]+1)*4])
    return list(set(range(1, 17)) - chiffres)

# Fonction pour convertir une lettre en chiffre
def lettreVersChiffre(char):
    if char == ".":
        return 0  # Remplacer les points par des zéros
    else:
        return ord(char) - ord('A') + 1  # Convertir A=1, B=2, ..., P=16

# Fonction inverse
def chiffreVerslettre(number):
    return chr(number + ord('A') - 1)

letters = [
    "........B.HAL..N",
    "..N.....D...OEF.",
    "..K.A..J..NO.B.P",
    "...CL.D..G.E.M.J",
    "...JH..P.......E",
    ".N.K.....I..JGOD",
    ".OM..IECNB.GH...",
    "HB...D..P.J.NFCI",
    ".HA.ME......KN.C",
    "D..ENB.H.POL....",
    "NM.B..O.JK..D...",
    ".PL....D.....A.O",
    ".E.HDC.....FPK..",
    ".C..EAN.OL.P.I..",
    "IA.NG.PM..KD..E.",
    "..O.IH.....NAC.."
]

# Initialisation du sudoku et de la liste des trous à remplir 
trous = []
sudoku = []

# Transformation de la grille
for ligne in letters:
    nouvelle_ligne = [lettreVersChiffre(char) for char in ligne]  # Conversion de chaque caractère
    sudoku.append(nouvelle_ligne)

# Transformation de trous
for i in range(16):
    for j in range(16):
        if sudoku[i][j] == 0:
            trous.append([i, j])

# Affichage de la grille initiale
#print(sudoku)
#print(trous)

# Résolution
possibles = [[] for i in trous]
caseAremplir = 0

while caseAremplir < len(trous):
    print(caseAremplir)
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

# Affichage de la grille remplie
for l in sudoku:
    ch = ""
    for number in l:
        ch += chiffreVerslettre(number)
    print(ch)