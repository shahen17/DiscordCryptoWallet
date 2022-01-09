
import os
import discord #importing discord module
import requests
import json
import http.client
import json


client = discord.Client()


#function to get bnb wallet balance
def get_sbnb_balance():
    my_api = #API endpoint url here
    response = requests.get(f'{my_api}')
    result = response.json()['result']
    formatsmartchain = int(result) / pow(10, 18)
    limited_float = round(formatsmartchain, 5)
    get_sbnb_balance = f'BSC BALANCE : {limited_float}'

    return get_sbnb_balance

#function to get busd wallet balance
def get_busd_balance():
    my_api2 = #API endpoint url here
    response = requests.get(f'{my_api2}')
    result = response.json()['result']
    formatsmartchain2 = int(result) / pow(10, 18)
    limited_float2 = round(formatsmartchain2, 5)
    get_busd_balance = f'BUSD BALANCE : {limited_float2}'

    return get_busd_balance


# TOKENS AVAILABLE ON WALLET/
def nms():
    nemesis = #API endpoint url here
    response = requests.get(f'{nemesis}') #ive took nemesis as an example
    result = response.json()['result']
    formatsmartchain2 = int(result) / pow(10, 9)
    limited_float2 = round(formatsmartchain2, 3)
    nms = f'NMS BALANCE : {limited_float2} (Tokens)'

    return nms


@client.event
async def on_ready():
    print('IM LOGGED IN {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
#On-user commands
    if message.content.startswith('$hello'):
        await message.channel.send(' message')

    if message.content.startswith('$name1'):
        await message.channel.send('message')

    if message.content.startswith('$name2'):
        await message.channel.send('message')           # add or delete (if conditions) per requirments

    if message.content.startswith('$name3'):
        await message.channel.send('message')

    if message.content.startswith('$name4'):
        await message.channel.send('message')

    if message.content.startswith('$name5'):
        await message.channel.send('message')



#on user command $wallet_balance , balances + available tokens will print in an embed form.
    if message.content.startswith('$wallet_balance'):
        avc = discord.Embed(
            colour=discord.Colour.blue(),
            title="wallet balance",
            description=get_sbnb_balance(),

        )
        avc.add_field(
            name="TOKENS (PCS)",
            value=nms(),
            inline=False,

        )
        await message.channel.send(embed=avc)


my_secret = #discord access token here
client.run(my_secret)
