import ipaddress
import socket

ip_str = input("Enter an IP address: ")

try:
    ip_address = ipaddress.ip_address(ip_str)
    print("Valid IP address:", ip_address)
except ValueError:
    print("Invalid IP address")

def scan_ports(target_ip, port_range):
    open_ports = []

    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        result = sock.connect_ex((target_ip, port))
        
        if result == 0:
            open_ports.append(port)
        
        sock.close()

    return open_ports

target_ip =ip_address
port_range = range(1, 1025)  


open_ports = scan_ports(target_ip, port_range)


if open_ports:
    print("Open ports:")
    for port in open_ports:
        print(f"Port {port} is open")
else:
    print("No open ports found.")



