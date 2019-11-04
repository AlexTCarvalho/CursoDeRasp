import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import sys
import time

#definições
Broker = "iot.eclipse.org"
PortaBroker = 1883
KeepAliveBroker = 60
TopicoSubscribe = "JezSubscribe" #se quer enviar pro rasp, é aqui
TopicoPublish = "JezCursodeRasp" #se quer enviar pro celular, é aqui

def on_connect(client, userdata, flags, rc):
    print("[STATUS] Conectado ao Broker. Resultado de conexao: "+str(rc))
    # faz subscribe automatico no topico
    client.subscribe(TopicoSubscribe)

def on_message(client,userdata,msg):
    MensagemRecebida = str(msg.payload)

    print("[MSG RECEBIDA] Topico: "+msg.topic+" / Mensagem: "+MensagemRecebida[2:-1])
    print()
    
    select()
    
def on_disconnect(client, userdata,rc=0):
    print("DisConnected result code "+str(rc))
    client.loop_stop()

def RaspSubscribe(client):
    client.loop_start()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(Broker, PortaBroker, KeepAliveBroker)
    time.sleep(10)
    client.on_disconnect = on_disconnect
    
    time.sleep(10)
    client.disconnect()
    
def RaspPublish():
    strSend = input("Envie para o celular: ")
    publish.single(TopicoPublish, strSend, hostname=Broker,keepalive=60)
    print()
    select()
    
def select():
    try:
        op = int(input("0 - Publicar no Celular, 1 - Receber do Celular, 2 - Sair: "))
        if (op == 0):
            RaspPublish()
        elif (op == 1):
            RaspSubscribe(client)
        elif (op == 2):
            print("XAU")
            sys.exit(0)
        else:
            print("Opcao invalida")
            select()
    except KeyboardInterrupt:
        print("XAU forçado")

print("[STATUS] Inicializando MQTT...")
# inicializa MQTT
client = mqtt.Client()
select()