




#color libs
from lib2to3.pgen2 import token
import colorama
from colorama import Fore, Back, Style


colorama.init(autoreset=True)

#webhook libs
from dhooks import Webhook
from discord_webhook import DiscordWebhook
import os

#discord bot libs
import discord
from discord.ext import commands


#title
from termcolor import cprint , colored
from pyfiglet import figlet_format,Figlet

#Title
from termcolor import cprint , colored
from pyfiglet import figlet_format,Figlet

#Yakuza cmd title
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Yakuza tool")

#Title of program
def title():
    f = Figlet(font='cosmic')
    print(f.renderText('YAKUZA TOOL'))

#Delete console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()



#Prints menu
def menu():
    f = Figlet(font='cosmic')
    print(f.renderText('YAKUZA TOOL'))
        
    print(f"{Fore.BLUE}[1.]" + f"{Fore.GREEN} Webhook send message   " + f"{Fore.BLUE}[2.]" + f"{Fore.GREEN} Bot control") 
    print(f"{Fore.BLUE}[]" + f"{Fore.GREEN}Empty                     " + f"{Fore.BLUE}[]" + f"{Fore.GREEN}Empty") 
    print(f"{Fore.BLUE}[]" + f"{Fore.GREEN}Empty                     " + f"{Fore.BLUE}[]" + f"{Fore.GREEN}Exit")
        
    print(" ")
    print(f"{Fore.GREEN}PROJECT MADE BY {Back.RED}YAKUZI")
    print(" ")


def bot_status_type_title():
                 
             
             print(f"{Fore.GREEN}Which status type you want to you?")
             print(f"{Fore.BLUE}[1.]" + f"{Fore.GREEN}Playing") 
             print(f"{Fore.BLUE}[2.]" + f"{Fore.GREEN}Twitch stream link") 
             print(f"{Fore.BLUE}[3.]" + f"{Fore.GREEN}Listening")
             print(f"{Fore.BLUE}[4.]" + f"{Fore.GREEN}Watching")
                 
             print(" ")
             print(f"{Fore.GREEN}PROJECT MADE BY {Back.RED}YAKUZI")
             print(" ")





menu()
while (selection := input("Option: ")) not in list("12345"):
             
    pass


#Selection #1
if (selection == "1"):

    
    webhook = DiscordWebhook(url = input("Webhook url: "), content = input("Your message:"))
    response = webhook.execute(), print("Message has been sent")
    

#Selection #3
if (selection == "2"):

        



     clearConsole()
      
     f = Figlet(font='cosmic')
     print(f.renderText('YAKUZA TOOL'))
     #menu
     print(f"{Fore.BLUE}[1.]" + f"{Fore.GREEN} Change bot status")
     print("")


     
     client = discord.Client()
    

     
     

     option = input("Option: ")


     if (option == "1"):
         client = discord.Client()
         TOKEN = input("Bot token: ")
         @client.event
         async def on_ready():
             clearConsole()
             title()
             
             

             bot_status_type_title()
             print("Sucessfully logged in as "f'{client.user}')

             option_botstatus = input("Option:")
             if (option_botstatus == "1"):

                 activity_game = input("Title of game: ")
                 await client.change_presence(activity=discord.Game(name=activity_game))


             if (option_botstatus == "2"):
                 streamtitle = input("Stream title: ")
                 streamlink = input("Twitch link displayed in status: ")
                 await client.change_presence(activity=discord.Streaming(name=streamtitle, url=streamlink))
             if (option_botstatus == "3"):
                 musicname = input("Name of song: ")
                 await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=musicname))
             if (option_botstatus == "4"):
                 nameofmovie = input("Name of a movie: ")
                 await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=nameofmovie))


             
             
             
             
             
             
             

             
             
         

    

         

            



         
         client.run(TOKEN)
         

         #How can i make python print something like "Invalid token"?

         
         
     
         
     


     
         









if (selection == "5"):
    exit