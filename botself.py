# -*- coding: utf-8 -*-
#adanncuy Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

adanncuy = LINETCR.LINE()
#adanncuy.login(qr=True)
adanncuy.login(token='EuOA9sDYBinaNbluGhU8.oJ0Q/i8re80a55npHIR2Ia.ZqqqeZHEvSQ9KoNNgBtaIvktfOODztnVHqWjQKl8xFg=')
adanncuy.loginResult()
print "adanncuy-Login Success\n\n=====[Sukses Login]====="

reload(sys)
sys.setdefaultencoding('utf-8')


selfMessage ="""╭━━━━━━━━━━━━━━━━╮
┣🇮🇩━⏩〔Hi〕
┣🇮🇩━⏩〔Me〕
┣🇮🇩━⏩〔Mymid〕
┣🇮🇩━⏩〔Mid @〕
┣🇮🇩━⏩〔SearchID〕
┣🇮🇩━⏩〔Checkdate 〕
┣🇮🇩━⏩〔Kalender〕
┣🇮🇩━⏩〔Steal contact〕
┣🇮🇩━⏩〔Pp @〕
┣🇮🇩━⏩〔Cover @〕
┣🇮🇩━⏩〔Auto like〕
┣🇮🇩━⏩〔Scbc Text〕
┣🇮🇩━⏩〔Cbc Text〕
┣🇮🇩━⏩〔Gbc Text〕
┣🇮🇩━⏩〔Bio @〕
┣🇮🇩━⏩〔Info @〕
┣🇮🇩━⏩〔Name @〕
┣🇮🇩━⏩〔Profile @〕
┣🇮🇩━⏩〔Contact @〕
┣🇮🇩━⏩〔Getvid @〕
┣🇮🇩━⏩〔Friendlist〕
┣🇮🇩━⏩〔Micadd @〕
┣🇮🇩━⏩〔Micdel @〕
┣🇮🇩━⏩〔Miclist〕
╰━━━━━━━━━━━━━━━━╯"""

botMessage ="""╭━━━━━━━━━━━━━━╮
┣🇮🇩━⏩〔Absen〕
┣🇮🇩━⏩〔Respon〕
┣🇮🇩━⏩〔Runtime〕
┣🇮🇩━⏩〔copy @〕
┣🇮🇩━⏩〔Copycontact〕
┣🇮🇩━⏩〔Mybackup〕
┣🇮🇩━⏩〔Mybio 〔T〕
┣🇮🇩━⏩〔Myname 〔T〕
┣🇮🇩━⏩〔@bye〕
┣🇮🇩━⏩〔Bot on/off〕
╰━━━━━━━━━━━━━━╯"""

mediaMessage ="""╭━━━━━━━━━━━━━━━━━━━━╮
┣🇮🇩━⏩〔Youtube J 〕
┣🇮🇩━⏩〔Youtubevideo J〕
┣🇮🇩━⏩〔Youtubesearch:0 J〕
┣🇮🇩━⏩〔Image NamaGambar〕
┣🇮🇩━⏩〔Say T〕
┣🇮🇩━⏩〔Say-en T〕
┣🇮🇩━⏩〔Say-jp T〕
┣🇮🇩━⏩〔Tr-id T 〔 En  ID〕
┣🇮🇩━⏩〔Tr-en T 〔ID  En〕
┣🇮🇩━⏩〔Tr-th T 〔ID Th〕
┣🇮🇩━⏩〔Id@en T 〔ID En〕
┣🇮🇩━⏩〔Id@th T 〔ID TH〕
┣🇮🇩━⏩〔En@id T 〔 En  ID〕
┣🇮🇩━⏩〔Gift〕
┣🇮🇩━⏩〔Giftbycontact〕
┣🇮🇩━⏩〔Gif gore〕
┣🇮🇩━⏩〔Google 〔T〕
┣🇮🇩━⏩〔Playstore NamaApp〕
┣🇮🇩━⏩〔Fancytext T〕
┣🇮🇩━⏩〔musik J-Penyanyi〕
┣🇮🇩━⏩〔lirik J-Penyanyi〕
┣🇮🇩━⏩〔musrik J-Penyanyi〕
┣🇮🇩━⏩〔ig 〔UsrNameIG〕
┣🇮🇩━⏩〔Checkig 〔UsrIG〕
┣🇮🇩━⏩〔apakah 〔T〕
┣🇮🇩━⏩〔kapan 〔T〕
┣🇮🇩━⏩〔hari 〔T 〕
┣🇮🇩━⏩〔berapa〔 T 〕
┣🇮🇩━⏩〔berapakah 〔T〕
╰━━━━━━━━━━━━━━━━━━━━╯"""

groupMessage ="""╭━━━━━━━━━━━━━━━━╮
┣🇮🇩━⏩〔Welcome〕
┣🇮🇩━⏩〔Say welcome〕
┣🇮🇩━⏩〔Invite creator〕
┣🇮🇩━⏩〔Cctv〕
┣🇮🇩━⏩〔Ciduk〕
┣🇮🇩━⏩〔Gn:〔NG〕
┣🇮🇩━⏩〔Tag all〕
┣🇮🇩━⏩〔lurk on/off〕
┣🇮🇩━⏩〔lurkers〕
┣🇮🇩━⏩〔Recover〕
┣🇮🇩━⏩〔Cancel〕
┣🇮🇩━⏩〔Cancelall〕
┣🇮🇩━⏩〔Gcreator〕
┣🇮🇩━⏩〔Ginfo〕
┣🇮🇩━⏩〔Gurl〕
┣🇮🇩━⏩〔List group〕
┣🇮🇩━⏩〔Pict group:〔NG〕
┣🇮🇩━⏩〔Spam: 〔T〕
┣🇮🇩━⏩〔Add all〕
┣🇮🇩━⏩〔Kick: (Mid)〕
┣🇮🇩━⏩〔Invite: (Mid)〕
┣🇮🇩━⏩〔Invite〕
┣🇮🇩━⏩〔Memlist〕
┣🇮🇩━⏩〔Getgroup image〕
┣🇮🇩━⏩〔Urlgroup Image〕
╰━━━━━━━━━━━━━━━━╯"""
ar="u3a3d2af88f1113cd00e7934f862af688"

setMessage ="""╭━━━━━━━━━━━━━━━╮
┣🇮🇩━⏩〔Notif on/off〕
┣🇮🇩━⏩〔Mimic on/off〕
┣🇮🇩━⏩〔Url on/off〕
┣🇮🇩━⏩〔Read on/off〕
┣🇮🇩━⏩〔Sider 0n/off〕
┣🇮🇩━⏩〔K on/off〕
┣🇮🇩━⏩〔Sticker on/off〕
┣🇮🇩━⏩〔Simi on/off〕
┣🇮🇩━⏩〔lurk on/off〕
┣🇮🇩━⏩〔Bot on/off 〕
╰━━━━━━━━━━━━━━━╯"""

creatorMessage ="""╭━━━━━━━━━━━━━━━━━━━╮
┣🇮🇩━⏩〔Crash〕
┣🇮🇩━⏩〔Kickall〕
┣🇮🇩━⏩〔Bc: 〔T〕
┣🇮🇩━⏩〔Join group: 〔NG〕
┣🇮🇩━⏩〔Leave group: 〔NG〕
┣🇮🇩━⏩〔Leave all group〕
┣🇮🇩━⏩〔Tag on/off〕
┣🇮🇩━⏩〔Bot restart〕
┣🇮🇩━⏩〔Turn off〕
╰━━━━━━━━━━━━━━━━━━━╯"""

