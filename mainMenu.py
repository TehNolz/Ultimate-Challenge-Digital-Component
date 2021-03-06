import globals
from Object import Object
from Button import Button
from util import *

def init():
    width = 1133
    height = 600
    global playGame
    global buttons
    
    r = RoundRect(-150, -150, 300, 300, 50)
    r *= 0.5
    Object.startGroup()
    
    #Settings button
    settingsButton = Button(width*0.25, height/2, r.copy())
    settingsButton.releaseAction = gotoSettingsScreen
    settingsButton.applyStyle('pulsate')
    settingsButton.text = "Settings"
    
    #Play button
    playButton = Button(width*0.50, height/2, r.copy())
    playButton.releaseAction = gotoGameSetupScreen
    playButton.applyStyle('rotate_pulsate')
    playButton.text = "Play"
    
    #Manual button
    manualButton = Button(width*0.75, height/2, r.copy())
    manualButton.releaseAction = gotoManualScreen
    manualButton.applyStyle('pulsate')
    manualButton.text = "Manual"
    
    quitButton = Button(37, 37, RoundRect(-25, -25, 50, 50) * 0.75)
    quitButton.releaseAction = exitGame
    quitButton.textSize *= 3
    quitButton.applyStyle('compact')
    quitButton.description = 'Quit'
    quitButton.icon = globals.imgIndex['tictactoe-cross'].copy()
    quitButton.iconScale = 0.5
    
    buttons = Object.endGroup()
    
def draw():
    scale(*globals.baseScaleXY)
    global buttons
    for o in buttons:
        o.update()

#Goto menu functions
def gotoGameSetupScreen(*args):
    if args[1] == LEFT:
        globals.currentMenu = "gameSetupScreen"
def gotoSettingsScreen(*args):
    if args[1] == LEFT:
        globals.currentMenu = "settings"
def gotoManualScreen(*args):
    if args[1] == LEFT:
        globals.currentMenu = "manual"
def exitGame(*args):
    # Desperate attempt at containing a memory leak in Processing
    for i in globals.imgIndex.values():
        g.removeCache(i)
    import settingsScreen
    del settingsScreen.onScreenFeatures
    del globals.imgIndex
    exit()
