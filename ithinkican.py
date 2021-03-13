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
    os.system('sudo ifconfig can0 txqueuelen 65536')
    os.system('sudo ip link set can1 type can bitrate 1000000')
    os.system('sudo ifconfig can1 txqueuelen 65536')

print("Opening up CAN devices...")
can0 = can.interface.Bus(channel = 'can0', bustyp = 'socketcan_ctypes')
can1 = can.interface.Bus(channel = 'can1', bustyp = 'socketcan_ctypes')

print("can1 sending periodic message...")
testMsg = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, 6, 7], extended_id=False)
testPeriodicTask = can1.send_periodic(testMsg, 1.0)

print("can0 receiving messages...")
for i in range(60):
    msg = can0.recv(3.0)
    if msg is None:
        print("\tcan0", "Timed out")
    else:
        print("\tcan0")

print("Done")
