#!/usr/bin/python3

import discord
from discord.ext import commands

def readtoken():
	with open("token", "r") as f:
		content = f.readlines()
	TOKEN = content[0]
	return(TOKEN)

TOKEN = readtoken()

prefix = '?'
channel = 371985665929379842

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(commands.when_mentioned_or(prefix),intents=intents)

async def moveroleto(servname,chanid,roleid):
	clowns = []
	guildid = discord.utils.get(client.guilds, name=servname).id
	guild = client.get_guild(guildid)
	vchannel = guild.get_channel(chanid)
	vchannelusr = list(vchannel.voice_states.keys())
	#get the user id in the channel
	#print(vchannelusr)
	#todo : if userid in role members then, if userid in channel then disconnect
	guirole = str(guild.get_role(roleid).members)
	#print(guirole)
	for i in vchannelusr:
		if guirole.find(str(i)) is not -1:
			clowns.append(i)
	print(clowns)
	for i in clowns:
		member = guild.get_member(i)
		print(member)
		await member.move_to(None, reason="clown")

@client.event
async def on_ready():
	print(f'{client.user} is now online!!')
	await moveroleto("Hoko's server",726821752700928020,794035241425043496)
	
@client.event
async def on_connect():
	watching = discord.Activity(type=discord.ActivityType.competing, name='?help')
	await client.change_presence(activity=watching)

@client.event
async def on_member_join(member):
	await client.get_channel(channel).send(f"{member.mention} vient de rejoindre dites lui coucou fdp!!")

@client.event
async def on_member_remove(member):
	await client.get_channel(channel).send(f"{member.mention} vient de nous quitter va te faire foutre salope tu va pas nous manquer!!")
	
@client.event
async def on_message(message):
	print(f"'{message.content}' was sent by {message.author}")

client.run(TOKEN)
