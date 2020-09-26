import requests
from bs4 import BeautifulSoup

def champ_lookup():

    summoner_name = input('Summoner name?')
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
    print(merged_list)
    return merged_list

champ_lookup()
# if __name__ == "__main__":
#     champ_lookup('prismy')