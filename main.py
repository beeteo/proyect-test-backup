import os, sys
import discord, json
import requests, cloudscraper
from discord.ext import commands

def get_prefix(client, message):
    try:
        if os.path.exists('Database'):
            if os.path.exists('Database/prefixs.json'):
                with open('Database/prefixs.json') as f:
                    data = json.load(f)

                return data[str(message.guild.id)]
            else:
                prefixs = {
                    str(message.guild.id): '-'
                }
                with open('Database/prefixs', 'w') as f:
                    json.dump(prefixs)
                with open('Database/prefixs.json') as f:
                    data = json.load(f)

                return data[str(message.guild.id)]                
        else:
            os.mkdir('Database')
    except:
            prefixs = {
                str(message.guild.id): '-'
            }
            with open('Database/prefixs', 'w') as f:
                json.dump(prefixs)
            with open('Database/prefixs.json') as f:
                data = json.load(f)

            return data[str(message.guild.id)]   
    return data[str(message.guild.id)]  

token = 'bot-token'
intents = discord.Intents(messages=True, guilds=True, members=True)
kory = commands.Bot(command_prefix=(get_prefix), intents=intents)

@kory.event
async def on_connect():
    print('Ready!')

@kory.event
async def on_guild_join(guild):
    data = {
            "server": {
                "name": str(guild.name),
                "id": str(guild.id),
                "bans": 0
            },
            "logs": {
                "use": "false",
                "channel": 0,
                "text": {
                    "embedmode": "embed"
                }
            }
        }
    with open(f'Database/Servers/{guild.id}.json', 'w') as f:
            json.dump(data, f, indent=4)

    try:
        with open('Database/prefixs.json', 'r') as f:
            prefixes = json.load(f)
            
        prefixes[str(guild.id)] = '-'
        
        with open('Database/prefixs.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
    except:
        prefixes[str(guild.id)] = '-'
        
        with open('Database/prefixs.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

@kory.event
async def on_guild_remove(guild):
    os.remove(f'Database/Servers/{guild.id}.json')
    with open('Database/prefixs.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('Database/prefixs.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        kory.load_extension(f'Cogs.{filename[:-3]}')

if __name__ == '__main__':
    kory.run(token)