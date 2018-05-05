import paho.mqtt.client as mqtt

host_name = "rpsolutions.ddns.net"


##Client(client_id=””, clean_session=True, userdata=None, ##protocol=MQTTv311, transport=”tcp”)

client = mqtt.Client(client_id = "rps-V")


##connect(host, port=1883, keepalive=60, bind_address="")


client.connect(host_name)



#publish(topic, payload=None, qos=0, retain=False)

client.publish('test','rps-V PRESENT')


