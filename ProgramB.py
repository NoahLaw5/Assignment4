# Program Name: Assignment4.py
# Course: IT3883/Section W01
# Student Name: Noah Lawhorn
# Assignment Number: Assignment#4
# Due Date: 10/26/2025
# Purpose: This program demonstrates basic network communication between client and server. Program A (Client side) will take message and send it to program B (Server Side) to be converted then sent back.
# List Specific resources used to complete the assignment. W3Schools.com was used for syntax purposes


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 4005)) #Binds the socket
s.listen(1)

print("Waiting")
conn, addr = s.accept()
print("Connected", addr)

data = conn.recv(1024) #Data received for decoding

if data:
    text = data.decode()
    print("Received: ", text)  #Converts the string to uppercase then encodes to bytes to sends back

    conn.send(text.upper().encode())

else:
    print("No data received")

conn.close()
s.close()