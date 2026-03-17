# sample2.py
# Demonstrates publishing multiple messages and consuming them sequentially.

import threading
import time
import sys


def ensure_paho():
    try:
        import paho.mqtt.client as mqtt  # type: ignore
        return mqtt
    except ImportError:
        print("Missing dependency: paho-mqtt. Install with: python -m pip install paho-mqtt")
        sys.exit(1)


def main() -> None:
    mqtt = ensure_paho()

    # Best effort: attempt to connect to a local MQTT broker (e.g., mosquitto).
    # If no broker is running, the script exits gracefully.
    broker = "localhost"
    port = 1883
    topic = "python1000snippets/sample2"

    received = []
    event = threading.Event()

    def on_connect(client, userdata, flags, rc):
        client.subscribe(topic)

    def on_message(client, userdata, msg):
        received.append(msg.payload.decode())
        if len(received) >= 3:
            event.set()

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(broker, port, 60)
    except Exception as e:
        print(
            "Unable to connect to MQTT broker at",
            f"{broker}:{port}",
            "— make sure a broker (e.g., mosquitto) is running.",
            "Error:",
            e,
        )
        return

    client.loop_start()

    # Publish multiple messages.
    for i in range(3):
        client.publish(topic, f"msg {i}")
        time.sleep(0.2)

    if event.wait(timeout=10):
        print("Received messages:", received)
    else:
        print("Did not receive all messages within 10 seconds.")

    client.loop_stop()
    client.disconnect()


if __name__ == "__main__":
    main()
