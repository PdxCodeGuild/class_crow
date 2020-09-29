import requests
from bs4 import BeautifulSoup

def champ_lookup():

    summoner_name = input('Summoner name? ')
    response = requests.get(f'https://na.op.gg/summoner/userName={summoner_name}')

    # response = requests.get('https://na.op.gg/summoner/userName=prismy')
    soup = BeautifulSoup(response.content, 'html.parser')


    game_result = soup.find_all('div', class_='GameResult')
    game_result_list = []
    for game in game_result:
        # print(game.get_text().strip())
        game_result_list.append(game.get_text().strip())

    #### parent class of champ_name is GameSettingInfo

    game_setting_info = soup.find('div', class_ = 'GameItemList')

    champ_name = game_setting_info.findChildren(class_='ChampionName')
    champ_name_list = []
    for champ in champ_name:
        # print(champ.get_text().strip())
        champ_name_list.append(champ.get_text().strip())

    cs_score = game_setting_info.findChildren(class_='CS')
    cs_list = []
    for cs in cs_score:
        # print(cs.get_text().strip())
        cs = cs.get_text().strip()
        # print(cs)
        if cs[-1] == 'S':
            cs_list.append(cs)
    # print(cs_list)

    

    merged_list = tuple(zip(game_result_list, champ_name_list, cs_list))
    avg_cs_list = tuple(zip(game_result, cs_list))
    print(merged_list)

    victory_cs = []
    defeat_cs = []
    
    
    print(avg_cs_list)
    
    return merged_list

def summoner_rank(summoner_name):
    
    # print(summoner_name)
    response = requests.get(f'https://na.op.gg/summoner/userName={summoner_name}')
    # print(response)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.get_text())

    rank = soup.find('div', class_='TierRank')
    for item in rank:
        rank = item
    # print(rank)

    lp = soup.find('span', class_='LeaguePoints')
    for item in lp:
        lp = item
    # print(item.strip())
    lp = item.strip()
    
    print(f'{summoner_name} : {rank} : {lp}')

def avg_cs():

    # summoner_name = input('Summoner name? ')
    # response = requests.get(f'https://na.op.gg/summoner/userName={summoner_name}')

    response = requests.get('https://na.op.gg/summoner/userName=j aldo')
    soup = BeautifulSoup(response.content, 'html.parser')


    game_result = soup.find_all('div', class_='GameResult')
    game_result_list = []
    for game in game_result:
        # print(game.get_text().strip())
        game_result_list.append(game.get_text().strip())

    # print(game_result_list)
    #### parent class of champ_name is GameSettingInfo
    game_setting_info = soup.find('div', class_ = 'GameItemList')

    cs_score = game_setting_info.findChildren(class_='CS')
    cs_list = []
    for cs in cs_score:
        # print(cs.get_text().strip())
        cs = cs.get_text().strip()
        # print(cs)
        if cs[-1] == 'S':
            cs_list.append(cs)
    # print(cs_list)

    avg_cs_list = tuple(zip(game_result_list, cs_list))

    # tallies total cs depending on result
    victory_cs_tally = 0
    defeat_cs_tally = 0

    # counts instances of victory/defeat
    defeat_counter = 0
    victory_counter = 0

    for i in range(len(avg_cs_list)):
        # print(avg_cs_list[i][0])
        if avg_cs_list[i][0] == 'Defeat':
            defeat_counter += 1
            defeat_cs = avg_cs_list[i][1]
            
            defeat_cs = int(defeat_cs[0:3])
            defeat_cs_tally += defeat_cs
            # print(defeat_cs)
        if avg_cs_list[i][0] == 'Victory':
            victory_counter += 1
            victory_cs = avg_cs_list[i][1]
            
            victory_cs = int(victory_cs[0:3])
            victory_cs_tally += victory_cs
            # print(victory_cs)
    avg_defeat_cs = defeat_cs_tally/defeat_counter
    avg_victory_cs = victory_cs_tally/victory_counter
    print (avg_defeat_cs)
    print (avg_victory_cs)
    
    
    
    # print(avg_cs_list)
    
    return avg_cs_list

# summoner_rank('ancientemblem')
# champ_lookup()

# avg_cs()


def youtube_search():
    search_query = input('What? ')
    response = (f'https://www.youtube.com/results?search_query={search_query}')
    # response =(f'<iframe width="722" height="406" src="https://www.youtube.com/embed/{search_query}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
    print(response)

def api_test():
    response = requests.get('https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist')
    # print(response.json())
    _object = response.json()
    setup = _object['setup']
    delivery = _object['delivery']
    print(delivery)
    return setup, delivery


api_test()