import discord
from discord.utils import get
from discord.ext import commands
import random

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
       
        await channel.set_permissions(message.author, read_messages=True, send_messages=True)
        
        admins = discord.utils.get(message.guild.roles, id=888569520439037982)
        await channel.set_permissions(admins, read_messages=True, send_messages=True)

        
        
        

 
            
        no_admins = [role for role in message.guild.roles if not role.permissions.administrator]
        for no_admin in no_admins: # todos los admins no pueden leer y escribir mensajes
            await channel.set_permissions(no_admin, read_messages=False, send_messages=False)
    
    if message.content.startswith("-add"): # le pone el rol del ticket a la persona que se menciona
        persona = await message.guild.fetch_member(int(message.content[5: ]))
        await message.channel.set_permissions(persona, read_messages=True, send_messages=True)
        
   
            
            
   
    
    if message.content == "-close": # borra el canal en el que se ponga -close
        channel = message.channel
        try:
            channel = renames.pop(channel)
            await channel.delete()
        except Exception:
            pass
        
        
        


    
    if message.content.startswith("-rename"): #cambia el nombre al canal de texto
        channel = message.channel
        nombre = message.content[8: ]
        renames[nombre] = channel.name


        
        await channel.edit(name=nombre)

            
        
       

                






bot.run("ODg5MTM1NTgxNzAxOTk2NTc1.YUc2Cg.WW9N7SjeKcVN79BCjfetKn_de6c")
