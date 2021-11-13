import discord
from discord.ext import commands 
from discord.ext.commands import has_permissions, MissingPermissions 
from discord import *


bot = commands.Bot(command_prefix = ["-"])

"""
@bot.event
async def on_message(message):
	print(message.content)
	print(message.author)
	fh = open('C:/Users/Marwan/Desktop/pyscripts/logs.txt', 'a')
	fh.write(message.author.name)
	fh.write(": ")
	fh.write(message.content + "\n")

	await bot.process_commands(message)
"""
snipe_message_content = None
snipe_message_author = None

@bot.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    # Variables outside a function have to be declared as global in order to be changed

    snipe_message_content = message.content
    snipe_message_author = message.author


@bot.command()
async def snipe(ctx):
	await ctx.send(f"**```From: {snipe_message_author} \nMessage: {snipe_message_content}```**")
	

'''
@bot.command()
@has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
	await member.kick(reason = reason)
'''

@bot.command()
async def test(ctx):
	await ctx.send('Working')







bot.run('OTA2MzYzMTAxODQ5NDc3MTU1.YYXiag.iALJK7w78XIWSmQdvLL081MSMZI')