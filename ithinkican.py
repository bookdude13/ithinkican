#!/user/bin/env python3

import can
import os

USE_VCAN=False

print("Setting up CAN devices...")
if not USE_VCAN:
    # Try to close if already open
    try:
        os.system('sudo ifconfig can0 down')
        os.system('sudo ifconfig can1 down')
    except:
        print("  Unable to shut down interfaces, might not be up")
    
    os.system('sudo ip link set can0 type can bitrate 1000000')
    os.system('sudo ifconfig can0 up txqueuelen 65536')
    os.system('sudo ip link set can1 type can bitrate 1000000')
    os.system('sudo ifconfig can1 up txqueuelen 65536')

print("Opening up CAN devices...")
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
can1 = can.interface.Bus(channel = 'can1', bustype = 'socketcan')

print("can1 sending periodic message...")
testMsg = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, 6, 7], extended_id=False)
testPeriodicTask = can1.send_periodic(testMsg, 1.0)

print("can0 receiving messages...")
while True:
    msg = can0.recv()
    print("\t", msg)

print("Done")
