import requests
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_server_status(ip, port, timeout=1, interval=1):
    url = f"http://{ip}:{port}"
    print(f"Checking server status at {url}")
    while True:
        clear_screen()
        print(f"Attempting to connect to {url}...")
        try:
            response = requests.get(url, timeout=timeout)
            print(f"Received response with status code: {response.status_code}")
            if response.status_code == 200:
                print(f"Server at {ip} is up.")
            else:
                print(f"Server at {ip} is reachable but returned status code: {response.status_code}")
        except requests.exceptions.Timeout:
            print(f"Request to {ip} timed out after {timeout} seconds.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while trying to reach {ip}: {e}")
        
        time.sleep(interval)

def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

def is_valid_port(port):
    if port.isdigit():
        port_number = int(port)
        return 1 <= port_number <= 65535
    return False

def prompt_for_ip():
    while True:
        user_ip = input("Enter the IP address of the server you want to check: ").strip()
        if is_valid_ip(user_ip):
            return user_ip
        else:
            print("Invalid IP address. Please enter a valid IP address.")

def prompt_for_port():
    while True:
        user_port = input("Enter the port number (1-65535) or press Enter to use the default port 30120: ").strip()
        if user_port == "":
            return 30120
        elif is_valid_port(user_port):
            return int(user_port)
        else:
            print("Invalid port number. Please enter a port number between 1 and 65535.")

server_ip = prompt_for_ip()
server_port = prompt_for_port()
print(f"Using IP address: {server_ip} and port: {server_port}")

try:
    check_server_status(server_ip, server_port)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
