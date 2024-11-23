import discord
import random
from bot_mantik import gen_pass
from discord.ext import commands


# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
# Botu başlatma
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# "Geri atık için ne yapılır?" komutunu tanımlama
# Geri dönüşüm önerisi
@bot.command()
async def geri_donusum(ctx):
    await ctx.send("Geri dönüştürülebilir malzemeler: Cam, kağıt, plastik ve metal. Unutmayın, geri dönüşüm gezegenimize fayda sağlar!")

# Atık azaltma komutu
@bot.command()
async def atik_azaltma(ctx):
    await ctx.send("Atık azaltmanın yolları: \n1. Tek kullanımlık plastiklerden kaçının. \n2. Yeniden kullanılabilir su şişeleri kullanın. \n3. Organik atıkları kompost yaparak değerlendirin.")


@bot.command()
async def geri_atik(ctx):
    # Kullanıcıya geri dönüşüm ile ilgili öneriler
    response = ("Geri atık için şu adımları izleyebilirsiniz:\n"
                "1. Atık maddeleri geri dönüşüme atın.\n"
                "2. Cam, plastik, kağıt gibi geri dönüştürülebilir malzemeleri ayırın.\n"
                "3. Geri dönüşüm kampanyaları düzenleyin.\n"
                "4. Sıfır atık yaşam tarzını benimseyin.\n"
                "5. Doğal kaynakları korumaya yardımcı olun.\n"
                "Daha fazla bilgi almak için çevre dostu kaynakları araştırabilirsiniz.")

    
    # Botun cevabını gönderme
    await ctx.send(response)

# Botun çalışması için gerekli token

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")

    elif message.content.startswith('$sifre'):
        await message.channel.send(gen_pass(5))

    else:
        await message.channel.send(message.content)
