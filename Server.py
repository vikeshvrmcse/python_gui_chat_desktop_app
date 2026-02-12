import socket as skt
server_skt = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
server_skt.bind(("localhost", 7777))
server_skt.listen()
data, address = server_skt.accept()
print(f"Connection established with {address}")
def receiveData():
        try:
            received_data = data.recv(1024).decode()
            if received_data:   
                return received_data
        except Exception as e:
            print(e)
def sendData(sending_data):
        try:
            data.send(sending_data.encode()) 
        except Exception as e:
            print(e)
def closeConnection():
    print("Connection closed.")
    data.close()
    server_skt.close()


