#!/usr/bin/env python3
from telethon import sync, events
from telethon import TelegramClient
import os
import sys 
client = TelegramClient(str(sys.argv[1]), 1796543, "3bdc204a7f37a225c5a08a6edcf3fe4d")
client.start()