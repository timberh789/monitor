from pynput.mouse import Button, Controller
from pynput import mouse, keyboard
from pynput.keyboard import Key 
import threading
from socket import*
from PIL import ImageGrab

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

def sendmsgcall(host='0.0.0.0', port= '5000'):
    monitor = socket()
    monitor.connect(host,port)

def screenshot()
    try:
        monitor.listen(5)
        golbal end(0)
        conn,addr = monitor.accept()
        thread = Thread(target=retreive_screenshot, args=(conn,))
        thread.start()
#screenshot

             
def retreive_screenshot(conn):
    with mss() as sct:
        # The region to capture
        rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

        while 'recording':
            # Capture the screen
            img = sct.grab(rect)
            # Tweak the compression level here (0-9)
            pixels = compress(img.rgb, 6)

            # Send the size of the pixels length
            size = len(pixels)
            size_len = (size.bit_length() + 7) // 8
            conn.send(bytes([size_len]))

            # Send the actual pixels length
            size_bytes = size.to_bytes(size_len, 'big')
            conn.send(size_bytes)

            # Send pixels
            conn.sendall(pixels)

#recev

def recv():
    data = monitor.recvfrom()

def sendmsg(msg):
    monitor.sendall(msg)




             
