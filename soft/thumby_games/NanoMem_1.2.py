# NanoMem
# By CoolieCoolster
# 10/21/2021
# Based on TinyMem
# Note: Save data management functionality throughout the program has been commented out until it can be tested for accuracy.


import thumby
import random
import time
import gc

gc.enable()


# GRAPHICS

# Title Screen Text (64x22)
s1e0=(0,0,255,1,243,102,204,159,1,255,0,255,1,237,45,237,1,255,0,255,1,243,102,204,159,1,255,0,255,1,125,125,125,1,255,0,255,1,243,102,76,102,243,1,255,0,255,1,109,125,69,199,0,255,1,243,102,76,102,243,1,255,0,0,
            192,48,201,1,225,0,192,1,1,225,16,9,9,193,32,193,1,193,32,193,1,193,56,0,129,81,1,192,161,65,1,1,129,1,193,48,201,1,193,32,192,0,1,65,161,32,1,193,161,65,1,193,32,241,9,1,192,32,192,1,129,97,32,192,
            0,1,0,0,4,3,0,0,0,0,1,1,0,0,1,0,0,8,57,8,0,57,0,56,9,56,0,24,49,25,0,58,9,16,8,57,0,56,56,41,0,57,8,17,9,56,0,0,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1)

# Start Game/Load Scores (24x7)
s1e1=(127,81,85,69,127,125,65,125,127,65,117,65,127,65,117,73,127,125,65,125,127,62,28,8)
s1e3=(8,28,62,127,81,69,127,65,93,127,65,93,65,127,65,117,73,127,65,85,127,81,69,127)

# Hard Mode Start (6x7)
s1e2=(124,102,67,67,102,124)

# Memory Game Outline (13x6)
s2e0 = (32,16,8,8,4,4,2,2,2,1,1,1,1)
s2e12 = (0,192,48,12,2,1,
           30,1,0,0,0,0)
s2e13 = (1,2,12,48,192,0,
           0,0,0,0,1,30)
s2e14 = (15,112,128,0,0,0,
           0,0,1,6,8,16)
s2e15 = (0,0,0,128,112,15,
           16,8,6,1,0,0)
s2e16 = (1,2,4,4,8,8,16,16,16,32,32,32,32)

# Scoreboard Outline (33x15)
s2e1=(127,64,223,80,64,95,85,64,95,69,64,65,95,65,64,127,192,87,93,64,95,81,64,95,81,95,64,95,69,91,64,95,85,
           0,0,127,64,64,64,64,64,64,64,64,64,64,64,64,64,127,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64)

# Select Speed (22x19)
s2e2=(4,142,149,132,4,0,0,151,157,128,31,144,128,31,145,159,128,15,16,12,16,15,
           0,207,66,143,0,0,0,207,66,13,192,79,202,0,207,72,14,64,200,64,0,0,
           0,7,5,2,0,0,0,7,1,0,7,1,7,0,5,7,0,0,7,0,0,0)

# ROUND text (20x5)
s2e3=(31,5,27,0,31,17,31,0,31,16,31,0,31,2,12,31,0,31,17,14)

# Lose Message (31x19)
s2e4=(0,128,159,145,14,0,31,21,128,151,157,0,135,156,7,128,159,130,12,159,128,159,17,128,31,149,0,31,17,14,0,
            0,207,66,143,0,137,0,0,207,130,13,128,207,10,192,64,15,192,128,15,194,13,192,3,206,3,0,0,0,0,0,
            0,7,5,2,0,4,0,0,7,0,1,0,7,0,7,5,0,7,0,3,7,0,7,4,7,0,0,0,0,0,0)

# Select Up/Down (24x17)
s2e5=(120,252,252,254,254,255,255,255,255,255,255,255,255,255,255,255,255,255,255,254,254,252,252,120,
            0,0,1,3,7,15,31,63,127,255,255,255,255,255,255,127,63,31,15,7,3,1,0,0,
            0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0)
s2e10=(0,0,0,128,192,224,240,248,252,254,255,255,255,255,254,252,248,240,224,192,128,0,0,0,
            60,126,127,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,127,126,60,
            0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0)

# Select Left (17x24)
s2e6=(224,248,254,255,255,255,255,254,252,248,240,224,192,128,0,0,0,
            255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,126,60,
            7,31,127,255,255,255,255,127,63,31,15,7,3,1,0,0,0)

# Select A/B (11x11)
s2e7=(255,255,255,127,63,63,79,135,7,3,3,
            7,7,1,0,0,0,0,0,1,2,4)
s2e11=(255,255,252,240,224,224,144,8,4,2,1,
            7,7,7,7,7,7,7,7,7,6,6)

# Memorize Text (31x5)
s2e8=(31,2,4,2,31,0,31,21,0,31,2,4,2,31,0,31,17,31,0,31,5,27,0,31,0,25,21,19,0,31,21)

