import codac

# Définir les intervalles des variables
x1 = codac.Interval(-10, 10)
x2 = codac.Interval(-10, 10)
x3 = codac.Interval(-1, 1)
#x4 = codac.Interval(-1, 1)
x4 = codac.Interval(21, 22)

# Calculer les intervalles pour les fonctions
f1 = x1 + 2 * x2 - x3
f2 = x1 - x2 - x4

print(f"Intervalle pour x1 + 2*x2 - x3: {f1}")
print(f"Intervalle pour x1 - x2 - x4: {f2}")

# On obtient [-31, 31] et [-21, 21] pour le premier intervalle x4
# On peut prendre ces contraintes égales à 0 car 0 appartient aux intervalles obtenus

# On obtient [-31, 31] et [-42, -1] pour le deuxième intervalle x4
# L'égalité à 0 pose problème pour la deuxième contrainte car 0 n'appartient pas au domaine possible de la deuxième contrainte

# Fonction pour calculer l'intersection de deux intervalles en vérifiant les valeurs None
def intersection(interval1, interval2):
    if interval1 is None or interval2 is None:
        return None  # Si l'un des intervalles est None, l'intersection est None
    lower_bound = max(interval1.lb(), interval2.lb())
    upper_bound = min(interval1.ub(), interval2.ub())
    if lower_bound <= upper_bound:
        return codac.Interval(lower_bound, upper_bound)  # Renvoie un nouvel intervalle
    else:
        return None  # Si les intervalles n'ont pas d'intersection

# Réécrire les contraintes pour isoler chaque variable
# Première contrainte : x1 + 2*x2 - x3 = 0
# => x1 = -2*x2 + x3
# => x2 = (x3 - x1)/2
# => x3 = x1 + 2*x2

# Deuxième contrainte : x1 - x2 - x4 = 0
# => x1 = x2 + x4
# => x2 = x1 - x4
# => x4 = x1 - x2

x1_from_c1 = codac.Interval(-2 * x2.ub() + x3.lb(), -2 * x2.lb() + x3.ub())
x1_from_c2 = codac.Interval(x2.lb() + x4.lb(), x2.ub() + x4.ub())
x1_filtered = intersection(x1, intersection(x1_from_c1, x1_from_c2))

x2_from_c1 = codac.Interval((x3.lb() - x1.ub()) / 2, (x3.ub() - x1.lb()) / 2)
x2_from_c2 = codac.Interval(x1.lb() - x4.ub(), x1.ub() - x4.lb())
x2_filtered = intersection(x2, intersection(x2_from_c1, x2_from_c2))

x3_from_c1 = codac.Interval(x1.lb() + 2 * x2.lb(), x1.ub() + 2 * x2.ub())
x3_filtered = intersection(x3, x3_from_c1)

x4_from_c2 = codac.Interval(x1.lb() - x2.ub(), x1.ub() - x2.lb())
x4_filtered = intersection(x4, x4_from_c2)

# Afficher les résultats
print(x1_filtered, x2_filtered, x3_filtered, x4_filtered)