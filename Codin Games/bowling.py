# Exemple de data
n = 1
games = [
    "32 71 23 44 5- 1- 11 15 16 7-"
]

# Fonctions
def game_to_list(game):
    game = game.split(" ")
    result = []
    for throw in game:
        throw = throw.replace("-", "0")
        throw = list(throw) 
        result.append(throw) 
    return result

# Test
print(game_to_list(games[0]))

def convert_to_num_game(game: list):
    result = list()
    for throw in game:
        for point in throw:
            if point.isdigit():
                point = int(point)
        result.append(throw)
    return result

# Test
print(convert_to_num_game(game_to_list(games[0])))