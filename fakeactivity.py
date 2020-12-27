#!/usr/bin/env python3
from telethon import sync, events
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import JoinChannelRequest, GetMessagesRequest
from telethon.tl.functions.messages import ImportChatInviteRequest, GetMessagesViewsRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateUsernameRequest
from markovchain import JsonStorage
from markovchain.text import MarkovText, ReplyMode
from telethon.errors import rpcerrorlist
from random import randint
import string
import os
import sys, getopt
import shutil
import time
import glob
import subprocess
import random

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def set_name(client):
    try:
        client(functions.account.UpdateUsernameRequest(username=get_random_string(7)))
        return
    except rpcerrorlist.UsernameOccupiedError:
        set_name(client)
                
def main(argv):
    #intro = '   _____ __________________  ______________       _    __\n  / ___//  _/ ____/ ____/ / / / ____/  _/ /      | |  / /\n  \\__ \\ / // __/ / / __/ /_/ / __/  / // /  _____| | / /\n ___/ // // /___/ /_/ / __  / /____/ // /__/_____/ |/ /\n/____/___/_____/\\____/_/ /_/_____/___/_____/     |___/\n                          by vtsoft\n'
    #print(intro)
    try:
        opts, args = getopt.getopt(argv,'',['sessions=', 'dir=', 'sleepseed=', 'names='])
    except getopt.GetoptError:
        print ('мануал читай, блять')
        sys.exit(2)
    names = 0
    sleepseed = 77
    dir = './telegram'
    for opt, arg in opts:
        if opt  == '--sessions':
            sessions = arg.strip().split(' ')
        elif opt  == '--dir':
            dir = arg
        elif opt  == '--names':
            names = arg
        elif opt  == '--sleepseed':
            sleepseed = float(arg)

    if sessions == ['@all']:
        sessions = glob.glob('*.session')

    clients = []
    usernames = []
    for user in sessions:
        clients.append(TelegramClient(user, 1796543, "3bdc204a7f37a225c5a08a6edcf3fe4d"))
    for client in clients:
        client.start()
        if client.get_entity('me').username == None:
            print('setting username')
            set_name(client)

    for client in clients:
        usernames.append(client.get_entity('me').username)

    media = glob.glob(dir + '/media/*')

    f = open(dir + '/msgs', 'r')
    messages = f.read().split('\n===\n===\n')

    f = open(dir + '/chatnames', 'r')
    chatnames = f.read().split('\n')  

    if names == 1:
        f = open(dir + '/names', 'r')
        names = f.read().split('\n')  
        for client in clients:
            client(functions.account.UpdateProfileRequest(
                first_name=names[random.randint(0, len(names))]
            ))
        
    markov = MarkovText()
    print('Generating Markov')
    for message in messages:
        markov.data(message)
    print('starting messenger')
    for client in clients:
        pid = os.fork()
        if pid == 0:
            try:
                while True: 
                    time.sleep(random.random()*sleepseed*random.random())
                    target = usernames[random.randint(0, len(usernames)-1)]
                    text = markov()
                    entity = client.get_entity(target)
                    client.send_message(entity=entity, message=text) 
                    print (client.get_entity('me').first_name + ' => ' + client.get_entity(target).first_name + ' "' + text + '"')
            except KeyboardInterrupt:
                exit(0)
            except rpcerrorlist.FloodWaitError:
                print(client.get_entity('me').first_name + ' FloodWaitError ban. waiting 600 seconds...')
                time.sleep (600)
            except rpcerrorlist.PeerFloodError:
                print(client.get_entity('me').first_name + ' PeerFloodError ban. waiting 600 seconds...')
                time.sleep (600)
    print('ctrl-c to exit')
    try:
        time.sleep(14881488)
    except KeyboardInterrupt:
            exit(0)

if __name__ == '__main__':
   main(sys.argv[1:])