adminMessage ="""╭━━━━━━━━━━━━━━━━━━━━╮
┣🇮🇩━⏩〔Allprotect on/off〕
┣🇮🇩━⏩〔Ban〕
┣🇮🇩━⏩〔Unban〕
┣🇮🇩━⏩〔Ban @〕
┣🇮🇩━⏩〔Unban @〕
┣🇮🇩━⏩〔Ban list〕
┣🇮🇩━⏩〔Clear ban〕
┣🇮🇩━⏩〔Kill〕
┣🇮🇩━⏩〔Kick @〕
┣🇮🇩━⏩〔Set member: (Jml)〕
┣🇮🇩━⏩〔Ban group: 〔NG〕
┣🇮🇩━⏩〔Del ban: 〔NG〕
┣🇮🇩━⏩〔List ban〕
┣🇮🇩━⏩〔Kill ban〕
┣🇮🇩━⏩〔Glist〕
┣🇮🇩━⏩〔Glistmid〕
┣🇮🇩━⏩〔Details group: 〔〔(Gid)〕
┣🇮🇩━⏩〔Cancel invite: 〔(Gid)〕
┣🇮🇩━⏩〔Invitemeto: 〔(Gid)〕
┣🇮🇩━⏩〔Acc invite〕
┣🇮🇩━⏩〔Removechat〕
┣🇮🇩━⏩〔Qr on/off〕
┣🇮🇩━⏩〔Autokick on/off〕
┣🇮🇩━⏩〔Autocancel on/off〕
┣🇮🇩━⏩〔Invitepro on/off〕
┣🇮🇩━⏩〔Join on/off〕
┣🇮🇩━⏩〔Joincancel on/off〕
┣🇮🇩━⏩〔R1 on/off〕
┣🇮🇩━⏩〔R2 on/off〕
┣🇮🇩━⏩〔R3 on/off〕
┣🇮🇩━⏩〔Rkick on/off〕
╰━━━━━━━━━━━━━━━━━━━━╯"""

rusuhMessage ="""╭━ W✒ E━ L✒ C━ O✒ M━ E✒✒✒
╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓
┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫
┃HALLO▪┃ ◾KAMI DATANG LAGI   ▪┃
┗ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯
UNTUK MENGGUSUR ROOM KALIAN
.        (҂`_´)
         <,︻╦̵̵̿╤─ ҉     ~  •
█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●
▂▄▅█████████▅▄▃▂…
[███████████████████]
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙
╔═╦═╗╔══╗╔═╦╗╔══╗╔══╗╔══╗╔═╗
║║║║║╚║║╝║║║║║╔═╣║╔═╣╚║║╝║╬║
║║║║║╔║║╗║║║║║╚╗║║╚╗║╔║║╗║╗╣
╚╩═╩╝╚══╝╚╩═╝╚══╝╚══╝╚══╝╚╩╝
────────────────────────────
.        (҂`_´)
         <,︻╦̵̵̿╤─ ҉     ~  •
█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●
▂▄▅█████████▅▄▃▂…
[███████████████████]
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙
╔═╦═╗╔══╗╔═╦╗╔══╗╔══╗╔══╗╔═╗
║║║║║╚║║╝║║║║║╔═╣║╔═╣╚║║╝║╬║
║║║║║╔║║╗║║║║║╚╗║║╚╗║╔║║╗║╗╣
╚╩═╩╝╚══╝╚╩═╝╚══╝╚══╝╚══╝╚╩╝
────────────────────────────
.        (҂`_´)
         <,︻╦̵̵̿╤─ ҉     ~  •
█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●
▂▄▅█████████▅▄▃▂…
[███████████████████]
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙
╔═╦═╗╔══╗╔═╦╗╔══╗╔══╗╔══╗╔═╗
║║║║║╚║║╝║║║║║╔═╣║╔═╣╚║║╝║╬║
║║║║║╔║║╗║║║║║╚╗║║╚╗║╔║║╗║╗╣
╚╩═╩╝╚══╝╚╩═╝╚══╝╚══╝╚══╝╚╩╝
────────────────────────────

        TAMPA BANYAK BASA-BASI
RATA NGGA RATA YANG PENTING BACOT
              TANGKIS GOBLOK
────────────────────────────
           ─────────────────
			╔══╗╔═╗╔══╗╔═╦═╗
			╚╗╔╝║╦╝║╔╗║║║║║║
			─║║─║╩╗║╠╣║║║║║║
			─╚╝─╚═╝╚╝╚╝╚╩═╩╝
			────────────────
					╔══╗╔═╗╔╦╗
					╚╗╗║║╬║║╔╝
					╔╩╝║║╔╝║╚╗
					╚══╝╚╝─╚╩╝
		`			──────────
              🇮🇩 🇮🇩 🇮🇩 🇮🇩 🇮🇩 🇮🇩 🇮🇩 
🇮🇩 Indonesia┏━┳┳┳━┳┳┓🇮🇩 🇮🇩 🇮🇩 🇮🇩 
🇮🇩 Indonesia┃━┫┃┃┏┫━┫┏┓🇮🇩 🇮🇩 🇮🇩 
🇮🇩 Indonesia┃┏┫┃┃┗┫┃┃┃┃🇮🇩 🇮🇩 🇮🇩 
🇮🇩 Indonesia┗┛┗━┻━┻┻┛┃┃🇮🇩 🇮🇩 🇮🇩 
🇮🇩 Indonesia┏┳┳━┳┳┳┓┏┫┣┳┓🇮🇩 🇮🇩 
🇮🇩 Indonesia┃┃┃┃┃┃┃┃┣┻┫┃┃🇮🇩 🇮🇩 
🇮🇩 Indonesia┣┓┃┃┃┃┣┫┃┏┻┻┫🇮🇩 🇮🇩 
🇮🇩 Indonesia┗━┻━┻━┻🇮🇩 🇮🇩 🇮🇩 🇮🇩 
━━━━━━━━RATA NI MAH━━━━━━━━
			╔═╗╔══╗╔══╗╔══╗
			║╬║║╔╗║╚╗╔╝║╔╗║
			║╗╣║╠╣║─║║─║╠╣║
			╚╩╝╚╝╚╝─╚╝─╚╝╚╝
			───────────────
			╔═╗╔══╗╔══╗╔══╗
			║╬║║╔╗║╚╗╔╝║╔╗║
			║╗╣║╠╣║─║║─║╠╣║
			╚╩╝╚╝╚╝─╚╝─╚╝╚╝
			───────────────
			╔═╗╔══╗╔══╗╔══╗
			║╬║║╔╗║╚╗╔╝║╔╗║
			║╗╣║╠╣║─║║─║╠╣║
			╚╩╝╚╝╚╝─╚╝─╚╝╚╝
			───────────────
			
━━━━━━━━━━━━━━━━━━━━━━━━━ """

helpMessage ="""╭━━━━━━━━━━━━━━╮
┣🇮🇩━⏩〔Help self〕
┣🇮🇩━⏩〔Help bot〕
┣🇮🇩━⏩〔Help group〕
┣🇮🇩━⏩〔Help set〕
┣🇮🇩━⏩〔Help media〕
┣🇮🇩━⏩〔Help admin〕
┣🇮🇩━⏩〔Help creator〕
┣🇮🇩━⏩〔Owner〕
┣🇮🇩━⏩〔Speed〕
┣🇮🇩━⏩〔Speed test〕
┣🇮🇩━⏩〔Status〕
┣🇮🇩━⏩〔Rusuh〕
╰━━━━━━━━━━━━━━╯"""


KAC=[adanncuy]
mid = adanncuy.getProfile().mid
Bots=[mid]
Creator=["u3a3d2af88f1113cd00e7934f862af688"]
admin=["u3a3d2af88f1113cd00e7934f862af688"]

contact = adanncuy.getProfile()
backup1 = adanncuy.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

responsename = adanncuy.getProfile().displayName


