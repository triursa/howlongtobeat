from config import *
from howlongtobeatpy import HowLongToBeat

def createlist():
    # Read the games from the text file
    with open('input/games.txt', 'r') as file:
        games = file.readlines()

    # Remove leading/trailing whitespace and convert to lowercase
    lower_games = [game.strip().lower() for game in games]

    # Return the lower_games list
    return lower_games

def dedupe(lower_games):
    games = []
    for game in lower_games:
        if game not in games:  # Remove duplicates
            games.append(game)

    # Return the deduplicated games list
    return games

def createcsv(games):
    with open(output_file, 'w') as f:
        f.write("Title,\n")
        for game in games:
            f.write(game + ",\n")


def howlongtobeat(games):
    
    with open(output_file, 'w') as f:
            f.write("title,game_name,main_story,main_extra,completionist,\n")
    
    for game in games:
        results_list = HowLongToBeat().search(f'{game}')
        results = f'{results_list[0].game_name}, {results_list[0].main_story}'
    print(results)
    
    return results
   
    

# Call the functions with appropriate arguments
lower_games = []
lower_games = createlist(lower_games)
games = dedupe(lower_games)
#createcsv(games)
howlongtobeat(games)

