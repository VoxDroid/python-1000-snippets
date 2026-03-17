# 0406-MQTT-Publish-Subscribe Cheatsheet

- Install `hbmqtt` with `python -m pip install hbmqtt`.
- Start an in-process broker using `Broker(config)` and `await broker.start()`.
- Use `MQTTClient` to connect and `client.subscribe()`/`client.publish()`.
- Use `await client.deliver_message()` to receive messages.
- Always call `client.disconnect()` and `broker.shutdown()` to clean up.
