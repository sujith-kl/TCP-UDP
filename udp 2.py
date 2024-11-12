import socket

# Create a UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server = ('localhost', 1234)

print("Type 'exit' to close the connection.")

try:
    while True:
        # Get user input to send to the server
        message = input("Send: ")

        # Exit the loop if the user types 'exit'
        if message.lower() == 'exit':
            print("Closing connection...")
            break

        # Send the message to the server
        client.sendto(message.encode('utf-8'), server)

        # Receive and print the server's response (optional)
        response, _ = client.recvfrom(1024)
        print(f"Received: {response.decode('utf-8')}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the socket gracefully
    client.close()
    print("Connection closed.")
