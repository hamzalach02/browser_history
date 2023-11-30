import socket
import pickle

def receive_and_store_tuple(client_socket, file_path):
    data_length = int.from_bytes(client_socket.recv(4), byteorder='big')

    serialized_data = b""
    while len(serialized_data) < data_length:
        serialized_data += client_socket.recv(1024)

    received_tuple = pickle.loads(serialized_data)

    with open(file_path, 'w') as file:
        for element in received_tuple:
            file.write(str(element) + '\n')

    return received_tuple

def start_server(server_ip, server_port, file_path):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    print("""
          ██╗     ████████║  ████████║  ██║   ██║  ████████║ ████████║ ███████║
          ██║     ██║   ██║  ██║        ██║   ██║  ██║       ██║   ██║ ██║   ██║
          ██║     ████████║  ██║        ████████║  ██║   ██║ ████████║ ███████║
          ██║     ██║   ██║  ██║        ██║   ██║  ██║   ██║ ██║   ██║ ██║   ██║
          ██████║ ██║   ██║  ████████║  ██║   ██║  ████████║ ██║   ██║ ██║    ██║
                  
      """)

     print(f"Server listening on {server_ip}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        received_data = receive_and_store_tuple(client_socket, file_path)
        print("data is written in the file history.txt")

        client_socket.close()

if __name__ == "__main__":
    server_ip = "your_linux_machine_ip" 
    server_port = 4014 #you can change the port it doesnt matter (but keep the same in the client.py)
    file_path = "history.txt"

    start_server(server_ip, server_port, file_path)
