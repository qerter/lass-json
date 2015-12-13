#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
import simplejson

import paho.mqtt.client as mqtt


_temp_queue = list()


MQTT_SERVER = "gpssensor.ddns.net"
MQTT_PORT = 1883
MQTT_KEEPLIVE_SEC = 60
TOPIC = "LASS/Test/PM25"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    if rc == 0:
        print >>sys.stderr, "NOTICE: Connected"
        client.subscribe(TOPIC)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # gather data from broker
    _temp_queue.append(msg.payload)


def on_disconnect(client, userdata, msg):
    print >>sys.stderr, "NOTICE: Disconnected"
    client.unsubscribe(TOPIC)


def dump_queue_to_json(queue):

    ret_list = list()

    for q in queue:

        ret_dict = dict()
        texts = q.strip().split("|")

        for text in texts:

            if not text:
                continue

            name, value = text.strip().split("=")
            ret_dict[name] = value

        ret_list.append(ret_dict)

    # json pretty print
    return simplejson.dumps(ret_list, sort_keys=True, indent=4 * " ")


def main():
    # init
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.connect(MQTT_SERVER, MQTT_PORT, MQTT_KEEPLIVE_SEC)

    # loop for gather data
    client.loop_start()

    # magic wait
    time.sleep(1)
    print >>sys.stderr, "NOTICE: Wait 15 seconds to gather MQTT data"
    time.sleep(15)

    client.loop_stop()
    print(dump_queue_to_json(_temp_queue))
    client.disconnect()


if __name__ == "__main__":
    main()
