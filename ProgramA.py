# Program Name: Assignment4.py
# Course: IT3883/Section W01
# Student Name: Noah Lawhorn
# Assignment Number: Assignment#4
# Due Date: 10/26/2025
# Purpose: This program demonstrates basic network communication between client and server. Program A (Client side) will take message and send it to program B (Server Side) to be converted then sent back.
# List Specific resources used to complete the assignment. W3Schools.com was used for syntax purposes


import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 4005)) #IP and port number, same on both client ad server

message = input("Enter a message: ") #prompts user to enter message

if message.strip() == "":
    print("No message")

else:
    client.send(message.encode()) #Converts to bytes

    reply = client.recv(1024).decode() #Receives bytes and Converts back to string
    print("Program B response: ", reply)

client.close()