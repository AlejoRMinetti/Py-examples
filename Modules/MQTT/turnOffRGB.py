# pip install paho-mqtt
import paho.mqtt.client as mqtt

# MQTT server environment variables
MQTT_HOST = "192.168.0.2"
MQTT_PORT = 1883 # Port for MQTT (often: 1883)
MQTT_KEEPALIVE_INTERVAL = 60

# for RGB control
Topic = "RGBunderDesk"

if __name__ == "__main__":
    # Connect to the MQTT server
    client = mqtt.Client()
    client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
    # send to turn off RGB
    client.publish(Topic, "E0")
    print("RGB apagado")