import network
from machine import Pin

ap = network.WLAN(network.AP_IF) # create access-point interface
ap.active(True)         # activate the interface
ap.config(essid='ESP-AP',password='12345678')

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

import car
car.run()
