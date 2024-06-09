import socket
import threading

clients = []


def broadcast(message, curr_client):
    with open("chat.txt", "a") as file:
        file.write(message + "\n")
    for client in clients:
        if client != curr_client:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(curr_client)


def handle(client_socket):
    nickname = client_socket.recv(1024).decode()
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"{nickname} -> {message}")
                broadcast(f"{nickname} -> {message}", client_socket)

            else:
                client_socket.close()
                clients.remove(client_socket)
        except:
            client_socket.close()
            clients.remove(client_socket)
            break


def start_tcp_server(host="localhost", port=8091):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((host, port))
    server.listen()

    while True:
        client_socket, addr = server.accept()
        print(f"dakavshireba moxda {addr}")
        clients.append(client_socket)
        threading.Thread(target=handle, args=(client_socket,)).start()


start_tcp_server()
