#!/usr/bin/python
import discord, bacula, asyncio
from discord.ext import commands, tasks
from config import read_config, default_config


class BatHook(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bacula_connection = None

        # create the background task and run it in the background
        #self.monitor_db = self.loop.create_task(self.background_db_mon())
        self.background_db_mon.start()

    async def on_ready(self):
        # Runs when ready
        print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

        await bot.change_presence(activity=discord.Game(name="In Debug mode!"))
        print(f'Successfully logged in and booted...!')

        print(f'Preparing Bacula backend...')
        self.bacula_connection = bacula.Bacula()

    @tasks.loop(seconds=5.0)
    async def background_db_mon(self):
        # Wait till we're ready before speaking.
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(666872163030007808) # channel ID goes here
        #while not self.is_closed():
        counter += 1
        print(counter)
        await channel.send(counter)
        await asyncio.sleep(5) # task runs every 60 seconds


if __name__ == '__main__':
    try:
        discord_config = read_config(filename='config.ini',
                                     section='discord')
    except Exception:
        # This exception is only handled at startup, other missing sections wont be handled.
        print("The config.ini was malformed or could not be found, would you like the software to regenerate it? [Y/n]:")
        if input().lower() == 'y':
            write_config(filename="config.ini")
            quit()


# We have to pop the token because discord py treats it as positional, the rest of the args can be passed normally
bot = BatHook()
bot.run(discord_config.pop('token'), **discord_config) 
