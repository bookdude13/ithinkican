#!/bin/bash

sudo modprobe vcan

# vcan0
sudo ip link add dev vcan0 type vcan
sudo ip link set vcan0 up

# Real CAN
#sudo ip link set can0 up type can bitrate 115200
#sudo ip link set can1 up type can bitrate 115200