wait = {
    "LeaveRoom":True,
    "Bot":True,
    "AutoJoin":False,
    "AutoJoinCancel":False,
    "memberscancel":30,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":False,
    'pap':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'copy':{},    
    'likeOn':{},
    'detectMention':False,
    'detectMention2':True,
    'detectMention3':False,
    'kickMention':False,  
    'sticker':False,  
    'timeline':True,
    "Timeline":True,
    "comment":"\n────────────────────────\n 🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n╭━ A✒ U━ T✒ O━ L✒ I━ K✒E✒✒\n╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓\n┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫\n┃adanncuyISTIFIK ◾ID SMULE▪adanncuy_MH┃\n┗ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n.        (҂`_´)\n         <,︻╦̵̵̿╤─ ҉     ~  •\n█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●\n▂▄▅█████████▅▄▃▂…\n[███████████████████]\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n───────────────\n",    
    "comment1":"\n────────────────────────\n 🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n╭━ A✒ U━ T✒ O━ L✒ I━ K✒E✒✒\n╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓\n┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫\n┃adanncuyISTIFIK ◾ID SMULE▪adanncuy_MH┃\n┗ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n.        (҂`_´)\n         <,︻╦̵̵̿╤─ ҉     ~  •\n█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●\n▂▄▅█████████▅▄▃▂…\n[███████████████████]\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n───────────────\n",
    "comment2":"\n────────────────────────\n 🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n╭━ A✒ U━ T✒ O━ L✒ I━ K✒E✒✒\n╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓\n┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫\n┃adanncuyISTIFIK ◾ID SMULE▪adanncuy_MH┃\n┗ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n.        (҂`_´)\n         <,︻╦̵̵̿╤─ ҉     ~  •\n█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●\n▂▄▅█████████▅▄▃▂…\n[███████████████████]\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n───────────────\n",
    "comment3":"\n────────────────────────\n 🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n╭━ A✒ U━ T✒ O━ L✒ I━ K✒E✒✒\n╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓\n┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫\n┃adanncuyISTIFIK ◾ID SMULE▪adanncuy_MH┃\n┗ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n.        (҂`_´)\n         <,︻╦̵̵̿╤─ ҉     ~  •\n█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●\n▂▄▅█████████▅▄▃▂…\n[███████████████████]\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n───────────────\n",
    "comment4":"\n────────────────────────\n 🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n╭━ A✒ U━ T✒ O━ L✒ I━ K✒E✒✒\n╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓\n┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫\n┃adanncuyISTIFIK ◾ID SMULE▪adanncuy_MH┃\n┗ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n.        (҂`_´)\n         <,︻╦̵̵̿╤─ ҉     ~  •\n█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●\n▂▄▅█████████▅▄▃▂…\n[███████████████████]\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n───────────────\n",
    "comment5":"\n────────────────────────\n 🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n╭━ A✒ U━ T✒ O━ L✒ I━ K✒E✒✒\n╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓\n┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫\n┃adanncuyISTIFIK ◾ID SMULE▪adanncuy_MH┃\n┗ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Indonesia\n.        (҂`_´)\n         <,︻╦̵̵̿╤─ ҉     ~  •\n█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●\n▂▄▅█████████▅▄▃▂…\n[███████████████████]\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n───────────────\n",
    "comment6":"SEKIAN LIKE DAN KOMENTAR GUE SEMOGA LU BAHAGIA DISANA WKWKWK",
    "commentOn":True,
    "commentBlack":{},
    "message":"Thx For Add Me (^_^)\nInvite Me To Your Group ヘ(^_^)ヘ",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "Contact":False,
    "Notif":False,
    "inviteprotect":False,    
    "alwaysRead":False,    
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }
    
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }    

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')
            
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       adanncuy.sendMessage(msg)
    except Exception as error:
       print error          
                        
       

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:

        if op.type == 0:
            return

        if op.type == 5:
           if wait["autoAdd"] == True:
              adanncuy.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                adanncuy.sendText(op.param1,str(wait["ThankS for add me"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	
	    if op.type == 55:
                try:
                     if op.param1 in wait2['readPoint']:     
                         if op.param2 in wait2['readMember'][op.param1]:
                              pass
                         else:
                              wait2['readMember'][op.param1] += op.param2
                         wait2['ROM'][op.param1][op.param2] = op.param2
                         with open('sider.json', 'w') as fp:
                          json.dump(wait2, fp, sort_keys=True, indent=4)
                     else:
                         pass
                except:
                    pass
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = adanncuy.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        adanncuy.sendText(op.param1, "╭━ SIDER✒D✒A✒ T✒ A✒N✒G✒✒" + "\n╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓" + "\n┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫" + "\n┃SIDER▪┃ ◾" + Name +  "▪┃" + "\n┗ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯")
                                        time.sleep(0.2)
                                        summon(op.param1)
                                    else:
                                        adanncuy.sendText(op.param1, "🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Merdeka"+"\n█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●" + "\n▂▄▅██D█O█R██▅▄▃▂…" + "\n[███████████████████]" + "\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙" + "\nNGINTIP..NIH..!!!" + Name + ".")
                                        time.sleep(0.2)
                                        summon(op.param1)
                                else:
                                    adanncuy.sendText(op.param1, " 🇮🇩 Indonesia🇮🇩 Indonesia🇮🇩 Merdeka"+"\n█۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●" + "\n▂▄▅██D█O█R██▅▄▃▂…" + "\n[███████████████████]" + "\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙" + "\nNGINTIP..NIH..!!!" + Name + ".")
                                    time.sleep(0.2)
                                    summon(op.param1)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      

        if op.type == 22:
            adanncuy.leaveRoom(op.param1)

        if op.type == 21:
            adanncuy.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    adanncuy.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = adanncuy.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        adanncuy.acceptGroupInvitation(op.param1)
                        adanncuy.sendText(op.param1,"Maaf " + adanncuy.getContact(op.param2).displayName + "\nMember Kurang Dari 30 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        adanncuy.leaveGroup(op.param1)                        
		    else:
                        adanncuy.acceptGroupInvitation(op.param1)
			adanncuy.sendText(op.param1,"♠Ketik ✴Help✴ Untuk Bantuan♠\n♠Harap Gunakan Dengan Bijak ^_^ ♠")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = adanncuy.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        adanncuy.rejectGroupInvitation(op.param1)
		    else:
                        adanncuy.acceptGroupInvitation(op.param1)
			adanncuy.sendText(op.param1,"♠Ketik ✴Help✴ Untuk Bantuan♠\n♠Harap Gunakan Dengan Bijak ^_^ ♠")
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        adanncuy.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			adanncuy.cancelGroupInvitation(op.param1, [op.param3])
			adanncuy.sendText(op.param1, "Blacklist Detected")
		    else:
			pass
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    adanncuy.cancelGroupInvitation(op.param1,[op.param3])
                    adanncuy.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass

        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               adanncuy.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    adanncuy.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        adanncuy.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        adanncuy.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        adanncuy.kickoutFromGroup(op.param1,[op.param2])
			adanncuy.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    adanncuy.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        adanncuy.kickoutFromGroup(op.param1,[op.param2])
			adanncuy.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                adanncuy.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        adanncuy.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    adanncuy.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    adanncuy.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass


        if op.type == 17:
          if wait["Notif"] == True:
            if op.param2 in Creator:
                return
            ginfo = adanncuy.getGroup(op.param1)
            contact = adanncuy.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            adanncuy.sendText(op.param1,"Assalamualaikum.wr.wb" + adanncuy.getContact(op.param2).displayName + "⋱ ⋮ ⋰" + "\n⋯ ◯ ⋯ ︵ 　　　　　　^v^" + "\n¸︵︵( ░░ )︵.︵.︵" + "\n(´░░░░░░ ') ░░░' ) `´︶´¯`︶´`︶´︶´`　^v^　　^v^" + "\n" + "\n╔┓┏╦━━╦┓╔┓╔━━╗╔╗" + "\n║┗┛║┗━╣┃║┃║╯╰║║║" + "\n║┏┓║┏━╣┗╣┗╣╰╯║╠╣" + "\n╚┛┗╩━━╩━╩━╩━━╝╚╝" + "\n♪♫•*¨*•.¸¸❤¸¸.•*¨*•♫♪♪♫•*¨*•.¸¸❤¸¸.•*¨*•♫♪" + "\nSELAMAT DATANG DI ✴ " + str(ginfo.name) + " ✴" + "\nYuk kenalan sama temen-temen 😄\nJangan lupa baca note ya kak...\nSemoga Betah Disini ^_^")
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            adanncuy.sendMessage(c)  
            adanncuy.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269548",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            adanncuy.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"

        if op.type == 15:
          if wait["Notif"] == True:
            if op.param2 in Creator:
                return
            adanncuy.sendText(op.param1,"Good Bye " + adanncuy.getContact(op.param2).displayName +  "\nSee You Next Time . . . (p′︵‵。) 🤗")
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269542",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            adanncuy.sendMessage(d)                  
            print "MEMBER HAS LEFT THE GROUP"
            
        if op.type == 25:
            msg = op.message
            
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        adanncuy.sendText(msg.to,text)             
            
            
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                adanncuy.sendText(msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = adanncuy.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  adanncuy.sendText(msg.to,ret_)
                                  adanncuy.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = adanncuy.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag!! Lagi Sibuk",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","Dia Lagi Off", cName + " Kenapa Tag Saya?","Dia Lagi Tidur\nJangan Di Tag " + cName, "Jangan Suka Tag Gua " + cName, "Kamu Siapa " + cName + "?", "Ada Perlu Apa " + cName + "?","Woii " + cName + " Jangan Ngetag, Riibut!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  adanncuy.sendText(msg.to,ret_)
                                  break   
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = adanncuy.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [ "┌─┐    ┌─┐\n│█ │ /█ /\n│█ │/█ /\n│█  /█ /─┬─┐\n│█ │█ |█ │█ │\n┌┴─┴─┐-┘─┘\n│█ ┌──┘█ █ █ │\n└┐█ █ █ █ █ █ “\n  ‎​(¯`" + cName + "´¯)♥jangan tag please...\nlagi kojom nah...."  ]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  adanncuy.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "20001316",
                                                       "STKPKGID": "1582380",
                                                       "STKVER": "1" }
                                  adanncuy.sendMessage(msg)                                
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = adanncuy.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Woii " + cName + ", Dasar Jones Ngetag Mulu!"]
                    balas1 = "Ini Foto Sii Jones Yang Suka Ngetag. . ."
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  adanncuy.sendText(msg.to,ret_)
                                  adanncuy.sendText(msg.to,balas1)
                                  adanncuy.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "11764508",
                                                       "STKPKGID": "6641",
                                                       "STKVER": "1" }
                                  adanncuy.sendMessage(msg)                                
                                  break  
                                  
        if op.type == 25:
            msg = op.message                                  
                              
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                adanncuy.sendText(msg.to,"Bot Sudah On Kembali.")  

        if op.type == 25:
          if wait["Bot"] == True:    
            msg = op.message
            
            
            if msg.contentType == 7:
              if wait["sticker"] == True:
                msg.contentType = 0
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                adanncuy.sendText(msg.to, filler)
                wait["sticker"] = False
            else:
                pass              

            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    adanncuy.sendChatChecked(msg.from_,msg.id)
                else:
                    adanncuy.sendChatChecked(msg.to,msg.id)
                    
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     adanncuy.like(url[25:58], url[66:], likeType=1005)
                     adanncuy.comment(url[25:58], url[66:], wait["comment"])
                     adanncuy.comment(url[25:58], url[66:], wait["comment1"])
                     adanncuy.comment(url[25:58], url[66:], wait["comment2"])
                     adanncuy.comment(url[25:58], url[66:], wait["comment3"])
                     adanncuy.comment(url[25:58], url[66:], wait["comment4"])
                     adanncuy.comment(url[25:58], url[66:], wait["comment5"])
                     adanncuy.comment(url[25:58], url[66:], wait["comment6"])
                     adanncuy.comment(url[25:58], url[66:], wait["comment7"])
                     adanncuy.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = False


            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            adanncuy.sendText(msg.to,"Sudah")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            adanncuy.sendText(msg.to,"Ditambahkan")
		    else:
			adanncuy.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        adanncuy.sendText(msg.to,"Terhapus")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        adanncuy.sendText(msg.to,"Tidak Ada Black List")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     adanncuy.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = adanncuy.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = adanncuy.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         adanncuy.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = adanncuy.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = adanncuy.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         adanncuy.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = adanncuy.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        adanncuy.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        adanncuy.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        adanncuy.sendText(msg.to,"Can not be used outside the group")
                    else:
                        adanncuy.sendText(msg.to,"Not for use less than group")
                        

 
            elif msg.text is None:
                return
 
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ar}
                adanncuy.sendMessage(msg)
		adanncuy.sendText(msg.to,"Itu Majikan Kami (^_^)")

 

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = adanncuy.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                adanncuy.sendMessage(msg)
		adanncuy.sendText(msg.to,"Itu Yang Buat Grup Ini")
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    adanncuy.sendText(msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = adanncuy.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                adanncuy.findAndAddContactsByMid(target)
                                contact = adanncuy.getContact(target)
                                cu = adanncuy.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                adanncuy.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                adanncuy.sendText(msg.to,"Profile Picture " + contact.displayName)
                                adanncuy.sendImageWithURL(msg.to,image)
                                adanncuy.sendText(msg.to,"Cover " + contact.displayName)
                                adanncuy.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = adanncuy.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                adanncuy.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                adanncuy.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break

            if msg.contentType == 13:
                if wait["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = adanncuy.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Copy"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        adanncuy.sendText(msg.to, "Not Found...")
                        pass
                    else:
                        for target in targets:
                            try:
                                adanncuy.CloneContactProfile(target)
                                adanncuy.sendText(msg.to, "Copied (^_^)")
                                wait['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["copy"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = adanncuy.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             adanncuy.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 adanncuy.findAndAddContactsByMid(target)
                                 adanncuy.inviteIntoGroup(msg.to,[target])
                                 adanncuy.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      adanncuy.sendText(msg.to,"Limit Invite")
                                      wait['invite'] = False
                                      break
                                  
 
            elif msg.text in ["Key creator","help creator","Help creator"]:
                adanncuy.sendText(msg.to,creatorMessage)
                adanncuy.sendText(msg)

            elif msg.text in ["Key group","help group","Help group"]:
                adanncuy.sendText(msg.to,groupMessage)
                adanncuy.sendText(msg)

            elif msg.text in ["Key","help","Help"]:
                adanncuy.sendText(msg.to,helpMessage)
                adanncuy.sendText(msg)

            elif msg.text in ["Key self","help self","Help self"]:
                adanncuy.sendText(msg.to,selfMessage)              
                adanncuy.sendText(msg)

            elif msg.text in ["Key bot","help bot","Help bot"]:
                adanncuy.sendText(msg.to,botMessage)
                adanncuy.sendText(msg)

            elif msg.text in ["Key set","help set","Help set"]:
                adanncuy.sendText(msg.to,setMessage)
                adanncuy.sendText(msg)
                
            elif msg.text in ["rusuh","Rusuh","RUSUH"]:
            	adanncuy.sendText(msg.to,rusuhMessage)               
                adanncuy.sendText(msg.to, "MY FAMS")
                
            elif msg.text in ["Key media","help media","Help media"]:
                adanncuy.sendText(msg.to,mediaMessage)
                adanncuy.sendText(msg)
                
            elif msg.text in ["Key admin","help admin","Help admin"]:
                adanncuy.sendText(msg.to,adminMessage)               
                adanncuy.sendText(msg)
                

 
            elif msg.text in ["List group"]:
                    gid = adanncuy.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = adanncuy.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    adanncuy.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = adanncuy.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = adanncuy.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    adanncuy.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    adanncuy.sendText(msg.to, "Khusus Admin")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        adanncuy.sendText(msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +adanncuy.getGroup(gid).name + "\n"
                        adanncuy.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    adanncuy.sendText(msg.to, "Khusus Admin")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if adanncuy.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    adanncuy.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    adanncuy.sendText(msg.to, "Khusus Admin")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = adanncuy.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = adanncuy.getGroup(i).name
		            if h == ng:
		                adanncuy.inviteIntoGroup(i,[Creator])
			        adanncuy.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        adanncuy.sendText(msg.to,"Khusus Admin")
		except Exception as e:
		    adanncuy.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = adanncuy.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = adanncuy.getGroup(i).name
		        if h == ng:
			    adanncuy.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		            adanncuy.leaveGroup(i)
			    adanncuy.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")
 
	    elif "Leave all group" == msg.text:
		gid = adanncuy.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			adanncuy.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		        adanncuy.leaveGroup(i)
		    adanncuy.sendText(msg.to,"Success Leave All Group")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = adanncuy.getGroupIdsJoined()
                for i in gid:
                    h = adanncuy.getGroup(i).name
                    gna = adanncuy.getGroup(i)
                    if h == saya:
                        adanncuy.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = adanncuy.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        adanncuy.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        adanncuy.sendText(msg.to,"Tidak Ada Yang Pending")
                else:
                    adanncuy.sendText(msg.to,"Tidak Bisa Digunakan Diluar Group")
 
            elif msg.text in ["Ourl","Url on"]:
                if msg.toType == 2:
                    X = adanncuy.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    adanncuy.updateGroup(X)
                    adanncuy.sendText(msg.to,"Url Sudah Aktif")
                else:
                    adanncuy.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.toType == 2:
                    X = adanncuy.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    adanncuy.updateGroup(X)
                    adanncuy.sendText(msg.to,"Url Sudah Di Nonaktifkan")

                else:
                    adanncuy.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    adanncuy.sendText(msg.to,"Auto Join Sudah Aktif")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    adanncuy.sendText(msg.to,"Auto Join Sudah Di Nonaktifkan")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    adanncuy.sendText(msg.to,"Auto Join Cancel Sudah Aktif")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    adanncuy.sendText(msg.to,"Auto Join Cancel Sudah Di Nonaktifkan")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")		    
		    
 
            elif msg.text in ["R1 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    adanncuy.sendText(msg.to,"Auto R1 Sudah Aktif")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["R1 off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    adanncuy.sendText(msg.to,"Auto R1 Sudah Off")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")	
		    
		    
            elif msg.text in ["R2 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = True
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    adanncuy.sendText(msg.to,"Auto R2 Sudah Aktif")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")
            elif msg.text in ["R2 off"]:
		if msg.from_ in admin:
                    wait["detectMention2"] = False
                    adanncuy.sendText(msg.to,"Auto R2 Sudah Off")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")	
		    

            elif msg.text in ["R3 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = True
                    wait["kickMention"] = False
                    adanncuy.sendText(msg.to,"Auto R3 Sudah Aktif")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["R3 off"]:
		if msg.from_ in admin:
                    wait["detectMention3"] = False
                    adanncuy.sendText(msg.to,"Auto R3 Sudah Off")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")	
		    
 
            elif msg.text in ["Rkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False                    
                    adanncuy.sendText(msg.to,"Auto R Kick Sudah Aktif")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Rkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    adanncuy.sendText(msg.to,"Auto R Kick Sudah Off")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")			  
		    
 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = True
                adanncuy.sendText(msg.to,"Auto Cancel Sudah Aktif")
		print wait["AutoCancel"]
	     else:
		    adanncuy.sendText(msg.to,"Khusus Admin")		

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = False
                adanncuy.sendText(msg.to,"Auto Cancel Sudah Di Nonaktifkan")
		print wait["AutoCancel"]
	     else:
		    adanncuy.sendText(msg.to,"Khusus Admin")	
		    

	    elif msg.text in ["Invitepro on"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                adanncuy.sendText(msg.to,"Invite Protect Sudah Aktif")
		print wait["inviteprotect"]
	     else:
		    adanncuy.sendText(msg.to,"Khusus Admin")		

	    elif msg.text in ["Invitepro off"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                adanncuy.sendText(msg.to,"Invite Protect Sudah Di Nonaktifkan")
		print wait["inviteprotect"]
	     else:
		    adanncuy.sendText(msg.to,"Khusus Admin")		    

	    elif "Qr on" in msg.text:
	     if msg.from_ in admin:	        
	        wait["Qr"] = True
	    	adanncuy.sendText(msg.to,"QR Protect Sudah Aktif")
	     else:
		    adanncuy.sendText(msg.to,"Khusus Admin")	    	

	    elif "Qr off" in msg.text:
	     if msg.from_ in admin:	        
	    	wait["Qr"] = False
	    	adanncuy.sendText(msg.to,"Qr Protect Sudah Di Nonaktifkan")
	     else:
		    adanncuy.sendText(msg.to,"Khusus Admin")	    	

                        

	    elif "Autokick on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = True
		     adanncuy.sendText(msg.to,"Auto Kick Sudah Aktif")
	     else:
	        adanncuy.sendText(msg.to,"Khusus Admin")	     

	    elif "Autokick off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = False
		     adanncuy.sendText(msg.to,"Auto Kick Sudah Di Nonaktifkan")
	     else:
	        adanncuy.sendText(msg.to,"Khusus Admin")	     


            elif msg.text in ["Allprotect on"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = True
                    wait["inviteprotect"] = True                   
                    wait["AutoKick"] = True
                    wait["Qr"] = True
                    adanncuy.sendText(msg.to,"All Protect Sudah Aktif Semua")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Allprotect off"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = False
                    wait["inviteprotect"] = False                    
                    wait["AutoKick"] = False
                    wait["Qr"] = False
                    adanncuy.sendText(msg.to,"All Protect Sudah Di Nonaktifkan Semua")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")


            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                adanncuy.sendText(msg.to,"Contact Sudah Aktif")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                adanncuy.sendText(msg.to,"Contact Sudah Di Nonaktifkan")
                

            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                adanncuy.sendText(msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                adanncuy.sendText(msg.to,"Always Read Sudah Di Nonaktifkan")                


            elif msg.text in ["Notif on"]:
                if wait["Notif"] == True:
                    if wait["lang"] == "JP":
                        adanncuy.sendText(msg.to,"Notif Di Aktifkanヾ(*´∀｀*)ﾉ")
                else:
                    wait["Notif"] = True
                    if wait["lang"] == "JP":
                        adanncuy.sendText(msg.to,"Sudah Onヽ(´▽｀)/")

            elif msg.text in ["Notif off"]:
                if wait["Notif"] == False:
                    if wait["lang"] == "JP":
                        adanncuy.sendText(msg.to,"Notif Di Nonaktifkan(　＾∇＾)")
                else:
                    wait["Notif"] = False
                    if wait["lang"] == "JP":
                        adanncuy.sendText(msg.to,"Sudah Off(p′︵‵。)")
                        
                        
            elif "Dooorrrr" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                adanncuy.sendText(msg.to,"Ngintip nih....!!!!!")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    adanncuy.sendText(msg.to, "Cek Sider Off")
                else:
                    adanncuy.sendText(msg.to, "Heh Belom Di Set")                         


            elif msg.text in ["Settings","Status"]:
                md = ""
		if wait["Notif"] == True: md+="┣🇮🇩━⏩✔️ Notif : On\n"
		else:md+="┣🇮🇩━⏩✖ Notif : Off\n"
		if wait["AutoJoin"] == True: md+="┣🇮🇩━⏩✔️ Auto Join : On\n"
                else: md +="┣🇮🇩━⏩✖ Auto Join : Off\n"
		if wait["AutoJoinCancel"] == True: md+="┣🇮🇩━⏩✔️ Auto Join Cancel : On\n"
                else: md +="┣🇮🇩━⏩✖ Auto Join Cancel : Off\n"                
		if wait["Contact"] == True: md+="┣🇮🇩━⏩✔️ Info Contact : On\n"
		else: md+="┣🇮🇩━⏩✖ Info Contact : Off\n"
                if wait["AutoCancel"] == True:md+="┣🇮🇩━⏩✔️ Auto Cancel : On\n"
                else: md+= "┣🇮🇩━⏩✖ Auto Cancel : Off\n"
                if wait["inviteprotect"] == True:md+="┣🇮🇩━⏩✔️ Invite Protect : On\n"
                else: md+= "┣🇮🇩━⏩✖ Invite Protect : Off\n"                
		if wait["Qr"] == True: md+="┣🇮🇩━⏩✔️ Qr Protect : On\n"
		else:md+="┣🇮🇩━⏩✖ Qr Protect : Off\n"
		if wait["AutoKick"] == True: md+="┣🇮🇩━⏩✔️ Auto Kick : On\n"
		else:md+="┣🇮🇩━⏩✖ Auto Kick : Off\n"
		if wait["alwaysRead"] == True: md+="┣🇮🇩━⏩✔️ Always Read : On\n"
		else:md+="┣🇮🇩━⏩✖ Always Read: Off\n"
		if wait["detectMention"] == True: md+="┣🇮🇩━⏩✔️ Auto R1 : On\n"
		else:md+="┣🇮🇩━⏩✖ Auto R1 : Off\n"		
		if wait["detectMention2"] == True: md+="┣🇮🇩━⏩✔️ Auto R2 : On\n"
		else:md+="┣🇮🇩━⏩✖ Auto R2 : Off\n"	
		if wait["detectMention3"] == True: md+="┣🇮🇩━⏩✔️ Auto R3 : On\n"
		else:md+="┣🇮🇩━⏩✖ Auto R3 : Off\n"			
		if wait["kickMention"] == True: md+="┣🇮🇩━⏩✔️ Auto R Kick : On\n"
		else:md+="┣🇮🇩━⏩✖ Auto R Kick : Off\n"				
		if wait["Sider"] == True: md+="┣🇮🇩━⏩✔️ Auto Sider : On\n"
		else:md+="┣🇮🇩━⏩✖ Auto Sider: Off\n"	
		if wait["Simi"] == True: md+="┣🇮🇩━⏩✔️ Simisimi : On\n"
		else:md+="┣🇮🇩━⏩✖ Simisimi: Off\n"		
                adanncuy.sendText(msg.to,"╭━━━━━━━━━━━━━━━━━━━━╮\n""│♠✴ SETTINGS ✴♠\n""│━━━━━━━━━━━━━━━━━━━━\n"+md+"╰━━━━━━━━━━━━━━━━━━━━╯")


            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                adanncuy.sendMessage(msg)
                
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = adanncuy.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    adanncuy.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    adanncuy.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = adanncuy.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    adanncuy.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    adanncuy.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = adanncuy.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    adanncuy.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    adanncuy.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = adanncuy.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    adanncuy.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    adanncuy.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = adanncuy.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    adanncuy.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    adanncuy.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = adanncuy.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    adanncuy.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    adanncuy.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = adanncuy.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    adanncuy.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    adanncuy.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = adanncuy.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    adanncuy.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    adanncuy.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = adanncuy.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    adanncuy.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    adanncuy.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = adanncuy.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    adanncuy.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    adanncuy.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}


            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["hehehe","hehe"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["you","kau","kamu"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","mohon","tolong"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","kaget"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["lucu","ngakak","lol"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '110',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["hmm","hmmm"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '101',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["tidur"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["woi","kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)
                

            elif "tag all" == msg.text.lower():
                 group = adanncuy.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 adanncuy.sendMessage(cnt)
                 
            elif "tagall" == msg.text.lower():
                 group = adanncuy.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 adanncuy.sendMessage(cnt)                 


            elif msg.text in ["Setview","Setpoint","Cctv"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                adanncuy.sendText(msg.to, "♠Checkpoint Checked♠")
                print "Setview"

            elif msg.text in ["Viewseen","Check","Ciduk","Cyduk"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = adanncuy.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╭━━━━━━━━━━━━━━━━━━━━╮\n│     ♠✴ LIST VIEWERS ✴♠\n│━━━━━━━━━━━━━━━━━━━━\n┣🇮🇩━⏩"
                        grp = '\n┣🇮🇩━⏩ '.join(str(f) for f in dataResult)
                        total = '\n│━━━━━━━━━━━━━━━━━━━━\n┣🇮🇩━⏩ Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╰━━━━━━━━━━━━━━━━━━━━╯"
                        adanncuy.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        adanncuy.sendText(msg.to, "♠Auto Checkpoint♠")                        
                    else:
                        adanncuy.sendText(msg.to, "♠Belum Ada Viewers♠")
                    print "Viewseen"


	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    adanncuy.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    adanncuy.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = adanncuy.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    adanncuy.findAndAddContactsByMids(mi_d)
		    adanncuy.sendText(msg.to,"Success Add all")


            elif msg.text in ["Invite"]:
                wait["invite"] = True
                adanncuy.sendText(msg.to,"Send Contact")
                
                

            elif msg.text in ["Autolike"]:
                wait["likeOn"] = True
                adanncuy.sendText(msg.to,"Sudah on")                


            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                adanncuy.sendText(msg.to,"Send Contact")
                

            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                adanncuy.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Copycontact"]:
                wait["copy"] = True
                adanncuy.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Sticker on"]:
                wait["sticker"] = True
                adanncuy.sendText(msg.to,"Sticker ID Detect Already On.")  
                
            elif msg.text in ["Bot off"]:
                wait["Bot"] = False
                adanncuy.sendText(msg.to,"Bot Sudah Di Nonaktifkan.")  

	    elif "Recover" in msg.text:
		thisgroup = adanncuy.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		adanncuy.createGroup("Recover", mi_d)
		adanncuy.sendText(msg.to,"Success recover")



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = adanncuy.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    adanncuy.updateGroup(X)
                else:
                    adanncuy.sendText(msg.to,"It can't be used besides the group.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in admin:
		    adanncuy.kickoutFromGroup(msg.to,[midd])
		else:
		    adanncuy.sendText(msg.to,"Admin Detected")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                adanncuy.findAndAddContactsByMid(midd)
                adanncuy.inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "uc889c1f8f74274f117e0a0d69ccc559c"
                adanncuy.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
                gs = adanncuy.getGroup(msg.to)
                adanncuy.sendText(msg.to,"Selamat Datang Di "+ gs.name)
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                adanncuy.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = adanncuy.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			adanncuy.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~adanncuyistifik")
		    adanncuy.sendText(msg.to,"Success BC BosQ")
		else:
		    adanncuy.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Cancel"]:
                gid = adanncuy.getGroupIdsInvited()
                for i in gid:
                    adanncuy.rejectGroupInvitation(i)
                adanncuy.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = adanncuy.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        adanncuy.updateGroup(x)
                    gurl = adanncuy.reissueGroupTicket(msg.to)
                    adanncuy.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        adanncuy.sendText(msg.to,"Can't be used outside the group")
                    else:
                        adanncuy.sendText(msg.to,"Not for use less than group")


            elif msg.text in ["timeline"]:
		try:
                    url = adanncuy.activity(limit=5)
		    adanncuy.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["@bye","@Bye"]:
		    adanncuy.leaveGroup(msg.to)		    
		    

            elif msg.text in ["Absen"]:
		adanncuy.sendText(msg.to,"Hadir!!")


            elif msg.text.lower() in ["respon"]:
                adanncuy.sendText(msg.to,responsename)

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		adanncuy.sendText(msg.to, "Progress...")
                adanncuy.sendText(msg.to, "%sseconds" % (elapsed_time))
                
            elif msg.text in ["Speed test"]:
                start = time.time()
                adanncuy.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                adanncuy.sendText(msg.to, "%sseconds" % (elapsed_time))                
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    adanncuy.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    adanncuy.sendText(msg.to,"send contact")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = adanncuy.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        adanncuy.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    adanncuy.sendText(msg.to,"Succes BosQ")
                                except:
                                    adanncuy.sendText(msg.to,"Error")
			    else:
				adanncuy.sendText(msg.to,"Admin Detected~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    adanncuy.sendText(msg.to,"Tidak Ada")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +adanncuy.getContact(mi_d).displayName + "\n"
                    adanncuy.sendText(msg.to,"===[Blacklist User]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = adanncuy.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        adanncuy.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                adanncuy.sendText(msg.to,"Succes BosQ")
                            except:
                                adanncuy.sendText(msg.to,"Succes BosQ")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    adanncuy.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All Success❉ ┐") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = adanncuy.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            adanncuy.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            adanncuy.kickoutFromGroup(msg.to,[jj])
                        adanncuy.sendText(msg.to,"Blacklist emang pantas tuk di usir")
		else:
		    adanncuy.sendText(msg.to, "Khusus creator")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = adanncuy.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            adanncuy.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                adanncuy.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

 
            elif "Kickall" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Kickall","")
                        gs = adanncuy.getGroup(msg.to)
                        adanncuy.sendText(msg.to,"Dadaaah~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            adanncuy.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        adanncuy.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        adanncuy.sendText(msg.to,str(e))
			    adanncuy.inviteIntoGroup(msg.to, targets)
 

	    elif msg.text in ["Bot restart","Reboot"]:
		if msg.from_ in Creator:
		    adanncuy.sendText(msg.to, "Bot Has Been Restarted...")
		    restart_program()
		    print "@Restart"
		else:
		    adanncuy.sendText(msg.to, "No Access")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    


            elif 'Crash' in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "adanncuy,'"}
                adanncuy.sendMessage(msg)

 
            elif "copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = adanncuy.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       adanncuy.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               adanncuy.CloneContactProfile(target)
                               adanncuy.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Mybackup"]:
                try:
                    adanncuy.updateDisplayPicture(backup1.pictureStatus)
                    adanncuy.updateProfile(backup1)
                    adanncuy.sendText(msg.to, "Done (^_^)")
                except Exception as e:
                    adanncuy.sendText(msg.to, str(e))

 
	    elif "musik " in msg.text:
					songname = msg.text.replace("musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						adanncuy.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						adanncuy.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						adanncuy.sendAudioWithURL(msg.to,abc)
						adanncuy.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
	
            elif 'lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        adanncuy.sendText(msg.to, hasil)
                except Exception as wak:
                        adanncuy.sendText(msg.to, str(wak))
             
            
            
            elif "Fancytext " in msg.text:
                    txt = msg.text.replace("Fancytext ", "")
                    adanncuy.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = adanncuy.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        adanncuy.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = adanncuy.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                adanncuy.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                adanncuy.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = adanncuy.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        adanncuy.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = adanncuy.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                adanncuy.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                adanncuy.sendText(msg.to,"Upload image failed.")
                                
            elif "Cpp" in msg.text:
                if msg.from_ in admin:
                    path = "adanncuy.jpg"
                    adanncuy.sendText(msg.to,"Update PP :")
                    adanncuy.sendImage(msg.to,path)
                    adanncuy.updateProfilePicture(path)                                
                                
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = adanncuy.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        adanncuy.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = adanncuy.getContact(target)
                                adanncuy.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                adanncuy.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = adanncuy.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        adanncuy.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = adanncuy.getContact(target)
                                adanncuy.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                adanncuy.sendText(msg.to,"Upload image failed.")

            elif msg.text.lower() in ["pap owner","pap creator"]:
                                link = ["http://dl.profile.line-cdn.net/0hFR-rB8h-GX0QCzWZMOZmKixOFxBnJR81aG9eSTUNREhtOVYqJWgFSWYDR05vOwp7K2sCGTELRUVo"]
                                pilih = random.choice(link)
                                adanncuy.sendImageWithURL(msg.to,pilih)

 
            elif "Spam: " in msg.text:
                  bctxt = msg.text.replace("Spam: ", "")
                  t = 10
                  while(t):
                    adanncuy.sendText(msg.to, (bctxt))
                    t-=1

            elif "Scbc " in msg.text:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = adanncuy.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      adanncuy.sendText(manusia, (bctxt))
                      t-=1

            elif "Cbc " in msg.text:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = adanncuy.getAllContactIds()
                  for manusia in orang:
                    adanncuy.sendText(manusia, (broadcasttxt))

 
            elif 'ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    tj = text1[0].replace("s150x150/","")
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    adanncuy.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    adanncuy.sendImageWithURL(msg.to, tj)
                except Exception as njer:
                	adanncuy.sendText(msg.to, str(njer))
                	
                	
            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                adanncuy.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                adanncuy.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtube ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    adanncuy.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    adanncuy.sendText(msg.to,"Could not find it")
                    
                    
            elif 'Youtubevideo ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        adanncuy.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        adanncuy.sendText(msg.to, "Could not find it")                    

 
            elif "Say " in msg.text:
                say = msg.text.replace("Say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                adanncuy.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                adanncuy.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                adanncuy.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = adanncuy.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                adanncuy.sendAudio(msg.to,"hasil.mp3")
                
            elif "lurk on" == msg.text.lower():
               #if msg.from_ in admin:
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         adanncuy.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     adanncuy.sendText(msg.to, "Set the lastseens' point (｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2


            elif "lurk off" == msg.text.lower():
               #if msg.from_ in admin:
                if msg.to not in wait2['readPoint']:
                    adanncuy.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    adanncuy.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))



                    
            elif "lurkers" == msg.text.lower():
            	#if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             adanncuy.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = adanncuy.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+ "@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          adanncuy.sendMessage(msg)
                          adanncuy.sendText(msg.to, "Jika sudah lihat sider please\ntulis lurk on lagi kak  (｀・ω・´)\n \n"  +  datetime.now().strftime('%H:%M:%S'))
                        except Exception as error:
                              print error
                        pass
               
                    else:
                        adanncuy.sendText(msg.to, "Lurking has not been set (｀・ω・´)\n \n"  +  datetime.now().strftime('%H:%M:%S'))    


            elif msg.text.lower() in ["hi","hai","halo","hallo"]:
                    beb = "Hi Sayang 😘 " +adanncuy.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    adanncuy.sendText(msg.to,beb)



            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                adanncuy.sendText(msg.to,"Sedang Mencari...")
                adanncuy.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                adanncuy.sendText(msg.to,"Tuh Linknya Kak (^_^)")


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = adanncuy.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        adanncuy.sendText(msg.to, g.mid)
                    else:
                        pass


            elif "Mybio " in msg.text:
                    string = msg.text.replace("Mybio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = adanncuy.getProfile()
                        profile.statusMessage = string
                        adanncuy.updateProfile(profile)
                        adanncuy.sendText(msg.to,"Done")

            elif "Myname " in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("Myname ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = adanncuy.getProfile()
                        profile.displayName = string
                        adanncuy.updateProfile(profile)
                        adanncuy.sendText(msg.to,"Done")



            elif msg.text.lower() in ["mymid","myid"]:
                middd = "Name : " +adanncuy.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                adanncuy.sendText(msg.to,middd)

            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                adanncuy.sendMessage(msg)

            elif msg.text in ["rusuhan","MY FAMS"]:
                msg.contentType = 13
                rusuhan1 = "udefd75736ced80dc8fca8966d246ac6f"
                rusuhan2 = "u959231880d4f63db97ad90f41859b5b4"
                rusuhan3 = "ucd1bf4681a9310045c6b6fce00b18172"
                rusuhan4 = "u702e1287d9166485864d4cd3abda3e59"
                rusuhan5 = "ua99f3c139ab0b25918184bb047403003"
                rusuhan6 = "u4ac89e2857f399253290ad9d3b751554"
                rusuhan7 = "u5d7fcdd055a6de2a6fd5735779235646"
                rusuhan8 = "u581f341f978151394fb5e1e505ab9851"
                rusuhan9 = "u90b96d89ce8813efbd11c548a5b6fa3c"
                rusuhan10 = "u8bc856497159637e0dcb8450fa06e8bd"
                rusuhan11 = "ue8683bf4a314bcf0b35c15194d587ca9"
                rusuhan12 = "uf20915cdf94ddfcfca65328ae9ecf32f"
                rusuhan13 = "u581d09157fc47e15ece9796a765080e8"
                rusuhan14 = "u8cf3c7c7aba529dab47755b0e7375251"
                rusuhan15 = "u8770ecbc6635e4837595eadcb5a9c9c2"
                rusuhan16 = "u4b3fda5c4db9a292fbba9a3417c836f9"
                rusuhan17 = "u1ba0f8d6a4fec5edf70df951190aef64"
                rusuhan18 = "ufcd3e0fb51c4a7e9c5ccfb4087b0ba5e"
                rusuhan19 = "u8a25013e3d9d9e3c4091dd03d3e6cff4"
                rusuhan20 = "u904a026b6ebe344ff4fdd72ca2b87dc5"
                rusuhan21 = "u52b0a26c865f3e71204a6fb6533bc06c"
                rusuhan22 = "uf44f06815769534c4fed2a905f0d527e"
                rusuhan23 = "ua23886c9dea0a603bde1f8b74622305f"
                rusuhan24 = "ue28d2f1e6447e85638ed5ae9f03f1c12"
                rusuhan25 = "u58443b7393aedc0dae4d4e0676450da4"
                rusuhan26 = "u5b343d9bf64c9db91b97238cb019b701"
                rusuhan27 = "u20001e62816b04fc2efd27d98035dc9a"
                rusuhan28 = "u619700f14e75b1130bfde4594a274533"
                rusuhan29 = "u49fe734da9f8acedf2acc1faa82e65f0"
                rusuhan30 = "u0837f03a621c6876df5c67d0a7386a53"
                rusuhan31 = "u8ee0919fab6e7b2a4aa45eef6ecffb7b"
                msg.contentMetadata = {'mid': ar}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan1}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan2}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan3}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan4}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan5}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan6}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan7}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan8}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan9}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan10}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan11}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan12}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan13}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan14}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan15}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan16}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan17}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan18}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan19}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan20}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan21}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan22}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan23}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan24}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan25}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan26}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan27}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan28}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan29}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan30}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': rusuhan31}
                random.choice(KAC).sendMessage(msg)
		random.choice(KAC).sendText(msg.to,"MASI BERANI BACOT FUCK...(-_-)")
		
            elif "apakah " in msg.text:
                apk = msg.text.replace("apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                adanncuy.sendAudio(msg.to,"hasil.mp3")
                
            elif "hari " in msg.text:
                apk = msg.text.replace("hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                adanncuy.sendAudio(msg.to,"hasil.mp3")   


            elif "berapa " in msg.text:
                apk = msg.text.replace("berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                adanncuy.sendAudio(msg.to,"hasil.mp3")
                
            elif "berapakah " in msg.text:
                apk = msg.text.replace("berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                adanncuy.sendAudio(msg.to,"hasil.mp3")                

            elif "kapan " in msg.text:
                apk = msg.text.replace("kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                adanncuy.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                adanncuy.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                adanncuy.sendText(msg.to,"Simisimi Di Nonaktifkan")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    adanncuy.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch " in msg.text:
                    query = msg.text.replace("Youtubesearch ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        adanncuy.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'


 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                adanncuy.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                adanncuy.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                adanncuy.sendText(msg.to, A)                

            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adanncuy.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adanncuy.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
                
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adanncuy.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
                
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adanncuy.sendText(msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = adanncuy.getAllContactIds()
                kontak = adanncuy.getContacts(contactlist)
                num=1
                msgs="━━━━━━━━━List Friend━━━━━━━━━"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n━━━━━━━━━List Friend━━━━━━━━━\n\nTotal Friend : %i" % len(kontak)
                adanncuy.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = adanncuy.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="━━━━━━━━━List Member━�����━━━━━━━-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n━━━━━━━━━List Member━━━━━━━━━\n\nTotal Members : %i" % len(group)
                adanncuy.sendText(msg.to, msgs)

            

 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = adanncuy.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    adanncuy.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = adanncuy.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            adanncuy.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = adanncuy.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                adanncuy.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = adanncuy.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                adanncuy.sendText(msg.to,path)
 
            elif "Name" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = adanncuy.getContact(key1)
                cu = adanncuy.channel.getCover(key1)
                try:
                    adanncuy.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    adanncuy.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Profile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = adanncuy.getContact(key1)
                cu = adanncuy.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    adanncuy.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    adanncuy.sendText(msg.to,"Profile Picture " + contact.displayName)
                    adanncuy.sendImageWithURL(msg.to,image)
                    adanncuy.sendText(msg.to,"Cover " + contact.displayName)
                    adanncuy.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Contact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = adanncuy.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                adanncuy.sendMessage(msg)

            elif "Info" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = adanncuy.getContact(key1)
                cu = adanncuy.channel.getCover(key1)
                try:
                    adanncuy.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    adanncuy.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Bio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = adanncuy.getContact(key1)
                cu = adanncuy.channel.getCover(key1)
                try:
                    adanncuy.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    adanncuy.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)


            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                adanncuy.sendText(msg.to,van)
                
                 
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                adanncuy.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n========== I N F O R M A S I ==========")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                adanncuy.sendText(msg.to, rst)                
                 
                
            elif "SearchID " in msg.text:
                userid = msg.text.replace("SearchID ","")
                contact = adanncuy.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                adanncuy.sendMessage(msg)
                
            elif "Searchid " in msg.text:
                userid = msg.text.replace("Searchid ","")
                contact = adanncuy.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                adanncuy.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        adanncuy.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        adanncuy.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        adanncuy.sendText(msg.to,"Error")      
                        
                        
            elif "Invitemeto " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitemeto ","")
                    if gid == "":
                        adanncuy.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            adanncuy.findAndAddContactsByMid(msg.from_)
                            adanncuy.inviteIntoGroup(gid,[msg.from_])
                        except:
                            adanncuy.sendText(msg.to,"Mungkin Saya Tidak Di Dalaam Grup Itu")


            elif msg.text in ["Glist"]:
                adanncuy.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = adanncuy.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "┣🇮🇩━⏩" + "%s\n" % (adanncuy.getGroup(i).name +" ~> ["+str(len(adanncuy.getGroup(i).members))+"]")
                adanncuy.sendText(msg.to,"╭━━━━━━━━━━━━━━━━━━━━╮\n│      ♠✴ LIST GROUPS✴♠\n│━━━━━━━━━━━━━━━━━━━━\n" + h + "│━━━━━━━━━━━━━━━━━━━━" + "\n│ Total Groups =" +" ["+str(len(gid))+"]\n╰━━━━━━━━━━━━━━━━━━━━╯")

            elif msg.text in ["Glistmid"]:   
                gruplist = adanncuy.getGroupIdsJoined()
                kontak = adanncuy.getGroups(gruplist)
                num=1
                msgs="━━━━━━━━━List GrupMid━━━━━━━━━"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n━━━━━━━━━List GrupMid━━━━━━━━━\n\nTotal Grup : %i" % len(kontak)
                adanncuy.sendText(msg.to, msgs)



            elif "Google: " in msg.text:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    adanncuy.sendText(msg.to,"Sedang Mencari...")
                    adanncuy.sendText(msg.to, "https://www.google.com/" + b)
                    adanncuy.sendText(msg.to,"Itu Dia Linknya. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        adanncuy.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = adanncuy.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            adanncuy.sendText(msg.to,h)
                        except Exception as error:
                            adanncuy.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = adanncuy.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                adanncuy.rejectGroupInvitation(i)
                            except:
                                adanncuy.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        adanncuy.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        adanncuy.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Acc invite"]:
                if msg.from_ in admin:
                    gid = adanncuy.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = adanncuy.getGroup(i)
                            _list += gids.name
                            adanncuy.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        adanncuy.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        adanncuy.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  


            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                adanncuy.sendGifWithURL(msg.to,gore)
                

                
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        adanncuy.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        adanncuy.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        adanncuy.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        adanncuy.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            adanncuy.sendText(msg.to,"Nothing")
                        else:
                            mc = "Target Mimic User:\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+adanncuy.getContact(mi_d).displayName + "\n"
                            adanncuy.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                adanncuy.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                adanncuy.sendText(msg.to,"Mimic change to target")
                            else:
                                adanncuy.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        adanncuy.sendText(msg.to,"Reply Message on")
                    else:
                        adanncuy.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        adanncuy.sendText(msg.to,"Reply Message off")
                    else:
                        adanncuy.sendText(msg.to,"Sudah off")



        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = adanncuy.fetchOps(adanncuy.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(adanncuy.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            adanncuy.Poll.rev = max(adanncuy.Poll.rev, Op.revision)
            bot(Op)

