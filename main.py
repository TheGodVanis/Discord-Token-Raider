#This will be the token for your "Master Client" (basically, it's the account that runs the selfbot commands.) Make sure not to use this account for spamming. Maed By vanis#6666 And the Vissage Team
#support tax evasion#7713

#This is the prefix for the bot.
prefix = "&"

import requests as req
from threading import Thread as thr
import discord
import random
from colorama import Fore as Color
import os
import datetime
import asyncio



tokens = open("tokens.txt", "r").read().splitlines()
valid = []
invalid = []



os.system('clear')
print("Logging in...")
class MyClient(discord.Client):
  async def on_connect(self):
    os.system('clear')
    print(
f"""
{Color.YELLOW}
             ████████╗   ██████╗  ██████╗ ███╗   ███╗██████╗ 
             ╚══██╔══╝   ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
                ██║█████╗██████╔╝██║   ██║██╔████╔██║██████╔╝
                ██║╚════╝██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗
                ██║      ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝
                ╚═╝      ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ 
                        -made by vanis#6666-

            {Color.WHITE}Discord Version {discord.__version__}
                       
{Color.GREEN}Client logged in as {Color.WHITE}{client.user.name}{Color.GREEN}
{Color.GREEN}You currently have {Color.WHITE}{len(tokens)}{Color.GREEN} tokens stored.
"""
  )





  async def on_message(self, message):
    if message.author != client.user:
      return
    elif message.content == f"{prefix}help":
      await help(message)  
    elif message.content.lower().startswith(f"{prefix}sspam"):
      await sspam(message)
    elif message.content.lower().startswith(f"{prefix}rspam"):
      await rspam(message)
    elif message.content.lower().startswith(f"{prefix}fspam"):
      await fspam(message)
    elif message.content.lower().startswith(f"{prefix}join"):
      await joiner(message)
    elif message.content.lower().startswith(f"{prefix}leave"):
      await leaver(message)
    elif message.content.lower().startswith(f"{prefix}check"):
      await checker(message)
    elif message.content.lower().startswith(f"{prefix}type"):
      await typing(message)
    elif message.content.lower().startswith(f"{prefix}dmspam"):
      await dmspammer(message)
    elif message.content.lower().startswith(f"{prefix}tspam"):
      await spam3(message)












async def dmspammer(message):
  await message.delete()
  spammsg = message.content[len(prefix)+7:]
  id = message.channel.id
  print(f"""
{Color.YELLOW}[{datetime.datetime.utcnow()} UTC]
{Color.GREEN}Spamming user id {Color.WHITE}{id} {Color.GREEN}with {Color.WHITE}{spammsg}
  """)
  for token in tokens:
    req.post(f"https://discord.com/api/users/@me/channels", headers={"authorization": token}, json={"recipient_id": id})
  while True:
    for token in tokens:
      req.post(f"https://discord.com/api/channels/{id}/messages", headers={"authorization": token}, json={"content": spammsg}) 


async def mp(message):
  await message.delete()
  id = message.channel.id()

def msgpur(id, token):
  msgs = req.get(f"https://discordapp.com/api/channels/{id}/messages", headers={"authorization": token}, params = {"limit" : 99999999999999})



async def typing(message):
  await message.delete()
  id = message.channel.id
  for token in tokens:
    req.post(f"https://discord.com/api/channels/{id}/typing", headers={"authorization": token})



async def help(message):
  await message.delete()
  emHelp = discord.Embed(
    title = "TBomb - Help",
    color = discord.Color.gold(),
    description = 
f"""
__**COMMANDS**__
```
{prefix}help
Shows this message.
 
{prefix}join <invite code>
Makes your tokens join a server. Make sure you only use the invite code and not the full link.
 
{prefix}fspam <message>
Makes your tokens the channel the command was sent to.
 
{prefix}sspam <message>
Makes your tokens the channel the command was sent to. This command makes your bots spam slower and it is useful for avoiding antispam bots.
 
{prefix}rspam
Mass spams all roles. Useful if @everyone isn't enabled in the target server.
 
{prefix}check
Checks your tokens.
 
{prefix}type
Triggers typing for all your bots.
 
{prefix}leave
Makes your tokens leave the server the command was sent to.
```
__**STATS**__
```
Tokens connected : {len(tokens)}
Client ID        : {client.user.id}
```
"""
  )
  emHelp.set_footer(text = "Made by Chaotic || Github coming soon")
  await message.channel.send(embed = emHelp, delete_after = 30)





#------------------------------------------------SPAMMERS------------------------------------------------#
def tokenspam(token, id, spammsg):
  while True:
      req.post(f"https://discord.com/api/channels/{id}/messages", headers={"authorization": token}, json={"content": spammsg})

