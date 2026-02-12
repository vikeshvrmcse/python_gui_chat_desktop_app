import socket as skt
client_skt = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
client_skt.connect(("localhost", 7777)) 
def receiveData():
    try:
        received_data = client_skt.recv(1024).decode()
        if received_data:
            return received_data
    except Exception as e:
        print(e)
def sendData(sending_data):
        try:
            client_skt.send(sending_data.encode())
        except Exception as e:
           
            print(e)
def closeConnection():
    print("Connection closed.")
    client_skt.close()

