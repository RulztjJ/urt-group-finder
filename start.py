import requests
import os
import sys
import fade


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

discord = requests.get("https://raw.githubusercontent.com/underatedtails/roblox-group-finder/main/urtcustom.json")
discord_data = discord.json()

text = f'''

  █    ██  ██▀███  ▄▄▄█████▓     ▄████  ██▀███   ▒█████   █    ██  ██▓███       █████▒ ██▓ ███▄    █ ▓█████▄ ▓█████  ██▀███  
  ██  ▓██▒▓██ ▒ ██▒▓  ██▒ ▓▒    ██▒ ▀█▒▓██ ▒ ██▒▒██▒  ██▒ ██  ▓██▒▓██░  ██▒   ▓██   ▒ ▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
 ▓██  ▒██░▓██ ░▄█ ▒▒ ▓██░ ▒░   ▒██░▄▄▄░▓██ ░▄█ ▒▒██░  ██▒▓██  ▒██░▓██░ ██▓▒   ▒████ ░ ▒██▒▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
 ▓▓█  ░██░▒██▀▀█▄  ░ ▓██▓ ░    ░▓█  ██▓▒██▀▀█▄  ▒██   ██░▓▓█  ░██░▒██▄█▓▒ ▒   ░▓█▒  ░ ░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
 ▒▒█████▓ ░██▓ ▒██▒  ▒██▒ ░    ░▒▓███▀▒░██▓ ▒██▒░ ████▓▒░▒▒█████▓ ▒██▒ ░  ░   ░▒█░    ░██░▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
 ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░  ▒ ░░       ░▒   ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░    ▒ ░    ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ░░▒░ ░ ░   ░▒ ░ ▒░    ░         ░   ░   ░▒ ░ ▒░  ░ ▒ ▒░ ░░▒░ ░ ░ ░▒ ░         ░       ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
  ░░░ ░ ░   ░░   ░   ░         ░ ░   ░   ░░   ░ ░ ░ ░ ▒   ░░░ ░ ░ ░░           ░ ░     ▒ ░   ░   ░ ░  ░ ░  ░    ░     ░░   ░ 
    ░        ░                       ░    ░         ░ ░     ░                          ░           ░    ░       ░  ░   ░       by URT
                                                                                                     ░                       

# Github: https://github.com/underratedtails
# Discord: {discord_data.get('discord')}

'''

def finder(text):
    cls()
    print(fade.purpleblue(text))
    webhook = input(fade.purpleblue("Enter your webhook: "))
    cls()
    print(fade.purpleblue(text))
    os.system(f'py bot.py -p proxies.txt --webhook-url {webhook}')

def option(text):   
    cls()
    print(fade.purpleblue(text))
    options = int(input(fade.purpleblue('# 1 - Start\n# 2 - Exit\n>> ')))
    if options == 1:
        finder(text)
    elif options == 2:
        sys.exit()


option(text)