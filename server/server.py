import socket
import json

with open('../config.json') as json_file:
  config = json.load(json_file)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((config['ip'], config['port']))

print('Server > ' + config['ip'] + ':' + str(config['port']))

clients = []

while True:
  data, addr = server_socket.recvfrom(1024)

  if addr not in clients:
    clients.append(addr)

  print(data.decode('utf-8'))

  for client in clients:
    server_socket.sendto(data, client)

server_socket.close()
