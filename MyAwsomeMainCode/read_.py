# -*- coding: utf-8 -*-
""" Bu kod FireBase den alir MQTT ye atar """
import firebase_admin
from firebase_admin import firestore, credentials
from time import sleep
import paho.mqtt.client as mqtt
import json
import os
import sys
Fb_Coll = "color"


def main():
    
    x = open("../ip.json")
    data_ = json.load(x)
    ip = data_["ip"]
    Server = ip
    x.close()
    cred = credentials.Certificate("../Login.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))



    def on_message(client, userdata, msg):
        """
        topic = msg.topic
        data = msg.payload.decode('UTF-8')
        print("Message coming")
        """
        #print("Firebase'den: Topic: {}, Message: {}".format(topic,data))
        pass



    client = mqtt.Client()  

    client.connect(Server, 1883, 60)


    client.on_connect = on_connect

    client.on_message = on_message

    x = 0

    while True:

        red_res = db.collection(Fb_Coll).document("color").get()

        red = red_res.to_dict()

        client.publish('/red' , red.get('/red'))
        print(red)
        #print(client.publish('/red' , red.get('/red')))

           

        """x += 1
        print("Read===Sayac",x)  
        """         
        sleep(2)

    client.loop_forever() 


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nPrograms was stopped")  
        sys.exit()
