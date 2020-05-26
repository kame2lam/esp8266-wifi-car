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


# HTTP redirection
@app.route('/redirect')
async def redirect(request, response):
    # Start HTTP response with content-type text/html
    await response.redirect('/')


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

# Another one, more complicated page
@app.route('/table')
async def table(request, response):
    # Start HTTP response with content-type text/html
    await response.start_html()
    await response.send('<html><body><h1>Simple table</h1>'
                        '<table border=1 width=400>'
                        '<tr><td>Name</td><td>Some Value</td></tr>')
    for i in range(10):
        await response.send('<tr><td>Name{}</td><td>Value{}</td></tr>'.format(i, i))
    await response.send('</table>'
                        '</html>')


def run():
    app.run(host='0.0.0.0', port=80)


if __name__ == '__main__':
    run()
    # To test your server:
    # - Terminal:
    #   $ curl http://localhost:8081