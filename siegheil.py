#!/usr/bin/env python3
from telethon import sync, events
from telethon import functions, types
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, GetMessagesRequest
from telethon.tl.functions.messages import ImportChatInviteRequest, GetMessagesViewsRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.errors import rpcerrorlist
import random
import os
import sys, getopt
import shutil
import time
import glob
import subprocess


def main(argv):
	#intro = "   _____ __________________  ______________         ____________\n  / ___//  _/ ____/ ____/ / / / ____/  _/ /        /  _/  _/  _/\n  \\__ \\ / // __/ / / __/ /_/ / __/  / // /  ______ / / / / / /\n ___/ // // /___/ /_/ / __  / /____/ // /__/_____// /_/ /_/ /\n/____/___/_____/\\____/_/ /_/_____/___/_____/    /___/___/___/\n\n                          by vtsoft\n"
	#print(intro)

	try:
		opts, args = getopt.getopt(argv,"",["target=","mode=","file=","msg=", "pause=", "sessions=", "verbose=", "noupdate="])
	except getopt.GetoptError:
		print ('мануал читай, блять')
		sys.exit(2)
	msg = 0
	pause = 0
	file = 0
	verbose = 0
	update = 0
	for opt, arg in opts:	 # Вот эта вот параша выглядит хуёво. TODO переделать
		if opt == '--target':
			target = arg.strip()
		elif opt  == '--mode':
			mode = arg.strip()
		elif opt  == '--msg':
			msg = arg.strip()
		elif opt  == '--pause':
			pause = arg.strip()
		elif opt  == '--sessions':
			sessions = arg.strip().split(" ")
		elif opt  == '--file':
			file = arg.strip()
		elif opt  == '--verbose':
			verbose = 1
		elif opt  == '--update':
			update = 1

	if update == 1:
		try:
			print('Проверяю обновления...')
			os.system('git remote update')
			if '(use "git pull" to update your local branch)' in subprocess.run(['git', 'status', '-uno'], stdout=subprocess.PIPE).stdout.decode('utf-8'):
				print('Найдено обновление. Обновить зигхайль? [Y/n]')
				a = input()
				if a.lower() == 'y' or a.lower() == '':
					os.system('git pull')
					print ('Обновлено')
					quit()
			else:
				print ('Обновление не требуется (или невозможно)')
		except SystemExit:
			sys.exit(0)
		except:
			print ('Беда с проверкой обновлений. Оставлю всё как есть.')
	if verbose == 1:
		print (" target:", target, "\n", "mode:", mode, "\n", "msg:", msg , "\n", "pause:", pause, "\n", "sessions:", sessions, "\n", "file:", file, "\n", "verbose: 1")

	try:
		mode
		sessions
	except NameError:
		print ('мануал читай, блять')
		sys.exit(2)

	if sessions == ['@all']:
		sessions = glob.glob('*.session')

	

	try:
		shutil.rmtree('pids')
	except:
		pass
	os.mkdir('pids')

	if mode == 'raid':
		for session in sessions:
			pid = os.fork()
			if pid == 0:
				raid(target, msg, pause, session, file)
		print ("\n Зигхайль рейдит (параллельно). Ctrl-c чтоб остановить.")
		try:
			time.sleep (14881488)
		except KeyboardInterrupt:
			exit()
	if mode == 'raid-seq':
		print ("\n Зигхайль рейдит (последовательно). Ctrl-c чтоб остановить.")
		raidseq(target, msg, pause, sessions, file)
	if mode == 'db':
		print ("\nЗигхайль собирает спам базу (последовательно). Ctrl-c чтоб остановить.")
		db(target, sessions, file)
	if mode == 'spam-seq':
		print ("\nЗигхайль выполняет рассылку спама (последовательно). Ctrl-c чтоб остановить.")
		spamseq(target, msg, pause, sessions, file)
	if mode == 'setpic':
		print ("\nЗигхайль устанавливает аватарки (последовательно). Ctrl-c чтоб остановить.")
		setpic(sessions, file)
	if mode == 'join':
		print ("\nЗигхайль накручивает подписчиков (последовательно). Ctrl-c чтоб остановить.")
		join(sessions, target, pause)
	if mode == 'read':
		print ("\nЗигхайль накручивает просмотры (последовательно). Ctrl-c чтоб остановить.")
		read(sessions, target)
	if mode == 'get-dialog-by-id':
		print ("\nЗигхайль читает диалог. Ctrl-c чтоб остановить.")
		getdialog(sessions, target)
	if mode == 'get-number':
		print ("\nЗигхайль получает номера. Ctrl-c чтоб остановить.")
		getnumber(sessions)
	if mode == 'validate':
		print ("\nЗигхайль валидирует сессии. Ctrl-c чтоб остановить.")
		validate(sessions)
	if mode == 'setname':
		print ("\nЗигхайль ставит имена. Ctrl-c чтоб остановить.")
		setname(sessions, msg)
	if mode == 'check-ban':
		print ("\nЗигхайль проверяет на бан. Ctrl-c чтоб остановить.")
		checkban(sessions, target)
	if mode == 'lol':
		lol(sessions)

