import discord
from discord.ext import commands
from discord.ui import Button, View

client = commands.Bot(command_prefix=".",help_command=None,intents=discord.Intents.all())
client .remove_command('help')
@client.event
async def on_ready():
    print('Logged in ')
@client.command(pass_content=True)    
async def Erza(message): 
    Color= 0x5865F2
    embed=discord.Embed(title='__**Erza Help**__',description='__**Commands**__',color=Color)
    embed.set_thumbnail(url=f'https://media.discordapp.net/attachments/840588197578276894/941774364494430208/Great-Teacher-Onizuka-featured-image_2.jpg?width=402&height=402')
    embed.add_field(name=f'**Chatbot**', value=f'-<Text>')
    embed.add_field(name=f'**Surveillance**', value=f'+Security')
    embed.add_field(name=f'**Ping**', value=f'-ping')
    embed.add_field(name=f'**Source**', value=f'Source')
    embed.add_field(name=f'**Dictionary **', value=f'Dictionary <Enter Query>')
    embed.add_field(name=f'**Mathematics**', value=f'Math <Enter Query>')
    embed.add_field(name=f'**Weather**', value=f'Weather <Location>')
    embed.add_field(name=f'**AFK**', value=f'!afk')
    embed.add_field(name=f'**Animal Kingdom**', value=f'.animals')
    embed.add_field(name=f'**Fun Kingdom**', value=f'.fun')
    embed.add_field(name=f'**Meme Maker Help**', value=f'.fun2')
    

    await message.channel.send(embed=embed) 
@client.command(pass_content=True)    
async def fun2(message): 
    Color= 0x5865F2
    embed=discord.Embed(title='__**Meme Maker Help**__',description='__**Commands**__',color=Color)
    embed.set_thumbnail(url=f'https://media.discordapp.net/attachments/840588197578276894/941778822628540476/animesher.png')
    embed.add_field(name=f'**Sus Eject**', value=f'Eject <Name>')
    embed.add_field(name=f'**Reverse**', value=f'Reverse <Text>')
    embed.add_field(name=f'**Mind goes brr..**', value=f'Change my mind <Text>')
    embed.add_field(name=f'**Danger**', value=f'Emergency meeting <Text>')
    embed.add_field(name=f'**Roasting**', value=f'Roastn')

    await message.channel.send(embed=embed)              
    
@client.command(pass_content=True)    
async def animals(message):
    view=View()
    button=Button(label="Dogs!", style=discord.ButtonStyle.green,row=0)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls dog")
    button.callback=button_callback
    view.add_item(button)
    
    button2=Button(label="Dogs Facts!", style=discord.ButtonStyle.green,row=0)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Dog facts")
    button2.callback=button_callback
    view.add_item(button2)
    
    button3=Button(label="Cats", style=discord.ButtonStyle.green,row=0)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls cat")
    button3.callback=button_callback
    view.add_item(button3)

    button4=Button(label="More Cats!", style=discord.ButtonStyle.green,row=0)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls pussy")
    button4.callback=button_callback
    view.add_item(button4)

    button5=Button(label="Cat Facts!", style=discord.ButtonStyle.green,row=0)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Cat facts")
    button5.callback=button_callback
    view.add_item(button5)
    
    button6=Button(label="Pikachu!", style=discord.ButtonStyle.green,row=1)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls pika")
    button6.callback=button_callback
    view.add_item(button6)

    button7=Button(label="Birds!", style=discord.ButtonStyle.green,row=1)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls bird")
    button7.callback=button_callback
    view.add_item(button7)    
    button8=Button(label="Bird Facts!", style=discord.ButtonStyle.green,row=1)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Bird facts")
    button8.callback=button_callback
    view.add_item(button8)    
    button9=Button(label="Panda!", style=discord.ButtonStyle.green,row=1)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls panda")
    button9.callback=button_callback
    view.add_item(button9)    
    button10=Button(label="Panda Facts!", style=discord.ButtonStyle.green,row=1)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Panda facts")
    button10.callback=button_callback
    view.add_item(button10)
    button11=Button(label="Fox!", style=discord.ButtonStyle.green,row=2)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls fox")
    button11.callback=button_callback
    view.add_item(button11)    
    button12=Button(label="Fox Facts!", style=discord.ButtonStyle.green,row=2)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Fox facts")
    button12.callback=button_callback
    view.add_item(button12)

    button13=Button(label="Koala!", style=discord.ButtonStyle.green,row=2)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls koala")
    button13.callback=button_callback
    view.add_item(button13)
    
    button14=Button(label="Koala Facts!", style=discord.ButtonStyle.green,row=2)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Koala facts")
    button14.callback=button_callback
    view.add_item(button14)

    button15=Button(label="Red Panda!", style=discord.ButtonStyle.green,row=2)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls red panda")
    button15.callback=button_callback
    view.add_item(button15)
    
    button16=Button(label="RedPaAnda Facts!", style=discord.ButtonStyle.green,row=3)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Redpanda facts")
    button16.callback=button_callback
    view.add_item(button16)

    button17=Button(label="Racoon!", style=discord.ButtonStyle.green,row=3)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls racoon")
    button17.callback=button_callback
    view.add_item(button17)
    
    button18=Button(label="Racoon Facts!", style=discord.ButtonStyle.green,row=3)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Racoon facts")
    button18.callback=button_callback
    view.add_item(button18)

    button19=Button(label="Kangroo!", style=discord.ButtonStyle.green,row=3)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls kangaroo")
    button19.callback=button_callback
    view.add_item(button19)
    
    button20=Button(label="Kangroo Facts!", style=discord.ButtonStyle.green,row=3)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Kangaroo facts")
    button20.callback=button_callback
    view.add_item(button20)

    button21=Button(label="Whale!", style=discord.ButtonStyle.green,row=4)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls whale")
    button21.callback=button_callback
    view.add_item(button21)
    
    button22=Button(label="Whale Facts!", style=discord.ButtonStyle.green,row=4)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Whale facts")
    button22.callback=button_callback
    view.add_item(button22)

    await message.send("Animal Kingdom",view=view)   

@client.command(pass_content=True)      
async def fun(message):
    view=View()
    button=Button(label="Memes!", style=discord.ButtonStyle.red,row=0)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls meme")
    button.callback=button_callback
    view.add_item(button)
    
    button2=Button(label="Hugs!", style=discord.ButtonStyle.red,row=1)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls hug")
    button2.callback=button_callback
    view.add_item(button2)
    
    button3=Button(label="Wink", style=discord.ButtonStyle.red,row=2)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls wink")
    button3.callback=button_callback
    view.add_item(button3)

    button4=Button(label="Pat!", style=discord.ButtonStyle.red,row=3)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls pat")
    button4.callback=button_callback
    view.add_item(button4)

    button5=Button(label="Joke!", style=discord.ButtonStyle.red,row=4)
    async def button_callback(interaction):
     await interaction.response.send_message(content="Pls joke")
    button5.callback=button_callback
    view.add_item(button5)

    await message.send("Fun Kingdom",view=view)                            
client.run('Enter your token here')