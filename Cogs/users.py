import discord
import requests
import os, sys
import random
from Core.randomcolor import randomcolor
from discord.ext import commands, tasks

class users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = randomcolor()

    @commands.command()
    async def avatar(self, ctx, user: discord.Member=None):
        if (user) is None:
            user = ctx.author
        else:
            user = ctx.author
        avatar = str(user.avatar_url_as(static_format="png", size=1024))

        embed = discord.Embed(
            title = user,
            color = self.color.get_color(),
            description = f'[Full Avatar]({avatar})'
        )
        embed.set_image(url=avatar)
        await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(users(bot=bot))