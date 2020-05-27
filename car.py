import tinyweb
import moto

# Create web server application
app = tinyweb.webserver()

car_control_html='''
<!DOCTYPE html>
<html>
<head>
<title>MicroPython Car</title>
<meta charset="UTF-8">
<style>
body {background-color: white}
h1 {color:red}

button {
        color: red;
        height: 200px;
        width: 200px;
        background:white;
        border: 3px solid #4CAF50; /* Green */
        border-radius: 50%;
        font-size: 250%;
        position: center;
}

.button {
  font: bold 11px Arial;
  height: 200px;
  width: 200px;
  font-size: 400%;
  text-decoration: none;
  background:white;
  color: #333333;
  padding: 2px 6px 2px 6px;
  border: 3px solid #4CAF50; /* Green */
  margin: 10px;
  position: center;
}

div{
  margin: 20px;
}
</style>
</head>
<body>
<center><h1>MicroPython Car Control</h1>
<div><a class="button" href="../forward">∧</a></div>
<div><a class="button" href="../left"><</a>
    <a class="button" href="../stop">S</a>
    <a class="button" href="../right">></a></div>
<div><a class="button" href="../backward">∨</a></div>
</center>
</body>
</html>
'''

# Index page
@app.route('/')
async def index(req, resp):
  await resp.start_html()
  await resp.send(car_control_html)

@app.route('/forward')
async def forward(req, resp):
  moto.forward()
  print('forward')
  await resp.start_html()
  await resp.send(car_control_html)
  
@app.route('/backward')
async def backward(req, resp):
  moto.backward()
  print('backward')
  await resp.start_html()
  await resp.send(car_control_html)
 
@app.route('/left')
async def left(req, resp):
  moto.left()
  print('left')
  await resp.start_html()
  await resp.send(car_control_html)

@app.route('/right')
async def right(req, resp):
  moto.right()
  print('right')
  await resp.start_html()
  await resp.send(car_control_html)
  
@app.route('/stop')
async def stop(req, resp):
  moto.stop()
  print('stop')
  await resp.start_html()
  await resp.send(car_control_html)

def run():
    app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    run()    
    #   http://localhost:80



