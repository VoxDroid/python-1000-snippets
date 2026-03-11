# 0207-MQTT-Client Cheatsheet

* Install with `pip install paho-mqtt`.
* Create client: `client = mqtt.Client()`.
* Callbacks: `on_connect`, `on_message`, `on_publish`, `on_disconnect`.
* Connect to broker: `client.connect(host, port, keepalive)`.
* Subscribe: `client.subscribe(topic, qos)`; QoS can be 0,1,2.
* Publish: `client.publish(topic, payload, qos=0)` returns (result, mid).
* Event loop: `client.loop_start()`/`loop_stop()`, `loop_forever()`, or manual `loop()`.
* Handle network errors by watching return codes and `on_disconnect`.
* Use public brokers like `broker.hivemq.com`, or run local RabbitMQ/EMQX.
* Use `client.enable_logger()` to see debug messages.
* For TLS, call `client.tls_set()` before `connect`.
* Best practice: clean session, handle reconnection, store messages if offline.
* Example:
  ```python
  client.on_message = on_message
  client.connect('broker', 1883)
  client.loop_start()
  client.publish('topic','msg')
  ```
