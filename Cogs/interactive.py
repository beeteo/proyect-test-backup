import discord
import os
import requests
import random
import json
from PIL import Image
from io import BytesIO
from discord.ext import commands
from Core.relationper import percentage
from Core.circleimage import Circle
from Core.randomcolor import randomcolor
from Core.emojis_select import Emojiselect

class interaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.percentage = percentage()
        self.circle = Circle()
        self.color = randomcolor()
        self.emojis = Emojiselect()
        self.base_url = 'https://nekos.best/api/v2/'

    def get_gif(self, category):
        response = []

        data = requests.get(
            url=self.base_url + category
        ).json()

        response.append(data['results'][0]['anime_name'])
        response.append(data['results'][0]['url'])
        response.append(category)
        return response

    @commands.command()
    async def ship(self, ctx, user: discord.Member=None):

        if user is None:
            return await ctx.send('Need tag a user')
        else:
            filename = f"Sources/Images/Created/{ctx.author.id}-{user.id}.png"
            background = Image.open("Sources/Images/Template.png")
            
            asset = ctx.author.avatar_url_as(size=1024)
            asset2 = user.avatar_url_as(size=1024)
            data = BytesIO(await asset.read())
            data2 = BytesIO(await asset2.read())
            pfp = Image.open(data).convert("RGBA")
            pfp = self.circle.circle(pfp)
            pfp = pfp.resize((120,120))
            pfp2 = Image.open(data2).convert("RGBA")
            pfp2 = self.circle.circle(pfp2)
            pfp2 = pfp2.resize((120,120))
            background.paste(pfp, (100,50), pfp)
            background.paste(pfp2, (560,50), pfp2)
            background.save(filename)
            
            embed = discord.Embed()
            embed.title = f'{ctx.author} + {user}'
            embed.color = 0xffa6f9
            embed.description = f'{self.percentage.relation_percentage()}**'
            await ctx.send(embed=embed)
            await ctx.send(file=discord.File(f'Sources/Images/Created/{ctx.author.id}-{user.id}.png'))
            os.remove(f'Sources/Images/Created/{ctx.author.id}-{user.id}.png')

    @commands.command()
    async def kiss(self, ctx, user: discord.Member=None):
        if user is None:
            return await ctx.send('Need tag a user')
        else:
            data = self.get_gif(category='kiss')
            emoji = self.emojis.get_emoji(category='kiss')
            embed = discord.Embed(
                color = self.color.get_color(),
                description = f'{ctx.author.mention} **Kissed** {user.mention} {emoji}'
            )
            embed.set_image(url=data[1])
            embed.set_footer(text='Anime: ' + data[0])
            await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, user: discord.Member=None):
        if user is None:
            return await ctx.send('Need tag a user')
        else:
            data = self.get_gif(category='hug')
            embed = discord.Embed()
            embed.description = f'{ctx.author.mention} **Gave** {user.mention} **a hug**'
            embed.color = self.color.get_color()
            embed.set_image(url=data[1])
            embed.set_footer(text='Anime: {}'.format(data[0]))
            await ctx.send(embed=embed)

    @commands.command()
    async def blush(self, ctx):
        data = self.get_gif(category='blush')
        embed = discord.Embed()
        embed.description = f'{ctx.author.mention} _blushed_'
        embed.color = self.color.get_color()
        embed.set_image(url=data[1])
        embed.set_footer(text='Anime: {}'.format(data[0]))
        await ctx.send(embed=embed)        

    @commands.command()
    async def dance(self, ctx):
        data = self.get_gif(category='dance')
        embed = discord.Embed()
        embed.description = f'{ctx.author.mention} _Began to dance_'
        embed.color = self.color.get_color()
        embed.set_image(url=data[1])
        embed.set_footer(text='Anime: {}'.format(data[0]))
        await ctx.send(embed=embed)   

    @commands.command()
    async def bored(self, ctx):
        data = self.get_gif(category='bored')
        embed = discord.Embed()
        embed.description = f'{ctx.author.mention} Is bored ;/'
        embed.color = self.color.get_color()
        embed.set_image(url=data[1])
        embed.set_footer(text='Anime: {}'.format(data[0]))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(interaction(bot=bot))