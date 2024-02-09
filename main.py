import typing
import random
import settings
import discord
from discord.ext import commands
from discord import app_commands
from keep_alive import keep_alive
import os

aalind = ["what happened on may 12th?"]


logger = settings.logging.getLogger("bot")

class MyView(discord.ui.View):
  
  @discord.ui.button(label="draw",style=discord.ButtonStyle.green)
  async def draw(self,interaction : discord.Interaction,button : discord.Button):
    
    button.disabled=True
    
    if dealercard > card2 :
      await interaction.response.send_message(f"**cards**\ndealers cards : {dealercard}\nyour card : {card2}\n\n you lost!")
    elif dealercard < card2 and card2 <= 21 :
      await interaction.response.send_message(f"**cards**\ndealers cards : {dealercard}\nyour card : {card2}\n\n you won!")
    elif dealercard == card2 :
      await interaction.response.send_message(f"**cards**\ndealers cards : {dealercard}\nyour card : {card2}\n\n you tied!")
    elif card2 > 21 and dealercard < 22:
      await interaction.response.send_message(f"**cards**\ndealers cards : {dealercard}\nyour card : {card2}\n\n you lost!")
    elif dealercard > 21 and card2 < 22 : 
      await interaction.response.send_message(f"**cards**\ndealers cards : {dealercard}\nyour card : {card2}\n\n you won!")
    elif dealercard > 21 and card2 > 21 :
      await interaction.response.send_message(f"**cards**\ndealers cards : {dealercard}\nyour card : {card2}\n\n you tied!")
      

  @discord.ui.button(label='stand',style=discord.ButtonStyle.red)
  async def stand(self,interaction:discord.Interaction,button : discord.Button):
    
    button.disabled=True
    
    if dealercard > card1 :
      await interaction.response.send_message(f"**cards**\ndealers cards : {dealercard}\nyour card : {card1}\n\n you lost!")
    elif dealercard < card1 and card1 <= 21 :
      await interaction.response.send_message(f"**cards**\ndealers cards : {dealercard}\nyour card : {card1}\n\n you won!")
    elif dealercard == card1 :
      await interaction.response.send_message(f"**cards**\ndealers cards : {dealercard}\nyour card : {card1}\n\n you tied!")
    elif card1 > 21 and dealercard < 22:
      await interaction.response.send_message(f"**cards**\ndealers cards : {dealercard}\nyour card : {card1}\n\n you lost!")
    elif dealercard > 21 and card1 < 22:
      await interaction.response.send_message(f"**cards**\ndealers cards : {dealercard}\nyour card : {card1}\n\n you won!")
    elif dealercard > 21 and card1 < 22:
      await interaction.response.send_message(f"**cards**\ndealers cards : {dealercard}\nyour card : {card1}\n\n you tied!")
      


