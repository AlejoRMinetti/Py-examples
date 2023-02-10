import os

def get_connected_devices():
    devices = []
    for i in range(1, 255):
        response = os.system("ping -c 1 192.168.0." + str(i))
        if response == 0:
            devices.append("192.168.0." + str(i))
    return devices

print(get_connected_devices())
# very slow, ther alternative: arp-scan
# sudo apt-get install arp-scan