import socket

def start_sniffer():
    # Socket connection setup
    host = socket.gethostbyname(socket.gethostname())
    print(f"Starting Network Sniffer on {host}...")
    
    # Raw socket create karein
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    conn.bind((host, 0))
    conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    # Traffic capture loop
    try:
        while True:
            raw_data, addr = conn.recvfrom(65535)
            print(f"Packet captured from Source IP: {addr[0]}")
    except KeyboardInterrupt:
        print("\nStopping Network Sniffer...")
        conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == "__main__":
    start_sniffer()