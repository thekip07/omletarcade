#discord: DizzeriX#9775

__author__ = "thekip07"
__version__ = "1.0"

from time import sleep 
from omletarcade.API import Public, Private
from omletarcade.errors import *

def set_timeout(time:int):
    try:
        sleep(time)
    except:
        raise Timeout(not_integer)

def get_token():
    print("[omletarcade]: https://omapi.ru/")