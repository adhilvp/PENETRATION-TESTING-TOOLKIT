import socket

def port_scan(target, ports):
    print(f"🔍 Scanning {target}...")
    for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"✅ {port} is open")
            sock.close()


if __name__ == "__main__":
    target = "scanme.nmap.org"
    ports = [21, 22, 23, 25, 53, 80, 443, 3306, 8080]
    port_scan(target, ports)




