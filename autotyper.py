import requests
from colorama import *
import threading
import ctypes
import os
from pystyle import System, Colorate, Colors
import base64
from time import sleep

DEVELOPER = "RequiredHandler#9113"
VERSION = "v1.0"


token = input(Colorate.Horizontal(Colors.rainbow, f"Your Token > "))
channel_id = input(Colorate.Horizontal(Colors.rainbow, f"Wich Channel ID? > "))

correct = (f'''
You filled this Data in this Terminal:
Token: {token}
ChannelID: {channel_id}
''')
print(Colorate.Horizontal(Colors.rainbow, correct))
correctdata = input(Colorate.Horizontal(Colors.rainbow, f"\n\n• Choice y/n » "))
if correctdata == 'y':
    print(Colorate.Horizontal(Colors.rainbow, f'Tool Starting! IF CODE: 401 COMMING ARE U PUTING DATA FAKE OR NOT FOUNDED!'))
    sleep(1.2)
    while True:
        typing = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/typing', headers={"authorization": token})
        print(typing.status_code)
        sleep(1.2)
    
if correctdata == 'n':
    os.system('cls')
    os.system('clear')
    os.system("python autotyper.py")





