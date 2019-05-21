# Siege-Discord-Bot

A bot to pick random Rainbow Six: Siege Operators based on a list of players added by users.
This bot was wrote and used on a Raspberry Pi. This was my first ever use of python, so code is not perfect.

## Using the Bot in Discord

The bot uses a questionmark as a prefix, however this can be changed in the code.
The Discord.py library has been used to allow the bot to run on discord.
The bot features a few simple commands to work the bot:

### ?play [name]

Adds a player to the player list.

### ?logoff [name]

Searches through the player list, will remove if parameter matches name in the list.

### ?attack

Every player in the player list is given a random attacker.

### ?defender

Every player in the player list is given a random defender.

### ?newAtt and ?newDef

Will given a random attacker or defender based on which command is used. Can be used if a player does not own the operator.

## Acknowledgments

https://www.gngrninja.com/code/2017/3/24/python-create-discord-bot-on-raspberry-pi
This guide was a great help in setting up this discord bot.
