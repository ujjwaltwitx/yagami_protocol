import socket, os, sys
sys.path.append("..")
sys.path.append("src")
from parser import Parser

class STPServer:
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port
        self.parser = Parser()
    
    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Server running on {self.host}:{self.port}")

        while True:
            client_socket, client_address = server_socket.accept()
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        try:
            request_data = client_socket.recv(1024).decode()
            print("Received request:\n", request_data)

            self.parser.parseRequest(request_data)
            payload = self.parser.body
            print("Parsed payload:", payload)

            response = "STP/1.0 200 OK\nContent-Type: text/plain\n\nPayload received"
            client_socket.sendall(response.encode())
        except Exception as e:
            print("Error handling request:", e)
        finally:
            client_socket.close()

if __name__ == '__main__':
    server = STPServer()
    server.start()
