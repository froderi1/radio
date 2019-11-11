#!/bin/bash

MQTTHOST="debian"
MQTTTOPIC="/home/radio"

if [ $(mpc | awk '{print $1;}') = "volume:" ] ; then
        mpc load radio > /dev/null
        mpc play 1 > /dev/null
        /usr/bin/mosquitto_pub -h $MQTTHOST -t $MQTTTOPIC -m "y_on"
        /usr/bin/mosquitto_pub -h $MQTTHOST -t $MQTTTOPIC -m "y_vcr1"
        echo 1
else
        mpc stop > /dev/null
        mpc clear > /dev/null
        /usr/bin/mosquitto_pub -h $MQTTHOST -t $MQTTTOPIC -m "y_dvd"
        /usr/bin/mosquitto_pub -h $MQTTHOST -t $MQTTTOPIC -m "y_off"
        echo 0
fi

