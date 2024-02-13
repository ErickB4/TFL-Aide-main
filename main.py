import nextcord
from nextcord.ui import Button, View
from nextcord.ext import commands
from nextcord import Interaction
import responses
import os
from PIL import Image, ImageDraw, ImageFont
import urllib

async def send_message(message, user_message, is_private):
  try:
      response = responses.handle_repsonse(message)
    
      if(response != None):
        await message.author.send(response) if is_private else await message.channel.send(response)
        
  except Exception as e:
    print(e)

def run_discord_bot():
  TOKEN = os.environ['MTE5MzY1Mzg3NDgxMzMyMTI1Ng.GLbOnN.vax1ekz34bk5kyOjxyix6cM6ELkewfGACYt_Qk']
  
  serverID = 1177411432338432071
  
  intents = nextcord.Intents.default()
  intents.members = True  
  
  client = commands.Bot(command_prefix='!', intents=intents)
  
  @client.event
  async def on_ready():
    print(f'{client.user} in now running')
    channel = client.get_channel(1177411433420570677)
    await channel.send('I am now online!')
  
  @client.slash_command(name = 'test', description='Just testing stuff',guild_ids=[serverID])
  async def test(interaction: Interaction):
    await interaction.response.send_message('fart')

    
  #get commands
  initial_extentions = []

  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      print(filename)
      initial_extentions.append('cogs.' + filename[:-3])

  if __name__ == '__main__':
    for extension in initial_extentions:
      client.load_extension(extension)
    
  bot.run(TOKEN)

