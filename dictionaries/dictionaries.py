locations = {0: "GameOver",
             1: "Horns Road",
             2: "Trinity Way",
             3: "Tesco",
             4: "High Street",
             5: "ICHS"}

#each direction gives us the key of the destination in the locations directory
exits = [{"Q":0},
         {"N":2, "Q":0},
         {"W":3, "E":4, "S":1, "Q":0},
         {"E":2, "Q":0},
         {"N":5, "W":2, "Q":0},
         {"S":4, "Q":0}]

loc = 1
while True:
    availableExits = ""
    print("You are at " + locations[loc] + "\nDirections available:")
    for direction in exits[loc].keys():
        print(direction,  end=' ')
        availableExits += direction
    print
    direction = input("Where do you want to go?\t").upper()
    if direction == 'Q':
        break
    if direction in availableExits:
        loc = exits[loc][direction]
    else:
        print("Route closed")












# myList = ["a", "b", "c"]
# newString = " mississipi,  ".join(myList)
# print(newString)
#




# game = {"GTA": "murder",
#         "FIFA": "football",
#         "COD": "shooter"}
# print(game)
# print(game["GTA"])
# game["LOL"] = "toxiccity"
# print(game)
# game["GTA"] = "driving"
# print(game)
#
# ordered_games = list(game.keys())
# ordered_games_description = list(game.values())
# print(ordered_games)
# print(ordered_games_description)
# ordered_games.sort()
# print(ordered_games)
# ordered_games_description=sorted(list(game.values()))
# print(ordered_games_description)
# for g in ordered_games:
#     print(g + " genre is " + game[g])
#
# while True:
#     inp = input("What game?")
#     if inp == "Q":
#         break
#     if inp in game:
#         genre = game.get(inp)
#         print(genre)
#         del game[inp]
#     else:
#         print("No game")


# locations = {0: "GameOver",
#              1: "Horns Road",
#              2: "Trinity Way",
#              3: "Tesco",
#              4: "High Street",
#              5: "ICHS"}
#
# exits = [{"Q":0},
#          {"N":2, "Q":0},
#          {"W":3, "E":4, "S":1, "Q":0},
#          {"E":2, "Q":0},
#          {"N":5, "W":2, "Q":0},
#          {"S":4, "Q":0}]


# myList = ["a", "b", "c"]
# newString = ",  ".join(myList)
# print(newString)
# print(myList)

