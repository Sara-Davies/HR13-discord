import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()

#intents = discord.Intents.all()
bot = commands.Bot(command_prefi = commands.when_mentioned_or("!"), intents=intents)

@bot.event
async def on_ready():
	print(f'Bot {bot.user} is online! Id: {bot.user.id}')

async def main():
	await bot.start(MTE1NDk5NDIwNTIyODI3MzcxNA.GjB3nW.NVoUT6OB7akftAv0Te58zBld7tJV-ntPZPbFLk)

@bot.command()
async def timer(ctx: commands.Context, time: int):
	await asyncio.sleep(time)
	await ctx.send("your time is up!")


asyncio.run(main())