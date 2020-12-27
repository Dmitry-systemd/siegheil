#!/usr/bin/env python3
from telethon import sync, events
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, GetMessagesRequest
from telethon.tl.functions.messages import ImportChatInviteRequest, GetMessagesViewsRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.errors import rpcerrorlist
from random import randint
import os
import sys, getopt
import shutil
import time
import glob
import subprocess

def main(argv):
    intro = '   _____ __________________  ______________       _    __\n  / ___//  _/ ____/ ____/ / / / ____/  _/ /      | |  / /\n  \\__ \\ / // __/ / / __/ /_/ / __/  / // /  _____| | / /\n ___/ // // /___/ /_/ / __  / /____/ // /__/_____/ |/ /\n/____/___/_____/\\____/_/ /_/_____/___/_____/     |___/\n                          by vtsoft\n'
    print(intro)
    nomedia = 0
    dir = './telegram'
    try:
        opts, args = getopt.getopt(argv,'',['session=', 'chat=', 'nomedia='])
    except getopt.GetoptError:
        print ('мануал читай, блять')
        sys.exit(2)
    for opt, arg in opts:
        if opt  == '--session':
            session = arg.strip()
        elif opt  == '--chat':
            chat = arg
        elif opt == '--nomedia':
            nomedia = 1
        elif opt  == '--dir':
            filee = arg
    client = TelegramClient(session, 1796543, "3bdc204a7f37a225c5a08a6edcf3fe4d")
    client.start()
    try:
        os.mkdir(dir)
        os.mkdir(dir + '/media')
    except:
        pass
    entity = 0
    if '@' in chat:
        entity=client.get_entity(chat)
    else:
        try:
            client(ImportChatInviteRequest(chat))
        except Exception as e:
            print ("эй втсофт с огромным хером у меня проблема " + str(e))
            entity = client.get_entity('https://t.me/joinchat/' + chat)
    x = 0
    y = 0
    for msg in client.iter_messages(entity=entity):
        try:
            if msg.media is not None and not hasattr(msg.media, 'document') and nomedia == 0:
                client.download_media(msg.media, dir + '/media')
                y = y + 1
                print(str(y) + ' медиа в базе, ' + str(x) + ' сообщений в базе', end='\r')
            if msg.text:
                f = open(dir + '/msgs', "a+") 
                f.write(str(msg.text) + '\n===\n===\n')
                x = x + 1
                print(str(y) + ' медиа в базе, ' + str(x) + ' сообщений в базе', end='\r')
        except Exception as e:
            print(str (e))
            exit(2)
        
        

if __name__ == '__main__':
   main(sys.argv[1:])

