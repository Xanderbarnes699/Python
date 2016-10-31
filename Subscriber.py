from mosquitto import *
from serial import *
from random import *

# FULL DEVICE NAME can be found by running: python PortScanner.py
# SPEED is usually 115200 for Microbit and 9600 for Arduino
port = Serial("/dev/cu.usbmodemfa131",9600,timeout=2)

randomID = random()
print("1")
client = Mosquitto("LightSubscriber" + str(randomID))
print("2")
client.connect("10.212.61.136")
print("3")
client.subscribe("/lights")
print("4")

def messageRecieved(broker, obj, msg):
    global client
    payload = msg.payload.decode()
    print("Message:" + msg.topic + "Containing:" + payload)
    ##port.readall()
    port.write(payload.encode())

client.on_message = messageRecieved

print("5")
while True:
    print("6")
    client.loop()


# The rest of your code goes in here !!!













