import discord
import datetime
import json
from main import *
from discord.ext import commands
from Core.randomcolor import randomcolor

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = randomcolor()
        self.usernames = []

    @commands.command()
    async def ban(self, ctx, user: discord.Member=None, *, reason=None):
        if user is None:
            return await ctx.send('Tag a member to use this commands.')
        elif user == ctx.author:
            return await ctx.send('No permission for ban you.')
        elif user == self.bot:
            return await ctx.send('No permission for ban me.')
        else:
            if reason is None:
                reason = 'Reason no asigned'
            try:
                with open(f'Database/Servers/{ctx.guild.id}.json') as f:
                    data = json.load(f)

                ban_reasons = int(data['server']['bans'])
                ban_reasons += 1
                data['server']['bans'] = ban_reasons
            
                with open(f'Database/Servers/{ctx.guild.id}.json', 'w') as f:
                    json.dump(data, f, indent=4)
                    
                with open('Database/prefixs.json') as f:
                    prefixs = json.load(f)
                    
                prefix = prefixs[str(ctx.guild.id)]

                if data['logs']['use'] == 'true':
                    send_log = await self.bot.fetch_channel(data['logs']['channel'])

                    embed = discord.Embed(
                        color = self.color.get_color(),
                        title = 'Case #{}'.format(data['server']['bans'])
                    )
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.add_field(name='Member banned:', value=user.mention, inline=True)
                    embed.add_field(name='Member ID:', value=user.id, inline=True)
                    embed.add_field(name='Command executed', value='{}ban {}'.format(prefix, user), inline=True)
                    embed.add_field(name='Banned by:', value=ctx.author, inline=True)
                    embed.add_field(name='Author ID:', value=ctx.author.id, inline=True)
                    embed.add_field(name='Reason:', value=reason, inline=True)
                    embed.set_thumbnail(url=user.avatar_url)
                    embed.set_footer(text='Date')
                    await send_log.send(embed=embed)

                await ctx.send(f'`{user}` Banned ✅')
            except:
                ban_em = discord.Embed(
                    color = self.color.get_color(),
                    description = 'The member you are trying to ban has a role higher than mine, to fix this raise my role above the one that this user has.'
                )
                ban_em.set_footer(text='Make sure that you have the necessary permissions to ban members')
                await ctx.send(embed=ban_em)

    @commands.command()
    async def purge(self, ctx, amount: int=None, arg: str=None):
        if arg == 'nuke':
            return 
        else:   
            # Check if the logs are activated and configured
            with open('Database/Servers/{}.json'.format(ctx.guild.id)) as f:
                data = json.load(f)
                
            with open('Database/prefixs.json') as f:
                prefixs = json.load(f)
            
            prefix = prefixs[str(ctx.guild.id)]
                
            if data['logs']['use'] == 'true':
                channel = await self.bot.fetch_channel(data['logs']['channel'])

                data_message = discord.Embed(
                    color = self.color.get_color()
                )
                data_message.timestamp = datetime.datetime.utcnow()
                data_message.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                data_message.add_field(name='Messages deleted:', value='{}'.format(amount), inline=True)
                data_message.add_field(name='Deleted by:', value='{}'.format(self.bot.user.name), inline=True)
                data_message.add_field(name='Author:', value='{}'.format(ctx.author), inline=True)
                data_message.add_field(name='Channel:', value='<#{}>'.format(ctx.channel.id), inline=True)
                data_message.add_field(name='Channel ID:', value=ctx.channel.id)
                if amount is None:
                    data_message.add_field(name='Executed command:', value=f'{prefix}purge', inline=True)
                else:
                    data_message.add_field(name='Executed command:', value=f'{prefix}purge {amount}', inline=True)
                data_message.set_footer(text='Date')
                await channel.send(embed=data_message)
            if amount is None:
                amount = 120
            await ctx.channel.purge(limit=amount)

def setup(bot):
    bot.add_cog(mod(bot=bot))