async def fspam(message):
  await message.delete()
  spammsg = message.content[len(prefix)+6:]
  id = message.channel.id
  for token in tokens:
      thr(target=tokenspam, args=(token, id, spammsg)).start()

async def rspam(message):
  await message.delete()
  roles = '\n'.join(role.mention for role in message.guild.roles)
  spammsg = f"""
@everyone
{roles}
"""
  id = message.channel.id
  for token in tokens:
      thr(target=tokenspam, args=(token, id, spammsg)).start()

async def spam3(message):
  await message.delete()
  id = message.content[len(prefix)+6:25]
  spammsg = message.content[len(prefix)+25:]
  while True:
    for token in tokens:
      thr(target = tokenspam, args = (token, id, message)).start()

async def sspam(message):
  await message.delete()
  spammsg = message.content[len(prefix)+6:]
  id = message.channel.id
  print(f"""
{Color.YELLOW}[{datetime.datetime.utcnow()} UTC]
{Color.GREEN}Spamming channel id {Color.WHITE}{id} {Color.GREEN}with {Color.WHITE}{spammsg}
  """)
  while True:
    for token in tokens:
      req.post(f"https://discord.com/api/channels/{id}/messages", headers={"authorization": token}, json={

        "content": spammsg, 
        "tts" : True

        }) 






#------------------------------------------------Checker------------------------------------------------#
async def checker(message):
  await message.delete()
  checked = discord.Embed(title = "TBomb - Token Checker", description = f"```Checking {len(tokens)} tokens...```", color = discord.Color.gold())
  msg = await message.channel.send(embed = checked)
  global valid
  global invalid
  for token in tokens:
        try:
            userdata = req.get("https://discordapp.com/api/users/@me", headers={"authorization": token}).json()
            print(f"{Color.WHITE}{token} {Color.BLACK}: {Color.GREEN}VALID {Color.BLACK}{userdata['username']}#{userdata['discriminator']}")
            valid.append(token)
        except:
            print(f"{Color.WHITE}{token} {Color.BLACK}: {Color.RED}INVALID")
            invalid.append(token)
            continue
        
  print(f"""
{Color.GREEN}Valid tokens   {Color.BLACK}: {Color.YELLOW}{len(valid)}
{Color.RED}Invalid tokens {Color.BLACK}: {Color.YELLOW}{len(invalid)}
""")
  open("tokens.txt", "w").write("\n".join(valid))
  checked = discord.Embed(title = "TBomb - Token Checker", color = discord.Color.gold(), description = f"""
```
Checked {len(tokens)} tokens!

-----RESULTS-----
Valid   : {len(valid)}
Invalid : {len(invalid)}
```
""")
  await msg.edit(embed = checked)
  valid.clear()
  invalid.clear()
  await asyncio.sleep(30)
  await msg.delete()


#-----------------------------------------------Leaver------------------------------------------------#
async def leaver(message):
  await message.delete()
  if isinstance(message.channel, discord.TextChannel):
    id = message.guild.id
    for token in tokens:
      userdata = req.get("https://discord.com/api/users/@me", headers={"authorization": token}).json()
      req.delete(f"https://discord.com/api/users/@me/guilds/{id}", headers={"authorization": token})
      print(f"{Color.WHITE}{userdata['username']}#{userdata['discriminator']}{Color.GREEN} has left {Color.WHITE}{message.guild.name}")
  elif isinstance(message.channel, discord.GroupChannel):
    id = message.channel.id
    for token in tokens:
      userdata = req.get("https://discord.com/api/users/@me", headers={"authorization": token}).json()
      req.delete(f"https://discord.com/api/channels/{id}", headers={"authorization": token})
      print(f"{Color.WHITE}{userdata['username']}#{userdata['discriminator']} {Color.GREEN} has left {Color.WHITE}{message.channel.name}")
  print(" ")

    
#-----------------------------------------------Joiner------------------------------------------------#
async def joiner(message):
  await message.delete()
  invlink = message.content[len(prefix)+5:]
  for token in tokens:
    #thr(target=join, args=(token, invlink)).start()
      userdata = req.get("https://discordapp.com/api/users/@me", headers={"authorization": token}).json()
      req.post(f"https://discord.com/api/invites/{invlink}", headers={"authorization": token})
      print(f"{Color.WHITE}{userdata['username']}#{userdata['discriminator']}{Color.GREEN} has joined {Color.WHITE}{invlink}")
      
  print(" ")

def join(token, invlink):
    try:
      userdata = req.get("https://discord.com/api/users/@me", headers={"authorization": token}).json()
      req.post(f"https://discordapp.com/api/invites/{invlink}", headers={"authorization": token})
      print(f"{Color.WHITE}{userdata['username']}#{userdata['discriminator']}{Color.GREEN} has joined {Color.WHITE}{invlink}")
      return
    except:
      pass




token = os.environ.get('token')
client = MyClient()
client.run(token, bot = False)