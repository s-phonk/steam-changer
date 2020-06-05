from steam.client import SteamClient
from random import choice
from threading import Thread
from tkinter import messagebox
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from time import sleep
import logging
from datetime import datetime
import os 



dirname = os.path.dirname(os.path.abspath(__file__))

client = SteamClient()

#logging
logging.basicConfig(filename=dirname+'\\sample.log', level=logging.INFO, filemode='w', format='%(asctime)s %(levelname)-8s %(message)s')
logging.info(datetime.fromtimestamp(1576280665))


Tk().withdraw()
messagebox.showinfo('Путь до файла', 'Введите путь до файла с login:pass')
filepass = askopenfilename() 
messagebox.showinfo('Путь до файла', 'Введите путь до файла с именами')
namepass = askopenfilename()

with open(namepass) as f:
    names = f.readlines()

#get number of lines
def get_lines():
    with open(filepass, "r") as backfile:
        lines = backfile.readlines()
        return len(lines)

lines = get_lines()

with open(filepass) as f:
    credentials = [x.strip().split(':', 1) for x in f]


global x
x=0

apps = ['1057850','730','570','444090']




global ses
def log_and_change(log, passw):
    global x 
    x+=1
    client.cli_login(username=log, password=passw)
    print("Your profile name is: %s" % client.user.name)
    client.change_status(player_name=choice(names))
    global ses
    ses = client.get_web_session(language='english')
    client.request_free_license(app_ids=apps)
    sleep(1)
    print('Successfully changed name and added games')
    print("Your new profile name is: %s" % client.user.name)
    client.logout()
    
    logging.info("Account: "+ log+ ". Successfully changed name and added games")
    
    print('-------------------------------------------------------')
    
for i in range(lines):
    log_and_change(credentials[x][0], credentials[x][1])
    



    
    
    


    


    



















