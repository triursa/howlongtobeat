# Read the input text file
input_file = 'games.txt'
output_file = 'dedupe_games.txt'
games = []
with open(input_file, 'r') as f:
    for line in f:
        game = line.strip()
        if game not in games:  # Remove duplicates
            games.append(game)

with open(output_file, 'w') as f:
    for game in games:
        f.write(game + "\n")