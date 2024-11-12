import socket

# Create a UDP socket
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to all available interfaces on port 1234
udp_server.bind(('0.0.0.0', 1234))

print("UDP Server is listening on port 1234...")

try:
    while True:
        # Receive a message (max 1024 bytes) from the client
        message, addr = udp_server.recvfrom(1024)

        # Decode and print the message along with client address
        decoded_message = message.decode('utf-8')
        print(f"Received from {addr}: {decoded_message}")

        # Optional: Echo the received message back to the client
        udp_server.sendto(message, addr)

except KeyboardInterrupt:
    print("\nServer is shutting down...")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the socket gracefully
    udp_server.close()
    print("Server closed.")
