#A Discord bot to add players to, and then randomly select characters for everyone to play.
#Wrote and run on a Raspberry Pi.
#Author: Scott Mitchinson

import discord
import random
from discord.ext import commands

TOKEN = ''	#Your Discord Token Here
PlayerList = [ ];
Attackers = ["Sledge", "Thatcher", "Ash", "Thermite", "Twitch", "Montagne", "Glaz",
             "Blitz", "IQ", "Buck", "Blackbeard", "Capitao", "Hibana", "Jackal",
             "Zofia", "Dokkaebi", "Lion", "Finka", "Maverick", "Nomad", "Recruit",
			 "Players Choice"];

Defenders = ["Smoke", "Mute", "Castle", "Pulse", "Doc", "Rook", "Kapkan", "Tachanka",
             "Frost", "Valkyrie", "Caveira", "Echo", "Mira", "Lesion", "Ela",
             "Alibi", "Clash", "Kaid", "Recruit", "Players Choice"];


description = '''Siege Bot'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('-----')

#Used through Discord to add player to the list
#Example use:
# ?play Scott
@bot.command()
async def play(name):
	if len(PlayerList) >= 5:
		await bot.say("There are Already 5 People Playing Siege")
	else:
		PlayerList.append(name)
		await bot.say("Added Player {} to the List!".format(name))

#Takes a player off the player list based on name
#Example use:
# ?logoff Scott
@bot.command()
async def logoff(name):
	if name in PlayerList:
		PlayerList.remove(name)
		await bot.say("Player {} Removed from Play".format(name))
	else:
		await bot.say("Player {} is not Playing".format(name))

#Bot will say a random Siege Attacker
@bot.command()
async def newAtt():
	await bot.say(Attackers[random.randint(0, len(Attackers) - 1)])

#Bot will say a random Siege Defender
@bot.command()
async def newDef():
	await bot.say(Defenders[random.randint(0, len(Defenders) - 1)])

#Will output every player in the player list with a random Attacker given to them
@bot.command()
async def attack():
	message = []
	Ops = []
	for player in PlayerList:
		contains = False
		newOp = Attackers[random.randint(0, len(Attackers) - 1)]
		while contains == False:
			if newOp not in Ops:
				Ops.append(newOp)
				contains = True
			else:
				newOp = Attackers[random.randint(0, len(Attackers) - 1)];
	count = 0
	for player in PlayerList:
		message.append("{} -- {}\n".format(player, Ops[count]))
		count = count + 1
	await bot.say(''.join(message))

#Will output every player in the player list with a random Defender given to them
@bot.command()
async def defend():
	message = []
	Ops = []
	for player in PlayerList:
		contains = False
		newOp = Defenders[random.randint(0, len(Defenders) - 1)]
		while contains == False:
			if newOp not in Ops:
				Ops.append(newOp)
				contains = True
			else:
				newOp = Defenders[random.randint(0, len(Defenders) - 1)];
	count = 0
	for player in PlayerList:
		message.append("{} -- {}\n".format(player, Ops[count]))
		count = count + 1
	await bot.say(''.join(message))

bot.run(TOKEN)