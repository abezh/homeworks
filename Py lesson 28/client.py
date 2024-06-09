import socket
import threading


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(message.decode())
            else:
                break
        except:
            break


def start_tcp_client(host='localhost', port=8091):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input("chaceret saxeli: ")
    client_socket.send(message.encode())

    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input()
        if message == "quit":
            client_socket.close()
            break
        client_socket.send(message.encode())


start_tcp_client()
