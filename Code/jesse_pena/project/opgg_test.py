import requests
from bs4 import BeautifulSoup



summoner_name = input('Summoner name?').lower
response = requests.get('https://na.op.gg/summoner/userName={summoner_name}')

response = requests.get('https://na.op.gg/summoner/userName={summoner_name}}')
soup = BeautifulSoup(response.content, 'html.parser')
text = soup.get_text()

game_result = soup.find_all('div', class_='GameResult')
# print(game_item_wrap)
for game in game_result:
    print(game.get_text().strip())





