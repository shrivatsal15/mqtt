import paho.mqtt.client as mqtt
import time
#f = open("/proc/loadavg", "r+")

#load = f.read()

def on_connect(client,userdata,flags,rc):
	print("connected")


def on_publish(client,userdata,result):
	print("data published")

client = mqtt.Client("clientid")
client.on_publish=on_publish

client.will_set("client/dead","client disconnected",0,True)
client.connect("192.168.75.140", 1883, 60)
client.on_connect=on_connect
#client.will_set("client/dead","client disconnected",0,True)
while True:
	f = open("/proc/loadavg", "r+")
	load = f.read()
#	print(type(load))
	loadl=load.split()
	ret=client.publish("hello/pc/1minavg",'1minavg '+loadl[0])
	ret=client.publish("hello/pc1/5minavg",'5minavg '+loadl[1])
	ret=client.publish("hello/pc3/10minavg",'10minavg '+loadl[2])
	#client.will_set("client/dead","client disconnected",0,True)
	time.sleep(5)
	f.close()
client.loop_forever()
