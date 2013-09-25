#!/usr/bin/env python

import mosquitto
import random
import time

mqttc = mosquitto.Mosquitto()

mqttc.connect("localhost", 1883)

mqttc.loop_start()

while True:
    try:
        payload = "%.1f" % random.uniform(10,40)
        rc, mid = mqttc.publish('temp/random', payload, qos=0, retain=False)
        if rc != 0:
            print rc
        time.sleep(0.5)
    except KeyboardInterrupt:
            break

mqttc.loop_stop()
mqttc.disconnect()
