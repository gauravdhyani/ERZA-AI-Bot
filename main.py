import discord
from discord.http import json_or_text
import requests
import json 
import random
import aiohttp
from chatterbot import ChatBot
from weather import *
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get
from afks import afkdata
from minichat import minichat
chatbot =  minichat.Minichat()



print("Bot Running....")

def remove(afk):
  a=afk
  a = a.replace('[AFK]', '')
  return a 

class MyClient(discord.Client):
                              
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    
    
    async def on_message(self, message):
        
        if message.content=="Time":
            bot = ChatBot(
                'Time Bot',
                logic_adapters=[
                    'chatterbot.logic.TimeLogicAdapter'
                    ]
                )

            # Print an example of getting one time based response
            response = bot.get_response(message.content)
            response = bot.get_response('What time is it?')
            await message.channel.send(response)
            print(response)
        elif message.content=="-ping":
          await message.channel.send(f'My ping is {round(client.latency * 1000)}ms!')
        elif message.content.startswith("Math"):
            Bot = ChatBot(
                'Math  Bot',
                logic_adapters=[
                    'chatterbot.logic.MathematicalEvaluation',])
            response = Bot.get_response(message.content[5:])
            await message.channel.send(response)
            print(response)
        elif message.content.startswith("Weather"):
            location = message.content.replace("Weather", '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid=181dcd47e131c91802c3bafb60fd0d6e&units=metric'
            try:
                data =parse_data(json.loads(requests.get(url).content))
                data2 =parse_data2(json.loads(requests.get(url).content))
                await message.channel.send(embed=weather_message(data,data2, location))
            except KeyError:
                await message.channel.send(embed=error_message(location))
            
                
        elif message.content=="Roast":
            data = requests.get('https://evilinsult.com/generate_insult.php?lang=en')
            text=data.text
            await message.delete()
            await message.channel.send(text)
        elif message.content=="Roastn":
            text="Are you Sakura Haruno?Because you are utterly useless!"
            await message.delete()
            await message.channel.send(text)    
        elif message.content.startswith("Dictionary"):
            dict1 = message.content[11:]
            dict1.lower()
            response= requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{dict1}')
            if response.status_code == 404 :
              await message.channel.send("Word not found!")
              return
            else:
              wordx=response.json()
              the_dictionary=wordx[0]
              meanings=the_dictionary['meanings']
              definitions=meanings[0]
              definition=definitions['definitions'] 
              meaningg=definition[0]
              meaning=meaningg['definition'] 
              example=meaningg.get('example',["None"])
              synonymslist=meaningg.get('synonyms',["None"])
              if isinstance(synonymslist,str):
                synonymslist=[synonymslist]
              synonyms=', '.join(synonymslist)
              deffinal=discord.Embed(title=f"'{dict1.upper()}'")
              deffinal.set_thumbnail(url="https://antisemitism.org/wp-content/uploads/2020/02/Urban-Dictionary-1030x579.png")
              deffinal.add_field(name="Definition",value=f"{meaning}") 
              deffinal.add_field(name="Example",value=f"{example}") 
              synonymslist=meaningg.get('synonyms',['None'])
              await message.channel.send(embed=deffinal)
        elif message.content.startswith("-"):
            question = message.content[1:]
            answer = chatbot.chat(question)
            await message.channel.send(answer) 
        elif message.content=="Source":
            await message.channel.send("https://github.com/gauravdhyani/ERZA-AI-Bot")
            
        elif message.content.startswith("!afk"):
             afk = message.content[5:]
             member=message.author
             
             if member.id in afkdata.keys():
               afkdata.pop(member.id)
             else:
               try:
                 await member.edit(nick=f"[AFK]{member.display_name}")
               except:
                 pass 
             afkdata[member.id]=afk  
             embed=discord.Embed(title="Member Afk", description=f"{member.mention} has gone afk",color=member.color)
             embed.set_thumbnail(url=message.author.avatar_url)
             embed.add_field(name='AFK note:',value=afk) 
             await message.channel.send(embed=embed) 
             await message.channel.send(f"{member.mention} has gone afk : {afk}")
        elif message.content.startswith(""): 
          member=message.author
          if member.id in afkdata.keys():
            try:
              afkdata.pop(message.author.id)
              await member.edit(nick=remove(member.display_name))
              await message.channel.send(f'Welcome back {member.mention}, AFK removed.')
            except:
              pass  
        
            
            
        for id, reason in afkdata.items():
            member= get(message.guild.members,id=id)
            if(message.reference and member==(await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions :
               await message.reply(f"{member.name} is AFK ; {reason}")
            

        async with aiohttp.ClientSession() as session:    
          if message.content=="Pls dog":    
            request = await session.get('https://some-random-api.ml/img/dog') 
            dogjson = await request.json() #
            embed = discord.Embed(title="Doggo!") 
            embed.set_image(url=dogjson['link']) 
            await message.channel.send(embed=embed)    
          elif message.content=="Dog facts":
            request2 = await session.get('https://some-random-api.ml/facts/dog')
            factjson = await request2.json()
            embed = discord.Embed(title="Doggo!")
            embed.set_footer(text=factjson['fact'])
            await message.channel.send(embed=embed)
          elif message.content=="Pls cat":    
            request = await session.get('https://some-random-api.ml/img/cat') 
            catjson = await request.json() #
            embed = discord.Embed(title="Cat!") 
            embed.set_image(url=catjson['link']) 
            await message.channel.send(embed=embed)
          elif message.content=="Pls pussy": 
            codes=[100,101,102,200,201,202,203,204,206,207,300,302,303,304,305,307,308,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,420,421,422,423,424,425,426,429,431,444,450,451,497,498,499,500,501,502,503,504,506,507,508,509,510,511,521,523,525,599] 
            errors = random.choice(codes)   
            request =f'https://http.cat/{errors}.jpg'
            embed = discord.Embed(title="Pussy!") 
            embed.set_image(url=request) 
            await message.channel.send(embed=embed)  
          elif message.content=="Cat facts":
            request2 = await session.get('https://some-random-api.ml/facts/cat')
            factjson = await request2.json()
            embed = discord.Embed(title="Cat!")
            embed.set_footer(text=factjson['fact'])
            await message.channel.send(embed=embed)
          elif message.content=="Pls hug":    
            request = await session.get('https://some-random-api.ml/animu/hug') 
            hugjson = await request.json() #
            embed = discord.Embed(title="Huggz!") 
            embed.set_image(url=hugjson['link']) 
            await message.channel.send(embed=embed)   
          elif message.content=="Pls wink":    
            request = await session.get('https://some-random-api.ml/animu/wink') 
            winkjson = await request.json() #
            embed = discord.Embed(title="Wink-Wink!") 
            embed.set_image(url=winkjson['link']) 
            await message.channel.send(embed=embed)
          elif message.content=="Pls pat":    
            request = await session.get('https://some-random-api.ml/animu/pat') 
            patjson = await request.json() #
            embed = discord.Embed(title="Pat-Pat!") 
            embed.set_image(url=patjson['link']) 
            await message.channel.send(embed=embed)    
          elif message.content=="Pls meme":    
            request = await session.get('https://some-random-api.ml/meme') 
            memejson = await request.json() #
            embed = discord.Embed(title="MEME!") 
            embed.set_image(url=memejson['image']) 
            embed.set_footer(text=memejson['caption'])
            await message.channel.send(embed=embed)
          elif message.content=="Pls joke":
            request2 = await session.get('https://some-random-api.ml/joke')
            jokejson = await request2.json()
            embed = discord.Embed(title="Jokes!")
            embed.set_footer(text=jokejson['joke'])
            await message.channel.send(embed=embed)
          elif message.content=="Pls bird":    
            request = await session.get('https://some-random-api.ml/img/birb') 
            birdjson = await request.json() #
            embed = discord.Embed(title="Birdie!") 
            embed.set_image(url=birdjson['link']) 
            await message.channel.send(embed=embed)    
          elif message.content=="Bird facts":
            request2 = await session.get('https://some-random-api.ml/facts/birb')
            factjson = await request2.json()
            embed = discord.Embed(title="Birdie!")
            embed.set_footer(text=factjson['fact'])
            await message.channel.send(embed=embed)
          elif message.content=="Pls panda":    
            request = await session.get('https://some-random-api.ml/img/panda') 
            pandajson = await request.json() #
            embed = discord.Embed(title="Pandu!") 
            embed.set_image(url=pandajson['link']) 
            await message.channel.send(embed=embed)    
          elif message.content=="Panda facts":
            request2 = await session.get('https://some-random-api.ml/facts/panda')
            factjson = await request2.json()
            embed = discord.Embed(title="Pandu!")
            embed.set_footer(text=factjson['fact'])
            await message.channel.send(embed=embed) 
          elif message.content=="Pls fox":    
            request = await session.get('https://some-random-api.ml/img/fox') 
            foxjson = await request.json() #
            embed = discord.Embed(title="Fox!") 
            embed.set_image(url=foxjson['link']) 
            await message.channel.send(embed=embed)    
          elif message.content=="Fox facts":
            request2 = await session.get('https://some-random-api.ml/facts/fox')
            factjson = await request2.json()
            embed = discord.Embed(title="Fox!")
            embed.set_footer(text=factjson['fact'])
            await message.channel.send(embed=embed)          
          elif message.content=="Pls koala":    
            request = await session.get('https://some-random-api.ml/img/koala') 
            koalajson = await request.json() #
            embed = discord.Embed(title="Koala!") 
            embed.set_image(url=koalajson['link']) 
            await message.channel.send(embed=embed)    
          elif message.content=="Koala facts":
            request2 = await session.get('https://some-random-api.ml/facts/koala')
            factjson = await request2.json()
            embed = discord.Embed(title="Koala!")
            embed.set_footer(text=factjson['fact'])
            await message.channel.send(embed=embed) 
          elif message.content=="Pls red panda":    
            request = await session.get('https://some-random-api.ml/img/red_panda') 
            red_pandajson = await request.json() #
            embed = discord.Embed(title="Red Pandu!") 
            embed.set_image(url=red_pandajson['link']) 
            await message.channel.send(embed=embed)    
          elif message.content=="Redpanda facts":
            request2 = await session.get('https://some-random-api.ml/facts/red_panda')
            factjson = await request2.json()
            embed = discord.Embed(title="Red Pandu!")
            embed.set_footer(text=factjson['fact'])
            await message.channel.send(embed=embed) 
          elif message.content=="Pls racoon":    
            request = await session.get('https://some-random-api.ml/img/racoon') 
            racoonjson = await request.json() #
            embed = discord.Embed(title="Racoon!") 
            embed.set_image(url=racoonjson['link']) 
            await message.channel.send(embed=embed)    
          elif message.content=="Racoon facts":
            request2 = await session.get('https://some-random-api.ml/facts/racoon')
            factjson = await request2.json()
            embed = discord.Embed(title="Racoon!")
            embed.set_footer(text=factjson['fact'])
            await message.channel.send(embed=embed)        
          elif message.content=="Pls kangaroo":    
            request = await session.get('https://some-random-api.ml/img/kangaroo') 
            kangaroojson = await request.json() #
            embed = discord.Embed(title="Kangaroo!") 
            embed.set_image(url=kangaroojson['link']) 
            await message.channel.send(embed=embed)    
          elif message.content=="Kangaroo facts":
            request2 = await session.get('https://some-random-api.ml/facts/kangaroo')
            factjson = await request2.json()
            embed = discord.Embed(title="Kangaroo!")
            embed.set_footer(text=factjson['fact'])
            await message.channel.send(embed=embed) 
          elif message.content=="Pls whale":    
            request = await session.get('https://some-random-api.ml/img/whale') 
            whalejson = await request.json() #
            embed = discord.Embed(title="Whale!") 
            embed.set_image(url=whalejson['link']) 
            await message.channel.send(embed=embed)    
          elif message.content=="Whale facts":
            request2 = await session.get('https://some-random-api.ml/facts/whale')
            factjson = await request2.json()
            embed = discord.Embed(title="Whale!")
            embed.set_footer(text=factjson['fact'])
            await message.channel.send(embed=embed)
          elif message.content=="Pls pika":    
            request = await session.get('https://some-random-api.ml/img/pikachu') 
            pikajson = await request.json() #
            embed = discord.Embed(title="Pika-Pi!") 
            embed.set_image(url=pikajson['link']) 
            await message.channel.send(embed=embed) 
          elif message.content.startswith("Eject"):
            name = message.content[6:]
            imposter=["true","false"]
            imposter2=random.choice(imposter)
            color=["black","blue","brown","cyan","darkgreen","lime","orange","pink","purple","red","white","yellow"]
            color2=random.choice(color)
            url=f'https://vacefron.nl/api/ejected?name={name}&impostor={imposter2}&crewmate={color2}'  
            embed = discord.Embed(title="SUS!", color=discord.Color.dark_red()) 
            embed.set_image(url=url) 
            await message.channel.send(embed=embed)
          elif message.content.startswith("Reverse"):
            content = message.content[8:]
            content2=content.replace(" ","%20")
            url=f'https://vacefron.nl/api/carreverse?text={content2}'  
            embed = discord.Embed(title="RUN!") 
            embed.set_image(url=url) 
            await message.channel.send(embed=embed)  
          elif message.content.startswith("Change my mind"):
            content = message.content[15:]
            content2=content.replace(" ","%20")
            url=f'https://vacefron.nl/api/changemymind?text={content2}'  
            embed = discord.Embed(title="Mah Mind!") 
            embed.set_image(url=url) 
            await message.channel.send(embed=embed)   
          elif message.content.startswith("Emergency meeting"):
            content = message.content[18:]
            content2=content.replace(" ","%20")
            url=f'https://vacefron.nl/api/emergencymeeting?text={content2}'  
            embed = discord.Embed(title="EMERGENCY!") 
            embed.set_image(url=url) 
            await message.channel.send(embed=embed) 
          elif message.content=="Pls duck": 
            url=f'https://random-d.uk/api/quack'
            request = await session.get(url) 
            url2= await request.json() #
            embed = discord.Embed(title="Quack-Quack!") 
            embed.set_image(url=url2['url']) 
            await message.channel.send(embed=embed)  
           

client = MyClient(intents=discord.Intents.all())
client.run('Enter your token here')
