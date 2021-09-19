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
                    
                except Exception:
                    id = 0
            else:
                id = 0

        admins = [role for role in message.guild.roles if role.permissions.administrator] #aqui se buscan todos los roles con permiso de administrador
        channel = await message.guild.create_text_channel(f"ticket-{int(ids[-1]) + 1}")
        role = await message.guild.create_role(name=f"ticket-{int(ids[-1]) + 1}") #se crea el rol para la persona que lo crea
        await message.author.add_roles(role)
        await channel.set_permissions(role, read_messages=True, send_messages=True)
        
        for admin in admins: # todos los admins pueden leer y escribir mensajes
            await channel.set_permissions(admin, read_messages=True, send_messages=True)
            
        no_admins = [role for role in message.guild.roles if not role.permissions.administrator]
        for no_admin in no_admins: # todos los admins no pueden leer y escribir mensajes
            await channel.set_permissions(no_admin, read_messages=False, send_messages=False)
    
    if message.content.startswith("-add"): # le pone el rol del ticket a la persona que se menciona
        persona = message.mentions
        rol = message.channel.name

        
        try:
            rol = renames.pop(rol)
            rol = discord.utils.get(message.guild.roles, name=rol)
            
        except Exception:
            rol = discord.utils.get(message.guild.roles, name=rol)
            
            
        await persona[0].add_roles(rol)
    
    if message.content == "-close": # borra el canal en el que se ponga -close
        channel = message.channel
        
        await channel.delete()


    
    if message.content.startswith("-rename"): #cambia el nombre al canal de texto
        channel = message.channel
        nombre = message.content[8: ]
        renames[nombre] = channel.name


        
        await channel.edit(name=nombre)

            
        
       

                






bot.run("NzkyNzQ3ODQ3NzYxMDAyNTM2.X-iN9w.r3AhEi0YUenvGe6gcSllESCh3bo")
