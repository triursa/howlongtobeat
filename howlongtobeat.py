import requests
from bs4 import BeautifulSoup

# Function to fetch game statistics from howlongtobeat.com
def get_hltb_stats(game_title):
    base_url = 'https://howlongtobeat.com/'
    search_url = base_url + 'search_results?page=1'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    params = {
        'queryString': game_title,
        't': 'games',
        'sorthead': 'popular',
        'sortd': 'Normal Order',
        'plat': '',
        'length_type': 'main'
    }
    
    try:
        # Send GET request to search for the game title
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        
        # Parse the HTML response
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Get the first search result
        result = soup.find('li', class_='search_list_details')
        if result:
            # Extract game details
            title = result.find('h3').text.strip()
            time_stats = result.find_all('div', class_='search_list_tidbit')
            if len(time_stats) == 3:
                main_story = time_stats[0].text.strip().split('\n')[0]
                main_extras = time_stats[1].text.strip().split('\n')[0]
                complete = time_stats[2].text.strip().split('\n')[0]
                return title, main_story, main_extras, complete
            else:
                return title, 'N/A', 'N/A', 'N/A'
        else:
            return game_title, 'Not Found', 'Not Found', 'Not Found'
    except Exception as e:
        print(f'Error fetching stats for "{game_title}": {e}')
        return game_title, 'N/A', 'N/A', 'N/A'

# Read the input text file
input_file = 'games.txt'
output_file = 'games_stats.txt'
games = []
with open(input_file, 'r') as f:
    for line in f:
        game = line.strip()
        if game not in games:  # Remove duplicates
            games.append(game)

# Fetch game statistics and write to output file
with open(output_file, 'w') as f:
    for game in games:
        title, main_story, main_extras, complete = get_hltb_stats(game)
        f.write(f'Title: {title}\n')
        f.write(f'Main Story: {main_story}\n')
        f.write(f'Main + Extras: {main_extras}\n')
        f.write(f'Complete: {complete}\n')
        f.write('\n')
