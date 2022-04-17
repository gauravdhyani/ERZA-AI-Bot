import discord

color = 0xFF6500
key_features = {
    'temp' : 'Temperature[°C]',
    'feels_like' : 'Feels Like[°C]',
    
}
def parse_data(data):
    data=data['weather']
    del data [0]['id']
    del data[0]['icon']
    del data[0]['main']
    a = {i:data[i] for i in range(len(data))}
    return data
    
def parse_data2(data2):
    data2=data2['main']
    del data2['humidity']
    del data2['pressure']
    del data2['temp_min']
    del data2['temp_max']
    return data2


def weather_message(data,data2, location):
    location = location.title()
    message = discord.Embed(
        title=f'{location} Weather',
        description=f'Here is the weather in {location}:',
        color=color
    )
    message.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
    message.add_field(name='Current Weather',
                      value=data[0]['description'].capitalize(),
                      inline=False
                    )
    for key in data2:
        message.add_field(
            name=key_features[key],
            value=str(data2[key]),
            inline=False
        )
         
    return message

def error_message(location):
    location = location.title()
    return discord.Embed(
        title='Error',
        description=f'There was an error retrieving weather data for {location}.',
        color=color
    )
