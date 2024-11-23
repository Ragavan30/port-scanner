import socket

target = input("172.217.255.255")
ports = [20,22,21,25,53,80,143,110 ,80, 443]  # Common ports

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()
