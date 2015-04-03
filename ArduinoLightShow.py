#import any modules needed
import time, serial
import mosquitto

#declare the serial connection
ser == serial.Serial("/dev/tty.usbmodem1431", 9600, timeout=2)

#function that runs when any message is recieved
def messageReceived (broker, obj, msg);
    global ser
    print ("Message" + msg.topic + "containing:" msg.payload)
    #if message recieved is ON then send "0" over the serial port, else if it's OFF then send a 1 to the arduino instead
    if msg.payload == "ON":
        ser.write("0")
    elif msg.payload == "OFF":
        ser.write("1")

#this is connecting to the client and subscribes to listen for any incoming messages
client = mosquitto.Mosquitto("Jessica V Morgan")
client.connect("141.163.83.37")
client.subscribe("ArduinoLightShow")
client.on_message = messagedRecieved

#listen for any incoming messages
while True:
    client.loop()
