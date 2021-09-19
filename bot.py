import discord
from discord.utils import get
from discord.ext import commands
import random
import time

intents = discord.Intents.default()
intents.members = True  
bot = commands.Bot(command_prefix='-', intents=intents)
id = ""
ids = []
renames = {}
@bot.event
async def on_ready():
    print("Listo")
    await bot.change_presence(activity=discord.Game(name="")) #puedes poner que esta jugando a lo que quieras

@bot.event
async def on_message(message):
    global id
    if message.content == "-ticket": # esta es la parte del codigo que crea el ticket
        for channel in message.guild.text_channels:
            if "ticket" in channel.name: # esto revisa si hay canales que se llamen ticket para llamarlos diferente
                id = channel.name[7:]
                try:
                    ids.append(id)
                    id = int(ids[-1]) + 1
                    
                except Exception:
                    id = 0
            else:
                id = 0

        admins = [role for role in message.guild.roles if role.permissions.administrator] #aqui se buscan todos los roles con permiso de administrador
        channel = await message.guild.create_text_channel(f"ticket-{id}")
        renames[channel] = channel
        await message.channel.send(f"{message.author} tu ticket se ha creado correctamente en {channel.mention}")
        await channel.send("@here se ha abierto un nuevo ticket")
       
        await channel.set_permissions(message.author, read_messages=True, send_messages=True)
        
        try:
            admins = discord.utils.get(message.guild.roles, id=888569520439037982)
            await channel.set_permissions(admins, read_messages=True, send_messages=True)
        except Exception:
            admins = discord.utils.get(message.guild.roles, id=889155705125359678)
            await channel.set_permissions(admins, read_messages=True, send_messages=True)
        
        for role in message.guild.roles:
            if role.id != 888569520439037982 and role.id != 889155705125359678:
                await channel.set_permissions(role, read_messages=False, send_messages=False)
        

        
        
        

 
            

        
    
    if message.content.startswith("-add"): # le pone el rol del ticket a la persona que se menciona
        persona = await message.guild.fetch_member(int(message.content[5: ]))
        await message.channel.set_permissions(persona, read_messages=True, send_messages=True)
        
   
            
            
   
    
    if message.content == "-close": # borra el canal en el que se ponga -close
        channel = message.channel
        try:
            channel = renames.pop(channel)
            time.sleep(random.randint(10, 20))
            await channel.delete()
        except Exception:
            pass
        
        
        


    
    if message.content.startswith("-rename"): #cambia el nombre al canal de texto
        channel = message.channel
        nombre = message.content[8: ]
        renames[nombre] = channel.name


        
        await channel.edit(name=nombre)

            
        
       

                






bot.run("TOKEN")
