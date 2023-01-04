#discord: DizzeriX#9775

__author__ = "thekip07"
__version__ = "1.0"

import socketio 
import requests
from time import sleep 
from colorama import *
from omletarcade.errors import *
from omletarcade import API

init(autoreset=True)

def set_timeout(time:int):
    try:
        sleep(time)
    except:
        raise TimeoutIsNotInteger(not_integer)

def get_token():
    print(Fore.CYAN + "[omletarcade]: " + Fore.WHITE + "https://omapi.ru/")