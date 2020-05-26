
from machine import Pin

BD1={'D4':2,'D3':0,'D2':4,'D1':5,'D0':16,
      'D5':14,'D6':12,'D7':13,'D8':15}
m1a=Pin(BD1['D1'],Pin.OUT)
m1b=Pin(BD1['D3'],Pin.OUT)
m2a=Pin(BD1['D2'],Pin.OUT)
m2b=Pin(BD1['D4'],Pin.OUT)
 
def stop():
 m1a.value(0)
 m1b.value(0)
 m2a.value(0)
 m2b.value(0)
 
def forward():
 m1a.value(1)
 m1b.value(0)
 m2a.value(1)
 m2b.value(0)

def backward():
 m1a.value(1)
 m1b.value(1)
 m2a.value(1)
 m2b.value(1)

def left():
 m1a.value(0)
 m1b.value(0)
 m2a.value(1)
 m2b.value(0)

def right():
 m1a.value(1)
 m1b.value(0)
 m2a.value(0)
 m2b.value(0)