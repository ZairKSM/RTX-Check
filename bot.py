import discord
from discord.ext import commands, tasks
from Nvidia import CheckNvidia
from time import *
import json
import os
from os import environ

TOKEN = environ["TOKEN"]
def init():
    with open("config.json", "r") as file:
        return json.load(file)

config=init()
url='https://shop.nvidia.com/fr-fr/geforce/store/?page=1&limit=9&locale=fr-fr&gpu=RTX%203080,RTX%203070,RTX%203060%20Ti,RTX%203060&manufacturer=NVIDIA&manufacturer_filter=NVIDIA~3,ACER~0,ALIENWARE~0,ASUS~8,DELL~0,EVGA~13,GAINWARD~2,GIGABYTE~8,HP~0,LENOVO~0,MSI~17,PNY~5,RAZER~0,ZOTAC~8'


client = commands.Bot(command_prefix=config["prefix"])

@client.event
async def on_ready():

    memberCount = client.get_all_members()
    print('We have logged in as {0.user},'.format(client))

    await client.change_presence(activity=discord.Streaming(name="Market Price checker", url="https://www.twitch.tv/something"))
    # Background
    notifsPrice.start()


@tasks.loop(seconds=60)

async def notifsPrice():
    notifsChannel = client.get_channel(756542448716480532)
    RTX = CheckNvidia()
    for k in range(len(RTX)):
        jsondata = eval(RTX[k][4].replace("true", "True").replace("false", "False").replace("null", "None"))

        if RTX[k][3] != "RUPTURE DE STOCK":
            status = f"BUYYYYYYYYY!!\n[Link1]({jsondata[0]['purchaseLink']}) And [Link2]({jsondata[0]['directPurchaseLink']})"
            embed = discord.Embed(title=f"Check {RTX[k][0]} ", url=url, color=discord.Colour.dark_blue())
            embed.add_field(name="**Status :**", value=status, inline=False)
            embed.add_field(name="**Price :**", value=RTX[k][2], inline=False)
            embed.set_image(url=RTX[k][1])
            embed.set_footer(text="Checker by Zaïr_KSM#4502")

            await notifsChannel.send(embed=embed)
        else:
            print(f'T')


@client.command()
async def check(channel,*,args = None):
    if args is not None:
        args= args.split()


        if args[0]=="3080":
            await channel.send("EN COUR DE CHARGEMENT")
            RTX = CheckNvidia()
            for i in RTX:
                print(i)
            if RTX[0][3]!= "RUPTURE DE STOCK":
                jsondata = eval(RTX[0][4].replace("true", "True").replace("false", "False").replace("null", "None"))
                status=f"BUYYYYYYYYY!!\n[Link1]({jsondata[0]['purchaseLink']}) And [Link2]({jsondata[0]['directPurchaseLink']})"
            else :
                status = RTX[0][3]
            embed = discord.Embed(title="Check Nvidia RTX 3080",url=url ,color= discord.Colour.dark_blue())
            embed.add_field(name="**Status :**", value=status, inline=False)
            embed.add_field(name="**Price :**", value=RTX[0][2], inline=False)
            embed.set_image(url=RTX[0][1])
            embed.set_footer(text="Checker by Zaïr_KSM#4502")
            await channel.send(embed=embed)
        elif args[0]=="3070":
            RTX = CheckNvidia()
            for i in RTX:
                print(i)
            if RTX[1][3]!= "RUPTURE DE STOCK":
                jsondata = eval(RTX[1][4].replace("true", "True").replace("false", "False").replace("null", "None"))
                status=f"BUYYYYYYYYY!!\n[Link1]({jsondata[0]['purchaseLink']}) And [Link2]({jsondata[0]['directPurchaseLink']})"
            else :
                status = RTX[1][3]
            embed = discord.Embed(title="Check Nvidia RTX 3070", url=url, color=discord.Colour.dark_blue())
            embed.add_field(name="**Status :**", value=status, inline=False)
            embed.add_field(name="**Price :**", value=RTX[1][2], inline=False)
            embed.set_image(url=RTX[1][1])
            embed.set_footer(text="Checker by Zaïr_KSM#4502")
            await channel.send(embed=embed)

        elif args[0]=="3060Ti":
            RTX = CheckNvidia()
            for i in RTX:
                print(i)
            if RTX[2][3]!= "RUPTURE DE STOCK":
                jsondata = eval(RTX[2][4].replace("true", "True").replace("false", "False").replace("null", "None"))
                status=f"BUYYYYYYYYY!!\n[Link1]({jsondata[0]['purchaseLink']}) And [Link2]({jsondata[0]['directPurchaseLink']})"
            else :
                status = RTX[2][3]
            embed = discord.Embed(title="Check Nvidia RTX 3060 Ti", url=url, color=discord.Colour.dark_blue())
            embed.add_field(name="**Status :**", value=status, inline=False)
            embed.add_field(name="**Price :**", value=RTX[2][2], inline=False)
            embed.set_image(url=RTX[2][1])
            embed.set_footer(text="Checker by Zaïr_KSM#4502")
            await channel.send(embed=embed)
        elif args[0]=="all":
            RTX = CheckNvidia()
            for i in RTX:
                print(i)
            for i in range(len(RTX)):

                if RTX[i][3]!= "RUPTURE DE STOCK":
                    jsondata = eval(RTX[i][4].replace("true", "True").replace("false", "False").replace("null", "None"))
                    status=f"BUYYYYYYYYY!!\n[Link1]({jsondata[0]['purchaseLink']}) And [Link2]({jsondata[0]['directPurchaseLink']})"
                else :
                    status = RTX[2][3]
                embed = discord.Embed(title=f"Check {RTX[i][0]}", url=url, color=discord.Colour.dark_blue())
                embed.add_field(name="**Status :**", value=status, inline=False)
                embed.add_field(name="**Price :**", value=RTX[i][2], inline=False)
                embed.set_image(url=RTX[i][1])
                embed.set_footer(text="Checker by Zaïr_KSM#4502")
                await channel.send(embed=embed)
        else:
            await channel.send("Les arguments possibles sont uniquement: 3060Ti , 3070, 3080 ou all")


    else:
        await channel.send("Les arguments possibles sont uniquement: 3060Ti , 3070, 3080 ou all")
client.run(TOKEN)