def raidseq(target, msg, pause, sessions, file):
	clients = []
	print ("стартую клиенты...")
	for user in sessions:
		clients.append(TelegramClient(user, 21724, "3e0cb5efcd52300aec5994fdfc5bdc16"))
	for client in clients:
			client.start()
	exit1 = 0
	print ("начинаю рейд... слава стопламерс!")
	while exit1 == 0:
		x = 0
		for client in clients:
			
			if '@' in target:
				entity=client.get_entity(target)
				client(JoinChannelRequest(entity))
			else:
				try:
					client(ImportChatInviteRequest(target))
					entity = client.get_entity('https://t.me/joinchat/' + target)
				except Exception:
					try:
						entity = client.get_entity('https://t.me/joinchat/' + target)
					except Exception as e:
						print (str(e) + ": пропускаю " + sessions[x])
						continue
				
			try:
				while True:
					if file != 0:
						if "|" in file:
							files = file.split("|")
						else:
							files = [file]
						for sex in files:
							if msg != 0:
								client.send_file(entity=entity, file=sex, caption=msg)
							else:
								client.send_file(entity=entity, file=sex)
						if '-' in pause:
							time.sleep(random.randint(int(pause.split('-')[0]), int(pause.split('-')[1])))
						else:
							time.sleep(pause)
					else:
						client.send_message(entity=entity, message=msg) 
						if '-' in pause:
							time.sleep(random.randint(int(pause.split('-')[0]), int(pause.split('-')[1])))
						else:
							time.sleep(pause)
			except KeyboardInterrupt:
				exit()
			except Exception as e:
				print (str(e) + ": пропускаю " + sessions[x])
				x = x + 1
				continue
			x = x + 1

def validate(sessions):
	pids = []
	for session in sessions:
		pid = os.fork()
		if pid == 0:
			client = TelegramClient(session, 21724 "3e0cb5efcd52300aec5994fdfc5bdc16")
			client.start()
			client.get_entity('me')
			f = open('.tmp', "a+") 
			f.write(session + '\n')
		pids.append(pid)
	time.sleep(5)
	for pid in pids:
		os.kill(pid, 9)

def getdialog(sessions, target):
	client = TelegramClient(sessions[0], 21724, "3e0cb5efcd52300aec5994fdfc5bdc16")
	client.start()
	
	for a in client.iter_dialogs():
		if a.entity.id == int(target):
			for msg in client.iter_messages(entity=a.entity):
				print ('---')
				print (msg.text)

def getnumber(sessions):
	clients = []
	for user in sessions:
		clients.append(TelegramClient(user, 21724, "8da85b0d5bfe62527e5b244c209159c3"))

	x=0
	for client in clients:
		client.start()
		entity = client.get_entity('me')
		print('{:32s} {:16s}'.format(sessions[x], entity.phone))
		x = x + 1

