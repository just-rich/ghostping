import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.messages = True  # Enable message events

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    channel_id = 1234567890  # Replace with your channel ID

    if message.channel.id == channel_id and not message.author.bot:
        reply = await message.channel.send("<@&1234567890>") # Replace with role ID
        await asyncio.sleep(1)  # Wait for 1 second
        await reply.delete()  # Delete the bot's message

    await bot.process_commands(message)

# Run the bot with your token
bot.run('bot-token-here')

