# Entrées
n = 3
cost = 100
budgets = [
    100,
    1,
    60
]

# Fonctions utiles

# Retourne True si les budgets sont suffisants, False sinon
def giftPossible(cost, budgets):
    return sum(budgets) >= cost

if not giftPossible(cost, budgets):
    print("IMPOSSIBLE")

else:
    amount_given = budgets.copy()
    while sum(amount_given) > cost:
        amount_given[amount_given.index(max(amount_given))] -= 1

    amount_given = sorted(amount_given)

    for amount in amount_given:
        print(amount)