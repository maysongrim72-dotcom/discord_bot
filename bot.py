import os
import discord
from discord.ext import commands

# Налаштування дозволів
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 1. СЮДИ ВСТАВТЕ СКОПІЙОВАНИЙ ID КАНАЛУ (без лапок)
TARGET_CHANNEL_ID = 1559477266227003422

@bot.event
async def on_ready():
    print(f"✅ Бот {bot.user} успішно запущений і працює!")

@bot.event
async def on_message(message):
    # Ігноруємо повідомлення від ботів та з самого цільового каналу
    if message.author.bot or message.channel.id == TARGET_CHANNEL_ID:
        return

    target_channel = bot.get_channel(TARGET_CHANNEL_ID)

    if target_channel:
        # Форматуємо повідомлення
        text = f"**{message.author.display_name}** у каналі {message.channel.mention}:\n{message.content}"

        # Пересилаємо прикріплені файли/фото (якщо є)
        files = []
        for attachment in message.attachments:
            files.append(await attachment.to_file())

        await target_channel.send(content=text, files=files)

    await bot.process_commands(message)

# 2. СЮДИ ВСТАВТЕ СВІЙ СЕКРЕТНИЙ ТОКЕН (у лапках)
bot.run(os.getenv("TOKEN"))
