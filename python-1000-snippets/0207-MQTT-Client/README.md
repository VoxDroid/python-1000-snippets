# MQTT Client

## Description
This snippet demonstrates an MQTT client using `paho-mqtt` to publish and subscribe.

## Code
```python
# Note: Requires `paho-mqtt`. Install with `pip install paho-mqtt`
try:
    import paho.mqtt.client as mqtt
    def on_message(client, userdata, msg):
        print(f"Received: {msg.payload.decode()}")
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("broker.hivemq.com", 1883)
    client.subscribe("test/topic")
    client.publish("test/topic", "Hello, MQTT!")
    client.loop_start()
    import time
    time.sleep(1)
    client.loop_stop()
except ImportError:
    print("Mock Output: Published: Hello, MQTT!, Received: Hello, MQTT!")
```

## Output
```
Mock Output: Published: Hello, MQTT!, Received: Hello, MQTT!
```
*(Real output with MQTT: `Received: Hello, MQTT!`)*

## Explanation
- **MQTT Client**: Publishes and subscribes to a topic using `paho-mqtt`.
- **Logic**: Connects to a public broker, publishes a message, and handles received messages.
- **Complexity**: O(1) for publish/subscribe (network latency varies).
- **Use Case**: Used in IoT or real-time messaging systems.
- **Best Practice**: Handle connection failures; use QoS levels; secure with TLS.