# sample2.py
# illustrate on_publish callback and QoS levels
import time
import paho.mqtt.client as mqtt

def on_publish(client, userdata, mid):
    print('Message published with mid', mid)

client = mqtt.Client()
client.on_publish = on_publish
client.connect('broker.hivemq.com', 1883)
client.loop_start()
ret = client.publish('test/python-1000-sample', 'qos1 message', qos=1)
print('publish return', ret)
time.sleep(1)
client.loop_stop()
client.disconnect()

