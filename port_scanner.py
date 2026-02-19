import socket

target = input("Enter target IP or domain: ")

print("\nScanning target:", target)
print("Please wait...\n")

try:
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()

except KeyboardInterrupt:
    print("\nScan stopped")
except socket.gaierror:
    print("Hostname could not be resolved")
except socket.error:
    print("Server not responding")






