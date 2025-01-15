import paho.mqtt.client as mqtt
import ssl
import json
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes
import aasbinding as binding
import logging

transport_type = 'websockets'



def on_subscribe(client, userdata, mid, reason_code_list, properties):
    # Since we subscribed only for a single channel, reason_code_list contains
    # a single entry
    if reason_code_list[0].is_failure:
        print(f"Broker rejected you subscription: {reason_code_list[0]}")
    else:
        logging.info(f"Broker granted the following QoS: {reason_code_list[0].value}")

def on_unsubscribe(client, userdata, mid, reason_code_list, properties):
    # Be careful, the reason_code_list is only present in MQTTv5.
    # In MQTTv3 it will always be empty
    if len(reason_code_list) == 0 or not reason_code_list[0].is_failure:
        print("unsubscribe succeeded (if SUBACK is received in MQTTv3 it success)")
    else:
        print(f"Broker replied with failure: {reason_code_list[0]}")
    client.disconnect()

def on_message(client, userdata, message):
    # userdata is the structure we choose to provide, here it's a list()
    logging.info(f"Recieved Message From Broker:")
    #pprint.pprint(json.loads(str(message.payload, 'utf-8')))
    logging.info(f"On Topic: {message.topic}. With QoS {str(message.qos)}")

    data = json.loads(str(message.payload, 'utf-8'))

    # binding for submodel repository
    if data["subject"] == "SUBMODEL" and data["data"]["@type"] == "ElementUpdateEvent": 
        logging.info(f'Subject is {data["subject"]}. Event Forwarding Passed First Test')
        logging.info(f'Event Type is {data["data"]["@type"]}. Event Forwarding Passed Second Test')
        binding.update_submodel_repo(data)

    else:
        logging.info(f'Subject is Not {data["subject"]} or Event is Not {data["data"]["@type"]}. Event Forwarding Failed, Terminating Event Forwarding....')

    #This is causing Error so it is commented out
    #
    # userdata.append(message.payload)
    # We only want to process 10 messages
    # if len(userdata) >= 10:
        #client.unsubscribe("$SYS/#")

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
    else:
        logging.info("Connection is successful")
        client.subscribe("events")
       

def connect_mqtt():
    broker = 'mqttbroker.factory-x.catena-x.net'
    Port = 443
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='fx-consumer', transport=transport_type)

    client.username_pw_set(username="fx-subscriber", password="password")

    client.tls_set(certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED)

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_unsubscribe = on_unsubscribe


   

    client.connect(broker, Port, keepalive=120)
    
    return client

def run():
    client = connect_mqtt()

    try:
        client.loop_forever()

    except KeyboardInterrupt:
        client.disconnect()
        client.loop_stop()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run()