import json

# define players and their starting elo
players = {'Ket': 1000, 'Lyte': 1000, 'Moo': 1000, 'Crispy': 1000, 'Skittles': 1000, 'Joran': 1000, 'Jod': 1000, 'Fred': 1000}

# read the current standings from the file, if it exists
try:
    with open('current_standings.json', 'r') as f:
        players = json.load(f)
except FileNotFoundError:
    pass


# print the initial ELO values of all the players
print("Initial ELO Values:")
for player, elo in players.items():
    print(f"{player}: {int(elo)}")


# ask for user input on who won and lost, and update elo accordingly
while True:
    winner = input("\nEnter the name of the winner: ")
    loser = input("Enter the name of the loser: ")
    if winner not in players or loser not in players:
        print("Invalid player names. Try again.")
    else:
        k_factor = 32 # this can be adjusted to change the rate of elo change
        winner_expected = 1 / (1 + 10**((players[loser] - players[winner])/400))
        loser_expected = 1 / (1 + 10**((players[winner] - players[loser])/400))
        players[winner] += k_factor * (1 - winner_expected)
        players[loser] += k_factor * (0 - loser_expected)
        print(f"{winner} now has an elo of {round(players[winner])}.")
        print(f"{loser} now has an elo of {round(players[loser])}.")
        if input("Enter q to quit, or any other key to continue: ") == 'q':
            break

# write the current standings to a file before the program exits
with open('current_standings.json', 'w') as f:
    json.dump(players, f)
