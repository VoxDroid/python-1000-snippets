# sample1.py
# Demonstrates a simple publish/subscribe interaction with a public MQTT broker.

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
    topic = "python1000snippets/sample1"

    received = []
    event = threading.Event()

    def on_connect(client, userdata, flags, rc):
        client.subscribe(topic)

    def on_message(client, userdata, msg):
        received.append(msg.payload.decode())
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

    # Publish a message and wait for it to be received.
    client.publish(topic, "Hello MQTT")

    if event.wait(timeout=10):
        print("Received:", received[0])
    else:
        print("Did not receive a message within 10 seconds.")

    client.loop_stop()
    client.disconnect()


if __name__ == "__main__":
    main()
