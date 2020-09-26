# bot.py
import os
import random
from dotenv import load_dotenv
import discord
import requests
from bs4 import BeautifulSoup

#1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

#2
bot = commands.Bot(command_prefix='!')

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
    response = requests.get('https://na.op.gg/summoner/userName={summoner_name}')

    response = requests.get('https://na.op.gg/summoner/userName={summoner_name}}')
    soup = BeautifulSoup(response.content, 'html.parser')

    game_result = soup.find_all('div', class_='GameResult')
    win_loss = []
    
    for game in game_result:
        
        
        win_loss.append(game.get_text().strip())
    
    await ctx.send(win_loss)
    print(win_loss)

    # dice = [
    #     str(random.choice(range(1, number_of_sides + 1)))
    #     for _ in range(number_of_dice)
    # ]
    # await ctx.send(', '.join(dice))

bot.run(TOKEN)