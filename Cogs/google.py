import discord
import random
from googleapiclient.discovery import build
from googletrans import Translator
from discord.ext import commands
from Core.randomcolor import randomcolor

class searches(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.google_key = 'google api key'
        self.color = randomcolor()

    def get_service(self):
        return build("youtube", "v3", developerKey=self.google_key)

    @commands.command()
    async def ggsearch(self, ctx, *, search):
        if ctx.channel.is_nsfw():
            ran = random.randint(0, 0)
            
            resource = build("customsearch", "v1", developerKey=self.google_key).cse()
            result = resource.list(
                q=f"{search}", cx="ab93645237db9c697", searchType="image"
            ).execute()
            
            url = result["items"][ran]["link"]
            
            embed = discord.Embed(
                title = result['items'][ran]['title'],
                color = self.color.get_color(),
                description = f"[{result['items'][ran]['title']}]({result['items'][ran]['link']})"
            )
            embed.set_image(url=url)
            msg = await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                color = self.color.get_color(),
                description = 'To use the command you need to be in a channel with NSFW category'
            )
            embed.set_footer(text='Why? This is to avoid +18 searches that can be sensitive to other users, and with the NSFW category they take into account what they can see or what they are going to search for.')
            await ctx.send(embed=embed)

    @commands.command()
    async def translate(self, ctx, language, *, message):

        translator = Translator()
        translation = translator.translate(message, dest=language)

        embed = discord.Embed(
            color = self.color.get_color(),
            description = f'''**Message:**\n```{message}```\n**Message translate:**\n```{translation.text}```
            '''
        )
        embed.set_author(name='Google Translate', icon_url=r'https://icon-library.com/images/google-icon/google-icon-26.jpg')
        embed.set_footer(text='Translate to: {}'.format(language))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(searches(bot=bot))