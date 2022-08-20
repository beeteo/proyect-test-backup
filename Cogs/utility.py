import discord
import requests
import random
import string
from discord.ext import commands
from Core.randomcolor import randomcolor

class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = randomcolor()

    def genpassword(self, length):
        password_data = []

        letters = string.ascii_lowercase
        result = ''.join(random.choice(letters) for i in range(length))
        password_data.append(result)
        password_data.append(length)

        return password_data

    @commands.command()
    async def gen_password(self, ctx, length: int):
        
        data = self.genpassword(length=length)

        await ctx.reply('Password length: {} | `{}`'.format(length, data[0]))

def setup(bot):
    bot.add_cog(utility(bot=bot))