import discord, asyncio
from discord.ext import commands
from discord.ext.commands import Bot


class QuickPoll(commands.Cog):
	""""""

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def quickpoll(self, ctx, question, *options: str):
		if len(options) <= 1:
			await ctx.send('You need more than one option to make a poll!')
			return
		if len(options) > 10:
			await ctx.send('You cannot make a poll for more than 10 things!')
			return

		if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
			reactions = ['✅', '❌']
		else:
			reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

		description = []
		for x, option in enumerate(options):
			description += '\n {} {}'.format(reactions[x], option)
		embed = discord.Embed(title=question, description=''.join(description))
		react_message = await ctx.send(embed=embed)
		for reaction in reactions[:len(options)]:
			await react_message.add_reaction(reaction)
		embed.set_footer(text='Poll ID: {}'.format(react_message.id))
		#await react_message.edit(content=react_message, embed=embed)
def setup(bot):
	bot.add_cog(QuickPoll(bot))