#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2022 Summer)
# Michiharu Takemoto (takemoto.development@gmail.com)
#
# 2022/05/08 Singe-data version

# You have to install AdaFruit CircuitPython DHT Libraries by
# $ pip3 install adafruit-circuitpython-dht
# .

import adafruit_dht
from board import *

import time
import datetime

def getTmp(pin):
    instance_dht = adafruit_dht.DHT11(pin=D4, use_pulseio=False)

    try:
        instance_dht.measure()
        temp_dht = instance_dht.temperature
        humid_dht = instance_dht.humidity
        return True, temp_dht, humid_dht
    except RuntimeError:
        print("RuntimeError: DHT11/22 returns wrong values, maybe.: " +
              str(datetime.datetime.now()))
        return False, 0, 0
    except OSError:
        print("OSError: DHT11/22: OS Error, but we ignore it.: " +
              str(datetime.datetime.now()))
        return False, 0, 0
