# Ingrid Andre Singson 
# 3146981

# Using some code from assignment 1 to help create program for this lab 
import socket
import sys

FORMAT = 'ascii'
SIZE = 2048

def server():
    # server port
    server_port = 13000

    # creating a server socket that uses IPv4 and TCP protocols
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('Error in server socket creation:', e)
        sys.exit(1)

    # associate 13000 port number to the server socket
    try:
        server_socket.bind(('', server_port))
    except socket.error as e:
        print('Error in server socket binding:', e)
        sys.exit(1)

    # only one client allowed at each time 
    server_socket.listen(1)

    while 1:
        try:
            # server accepts client connection 
            connection_socket, addr = server_socket.accept()

            # send client welcome message and server menu options
            msg_to_client = 'Welcome to the online phone book.\n\nPlease select the operation\n1)' \
            'Add a new entry\n2)Search\n3)Terminate the connection\n\nChoice: '.encode(FORMAT)

            connection_socket.send(msg_to_client)

            # server receives client menu option 
            msg_from_client = connection_socket.recv(SIZE).decode(FORMAT)

            phonebook = {}

            while msg_from_client != '3':

                server_menu = '\nPlease select the operation \n1)Add a new entry\n2)Search\n3)Terminate the connection\n\nChoice: '.encode(FORMAT)

                # perform phone adding subprotocol
                if msg_from_client == '1':

                    # ask client for name
                    msg_to_client = 'Enter the name: '.encode(FORMAT)
                    connection_socket.send(msg_to_client)
                    
                    name = connection_socket.recv(SIZE).decode(FORMAT)

                    # ask client for phone number 
                    msg_to_client = 'Enter the phone number: '.encode(FORMAT)
                    connection_socket.send(msg_to_client) 

                    phone_number = connection_socket.recv(SIZE).decode(FORMAT)

                    # add information to phonebook
                    # if name already exists, add number under name
                    if name in phonebook:
                        phonebook[name].append(phone_number)
                    
                    # if name does NOT exist, create a new entry 
                    else:
                        phonebook[name] = [phone_number]
                    
                    # send client server menu options 
                    connection_socket.send(server_menu)

                    # receive client menu option
                    msg_from_client = connection_socket.recv(SIZE).decode(FORMAT)

                # perform phone search protocol
                if msg_from_client == '2':

                    # ask client for the search word
                    msg_to_client = 'Enter the search word: '.encode(FORMAT)
                    connection_socket.send(msg_to_client)

                    # receive search word from client
                    msg_from_client = connection_socket.recv(SIZE).decode(FORMAT)
                    search_word = msg_from_client

                    # send phonebook entries with search word to clint
                    for key in phonebook:
                        if search_word in key:
                            print(key, phonebook[key])


                    # send client server menu options
                    connection_socket.send(server_menu)

                    # receive client menu option
                    msg_from_client = connection_socket.recv(SIZE).decode(FORMAT)

                # Phone search subprotocol
            
            
    
            connection_socket.close()

        except socket.error as e:
            print('An error occurred', e)
            server_socket.close()
            sys.exit(1)
        except:
            print('Goodbye')
            server_socket.close()
            sys.exit(0)

#-----------------------------------------------------

server()