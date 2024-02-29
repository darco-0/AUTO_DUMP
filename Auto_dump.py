import random,string,time,re,sys,os
from concurrent.futures import ThreadPoolExecutor as tdp
import os,requests,base64,zlib,pip,urllib,sys,time,random,platform,pip,uuid,subprocess
print(f'\x1b[38;5;196m(\x1b[38;5;48m~\x1b[38;5;196m)\x1b[38;5;48m Loading Installed ')

try:
    import requests as r
    from bs4 import BeautifulSoup as bs
except:
    os.system("pip install bs4 requests")
    os.system("clear")
def clear():
	os.system('clear')
	print(logo)
def logo():
	print(logo)
def linex():
	print('\33[1;32m----------------------------------------------')

os.system('clear')
##------------(COLOUR)-------------##   

RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'

A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[1;96m'
B = '\x1b[38;5;8m'
H = '\x1b[1;92m' 
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
T = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
##------------(LINE)-------------##  
def linex():
        print(f'{R}--------------------------------------------------')
def clear():
        os.system(f'clear')
        print(logo)

##------------(LOGO)------------##
os.system('xdg-open https://t.me/team_x_draco_box_2')

logo=(f"""{A}

{A}:::::::::  :::::::::      :::      ::::::::   ::::::::  
{G}:+:    :+: :+:    :+:   :+: :+:   :+:    :+: :+:    :+: 
{A}+:+    +:+ +:+    +:+  +:+   +:+  +:+        +:+    +:+ 
{G}+#+    +:+ +#++:++#:  +#++:++#++: +#+        +#+    +:+ 
{A}+#+    +#+ +#+    +#+ +#+     +#+ +#+        +#+    +#+ 
{G}#+#    #+# #+#    #+# #+#     #+# #+#    #+# #+#    #+# 
{A}#########  ###    ### ###     ###  ########   ########   \033[0;41m𝙀𝙢𝙤𝙣\033[0;92m
 {G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {R}❲{G}😇{R}❳{G} 𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍 {R}:{G} 𝗘𝗠𝗢𝗡
 {R}❲{G}💚{R}❳{G} 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆  {R}:{G} 𝙈𝘿 𝙔𝙖𝙨𝙞𝙣 𝘼𝙝𝙢𝙚𝙙 𝙚𝙢𝙤𝙣
 {R}❲{G}😻{R}❳{G} 𝙑𝙀𝙍𝙎𝙄𝙊𝙉   {R}:{G}   2.1
 {R}❲{G}💚{R}❳{G} 𝙎𝙏𝘼𝙏𝙐𝙎    {R}:{G} \033[0;41m𝗙𝗥𝗘𝗘\033[0;92m
 {R}❲{G}😻{R}❳{G} 𝙏𝙊𝙊𝙇𝙎     {R}:{G} 𝗔𝗨𝗧𝗢 𝗗𝗨𝗠𝗣
 {G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

uids=[]
n=0
c=0
  
clear()
#file=input("ENTER ")
try:
    open(file,"r").read()
except:
    file="/sdcard/-AUTO-DUMP.txt"

def s(code):
    ln=15-len(code)
    lim=int("9"*(ln))+1
    for i in range(lim):
        uids.append(code+str(i).zfill(ln))

def gen(code,tt):
    clear()
    print('[1] START FOR AUTO DUMP ..')
    linex()
    op=int(input("""select :  """))
    clear()
    print(' process his been started ...')
    print(' Use CTRL+z for stop')
    linex()
    if op==2:
        s(code)
    else:
        for i in range(tt):
            uids.append(code+''.join(random.choice(string.digits) for _ in range(
        15-len(code)
        )))
        
def geno(code,l,tt):
    for i in range(tt):
        uids.append(code+''.join(random.choice(string.digits) for _ in range(
        l-len(code)
        )))

uao=['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.0.1','Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo P1ma40 Build/LMY47D)',
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7102 Build/KOT49H)',
'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G920K Build/NRD90M)']

def inputs():
    os.system("clear")
    print({A})
    print(' \nENTER YOUR DUMP LIMIT')
    print(' \nExample : 10001 ,100089,100090**etc')
    linex()
    code=input("SELECT YOUR LIMIT : ")
    clear()
    print('\nENTER YOUR COUNT LIMIT')
    print(' \nExample : 10000,100000,300000,3000484, etc')
    linex()
    tt=int(input("Total ids :"))
    l=0
    if len(code)<4:
        l=int(input("Uid length: "))
    return code,tt,l
    
def getname(uid):
    global n,c
    ua=random.choice(uao)
    hd={'authority':'m.facebook.com',

           'method': 'GET',
            'user-agent':ua
                        
            }
    url="https://m.facebook.com/profile.php?id="+uid
    pi=r.get(url,headers=hd)
    bp=bs(pi.content,"html.parser")
    name=bp.find("title").text.split("|")[0].strip()
    if "Content not found" not in name and "Log in to Facebook" not in name:
        n+=1
        
        
        print(f"\033[1;34m[-AUTO-DUMP-SUCCESFULL]\033[1;32m{uid}")
        open(file,"a").write(uid+" | "+name+"\n")
    #else:
        print(f"\033[1;34m[-AUTO-DUMP-SUCCESFULL]\033[1;32m{uid}")
    
    c+=1
    print(f'[Couting : %s ]'%(n),end="\r")


def run():
    with tdp(max_workers=60) as t:
        for uid in uids:
            t.submit(getname,uid)

while True:
    code,tt,l=inputs()
    if len(code)>=4:
        gen(code,tt)
    else:
        geno(code,l,tt)
    
    run()
    print("DUMP IDS ARE SAVE: "+file)
    rr=input("DUMP AGAIN? [Y or N]")
    if rr in ["Y","y"]:
        code,tt,l=inputs()
        n=0
        c=0
        uids=[]
        gen(code,tt)
        run()
    else:
        break
