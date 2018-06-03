# TTN Uno

This device was created by The Things Network Kickstarter campaign and works quite well on TTN Adelaide. Unfortunately it does not work out of the box as in the EU and US regions.

Largely this is due to the firmware as the Microchip Lora modem firmware that the device shipped with does not have support for the AU915 frequency plan.


To make this work you need to ensure you have:
1) Updated the firmware of your device is at 1.0.3+ (HEX and instructions here: https://github.com/TheThingsNetwork/arduino-device-lib/issues/222)
2) Use the current HEAD revision of the Arduino Library (https://github.com/TheThingsNetwork/arduino-device-lib)


More info:https://www.thethingsnetwork.org/docs/devices/uno/

For those that need the Microchip utility to work on Linux: https://www.gaggl.com/2018/04/microchip-lorawan-development-utility-on-ubuntu/
