# Exemples de data pour run
champion_names = ["KEN", "TANK"]
n = 14
beats = [
    [">", "PUNCH"],
    ["<", "PUNCH"],
    [">", "KICK"],
    ["<", "KICK"],
    [">", "PUNCH"],
    ["<", "PUNCH"],
    ["<", "SPECIAL"],
    [">", "SPECIAL"],
    [">", "PUNCH"],
    ["<", "KICK"],
    [">", "KICK"],
    ["<", "KICK"],
    ["<", "SPECIAL"],
    [">", "SPECIAL"]
]

# Définition des champions
champions = [
    {
        "NAME": "KEN",
        "LIFE": 25,
        "PUNCH": 6,
        "KICK": 5,
        "RAGE": 0,
        "HITS": 0,
        "DAMAGE": 0
    },
    {
        "NAME": "RYU",
        "LIFE": 25,
        "PUNCH": 4,
        "KICK": 5,
        "RAGE": 0,
        "HITS": 0,
        "DAMAGE": 0
    },
    {
        "NAME": "TANK",
        "LIFE": 50,
        "PUNCH": 2,
        "KICK": 2,
        "RAGE": 0,
        "HITS": 0,
        "DAMAGE": 0
    },
    {
        "NAME": "VLAD",
        "LIFE": 30,
        "PUNCH": 3,
        "KICK": 3,
        "RAGE": 0,
        "HITS": 0,
        "DAMAGE": 0
    },
    {
        "NAME": "JADE",
        "LIFE": 20,
        "PUNCH": 2,
        "KICK": 7,
        "RAGE": 0,
        "HITS": 0,
        "DAMAGE": 0
    },
    {
        "NAME": "ANNA",
        "LIFE": 18,
        "PUNCH": 9,
        "KICK": 1,
        "RAGE": 0,
        "HITS": 0,
        "DAMAGE": 0
    },
    {
        "NAME": "JUN",
        "LIFE": 60,
        "PUNCH": 2,
        "KICK": 1,
        "RAGE": 0,
        "HITS": 0,
        "DAMAGE": 0
    }
]

# Fonctions
def get_champion_index(champion_name: str, champion_list: list):
    k = 0
    for champion in champion_list:
        if champion["NAME"] == champion_name:
            return k
        k += 1

def attack(attacker_index: int, defender_index: int, attack_type: str, champion_list: list):

    if attack_type in ["PUNCH", "KICK"]:
        damage = champion_list[attacker_index][attack_type]
        champion_list[defender_index]["RAGE"] += 1
    
    else:
        if champion_list[attacker_index]["NAME"] == "KEN":
            damage = 3 * champion_list[attacker_index]["RAGE"]
        elif champion_list[attacker_index]["NAME"] == "RYU":
            damage = 4 * champion_list[attacker_index]["RAGE"]
        elif champion_list[attacker_index]["NAME"] == "TANK":
            damage = 2 * champion_list[attacker_index]["RAGE"]
        elif champion_list[attacker_index]["NAME"] == "VLAD":
            damage = 2 * (champion_list[attacker_index]["RAGE"] + champion_list[defender_index]["RAGE"])
        elif champion_list[attacker_index]["NAME"] == "JADE":
            damage = champion_list[attacker_index]["HITS"] * champion_list[attacker_index]["RAGE"]
        elif champion_list[attacker_index]["NAME"] == "ANNA":
            damage = champion_list[attacker_index]["DAMAGE"] * champion_list[attacker_index]["RAGE"]
        elif champion_list[attacker_index]["NAME"] == "JUN":
            damage = champion_list[attacker_index]["RAGE"]
            champion_list[attacker_index]["LIFE"] += champion_list[defender_index]["RAGE"]
        champion_list[attacker_index]["RAGE"] = 0
    
    champion_list[defender_index]["LIFE"] -= damage
    champion_list[defender_index]["DAMAGE"] += damage
    champion_list[attacker_index]["HITS"] += 1


# Boucle principale
champion_1, champion_2 = champion_names[0], champion_names[1]
index_champion_1 = get_champion_index(champion_1, champions)
index_champion_2 = get_champion_index(champion_2, champions)
k = 0
while k < n and champions[index_champion_1]["LIFE"] > 0 and champions[index_champion_2]["LIFE"] > 0:
    attack_type = beats[k][1]
    attacker = champion_2 if beats[k][0] == "<" else champion_1
    defender = champion_1 if attacker == champion_2 else champion_2
    attacker_index = index_champion_1 if attacker == champion_1 else index_champion_2
    defender_index = index_champion_2 if defender == champion_2 else index_champion_1
    attack(attacker_index, defender_index, attack_type, champions)
    
    #test
    print("\n\n", champions[index_champion_1], "\n", champions[index_champion_2], "\n\n")
    k += 1

# Affichage des résultats
winner = champion_1 if champions[index_champion_1]["LIFE"] > champions[index_champion_2]["LIFE"] else champion_2
index_winner = get_champion_index(winner, champions)
loser = champion_2 if winner == champion_1 else champion_1
print(f"{winner} beats {loser} in {champions[index_winner]['HITS']} hits")
    




