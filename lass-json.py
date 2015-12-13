#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import simplejson
import time
import sys

temp_queue = list()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
	if rc == 0:
		print >>sys.stderr, "NOTICE: Connected"
		client.subscribe("LASS/Test/PM25")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

	# gather data from broker
	temp_queue.append(msg.payload)

def on_disconnect (client, userdata, msg):
	print >>sys.stderr, "NOTICE: Disconnected"
	client.unsubscribe("LASS/Test/PM25")

def queue_to_json (queue):
	
	ret_json = str()
	ret_list = list()

	for q in queue:
		texts  = q.strip().split('|')
		ret_dict = dict()
		for text in texts:
			if text != "":
				name, value  = text.strip().split('=')
				ret_dict[name] = value
		ret_list.append(ret_dict)

	# json pretty print
	ret_json = simplejson.dumps (ret_list, sort_keys=True, indent=4 * ' ')

	return ret_json

def main ():
	# init 
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.on_disconnect = on_disconnect
	client.connect("gpssensor.ddns.net", 1883, 60)

	# loop for gather data
	client.loop_start ()

	# magic wait
	time.sleep(1)
	print >>sys.stderr, "NOTICE: Wait 15 seconds to gather MQTT data"
	for i in range(1, 16):
		print >>sys.stderr, "NOTICE: " + str(i)
		time.sleep(1)

	client.loop_stop()
	print(queue_to_json (temp_queue))
	client.disconnect()

if __name__ == '__main__': 
	main ()
