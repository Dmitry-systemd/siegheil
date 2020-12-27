#!/usr/bin/env python
from telethon import sync, events
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import JoinChannelRequest, GetMessagesRequest
from telethon.tl.functions.messages import ImportChatInviteRequest, GetMessagesViewsRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.errors import rpcerrorlist
from random import randint
import asyncio
from telethon import events
import string
import os
import sys, getopt
import shutil
import time
import glob
import subprocess
import random
import os
from os import system


screen = 0
client = TelegramClient(sys.argv[1], 1796543, "3bdc204a7f37a225c5a08a6edcf3fe4d")
client.start()

@client.on(events.NewMessage())
async def handler(event):
    for dialog in await client.iter_dialogs():
        await print('{:3}. {:15} [{:^4}] {:50} '.format(x, dialog.id, dialog.unread_count, dialog.name))



client.run_until_disconnected()