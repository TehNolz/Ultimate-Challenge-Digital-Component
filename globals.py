from util import *
import logging
import os

#Data
imgIndex = {}
cardConfig = {}
userConfig = {
    "playerCount": 4,
    "players": [
        None,
        None,
        None,
        None,
        None,
        None,
    ],
    "settings": {
        "useDecks": [
            "base",
            "expansion1",
            "expansion2"
        ],
        "bg_select": 'Blue',
        "primary_color": color(50, 230, 230),
        "objectAnims_OnOff": True,
        "anims_OnOff": True,
        "font": 'Open Sans',
        "enable_debug_console": False
    }
}
fonts = {}

#Scale
baseScale = 1.0
baseScaleXY = Vector2(1,1)

# Base screen size
# Probably not implemented everywhere, but not my problem >:(
baseScreenSize = Vector2(1133, 600)

#Menus
currentMenu = "mainMenu"

# Background
backgroundImgName = 'background'
backgroundImg = None

#Misc
maxLogFiles = 4
logFile = lambda x: 'data\\logs\\ucdc_app.'+str(x)+'.log'
# This is to trigger exceptions if the program loads from %appdata%
# It basically just helps with the traceback
os.listdir('data')
if not os.path.exists('data\\logs'):
    os.mkdir('data\\logs')
for i in list(range(maxLogFiles))[::-1]:
    if os.path.exists(logFile(i)):
        if i == maxLogFiles-1:
            os.remove(logFile(i))
        else:
            os.rename(logFile(i), logFile(i+1))
    
logging.basicConfig(filename=logFile(0), level=logging.NOTSET, format='[%(asctime)s][%(name)s:%(levelname)s] %(message)s',  filemode='w+', datefmt='%X')
log = logging.getLogger("LOG")
playerCount = 0
font = None

#Text boxes
activeTextBox = None
textBoxDict = {"global": []}
