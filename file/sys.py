import time
import os
from os import system, name 

#fungsi utk membersihkan layar
def clear():
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#Pesan ketika keluar
def msg_quit():
    print("""
    
'########::'#######:::::'###:::::'######::'########:
... ##..::'##.... ##:::'## ##:::'##... ##:... ##..::
::: ##:::: ##:::: ##::'##:. ##:: ##:::..::::: ##::::
::: ##:::: ##:::: ##:'##:::. ##:. ######::::: ##::::
::: ##:::: ##:::: ##: #########::..... ##:::: ##::::
::: ##:::: ##:::: ##: ##.... ##:'##::: ##:::: ##::::
::: ##::::. #######:: ##:::: ##:. ######::::: ##::::
:::..::::::.......:::..:::::..:::......::::::..:::::
'########::'##::::'##:'##:::::::'##::::'##:::::::'##::::::::::'#####:::
 ##.... ##: ##:::: ##: ##::::::: ##:::: ##:::::'####:::::::::'##.. ##::
 ##:::: ##: ##:::: ##: ##::::::: ##:::: ##:::::.. ##::::::::'##:::: ##:
 ##:::: ##: ##:::: ##: ##::::::: ##:::: ##::::::: ##:::::::: ##:::: ##:
 ##:::: ##: ##:::: ##: ##::::::: ##:::: ##::::::: ##:::::::: ##:::: ##:
 ##:::: ##: ##:::: ##: ##::::::: ##:::: ##::::::: ##:::'###:. ##:: ##::
 ########::. #######:: ########:. #######::::::'######: ###::. #####:::
........::::.......:::........:::.......:::::::......::...::::.....::::

Copyright (c) Kelompok 7 BSI - Dasar Pemrograman

    """)
    print("Terima kasih sudah menggunakan program kami...")
    time.sleep(2)
    print("Akan keluar dalam 5 detik...")
    time.sleep(5)
    clear()
    quit()

#atur panjang lebar program
def check_width():
    cmd = ''' 
    mode con: cols=100 lines=40
    '''
    os.system(cmd)

def msg_waring(msg):
    print("\033[93m" + msg + "\033[0m")
