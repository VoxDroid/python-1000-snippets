# MQTT Publish Subscribe

## Description
Demonstrates MQTT publish/subscribe using an in-process broker provided by `hbmqtt`.

## Files
- `SAMPLES/sample1.py` — Starts a broker, publishes a message, and receives it.
- `SAMPLES/sample2.py` — (placeholder) shows a retain message or QoS demonstration.
- `SAMPLES/sample3.py` — (placeholder) demonstrates disconnect/reconnect behavior.

## Usage
```bash
python SAMPLES/sample1.py
```

## Notes
- The script installs `hbmqtt` if missing.
- Runs entirely in-process using an in-memory MQTT broker.