# Repeat Text (21x5)
s2e9=(31,5,27,0,31,21,0,31,5,7,0,31,21,0,31,5,31,0,1,31,1)

# Regular Mode Highscores (15x7)
s3e0=(64,95,69,91,64,95,85,81,64,95,81,93,64,80,64)

# Hard Mode Highscores (17x7)
s3e1=(64,95,68,95,64,95,69,95,64,95,69,91,64,95,81,78,64)

# Highscore Counts (5x19)
s3e2=(146,159,144,0,18,
            78,74,203,0,137,
            4,5,7,0,4)

# Return to Main Menu (9x28)
s3e3=(252,252,252,28,127,62,28,8,0,
            247,151,247,0,0,124,20,124,0,
            222,202,214,0,1,125,85,41,1,
            15,15,15,0,0,0,0,0,0)

# Numbers for Scoreboard (3x5)
n=((31,17,31),(17,31,16),(29,21,23),(21,21,31),(7,4,31),(23,21,29),(31,21,29),(1,1,31),(31,21,31),(23,21,31))

# Select Speed Animation Frames
a=((0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(1,1,1))
e=(a[5],a[5],a[5],a[4],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[6],a[1],a[6],a[3],a[6],a[0],a[6],a[1],a[4],a[1],a[6],a[0],a[1],a[1],a[1],a[1],a[6],a[0],a[6],a[1],a[4],a[1],a[6],a[0],a[6],a[1],a[1],a[1],a[6],a[0],a[6],a[2],a[2],a[2],a[2],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[6],a[1],a[6],a[3],a[6],a[0],a[6],a[5],a[6],a[1],a[1],a[0],a[6],a[1],a[4],a[1],a[6],a[0],a[6],a[1],a[4],a[1],a[6],a[0],a[4],a[5],a[5],a[5],a[4],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[0],a[6])


# GLOBAL VARIABLES

# Scoreboard Variables
c=s=t=0

# Game settings
hard_mode=0
speed=750
retry=1

# Game State
lost=0

# Input Sequence
sequence=[]

# Hard Mode Unlocked
h=1


# FUNCTIONS

# Placeholder functions
def bl(sprite,x,y,d1,d2):
    thumby.display.blit(sprite,x,y,d1,d2,0)
def ds(sprite,x,y,d1,d2,xm,ym):
    thumby.display.drawSprite(sprite,x,y,d1,d2,xm,ym,0)
def dl(x1,y1,x2,y2):
    thumby.display.drawLine(x1,y1,x2,y2,1)
def erase():
    thumby.display.fill(0)
def img():
    thumby.display.update()

# Converts inputs to values
def keys():
    if(thumby.buttonU.justPressed()):
        return 1
    if(thumby.buttonD.justPressed()):
        return 2
    if(thumby.buttonL.justPressed()):
        return 3
    if(thumby.buttonR.justPressed()):
        return 4
    if(thumby.buttonA.justPressed()):
        return 0
    if(thumby.buttonB.justPressed()):
        return 5
    return None

# Converts input values to variable
def key(k=keys()):
    while(k is None):
        k = keys()
    return k

# Title and high score pages
def menu():
    global h,hard_mode
    while(1):
        erase()
        thumby.display.rect(1,1,70,38,1)
        bl(s1e0,4,5,64,22)
        bl(s1e3,5,29,24,7)
        bl(s1e1,43,29,24,7)
        #thumby.files.openFile(/Games/NanoMem/data.txt)
        #thumby.files.readFile(1)
        #if(thumby.files.readFile()=='h'):
        #    h=1
        #    thumby.files.closeFile()
        #    bl(s1e2,33,29,6,7)
        #elif(thumby.files.readFile()=='r'):
        #    thumby.files.closeFile()
        #else:
        #    thumby.files.openFile(/Games/NanoMem/data.txt,w)
        #    thumby.files.writeFile(r000000000000000000000000)
        #    thumby.files.closeFile()
        img()
        if thumby.buttonR.justPressed()==1:
            hard_mode=0
            break
        elif thumby.buttonU.justPressed()==1 and h==1:
            hard_mode=1
            break
        elif thumby.buttonL.justPressed()==1:
            erase()
            thumby.display.rect(1,1,70,38,1)
            bl(s3e0,10,5,15,7)
            bl(s3e2,6,14,5,19)
            bl(s3e3,31,5,9,28)
            for i in range(3):
                PrintNumber(0,4,13,14+7*i) # Set to zero until highscore saving functionality is implemented and verified to work.
            if h==1:
                bl(s3e1,47,5,17,7)
                bl(s3e2,44,14,5,19)
                for i in range(3):
                    PrintNumber(0,4,51,14+7*i) # Set to zero until highscore saving functionality is implemented and verified to work.
            img()
            while(not thumby.buttonA.justPressed()==1 or thumby.buttonB.justPressed()==1):
                continue

# Starts game
def game():
    global c,s,t,speed,sequence
    c=s=t=0
    j=5
    BaseUI()
    thumby.display.blit(s2e2,48,18,22,19)
    img()
    while(thumby.buttonL.justPressed()==0 and thumby.buttonA.justPressed()==0 and thumby.buttonB.justPressed()==0):
        if j==84:
            j-=84
        for i in range(19):
            thumby.display.blit(e[j+i],42,18+i,3,1)
        thumby.display.update()
        wait(50)
        j+=1
    if thumby.buttonL.pressed()==1:
        speed=1000
    elif thumby.buttonA.pressed()==1:
        speed=800
    else:
        speed=600
    random.seed(time.ticks_ms())
    if hard_mode==0:
        sequence=[random.randint(1,4) for i in range(250)]
    else:
        sequence=[random.randint(0,5) for i in range(250)]
        
# Draw game screen
def BaseUI():
    erase()
    bl(s2e0,7,1,13,6)
    bl(list(reversed(s2e0)),20,1,13,6)
    bl(s2e12,1,7,6,13)
    bl(s2e13,33,7,6,13)
    bl(s2e14,1,20,6,13)
    bl(s2e15,33,20,6,13)
    bl(s2e16,7,33,13,6)
    bl(list(reversed(s2e16)),20,33,13,6)
    dl(7,7,32,32)
    dl(7,32,32,7)
    bl(s2e1,38,1,33,15)
    r=t-c
    PrintNumber(r,3,42,9)
    PrintNumber(s,4,56,9)
    if hard_mode==1:
        dl(2,1,15,1)
        dl(1,1,1,38)
        dl(2,38,15,38)

# Prints numbers to scoreboard
def PrintNumber(number,totalDigits,x,y):
    scoreString=str(number)
    digits=len(scoreString)
    xPos=x
    yPos=y
    zerosToAdd=totalDigits-digits
    for i in range(totalDigits):
        if i < zerosToAdd:
            PrintDigit(0,xPos,yPos)
        else:
            PrintDigit(int(scoreString[i-zerosToAdd]),xPos,yPos)
        xPos += 4

# Locates sprite data for numbers
def PrintDigit(num,x,y):
    thumby.display.blit(n[num],x,y,3,5)

# Generate sequence
def code():
    global c,t
    c-=c
    t+=1
    c+=t
    SequenceUI()
    wait(725)
    for index, val in enumerate(sequence[:t]):
        bot(val)
        img()
        wait(speed)
        SequenceUI()
        wait(speed/2)

# Game screen during sequence
def SequenceUI():
    BaseUI()
    PrintNumber(t,3,49,25)
    bl(s2e3,45,18,20,5)
    bl(s2e8,39,32,31,5)
    img()
    
# Generate sequence output
def metabot(a,b,c,d,e,f):
    thumby.audio.play(a,speed)
    thumby.display.blit(b,c,d,e,f)
def bot(x):
    if x==1:
        metabot(262,s2e5,8,2,24,17)
    elif x==2:
        metabot(330,s2e10,8,21,24,17)
    elif x==3:
        metabot(349,s2e6,2,8,17,24)
    elif x==4:
        thumby.audio.play(294,speed)
        ds(s2e6,21,8,17,24,1,0)
    elif x==0 and hard_mode==1:
        metabot(392,s2e7,2,2,11,11)
    elif x==5 and hard_mode==1:
        metabot(440,s2e11,2,27,11,11)

# Wait until animations and audio effects finish
def wait(dur):
    init=time.ticks_ms()
    while(time.ticks_ms()-init<dur):
        pass
    
# Take inputs
def copy():
    global c
    c-=t
    InputUI()
    while (c<t):
        k = key()
        if hard_mode==0 and (k==0 or k==5):
            continue
        CheckInput(k)
        img()
        wait(600)
        InputUI()
        if lost==1:
            break

# Game screen during input
def InputUI():
    BaseUI()
    PrintNumber(t,3,49,25)
    bl(s2e3,45,18,20,5)
    bl(s2e9,44,32,21,5)
    img()
    
# Checks inputted direction
def CheckInput(x):
    global s,c,lost
    bot(x)
    if x==sequence[c]:
        s += 1
        c += 1
    else:
        lost=1


# FUNCTION ORDER

while(1):
    menu()
    while(1):
        game()
        while(1):
            code()
            copy()
            if lost==1:
                break
        BaseUI()
        bl(s2e4,39,18,31,19)
        img()
        while(lost==1):
            if thumby.buttonA.justPressed()==1:
                retry=1
                lost=0
            elif thumby.buttonB.justPressed()==1:
                retry=0
                lost=0
        if retry==0:
            break
