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

    # print(games)
    # Return the deduplicated games list
    return games

def createcsv(games):
    with open(output_file, 'w') as f:
        f.write("Title,\n")
        for game in games:
            f.write(game + ",\n")


def howlongtobeat(games):
    
    with open(output_file, 'w') as f:
            f.write("game_name,game_alias,game_image_url,game_web_link,review_score,profile_dev,profile_platforms,release_world,main_story,main_extra,completionist,all_styles,user_submitted_name,\n")
    
    #games = ["Super Mario Bros. 3"]
    for game in games:
        results_list = HowLongToBeat().search(f'{game}', similarity_case_sensitive=False)
        if results_list is not None and len(results_list) > 0: 
            results = f'"{results_list[0].game_name}","{results_list[0].game_alias}","{results_list[0].game_image_url}","{results_list[0].game_web_link}","{results_list[0].review_score}","{results_list[0].profile_dev}","{results_list[0].profile_platforms}","{results_list[0].release_world}","{results_list[0].main_story}","{results_list[0].main_extra}","{results_list[0].completionist}","{results_list[0].all_styles}","{game}",\n'
            print(results)
            with open(output_file, 'a') as f:
                f.write(results)
        else:
            print(f'{game},,,,,,,,,,,,,')
            with open (fix_file, 'a') as f:
                f.write(f'{game}\n')
        time.sleep(1)
    
    return results

# Call the functions with appropriate arguments
lower_games = []
lower_games = createlist()
games = dedupe(lower_games)
#createcsv(games)
howlongtobeat(games)

