# Entrées
s = "Hello world"
n = 4
changes = [
    "0|11|!",
    "0|5|,\n",
    "0|7| w",
    "0|10|\n"
]

for change in changes:
    line, pos, char = change.split("|")

