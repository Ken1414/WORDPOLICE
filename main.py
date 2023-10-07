import discord
#from discord.ext import commands
import os
import keep_alive

client = discord.Client()
#bot = commands.bot


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(name="言論統制", type=discord.ActivityType.listening))

#-------------------------------
file_path = "word_list.txt"

def load_words():
    try:
        with open(file_path, "r") as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        return []

def save_words(words):
    with open(file_path, "w") as file:
        file.write("\n".join(words))

words1 = load_words()

#-------------------------------


@client.event
async def on_message(message):
    if message.author.bot:
        return

    elif message.content == '!Hi':
        await message.channel.send('HELLO!')

    elif message.content == 'Auther.OpenList':
        await message.channel.send(words1)

    if message.content.startswith('!add_word '):
        new_word = message.content.split('!add_word ')[1]
        words1.append(new_word)
        await message.channel.send(f'禁止ワード "{new_word}" を追加しました。')
        return

    if message.content.startswith('!remove_word '):
        remove_word = message.content.split('!remove_word ')[1]
        if remove_word in words1:
            words1.remove(remove_word)
            await message.channel.send(f'禁止ワード "{remove_word}" を削除しました。')
        else:
            await message.channel.send(f'禁止ワード "{remove_word}" はリストに存在しません。')
        return

    for word in words1:
        if word in message.content:
            #await message.channel.send('so bad')
            await message.delete()
            await message.channel.send(
                f'{message.author.mention} 禁止ワードが含まれています!')


keep_alive.keep_alive()
client.run(os.getenv('TOKEN'))
