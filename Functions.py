from random import choice as flip
import random
import discord

def CreateCoinflip():
    pass

def CreateJackpot():
    pass

def CreateRPS():
    pass

def JoinCoinflip():
    pass

def JoinJackpot():
    pass

def JoinRPS():
    pass

def CreateFlipID():
    return str(random.randrange(1052015621,9090825621))

def CreateDepoID():
    return str(random.randrange(101011,909099))

def LogFlip(user, id, result):
    embed = discord.Embed(
        title = "Coinflip By Player: {0}".format(user),
        color = discord.Color.gold()
    )
    embed.add_field("Results: {0}".format(result))
    return embed

def FlipCoinOutput():
    SidesTable = ["Heads", "Tails"]
    return flip(SidesTable)
