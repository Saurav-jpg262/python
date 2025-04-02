games = []

while True:
    user_game = input("Enter a game, or press enter to stop\n")
    if user_game == "":
        break
    else:
        games.append(user_game)

print("Your favorite games are:  ")
for game in games:
    print(game)