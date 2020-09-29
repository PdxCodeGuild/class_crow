import os
import random
from dotenv import load_dotenv
import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
bot = commands.Bot(command_prefix='!')


# reference: https://realpython.com/python-requests/
# reference: https://realpython.com/how-to-make-a-discord-bot-python/

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
         'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='photodump'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckAnyFailure):
        await ctx.send('you do not have the correct role for this command')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

@bot.command(name='opgg', help='Looks up user\'s op.gg')
async def op_gg(ctx, summoner_name):

    response = requests.get(f'https://na.op.gg/summoner/userName={summoner_name}')
    soup = BeautifulSoup(response.content, 'html.parser')


    game_result = soup.find_all('div', class_='GameResult')
    game_result_list = []

    for game in game_result:
        game_result_list.append(game.get_text().strip())

    #### parent class of champ_name is GameSettingInfo
    game_setting_info = soup.find('div', class_ = 'GameItemList')
    champ_name = game_setting_info.findChildren(class_='ChampionName')
    champ_name_list = []

    for champ in champ_name:
        champ_name_list.append(champ.get_text().strip())

    cs_score = game_setting_info.findChildren(class_='CS')
    cs_list = []

    for cs in cs_score:
        cs = cs.get_text().strip()
        if cs[-1] == 'S':
            cs_list.append(cs)

    merged_list = tuple(zip(game_result_list, champ_name_list, cs_list))

    await ctx.send(merged_list)

@bot.command(name='avg_cs', help='Looks up user\'s avg cs by defeat or victory')
async def avg_cs(ctx, summoner_name):

    response = requests.get('https://na.op.gg/summoner/userName=j aldo')
    soup = BeautifulSoup(response.content, 'html.parser')

    game_result = soup.find_all('div', class_='GameResult')
    game_result_list = []

    for game in game_result:
        game_result_list.append(game.get_text().strip())

    #### parent class of champ_name is GameSettingInfo
    game_setting_info = soup.find('div', class_ = 'GameItemList')

    cs_score = game_setting_info.findChildren(class_='CS')
    cs_list = []
    
    for cs in cs_score:
        cs = cs.get_text().strip()
        
        if cs[-1] == 'S':
            cs_list.append(cs)
    

    avg_cs_list = tuple(zip(game_result_list, cs_list))

    # tallies total cs depending on result
    victory_cs_tally = 0
    defeat_cs_tally = 0

    # counts instances of victory/defeat
    defeat_counter = 0
    victory_counter = 0

    for i in range(len(avg_cs_list)):
        if avg_cs_list[i][0] == 'Defeat':
            defeat_counter += 1
            defeat_cs = avg_cs_list[i][1]     
            defeat_cs = int(defeat_cs[0:3])
            defeat_cs_tally += defeat_cs
     
        if avg_cs_list[i][0] == 'Victory':
            victory_counter += 1
            victory_cs = avg_cs_list[i][1] 
            victory_cs = int(victory_cs[0:3])
            victory_cs_tally += victory_cs

    avg_defeat_cs = defeat_cs_tally/defeat_counter
    avg_victory_cs = victory_cs_tally/victory_counter
    
    await ctx.send(f'{summoner_name} \n victory: {avg_victory_cs} \n defeat: {avg_defeat_cs}')

bot.run(TOKEN)
