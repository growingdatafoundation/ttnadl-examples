#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lora_join.py
#  
#  Copyright 2017 Leo Gaggl <leo@g3i.com.au>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import socket
import time
import binascii
import pycom
from network import LoRa

pycom.heartbeat(False) #needs to be disabled for LED functions to work
pycom.rgbled(0x7f7f00) #yellow

# replace with your actual app_eui and app_key
app_eui=binascii.unhexlify('0000000000000000')
app_key=binascii.unhexlify('00000000000000000000000000000000')

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.AU915, public=1,  adr=1, tx_retries=0)

# Set up channels to leave 8-15 and 65
for index in range(0, 8):
    lora.remove_channel(index)	# remove 0-7
for index in range(16, 65):
	lora.remove_channel(index)	# remove 16-64
for index in range(66, 72):
	lora.remove_channel(index)	# remove 66-71
                      
#Join TTN Network via OTAA
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
	pycom.rgbled(0x7f0000) #red
	time.sleep(5)
	print('Trying to join TTN Network!')
	pass

print('Network joined!')
pycom.rgbled(0x007f00) #green
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

while True:
	print('Sending Packet')
	s.send('Hello LoPy')
	print('Done sending')
	time.sleep(60)
