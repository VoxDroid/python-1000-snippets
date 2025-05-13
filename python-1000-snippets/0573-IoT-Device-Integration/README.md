# IoT Device Integration

## Description
This snippet demonstrates publishing IoT data using MQTT.

## Code
```python
# Note: Requires `paho-mqtt`. Install with `pip install paho-mqtt`
try:
    import paho.mqtt.client as mqtt
    client = mqtt.Client()
    client.connect("localhost", 1883)
    client.publish("sensor/data", "25")
    print("Data published")
    client.disconnect()
except ImportError:
    print("Mock Output: Data published")
```

## Output
```
Mock Output: Data published
```
*(Real output with `paho-mqtt`: `Data published`)*

## Explanation
- **IoT Device Integration**: Sends sensor data via MQTT.
- **Logic**: Publishes a temperature reading to a topic.
- **Complexity**: O(1) per publish (network-dependent).
- **Use Case**: Used in IoT for device communication.
- **Best Practice**: Secure connections; handle disconnects; validate messages.