#Packages/Data

import discord
from discord.ext import commands
from colorama import Fore, Style, Back
import json
from hashlib import sha256
from random import choice as flip
import random
import os
from Functions import CreateCoinflip,JoinJackpot,CreateRPS,JoinCoinflip,CreateJackpot,JoinRPS,LogFlip,FlipCoinOutput,CreateDepoID,CreateFlipID

client = commands.Bot(command_prefix = "$")
JSONFile = open("config.json")
Config = json.load(JSONFile)
Whitelisted = {
    "804779331460923444", #Roll
    "883722477585449000", #Vix
    "644918632446689280" #Brett
}

#Commands

@client.event
async def on_ready():
    print("Bot Online. User: {0.name}".format(client.user))
    await client.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.listening, name = "$commands"))

@client.command()
async def commands(msg):
    embed = discord.Embed(
        title = "List of Commands:",
        color = discord.Color.gold()
    )
    embed.add_field(name = "Main Commands:", value = "$deposit (method)\n$balance\n$payments\n$flipacoin\n $BalanceUser (user)")
    embed.add_field(name = "Gambling Commands:", value = "$CreateFlip (amount)\n$JoinFlip (FlipID)\n$TipUser (User) (Amount)")
    embed.add_field(name = "Moderator Commands:", value = "$AddAmount (Amount) (User)\n$WipeUser (User)")
    embed.set_image(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
    embed.set_author(name="Commands Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
    await msg.send(embed=embed)

@client.command()
async def AddUser(msg, user):
    if str(msg.author.id) in Whitelisted:
        for usermention in msg.message.mentions:
            jsonfile = open("Data.json","r")
            if not str(usermention.id) in jsonfile:
                DataLoading = {f"{usermention.id}": 0}
                with open("Data.json","r+") as jsonfile:
                    jsondata = json.load(jsonfile)
                    jsondata.update(DataLoading)
                    jsonfile.seek(0)
                    json.dump(jsondata,jsonfile)
                jsonfile.close()
                embed = discord.Embed(
                    title = "Player Successfully Added to Database!",
                    color = discord.Color.blurple()
                )
                embed.set_author(name="Moderation Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
                await msg.send(embed=embed)
            else:
                embed = discord.Embed(
                    title = "User Already In Database"
                )
                embed.set_author(name="Moderation Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
                await msg.send(embed=embed)

@client.command()
async def AddAmount(msg,amount,user):
    if str(msg.author.id) in Whitelisted:
        amt = int(amount)
        j_file = open("Data.json","r")
        json_object = json.load(j_file)
        j_file.close()
        for usermention in msg.message.mentions:
            json_object[str(usermention.id)] += amt
        j_file = open("Data.json", "w")
        json.dump(json_object,j_file)
        j_file.close()
        embed = discord.Embed(
            title = f"Successfully Added {amt} to Balance",
            color = discord.Color.blurple()
        )
        embed.set_author(name="Moderation Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
        embed.add_field(name = "Moderator: {0.author.name}".format(msg), value = f"User: {usermention.name}")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
        await msg.send(embed=embed)
    else:
        embed = discord.Embed(
            title = "You are not authorized to do this action.",
            color = discord.Color.blurple()
        )
        embed.set_author(name="Moderation Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
        await msg.send(embed=embed)
@client.command()
async def flipacoin(msg):
    embed = discord.Embed(
        title = "Flip a Coin!",
        color = discord.Color.gold()
    )
    embed.add_field(name = "Your Coin Landed on:", value = FlipCoinOutput())
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
    embed.set_author(name="Coinflip Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
    await msg.send(embed=embed)

@client.command()
async def deposit(msg,method):
    if method.lower() == "ltc" or method.lower() == "litecoin":
        embed = discord.Embed(
            title = "Deposit with Litecoin",
            color = discord.Color.light_gray()
        )
        embed.set_author(name="Deposit Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
        embed.add_field(name = "Deposit ID: " + CreateDepoID(), value = "LTC Address: " + Config["current-ltc"], inline=True)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
        await msg.send(embed=embed)
    elif method.lower() == "btc" or method.lower() == "bitcoin":
        embed = discord.Embed(
            title = "Deposit with Bitcoin",
            color = discord.Color.gold()
        )
        embed.set_author(name="Deposit Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
        embed.add_field(name = "Deposit ID: " + CreateDepoID(), value = "BTC Address: " + Config["current-btc"], inline=True)
        await msg.send(embed=embed)
    elif method.lower() == "eth" or method.lower() == "ethereum":
        embed = discord.Embed(
            title = "Deposit with Ethereum",
            color = discord.Color.blurple()
        )
        embed.set_author(name="Deposit Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
        embed.add_field(name = "Deposit ID: " + CreateDepoID(), value = "ETH Address: " + Config["current-eth"], inline=True)
        await msg.send(embed=embed)
    elif method.lower() == "cashapp":
        embed = discord.Embed(
            title = "Deposit with Cashapp",
            color = discord.Color.green()
        )
        embed.set_author(name="Deposit Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
        embed.add_field(name = "Deposit ID: " + CreateDepoID(), value = "Cashtag: " + Config["current-cashapp"], inline=True)
        await msg.send(embed=embed)
    else:
        await msg.send("Deposit Method Error.")

@client.command()
async def balance(msg):
    embed = discord.Embed(
        title = "Balance",
        color = discord.Color.gold()
    )
    j_file = open("Data.json","r")
    json_object = json.load(j_file)
    j_file.close()
    embed.set_author(name="Balance Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
    embed.add_field(name=f"${json_object[str(msg.author.id)]}" + " Coins", value = "Tip: Make a ticket to Withdraw your balance.")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
    await msg.send(embed=embed)

@client.command()
async def payments(msg):
    embed = discord.Embed(
        title = "Accepted Deposit Methods",
        color = discord.Color.gold()
    )
    embed.set_author(name="Deposit Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
    embed.add_field(name = "Hint: Type $deposit (method) to purchase coins", value = "Cashapp\nBTC\nETH\nLTC")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
    await msg.send(embed=embed)

@client.command()
async def CreateFlip(msg,amount):
    j_file = open("Data.json","r")
    json_object = json.load(j_file)
    j_file.close()
    if int(amount) <= int(json_object[str(msg.author.id)]) and int(amount) > 0:
        j_file = open("Data.json","r")
        json_object = json.load(j_file)
        j_file.close()
        json_object[str(msg.author.id)] -= int(amount)
        j_file = open("Data.json", "w")
        json.dump(json_object,j_file)
        j_file.close()
        embed = discord.Embed(
            title = f"{msg.author.name}#{msg.author.discriminator}'s Coinflip",
            color = discord.Color.gold()
        )
        embed.set_author(name="Flip Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
        FlipID1 = CreateFlipID()
        with open("Flips.json","r+") as jsonfile:
            DataJS = {f"{FlipID1}": f"{int(amount)}",f"{FlipID1}ID": f"{msg.author.id}"}
            jsondata = json.load(jsonfile)
            jsondata.update(DataJS)
            jsonfile.seek(0)
            json.dump(jsondata,jsonfile)
        embed.add_field(name = f"Amount: ${str(amount)}", value = f"FlipID: {FlipID1}")
        embed.add_field(name = f"UserID: {msg.author.id}",value = f"Ping: {msg.author.mention}")
        await msg.send(embed=embed)
    else:
        await msg.send("User Balance Insufficient / Bot Error")

@client.command()
async def JoinFlip(msg,id):
    FlipAmount = open("Flips.json","r")
    AmtJSON = json.load(FlipAmount)
    FlipAmount.close()
    UserData = open("Data.json","r")
    JSONData = json.load(UserData)
    UserData.close()
    JoinID = str(msg.author.id)
    FlipID = str(id)
    FlipUserID = FlipID + "ID"
    FlipUser = await client.fetch_user(AmtJSON[FlipUserID])
    RandomTable = [FlipUser,msg.author]
    if int(AmtJSON[FlipID]) <= int(JSONData[JoinID]):
        j_file = open("Data.json","r")
        json_object = json.load(j_file)
        j_file.close()
        json_object[str(msg.author.id)] -= int(AmtJSON[FlipID])
        j_file = open("Data.json", "w")
        json.dump(json_object,j_file)
        j_file.close()
        embed = discord.Embed(
            title = f"{FlipUser.name}#{FlipUser.discriminator}'s Coinflip",
            color = discord.Color.gold()
        )
        Winner = random.choice(RandomTable)
        embed.add_field(name = "Amount", value = f"${int(AmtJSON[FlipID])}")
        embed.add_field(name = "Player 1:", value = FlipUser.mention)
        embed.add_field(name = "Player 2", value = msg.author.mention)
        embed.add_field(name = "Tip:", value = "use $commands for a list of cmds")
        embed.add_field(name = "Outcome", value = f"{Winner.mention}")
        embed.set_author(name="Flip Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
        await msg.send(embed=embed)
        j_file = open("Data.json","r")
        json_object = json.load(j_file)
        j_file.close()
        json_object[str(Winner.id)] += int(AmtJSON[FlipID]) * 1.9
        j_file = open("Data.json", "w")
        json.dump(json_object,j_file)
        j_file.close()
        j_file = open("Flips.json","r")
        json_object = json.load(j_file)
        j_file.close()
        del json_object[FlipUserID]
        del json_object[FlipID]
        j_file = open("Data.json", "w")
        json.dump(json_object,j_file)
        j_file.close()
    else:
        await msg.send("Not Available / Not Enough Balance")
@client.command()
async def TipUser(msg,userid,amount):
    amt = int(amount)
    UserData = open("Data.json","r")
    JSONData = json.load(UserData)
    if amt <= int(JSONData[f"{msg.author.id}"]) and amt > 0:
        j_file = open("Data.json","r")
        json_object = json.load(j_file)
        j_file.close()
        for usermention in msg.message.mentions:
            json_object[str(usermention.id)] += amt
            json_object[str(msg.author.id)] -= amt
        j_file = open("Data.json", "w")
        json.dump(json_object,j_file)
        j_file.close()
        embed = discord.Embed(
           title = f"{msg.author.name} sent a tip.",
           color = discord.Color.blurple()
        )
        embed.set_author(name="Tips Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
        embed.add_field(name = f"Amount: ${str(amt)}", value = f"Recipient: {usermention.name}")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
        await msg.send(embed=embed)
    else:
        await msg.send("Not Available / Not Enough Balance")
@client.command()
async def WipeUser(msg,user):
    if str(msg.author.id) in Whitelisted:
        amt = 0
        j_file = open("Data.json","r")
        json_object = json.load(j_file)
        j_file.close()
        for usermention in msg.message.mentions:
            json_object[str(usermention.id)] = amt
        j_file = open("Data.json", "w")
        json.dump(json_object,j_file)
        j_file.close()
        embed = discord.Embed(
            title = f"Successfully Wiped User {usermention.name}",
            color = discord.Color.blurple()
        )
        embed.set_author(name="Moderation Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
        embed.add_field(name = "Moderator: {0.author.name}".format(msg), value = f"User: {usermention.name}")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
        await msg.send(embed=embed)
    else:
        embed = discord.Embed(
            title = "You are not authorized to do this action.",
            color = discord.Color.blurple()
        )
        embed.set_author(name="Moderation Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
        await msg.send(embed=embed)

@client.command()
async def BalanceUser(msg):
    embed = discord.Embed(
        title = "Balance",
        color = discord.Color.gold()
    )
    for usermention in msg.message.mentions:
        usermentionid = usermention.id
    j_file = open("Data.json","r")
    json_object = json.load(j_file)
    j_file.close()
    embed.set_author(name="Balance Manager", icon_url="https://cdn.discordapp.com/attachments/952576761697292319/952693662364631091/istockphoto-1209243460-612x612.jpg")
    embed.add_field(name=f"${json_object[str(usermentionid)]}" + " Coins", value = "Tip: Make a ticket to Withdraw your balance.")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/939693121250418780/952429451453554718/istockphoto-1209243460-612x612.jpg?width=427&height=427")
    await msg.send(embed=embed)

client.run(Config["token"])
