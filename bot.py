import discord
from discord.ext import commands
import requests
import random

plastik = """Evde plastik atıkları değerlendirmek için birçok yaratıcı ve eğlenceli etkinlik yapabilirsin. İşte bazı fikirler:

1. Saksı Yapımı
Kullanmadığın plastik şişeleri keserek saksıya dönüştürebilirsin. Üzerini boyayarak veya süsleyerek daha güzel hale getirebilirsin.

2. Kalemlik veya Organizer
Büyük plastik şişelerin alt kısmını keserek kalemlik, makyaj fırçası veya masa düzenleyici olarak kullanabilirsin.

3. Kuş Yemliği
Plastik şişelerin yanlarını kesip içine yem koyarak kuşlar için yemlik yapabilirsin. Bahçeye veya pencere kenarına asabilirsin.

4. Oyuncak Yapımı
Plastik kapaklardan ve şişelerden arabalar, robotlar veya hayvan figürleri yapabilirsin.

5. Çiçek veya Dekoratif Objeler
Plastik kaşık ve şişelerden çiçekler yaparak odanı süsleyebilirsin. Ayrıca plastik şişe diplerinden mozaik veya duvar süsü yapabilirsin.

6. Plastik Poşetlerden Sepet veya Çanta
Eski plastik poşetleri şeritler halinde kesip örgü tekniğiyle küçük sepetler veya çantalar yapabilirsin.

7. Fener ve Lamba Tasarımı
Şeffaf plastik şişelerin içini LED ışıklarla süsleyerek dekoratif lambalar yapabilirsin.

8. Şişe Kapaklarıyla Mozaik Sanatı
Plastik kapakları farklı renklerde bir araya getirerek mozaik tablolar veya dekoratif desenler oluşturabilirsin.
"""

atik_hakkinda_bilgiler = """Evde atıkları ayrıştırarak geri dönüşüme katkıda bulunabilirsin. İşte hangi atıkların çöpe, hangilerinin geri dönüşüme atılabileceğine dair bir liste:

♻️ Geri Dönüştürülebilir Atıklar

📄 Kağıt ve Karton:
✅ Gazete, dergi, kitap
✅ Karton kutular (pizza kutusu temizse)
✅ Kağıt poşetler, broşürler
🚫 Islak, yağlı veya kirlenmiş kağıtlar (örneğin, kullanılmış peçete)

🛍️ Plastik:
✅ Su ve içecek şişeleri
✅ Yoğurt kapları, süt kutuları
✅ Plastik poşetler, ambalajlar
🚫 Yağlı veya kirli plastikler

🥫 Metal:
✅ Kola, meyve suyu ve konserve kutuları
✅ Alüminyum folyo ve metal kapaklar
🚫 Paslı ve kirlenmiş metaller

🍾 Cam:
✅ Cam şişeler (su, meşrubat, sirke vb.)
✅ Kavanozlar
🚫 Kırık cam, ampul, pencere camı (bunlar özel atık olarak değerlendirilir)

🚮 Çöpe Atılması Gerekenler

❌ Islak mendil ve peçeteler
❌ Kirli veya yağlı kağıtlar
❌ Kullanılmış pipetler ve plastik çatal-bıçaklar
❌ Kırık seramik ve camlar

⚠️ Tehlikeli ve Özel Atıklar (Ayrı Toplanmalı)

🔋 Piller (pil toplama kutularına)
💡 Ampuller ve floresan lambalar
🛢️ Motor yağı ve kimyasal maddeler
🖥️ Elektronik atıklar (eski telefon, bilgisayar, kablolar)

Eğer yaşadığın yerde geri dönüşüm kutuları varsa, atıklarını doğru şekilde ayırarak doğaya katkı sağlayabilirsin! 🌱♻️

"""

ayristirma_süresi = """ev atıklarının ayrıştırılma süreci ile ilgili bilgiler:
Hızlı Ayrışanlar (0-1 Yıl)

📝 Kağıt – 2-6 ay
🍎 Meyve kabukları – 2 hafta - 2 ay
☕ Kağıt bardak – 5 yıl

Orta Sürede Ayrışanlar (10-100 Yıl)

🧦 Pamuklu kumaş (kıyafet, havlu) – 6 ay - 5 yıl
🛍️ Plastik poşet – 10-20 yıl
🥫 Alüminyum kutular (kola, konserve kutusu) – 80-100 yıl

Çok Geç Ayrışanlar (100+ Yıl)

🍼 Plastik şişe – 450 yıl
👞 Deri ayakkabı – 25-50 yıl
☂️ Plastik kaplamalı şemsiye – 500 yıl
💳 Kredi kartı (PVC plastik) – 1000 yıl

Asla Ayrışmayanlar

🖥️ Elektronik atıklar (telefon, bilgisayar parçaları)
⚡ Piller ve bataryalar
☠️ Radyoaktif atıklar

"""

yardim = """
Sunucu komutları :

$hello      : bot kendini tanıtır.
$bot        : mesaj verir.
$dog        : dog mem verir
$duck       : duck mem verir
$mem        : komik 1 tane mem verir (hep aynı mem verir buarada).
$mem2       : mem komutunun aynısı sayılır
$hepsi      : karışık mem ler verir
$PLS91      : plastik hakkında bilgi verir
$ATK91      : atık hakkında bilgi verir
$EVATIK91   : ev atıklarının ayrıştırma süreci ile ilgili bilgi verir
"""
mim_nadirlik = """
    duck: 0.5, 
    dog:  0.3,  
    mem:  0.15, 
    mem2: 0.05 (en nadir) """

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
#atık bilgileri
@bot.command()
async def PLS91(ctx):
    await ctx.send(plastik)

@bot.command()
async def ATK91(ctx):
    await ctx.send(atik_hakkinda_bilgiler)

@bot.command()
async def EVATIK91(ctx):
    await ctx.send(ayristirma_süresi)

@bot.command()
async def YARDIM(ctx):
    await ctx.send(yardim)

@bot.command()
async def MEM_NADİRLİK(ctx):
    await ctx.send(mim_nadirlik)

@bot.command()
async def heh(ctx, count_heh = 20):
    await ctx.send("he" * count_heh)
    

@bot.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')
        
    
@bot.command()
async def mem(ctx):
    with open('images/mem1.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    with open('images/mem2.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
import os
print(os.listdir('images'))
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

rarities = {
    duck: 0.5, 
    dog: 0.3,  
    mem: 0.15, 
    mem2: 0.05  
}

@bot.command()
async def hayvan(ctx):
    commands = list(rarities.keys())
    probabilities = list(rarities.values())
    chosen_command = random.choices(commands, weights=probabilities, k=1)[0]
    await chosen_command(ctx)

@bot.command()
async def hepsi(ctx):
    commands = list(rarities.keys())
    probabilities = list(rarities.values())
    chosen_command = random.choices(commands, weights=probabilities, k=1)[0]
    await chosen_command(ctx)
    
bot.run("###############################")
