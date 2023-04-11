# Read the list of games from a file
with open('games.txt', 'r') as file:
    games = file.read().splitlines()

# Function to convert a string to title case
def title_case(string):
    skip_words = ['a', 'an', 'the']
    words = string.split()
    return ' '.join([word.capitalize() if word not in skip_words else word for word in words])

# Convert games to title case
games_title_case = [title_case(game) for game in games]

# Export the list of games to a text file with one item per line
with open('games_title_case.txt', 'w') as file:
    file.write('\n'.join(games_title_case))