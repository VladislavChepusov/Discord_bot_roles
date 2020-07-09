import discord
#from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, MissingPermissions

#import time
#from twisted.internet import task, reactor
#import schedule
import asyncio

import re 
from pprint import pprint
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


 #Prefix for commands (can be changed to a more convenient one) //
Bot=commands.Bot(command_prefix='//')

#Power On Message
@Bot.event
async def on_ready():
    print('I {0.user.name} alive!\n(Full name={0.user})'.format(Bot))

#Automatic issue invladinoy role to new users
@Bot.event
async def on_member_join(member):
    getrole = discord.utils.get(member.guild.roles,name="invalid_nickname")
    await member.add_roles(getrole)


#######Interaction with google sheets#######
# File obtained in the Google Developer Console
CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets document (can be taken from its URL)
 #please, fill!!!! 
spreadsheet_id = '!!!enter your here URL!!!'

# Log in and get service - an instance of access to the API
#DO NOT TOUCH
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)



     

e=False
h=False
#hard mode
@Bot.command(pass_context=True) 
@commands.has_permissions(administrator=True) 
async def hard(ctx):
     global h,e
     h=True
     e=False
     while h and (not e):
        await group(ctx)
        print('Working hard')
        await asyncio.sleep(20) # task runs every 20 seconds

#soft mode
@Bot.command(pass_context=True) 
@commands.has_permissions(administrator=True) 
async def soft(ctx):
     global h,e
     h=False
     e=True
     while e and (not h):
        await ez(ctx)
        print('Working soft')
        await asyncio.sleep(20) # task runs every 20 seconds 
         
# For soft mode
@Bot.command(pass_context=True) 
@commands.has_permissions(administrator=True) #permission to use
async def ez(ctx):
    role = discord.utils.get(ctx.guild.roles, name="invalid_nickname")
    if role is None:
        await ctx.send('There is no "invalid_nickname" role on this server!')
        return
    for member in ctx.message.guild.members:
        if role in member.roles:
            st="{0.nick} ".format(member)
            if  len(st)==5:
                    q="{0.name}".format(member)
                    z=q.split(' ')
            else:
                q="{0.nick}".format(member)
                z=q.split(' ')
            try:
                results = service.spreadsheets().values().batchGet(
                spreadsheetId = spreadsheet_id, 
                ranges = f'Group!A1:A33', 
                valueRenderOption = 'FORMATTED_VALUE',  
                dateTimeRenderOption = 'FORMATTED_STRING').execute() 
                sheet_values = results['valueRanges'][0]['values']
                print('______________________________')
                for i in sheet_values:
                    #ni=f'{z[-1]} {z[1]}'
                    if re.search(rf'\b{z[-1]}\b', str(i)):
                        await member.remove_roles(discord.utils.get(member.guild.roles,name="invalid_nickname"))
                        await member.add_roles(discord.utils.get(member.guild.roles,name=z[-1]))
                        #await ctx.send("Оригинальный ник: {0.name} Серверный ник: {0.nick} ".format(member)) 
                        #await ctx.send("Пользователю {0.name}( {0.nick}) была присвоена роль".format(member))
                        await ctx.send(f'The user  {member.name}({member.nick}) has been assigned a role  @{z[-1]}')
            except Exception:
                print("Worked exclusion")
            finally:
                print("Final")

    
# For hard mode
@Bot.command(pass_context=True) 
@commands.has_permissions(administrator=True) #permission to use
async def group(ctx):
    role = discord.utils.get(ctx.guild.roles, name="invalid_nickname")
    if role is None:
        await ctx.send('There is no "invalid_nickname" role on this server!')
        return
    for member in ctx.message.guild.members:
        if role in member.roles:
            st="{0.nick} ".format(member)
            if  len(st)==5:
                    q="{0.name}".format(member)
                    z=q.split(' ')
            else:
                q="{0.nick}".format(member)
                z=q.split(' ')
            try:
                results = service.spreadsheets().values().batchGet(
                spreadsheetId = spreadsheet_id, 
                ranges = f'{z[-1]}!A1:A33', 
                valueRenderOption = 'FORMATTED_VALUE',  
                dateTimeRenderOption = 'FORMATTED_STRING').execute() 
                sheet_values = results['valueRanges'][0]['values']
                print('______________________________')
                for i in sheet_values:
                    ni=f'{z[0]} {z[1]}'
                    if re.search(rf'\b{ni}\b', str(i)):
                        await member.remove_roles(discord.utils.get(member.guild.roles,name="invalid_nickname"))
                        await member.add_roles(discord.utils.get(member.guild.roles,name=z[-1]))
                        await ctx.send(f'The user  {member.name}({member.nick}) has been assigned a role @{z[-1]}')
            except Exception:
                print("Worked exclusion")
            finally:
                print("Final")

 #please, fill!!!!              
Bot.run('!!!!enter your token here!!!!!')



         
