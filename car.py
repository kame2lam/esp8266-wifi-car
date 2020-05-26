#!/usr/bin/env micropython

import network
from machine import Pin

ap = network.WLAN(network.AP_IF) # create access-point interface
ap.active(True)         # activate the interface
ap.config(essid='ESP-AP',password='12345678')

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

import tinyweb
import moto

# Create web server application
app = tinyweb.webserver()

# Index page
@app.route('/')
async def index(request, response):
    # Start HTTP response with content-type text/html
    await response.start_html()
    # Send actual HTML page
    await response.send('<html><body><h1>Hello, world! (<a href="/table">table</a>)</h1></html>\n')

@app.route('/forward')
async def forward(request, response):
  moto.forward()

@app.route('/backward')
async def backward(request, response):
  moto.backward()
  
@app.route('/left')
async def left1(request, response):
  moto.left()

@app.route('/right')
async def right(request, response):
  moto.right()
  
@app.route('/stop')
async def stop(request, response):
  moto.stop()

def run():
    app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    run()    
    #   http://localhost:80
