
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 53))
print(f'ip: {s.getsockname()[0]} port: {s.getsockname()[1]}')
s.close()

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(f'hostname: {hostname} ip: {ip}')

interfaces = socket.getaddrinfo(socket.gethostname(), None)
for interface in interfaces:
    print(f'ip: {interface[4][0]} port: {interface[4][1]}')
