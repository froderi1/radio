#!/usr/bin/python
import paho.mqtt.client as mqtt
import os
import time

# Playlists for Stations and 3miles
# are stored in /var/lib/mpd/playlists/stations.m3u 

os.system("mpc stop")
os.system("mpc clear")

def station_nr(station):
#   client.publish("/home/radio" , "y_on")
#   client.publish("/home/radio" , "y_vcr1")
   os.system("mpc stop")
   os.system("mpc clear")
   os.system("mpc load stations")
   os.system("mpc play " + station)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/home/radio")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    print(str(msg.payload))

    if str(msg.payload) == "power":
	os.system("mpc_onoff.sh")

    if str(msg.payload) == "pause":
        os.system("mpc toggle")

    if str(msg.payload) == "radio_off":
#        client.publish("/home/radio" , "y_dvd")
#        client.publish("/home/radio" , "y_off")
        os.system("mpc stop")
        os.system("mpc clear")
        os.system("music_stop")

    if str(msg.payload) == "station":
        client.publish("/home/radio" , "y_on")
        time.sleep(2)
        client.publish("/home/radio" , "y_vcr1")
        print(msg.topic + str(msg.payload))
	# read station number from text file
	f = open('/home/frank/radio/station.txt', 'r')
	station = int(f.read())
	f.close
	print("station_change")
	station += 1
	if station > 5:
	    station = 1
	print (str(station))
	os.system("mpc play " + str(station))
	f = open('/home/frank/radio/station.txt', 'w')
	f.write('%d' % station)
	f.close

    if str(msg.payload) == "oldies":
          station_nr("1")

    if str(msg.payload) == "relax":
          station_nr("2")

    if str(msg.payload) == "fip":
          station_nr("3")

    if str(msg.payload) == "rock":
          station_nr("4")

    if str(msg.payload) == "jazz":
          station_nr("5")

    if str(msg.payload) == "groove":
          station_nr("6")

    if str(msg.payload) == "reggae":
          station_nr("7")

    if str(msg.payload) == "wdr2":
          station_nr("8")

    if str(msg.payload) == "wdr4":
          station_nr("9")

    if str(msg.payload) == "xmas":
          station_nr("10")

    if str(msg.payload) == "walzer":
          client.publish("/home/radio" , "y_on")
          time.sleep(2)
          client.publish("/home/radio" , "y_vcr1")
          os.system("mpc stop")
          os.system("mpc clear")
          os.system("mpc load walzer")
          os.system("mpc play 1")


    if str(msg.payload) == "3miles":
          client.publish("/home/radio" , "y_on")
          time.sleep(2)
          client.publish("/home/radio" , "y_vcr1")
          os.system("mpc stop")
          os.system("mpc clear")
          os.system("mpc load 3miles")
          os.system("mpc play 1")

    if str(msg.payload) == "music":
          client.publish("/home/radio" , "y_on")
          time.sleep(2)
          client.publish("/home/radio" , "y_vcr1")
          os.system("mpc stop")
          os.system("mpc clear")
          os.system("music_start &")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("debian", 1883, 60)

client.loop_forever()
