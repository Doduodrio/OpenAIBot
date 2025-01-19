from dotenv import load_dotenv
import os
import discord

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guilds = "\n - ".join([f"{guild.name} (id: {guild.id})" for guild in client.guilds])
    print(f"{client.user} is active in the following guilds:")
    print(f" - {guilds}\n")
    team_ids = [587040390603866122, 1278560382239113293]
    for id in team_ids:
        user = client.get_user(id)
        await user.send("Bot is online")
    print("Bot sent DMs to team upon activating!")

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    msg = message.content.lower()

    if "hello" in msg:
        await message.reply(f"Hello, {message.author.display_name}!")
        print(f"Bot said hello to {message.author.name}")

client.run(BOT_TOKEN)