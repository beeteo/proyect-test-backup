import discord
import json
import time
from discord.ext import commands
from Core.randomcolor import randomcolor

class setupp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = randomcolor()

    @commands.command()
    async def setuplogs(self, ctx):
        embed = discord.Embed(
            description = 'Hello, this command is to configure the logs to this enter [**bans, expulsions, mutes and more**]\n\nJust to configure, write in the chat how you want your configuration with the options that will be given to you.\n\nYou only have 1 minute for each question\n\nNote: if you run out of time you will have to start over.\n\n\n**1: In which channel would you like to receive these notifications? / logs**\Mention the channel, example: <#{}>'.format(ctx.channel.id),
            color = self.color.get_color()
        )
        await ctx.send(embed=embed)
        
        def check(m):
            return ctx.author == m.author
        try:
            msg = await self.bot.wait_for('message', timeout=60.0, check=check)
            channel_id = int(msg.content[2:-1])
        except TimeoutError:
            return
        try:
            embed = discord.Embed(
                description = '**2: How do you want the logs to be sent [Embed or text]**',
                color = self.color.get_color()
            )
            await ctx.send(embed=embed)

            msg2 = await self.bot.wait_for('message', timeout=60.0, check=check)

            if 'embed' or 'Embed' in msg2.content:
                embedmode = 'true'
            elif 'text' or 'Text' in msg2.content:
                embedmode = 'false'
            
            data = {
                "server": {
                    "name": str(ctx.guild.name),
                    "id": str(ctx.guild.id)
                },
                "logs": {
                    "use": "true",
                    "channel": int(channel_id),
                    "text": {
                        "embedmode": str(embedmode)
                    }
                }
            }
            omg = await ctx.send('Saving changes...')
            time.sleep(2)

            with open(f'Database/Servers/{ctx.guild.id}.json', 'w') as f:
                json.dump(data, f, indent=4)
            await ctx.send('Done!')
            await ctx.author.send(file=discord.File(f'Database/Servers/{ctx.guild.id}.json'))
        except TimeoutError:
            return

    @commands.command()
    async def setupstatus(self, ctx, status=None):
        with open('Database/Servers/{}.json'.format(ctx.guild.id)) as f:
            data = json.load(f)

        if status is None:
            status_logs = data['logs']['use']
            logs_id = data['logs']['channel']
            channel = await self.bot.fetch_channel(data['logs']['channel'])
            if status_logs == 'true':
                embed = discord.Embed(
                    color = self.color.get_color(),
                    description = f'Logs: {status_logs}\nChannel: {channel.mention}\nChannel ID: {logs_id}'
                )
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(setupp(bot=bot))