def read(sessions, target):
	clients = []
	for user in sessions:
		clients.append(TelegramClient(user, 21724, "8da85b0d5bfe62527e5b244c209159c3"))

	x=0
	for client in clients:
		client.start()
		print (sessions[x])
		entity = 0
		if '@' in target:
			entity=client.get_entity(target.split(':')[0])
		else:
			try:
				client(ImportChatInviteRequest(target))
			except:
				print ("эй theerha с огромным хером у меня проблема " + str(e))
				entity = client.get_entity('https://t.me/joinchat/' + target)
		ids = []

		if ':' in target:
			if '-' in target:
				for msg in client.iter_messages(entity=entity, max_id=int(target.split(':')[1].split('-')[1]), min_id=int(target.split(':')[1].split('-')[0])):
					ids.append(msg.id)
			elif '+' in target:
				for msg in client.iter_messages(entity=entity, min_id=int(target.split(':')[1].split('+')[0])):
					ids.append(msg.id)
			else:
				ids = [int(target.split(':')[1])]
		else:
			for msg in client.iter_messages(entity):
				ids.append(msg.id)
		res = client(GetMessagesViewsRequest(
			peer=entity,
			id=ids,
			increment=True))
		x = x + 1 

	print ('Накручено ' + str(x) + ' просмотров (если ты все делаешь правильно)')
def setpic(sessions, file):
	clients = []
	for user in sessions:
		clients.append(TelegramClient(user, 21724, "3e0cb5efcd52300aec5994fdfc5bdc16"))
	x = 0
	for client in clients:
		print(sessions[x])
		x = x + 1
		client.start()
		client(UploadProfilePhotoRequest(client.upload_file(file)))

def join(sessions, target, pause):
	targets = []
	if ' ' in target:
		targets = target.split(' ')
	else:
		targets = [target]
	clients = []

	for user in sessions:
		clients.append(TelegramClient(user, 21724, "3e0cb5efcd52300aec5994fdfc5bdc16"))
	x = 0
	for client in clients:
		print(sessions[x])
		x = x + 1
		client.start()
		for target in targets:
			if '@' in target:
				entity=client.get_entity(target)
				client(JoinChannelRequest(entity))
				if '-' in pause:
					time.sleep(random.randint(int(pause.split('-')[0]), int(pause.split('-')[1])))
				else:
					time.sleep(pause)
			else:
				try:
					client(ImportChatInviteRequest(target))
				except:
					pass
				entity = client.get_entity('https://t.me/joinchat/' + target)
				if '-' in pause:
					time.sleep(random.randint(int(pause.split('-')[0]), int(pause.split('-')[1])))
				else:
					time.sleep(pause)
def raid(target, msg, pause, session, file):
	client = TelegramClient(session, 21724, "3e0cb5efcd52300aec5994fdfc5bdc16")
	client.start()
	if '@' in target:
		entity=client.get_entity(target)
		client(JoinChannelRequest(entity))
	else:
		try:
			client(ImportChatInviteRequest(target))
		except:
			pass
		entity = client.get_entity('https://t.me/joinchat/' + target)

	try:
		while True:
			if file != 0:
				if " " in file:
					files = file.split(" ")
				else:
					files = [file]
				for sex in files:
					if msg != 0:
						client.send_file(entity=entity, file=sex, caption=msg)
					else:
						client.send_file(entity=entity, file=sex)
				if '-' in pause:
					time.sleep(random.randint(int(pause.split('-')[0]), int(pause.split('-')[1])))
				else:
					time.sleep(pause)
			else:
				client.send_message(entity=entity, message=msg) 
				if '-' in pause:
					time.sleep(random.randint(int(pause.split('-')[0]), int(pause.split('-')[1])))
				else:
					time.sleep(pause)
	except KeyboardInterrupt:	
		exit()

