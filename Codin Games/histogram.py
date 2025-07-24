### But du puzzle : afficher un histograme en ascii art de la fréquence de chaque lettre de l'input.


### Entrées
input = "Coding game"
s = input.replace(" ", "")
s = s.upper()

### Calcul des fréquences.
frequences = [[chr(i+65), 0] for i in range(26)]

for char in s:
    frequences[ord(char)-65][1] += 1

for freq in frequences:
    freq[1] = (freq[1]/len(s))*100

# Vérification du calcul
#print(frequences)

### Les print de sortie

if frequences[0][1] > 0:
    print("  +" + int(round(frequences[0][1], 0))*"-" + "+")
    print(frequences[0][0] + " |" + int(round(frequences[0][1], 0))*" " + "|" + str(round(frequences[0][1], 2)).replace(".", ",") + "%")
else:
    print("  +")

for i in range(1, len(frequences)-1):
    if frequences[i][1] == 0 and frequences[i+1][1] == 0:
        print("  +")
    elif frequences[i][1] != 0 and frequences[i+1][1] != 0:
        print("  +" + (int(round(min(frequences[i][1], frequences[i+1][1]), 0))-1)*"-" + "+" + int(round(abs(frequences[i+1][1] - frequences[i][1]), 0))*"-" + "+")
    else:
        print("  +" + int(round(max(frequences[i][1], frequences[i+1][1]), 0))*"-" + "+")
    if frequences[i][1] > 0:
        print(frequences[i][0] + " |" + int(round(frequences[i][1], 0))*" " + "|" + str(round(frequences[i][1], 2)).replace(".", ",") + "%")
    else:
        print(frequences[i][0] + " |0,00%")
