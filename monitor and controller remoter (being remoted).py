from pynput.mouse import Button, Controller
from pynput import mouse, keyboard
from pynput.keyboard import Key 
import threading
from socket import *
import mss
import numbers

mouse = Controller()

listener = mouse.Listener(   #monitoring the mouse
    on_move=onmove,
    on_click=onclick,
    on_scroll=onscroll,
    on_press=onpress.
    on_release=onrelease)
listener.start()

def setmouse (x,y):#controlling mouse
    mouse.position = (x,y)

#controlling the mouse

def clickleft ():
    mouse.press(Button.left)
    mouse.release(Button.left)

def clickright ():
    mouse.press(Button.right)
    mouse.release(Button.right)

def pressleft ():
    mouse.press(Button.left)

def pressright():
    mouse.press(Button.right)

def releaseleft():
    mouse.realease(Button.left)

def relaeseright():
    mouse.release(Button.right)

def scroll(times):
    mouse.scroll(0,times)

#react for monitor

def onmove(x,y):
    sendmsg("clicked"+' '+x+' ' +y)

def onclick(x,y,button,pressed):
    sendmsg(x+' ' +y+' ' +button+' ' +pressed+' '+"pressed")

def onscroll():
    sendmsg("scrolled")

#mouse end

#keyboard start

def clickkey(keykey):
    mouse.press(Key.keykey)
    mouse.release(Key.keykey)

def presskey(keykey):
    mouse.press(Key.keykey)

def releasekey(keykey):
    mouse.release(Key.keykey)

def typekey(word):
    mouse.type(word)

#manykey

def keys2 (key1,key2):       #two keys
    with mouse.pressed(key2):
        mouse.press(key1)
        mouse.release(key1)

def key3 (key1,key2,key3):
    with mouse.pressed(key1):
        with mouse.pressed(key2):
            mouse.press(key3)
            mouse.release(key3)

#monitor keyboard

def onpress(key):
    sendmsg(key)

def onrelease(key):
    sendmsg(key)


#keyboard end

def sendmsgcall(host, port):
    monitor = socket()
    monitor.connect(host,port)
def screenshot():
    screen = Thread(target = sendscreen, daemon=True)
    screen.start
def screenshottheard():
    screenshotphoto = mss.shot()


#screenshot

def sendscreen():
    screenshotphoto = mss.shot()
    sendmsg(screenshotphoto)
def getcomannd():
    while 1=1:
        recv()
        data = tuple(data1)
        setmouse(data["xy"])
        if data.index(1) = "clickleft" :
            clickleft()
        if data.index(2) = "clickright" :
            clickright()
        if data.index(3) = "pressleft" :
            pressleft()
        if data.index(3) = "pressright":
            pressright()
        if data.index(3) = "releaseleft":
            
            
            
            
def getcommanda():
    gc = Thread(target = getcommand, daemon=True)
    gc.start     
                
#recev

def recv():
    data1 = monitor.recvfrom()

def sendmsg(msg):
    monitor.sendall(msg)

def switch(msg):
    if msg = "start monitor"
       while 1=1 :
            screenshot
            getcommanda
            
        
    
    
#main

sendmsgcall(0.0.0.0,5000)



             
