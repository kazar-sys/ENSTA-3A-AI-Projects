input = "4sp 2_ nl 2sp 1. 1^ 1o 1sp 1~ 1bS nl 1sp 1Y 1sp 1/ 1sQ 1~ 1) 1sp 1} 6sp 5_ nl 1sp 1l 1/ 2sp 1/ 1sp 1/ 4sp 1, 1- 1~ 5sp 2~ 2- 1. 1, 1_ nl 4sp 1( 1sp 1( 4sp 1/ 2sp 1~ 1- 1. 1_ 9sp 1^ 1. nl 5sp 1bS 1sp 1sQ 2- 1sQ 2- 1. 4sp 1sQ 1- 1. 1_ 7sp 1bS nl 6sp 1sQ 1- 1. 8_ 5sp 1~ 2- 1. 1, 2_ 1sp 1^ 1. nl 16sp 1sQ 1~ 1r 1- 1. 1, 3_ 1. 1- 1sQ 1- 1. 1sp 1^ 1. nl 17sp 1Y 1I 4sp 1bS 6sp 1~ 1- 1. 1bS nl 17sp 2| 5sp 1bS 8sp 1` 1bS nl 17sp 2| 5sp 2/ nl 17sp 2| 4sp 2/ nl 17sp 1( 1) 3sp 2/ nl 17sp 2| 2sp 2/ 4sp 1~ 1F 1r 1a 1n nl 17sp 2| 1sp 1( 1sp 1c nl 4sp 3_ 1. 1_ 1sp 2_ 2sp 3_ 1I 1| 2_ 1` 2- 2_ 1. 1_ 1sp 2_ 2sp 1_ nl 2sp 1sQ 1~ 5sp 1~ 2sp 1sQ 1~ 3sp 2: 2sp 2~ 2sQ 4sp 1~ 2sp 2~ nl 17sp 2: nl 17sp 1. 1: nl 18sp 1. nl 2sp 32~"
symbols = list()
for symbol in input.split(" "):
    if symbol != "nl":
        if not symbol.isdigit():
            j = 0
            while symbol[j].isdigit():
                j += 1
            symbols.append([int(symbol[0:j]), symbol[j:]])
        else:
            symbols.append([int(symbol[:-1]), symbol[-1]])
    else:
        symbols.append("nl")

text = ""
for sublist in symbols:
    if isinstance(sublist, list):
        if sublist[1] not in ["sp", "bS", "sQ"]:
            for i in range(sublist[0]):
                text += sublist[1]
        else:
            if sublist[1] == "sp":
                for i in range(sublist[0]):
                    text += " "
            elif sublist[1] == "bS":
                for i in range(sublist[0]):
                    text += "\\"
            elif sublist[1] == "sQ":
                for i in range(sublist[0]):
                    text += "'"
    else:
        text += "\n"
print(text)



