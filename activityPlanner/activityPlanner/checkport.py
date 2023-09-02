import socket


def is_port_available(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("127.0.0.1", port))
        return True
    except OSError:
        return False


# Usage example:
port_number = 8000
if is_port_available(port_number):
    print(f"Port {port_number} is available.")
else:
    print(f"Port {port_number} is not available.")
