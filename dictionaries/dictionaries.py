locations = {0: "GameOver",
             1: "Horns Road",
             2: "Trinity Way",
             3: "Tesco",
             4: "High Street",
             5: "ICHS"}

exits = [{"Q":0},
         {"N":2, "Q":0},
         {"W":3, "E":4, "S":1, "Q":0},
         {"E":2, "Q":0},
         {"N":5, "W":2, "Q":0},
         {"S":4, "Q":0}]




# myList = ["a", "b", "c"]
# newString = ",  ".join(myList)
# print(newString)


# game = {"GTA": "murder",
#         "FIFA": "football",
#         "COD": "shooter"}
# print(game)
#
# print(game.items())
# g_tuple = tuple(game.items())
# print(g_tuple)
#
# for playing in g_tuple:
#     game, genre = playing
#     print(game + " has a genre of " + genre)


# print(game["COD"])
# game["LOL"] = "toxiccity"
# print(game)
# game["GTA"] = "driving"
# print(game)
# del game["GTA"]
# print(game)

# while True:
#     inp = input("What game?")
#     if inp == "Q":
#         break
#     if inp in game:
#         genre = game.get(inp)
#         print(genre)
#     else:
#         print("No game")

# ordered_games = list(game.keys())
# print(ordered_games)
# ordered_games.sort()
# print(ordered_games)
# ordered_games=sorted(list(game.keys()))
# print(ordered_games)
# for g in ordered_games:
#     print(g + " genre is " + game[g])