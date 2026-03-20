# Ingrid Andre Singson
# 3146981

# Using some code from assignment 1 to help create the program for this lab
import socket 

FORMAT = 'ascii'
SIZE = 2048

def client():
    # server information
    server_name = 'localhost'
    server_port = 13000

    # create client socket using IPv4 and TCP protocols
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('Error in client socket creation:', e)
        sys.exit(1)

    try: 
        # client connects with the server
        client_socket.connect((server_name, server_port))

        # welcome message from the server
        msg_from_server = client_socket.recv(SIZE).decode(FORMAT)

        # print msg from server to client then send client choice to server
        msg_to_server = input(msg_from_server)
        client_socket.send(msg_to_server.encode(FORMAT))

        # keep running program as long as client does not choose 3
    
        while msg_to_server != '3':
            
            if msg_to_server == '1':

                msg_from_server = client_socket.recv(SIZE).decode(FORMAT)

                # send server the client name
                msg_to_server = input(msg_from_server).encode(FORMAT)
                client_socket.send(msg_to_server)

                # send server client phone number
                msg_from_server = client_socket.recv(SIZE).decode(FORMAT)
                msg_to_server = input(msg_from_server).encode(FORMAT)
                client_socket.send(msg_to_server)

                # get server menu options again
                msg_from_server = client_socket.recv(SIZE).decode(FORMAT)

                # send client choice to server
                msg_to_server = input(msg_from_server)
                client_socket.send(msg_to_server.encode(FORMAT))
            
            if msg_to_server == '2':

                # server asks client for the search word
                msg_from_server = client_socket.recv(SIZE).decode(FORMAT)

                # client sends the search word to the server
                msg_to_server = input(msg_from_server)
                client_socket.send(msg_to_server.encode(FORMAT))

                # client receives phonebook entries with search word
                msg_from_server = client_socket.recv(SIZE).decode(FORMAT)
                print(msg_from_server)

                # get server menu options again
                msg_from_server = client_socket.recv(SIZE).decode(FORMAT)

                # send client choice to server
                msg_to_server = input(msg_from_server)
                client_socket.send(msg_to_server.encode(FORMAT))

        

        client_socket.close()
        print('Connection terminated.')


    except socket.error as e:
        print('An error occurred:', e)
        client_socket.close()
        sys.exit(1)

#-----------------------------------------------------
client()