def db(target, sessions, file):
	x = 0
	if "/" in target:
		f = open(target, "r")
		targets = f.read().split("\n")
	else:
		targets = target.split(" ")

	clients = []
	for user in sessions:
		clients.append(TelegramClient(user, 21724, "3e0cb5efcd52300aec5994fdfc5bdc16"))

	for client in clients:
		client.start()

	for penis in targets:
		for client in clients:
			participants = []
			user = sessions[clients.index(client)]
			if '@' in penis:
				try:
					entity=client.get_entity(penis)
					participants = client.get_participants(entity)
				except rpcerrorlist.ChannelPrivateError:
					print (" " + user + ", похоже, забанен в " + penis + ". Пробуем следующего фейка.")
					continue
			else:
				try:
					client(ImportChatInviteRequest(target))
				except rpcerrorlist.InviteHashExpiredError:
					print (" " + user + ", похоже, забанен в " + penis + " (или указана неверная ссылка на чат, хз). Пробуем следующего фейка.")
					continue
				except rpcerrorlist.UserAlreadyParticipantError:
					pass
				except rpcerrorlist.FloodWaitError as e:
					print (user + " словил бан за флуд: " + e)
					continue
				entity = client.get_entity('https://t.me/joinchat/' + penis)
				participants = client.get_participants(entity)

			for participant in participants:
				if participant.username:
					f = open(file, "a+") 
					f.write('@' + participant.username + '\n')
					x = x + 1
			print (" Успешно обработан " + penis)
			break

	print (" Зигхайль завершил сбор базы. Было найдено " + str(x) + " юзеров. (В базе будут удалены дубликаты)")
	uniqlines = set(open(file,'r').readlines())
	gotovo = open(file,'w').writelines(set(uniqlines))
	print (" Обработка базы завершена.")

def spamseq(target, msg, pause, sessions, file):
	f = open(target, "r")
	targets = f.read().split("\n")

	clients = []
	for user in sessions:
		clients.append(TelegramClient(user, 21724, "3e0cb5efcd52300aec5994fdfc5bdc16"))
	for client in clients:
		client.start()

	for client in clients:
		for target in targets:
			try:
				if target == "":
					continue
				entity=client.get_entity(target)
				if file != 0:
					if " " in file:
						files = file.split(" ")
					else:
						files = [file]
					for sex in files:
						if msg != 0:
							client.send_file(entity=entity, file=sex, caption=msg)
						else:
							client.send_file(entity=entity, file=sex)
					time.sleep(pause)
				else:
					client.send_message(entity=entity, message=msg) 
			except Exception as e:
				print ("эй theerha с огромным хером у меня проблема " + str(e))
				break

def setname(sessions, msg):
	clients = []
	for user in sessions:
		clients.append(TelegramClient(user, 21724, "3e0cb5efcd52300aec5994fdfc5bdc16"))
	for client in clients:
		client.start()
		client(functions.account.UpdateProfileRequest(
			first_name=msg.split('|')[0],
			last_name=msg.split('|')[1],
			about=msg.split('|')[2]
		))
from telethon.tl.types import ChannelParticipantsSearch
def lol(session):
	client = TelegramClient(session[0], 21724, "3e0cb5efcd52300aec5994fdfc5bdc16")
	client.start()
	channel = client.get_entity('@linuxsucks')
	participants = client(GetParticipantsRequest(
        channel, limit=1000, hash=0, filter=ChannelParticipantsSearch(''), offset=0
    ))
	for a in participants.users:
		print (a.id)

		
	
def checkban(sessions, target):
	clients = []
	for user in sessions:
		clients.append(TelegramClient(user, 21724, "3e0cb5efcd52300aec5994fdfc5bdc16"))

	x=0
	for client in clients:
		client.start()
		try:
			entity = client.get_entity(target)
			if 'ChannelForbidden(' in str(entity):
				print('{:32s} {:10s}'.format(sessions[x], 'BANNED'))
			else:
				print('{:32s} {:10s}'.format(sessions[x], 'OK'))
		except:
			print('{:32s} {:10s}'.format(sessions[x], 'EL PROBLEMA'))
		x = x + 1



if __name__ == "__main__":
   main(sys.argv[1:])

