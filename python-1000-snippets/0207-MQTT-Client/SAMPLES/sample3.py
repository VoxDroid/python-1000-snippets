# sample3.py
# run client with loop_forever and handle unexpected disconnects
import paho.mqtt.client as mqtt

client = mqtt.Client()

client.on_connect = lambda c, u, f, rc: print('connected with result', rc)
client.on_disconnect = lambda c, u, rc: print('disconnected', rc)

client.connect('broker.hivemq.com', 1883)
# schedule disconnect after 1 second to avoid infinite loop
import threading, time

def stopper():
    time.sleep(1)
    client.disconnect()

threading.Thread(target=stopper, daemon=True).start()
client.loop_forever()

