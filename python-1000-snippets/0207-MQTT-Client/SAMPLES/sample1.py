# sample1.py
# publish and subscribe to a public broker; disconnect after receiving message
import time
try:
    import paho.mqtt.client as mqtt
except ImportError:
    print('paho-mqtt required; install with pip install paho-mqtt')
    raise

def on_message(client, userdata, msg):
    print('Received:', msg.payload.decode())
    client.disconnect()

client = mqtt.Client()
client.on_message = on_message
client.connect('broker.hivemq.com', 1883, 60)
client.subscribe('test/python-1000-sample', qos=0)
client.loop_start()
client.publish('test/python-1000-sample', 'hello world', qos=0)
# wait for message or timeout
time.sleep(2)
client.loop_stop()

