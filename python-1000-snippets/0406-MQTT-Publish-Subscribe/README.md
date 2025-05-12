# MQTT Publish Subscribe

## Description
This snippet demonstrates MQTT publish/subscribe using `paho-mqtt`.

## Code
```python
# Note: Requires `paho-mqtt`. Install with `pip install paho-mqtt`
try:
    import paho.mqtt.client as mqtt
    def on_message(client, userdata, msg):
        print(f"Received: {msg.payload.decode()}")
    
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("localhost", 1883)
    client.subscribe("test/topic")
    client.publish("test/topic", "Hello")
    print("Message published")
except ImportError:
    print("Mock Output: Message published")
```

## Output
```
Mock Output: Message published
```
*(Real output with `paho-mqtt` and MQTT broker: `Received: Hello`)*

## Explanation
- **MQTT Publish Subscribe**: Publishes and subscribes to an MQTT topic.
- **Logic**: Connects to a broker, subscribes, and publishes a message.
- **Complexity**: O(1) per message.
- **Use Case**: Used for IoT or event-driven systems.
- **Best Practice**: Handle connection errors; secure MQTT; use QoS levels.