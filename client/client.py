import socket
import json

with open('../config.json') as json_file:
  config = json.load(json_file)

with open('../template.txt') as file:
  template_reset = file.read()


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect((config['ip'], config['port']))

connecting_msg = '< ' + config['name'] + ' connected >'
with open('chat.txt') as file:
  file.write('<! You logged in as: ' + config['name'] + ' !>\n')
client_socket.sendall(str.encode(connecting_msg))

while True:
  data = client_socket.recv(1024)

  print(data.decode('utf-8'))

  if not data:
    break

client_socket.close()