def run():
  intents = discord.Intents.default()
  intents.message_content = True
  discord.Intents.all()


  bot = commands.Bot(command_prefix='j!', intents=intents)

  @bot.event
  async def on_ready():
    await bot.change_presence(activity=discord.Game(name="/help"))
    logger.info(f"User: {bot.user} (ID : {bot.user.id})")
    print(bot.user)
    print(bot.user.id)
    await bot.tree.sync()
    print("________________")


  @bot.command()
  async def sync(ctx) -> None:
    fmt = await ctx.bot.tree.sync()
    await ctx.send(
      f"Synced {len(fmt)} commands"
    )

    
  
  @bot.tree.command(description="give help!",name = "help")
  async def help(interaction: discord.Interaction):
    await interaction.response.send_message("**Help guide**\n*/hello* : welcomes user\n*/credits* : shows you cool credits\n*/welcome* : welcomes user you choose\n*/joindate* : shows you when a member joined the server\n*/calculate* : basic calculator\n/*anonmessage* : sends anonymous/public messages directed to users\n/*anonthread* : sends a anonymous/public thread(message)\n/*coinflip* : flips a coin\n/*dice* : rolls a dice\n/*cards* : blackjack")
  
  @bot.tree.command(description="welcomes user", name="hello")
  async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}")
  
  @bot.tree.command(description="shows you cool credits", name="credits")
  async def credits(interaction: discord.Interaction):
    await interaction.response.send_message("**joels big brain**\nCreated by : *joelthbej*")

  @bot.tree.command(description="shows you when a member joined the server", name="joindate")
  async def joindate(interaction: discord.Interaction, member : discord.Member):
    await interaction.response.send_message(f"{member.mention} joined the server on {discord.utils.format_dt(member.joined_at)}")
  @bot.tree.command(description="hello to the person you want to sag hello to", name="welcome")
  async def welcome(interaction: discord.Interaction, member : discord.Member):
    await interaction.response.send_message(f"Hello, {member.mention}")

  #maths!

  @bot.tree.command(description="i am a human calculator!111", name="calculate")
  @app_commands.describe(operation="Enter aritmetic operation (addition/subtraction/multiplication/division)")
  async def calculate(interaction: discord.Interaction, operation: typing.Literal['Addition', 'Subtraction', 'Multiplication', 'Division'], number1: float, number2: float):
    if operation.upper() == 'A' or operation.upper() == 'ADDITION' or operation.upper() == 'PLUS' or operation.upper() == '+' or operation.upper() == 'ADD' :
      number3 = number1+number2
      await interaction.response.send_message(f"{number1} + {number2} = {number3}")
    elif operation.upper() == 'S' or operation.upper() == 'SUBTRACTION' or operation.upper() == 'MINUS' or operation.upper() == '-' or operation.upper() == 'SUBTRACT' :
      number3 = number1-number2
      await interaction.response.send_message(f"{number1} - {number2} = {number3}")
    elif operation.upper() == 'M' or operation.upper() == 'MULTIPLICATION' or operation.upper() == 'TIMES' or operation.upper() == 'x' or operation.upper() == '*' or operation.upper() == 'MULTIPLY' :
      number3 = number1*number2
      await interaction.response.send_message(f"{number1} * {number2} = {number3}")
    elif operation.upper() == 'D' or operation.upper() == 'DIVISION' or operation.upper() == 'DIVIDE' or operation.upper() == '/' or operation.upper() == '÷' :
      number3 = number1/number2
      await interaction.response.send_message(f"{number1} / {number2} = {number3}")
    else :
      await interaction.response.send_message("I don't understand")

  @bot.tree.command(description="sends anonymous/public messages directed to users",name="anonmessage")
  @app_commands.describe(anon_or_public = "Choose if you want the message to be anonymous or public",message = "Message you would like to send", member = "Member you would like this message to be sent to")
  async def anonmessage(interaction: discord.Interaction, anon_or_public : typing.Literal['Anonymous','Public'], message : str, member : discord.Member):
    anon_or_public = anon_or_public.upper()
    if anon_or_public == 'ANON' or anon_or_public == 'A' or anon_or_public == 'ANONYMOUS' :
      await interaction.response.send_message("Sending message...", ephemeral=True)
      await interaction.channel.send(f'Dear, {member.mention}\nAnonymous says, "{message}"')
    elif anon_or_public == 'PUBLIC' or anon_or_public == 'P' :
      await interaction.response.send_message("Sending message...", ephemeral=True)
      await interaction.channel.send(f'Dear, {member.mention}\n\n{interaction.user.mention} says, "{message}"')
    else :
      await interaction.response.send_message("I don't understand", ephemeral=True)
      
  @bot.tree.command(description="makes anonymous/public threads",name="anonthread")
  @app_commands.describe(anon_or_public = "Choose if you want the thread to be anonymous or public",thread = "Thread you would like to share" )
  async def anonthread(interaction: discord.Interaction, anon_or_public : typing.Literal['Anonymous','Public'], thread : str):
    anon_or_public = anon_or_public.upper()
    if anon_or_public == 'ANON' or anon_or_public == 'A' or anon_or_public == 'ANONYMOUS' :
      await interaction.response.send_message("Sending message...", ephemeral=True)
      await interaction.channel.send(f'**Anonymous thread :** \nAnonymous says, "{thread}"')
    elif anon_or_public == 'PUBLIC' or anon_or_public == 'P' :
      await interaction.response.send_message("Sending message...", ephemeral=True)
      await interaction.channel.send(f'**Public thread :** \n{interaction.user.mention} says, "{thread}"')
    else :
      await interaction.response.send_message("I don't understand", ephemeral=True)


  @bot.tree.command(description="lets play some ultimate trivia",name="trivia")
  @app_commands.describe(triviacato = "choose a category" )
  async def triviac(interaction: discord.Interaction, triviacato : typing.Literal['all','aalind']):
    if triviacato == 'aalind' :
      await interaction.response.send(f'**aalind trivia question :** \n{random.choice(aalind)}')

  
  @bot.tree.command(description="lets do some gambling",name="coinflip")
  async def coinflip(interaction : discord.Interaction):
      await interaction.response.send_message(f"{interaction.user.mention} flipped a coin and got {random.choice(['heads','tails'])}")

  
  @bot.tree.command(description="gambling on the next level",name="dice")
  @app_commands.describe(range="how many faces the dice will have")
  async def dice(interaction : discord.Interaction, range : int):  
    await interaction.response.send_message(f"{interaction.user.mention} rolled a {random.randint(1,range)} on a dice with {range} faces")


  @bot.tree.command(description="actual gambling",name="cards")
  async def cards(interaction : discord.Interaction):
    
    global dealercard,card1,card2

    dealercard=random.randint(1,21)
    card1=random.randint(1,21)
    card2=(random.randint(1,10)+card1)

    if card2<16:
      card2=16

    if dealercard<16 :
      dealercard += random.randint(1,10)
      if dealercard < 16 :
        dealercard = 16

    
    view=MyView()
    await interaction.response.send_message(f"**cards**\ndealers cards : ? ?\nyour card : {card1}",view=view)
 
  
  
  bot.run(settings.DISCORD_API_SECRET, root_logger=True)


keep_alive()

try:
  if __name__ == "__main__":
    run()
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  os.system('kill 1')
  os.system("python restarter.py")
