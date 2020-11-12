#!/usr/bin/python
import discord, bacula
from discord.ext import commands
from config import read_config, write_config


# Prefixes the bot will respond to
def get_prefix(bot, message):
    prefixes = ['>', '!']

# Commands the bot can run-once
initial_extensions = []

# Create bot object
bot = commands.Bot(command_prefix=get_prefix, description='A Robot made of tape.')

# Create bacula object
bacula_connection = None

if __name__ == '__main__':
    try:
        discord_config = read_config(filename='config.ini',
                                     section='discord')
    except Exception:
        print("The config.ini was malformed or could not be found, would you like the software to regenerate it? [Y/n]:")
        if input().lower() == 'y':
            write_config(filename="config.ini")
            quit()

@bot.event
async def on_ready():
    # Runs when ready
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    await bot.change_presence(activity=discord.Game(name="In Debug mode!"))
    print(f'Successfully logged in and booted...!')

    print(f'Preparing Bacula backend...')
    bacula_connection = bacula.Bacula()


# We have to pop the token because discord py treats it as positional, the rest of the args can be passed normally
bot.run(discord_config.pop('token'), **discord_config) 
