import socket
import json

payload_data = {"message": "Hello, STP Server!"}
payload_json = json.dumps(payload_data)
content_length = len(payload_json)

request = '''GET /endpoint YAGAMI/1.1
Content-Type: json
Content-Length: 648
Content-Encoding: gzip
Expires: Fri, 13 March 2024

{"Ujjwal" : "Singh"}''' 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(("127.0.0.1", 8080))
    client_socket.sendall(request.encode())
    response = client_socket.recv(1024).decode()
    print("Response from server:", response)
