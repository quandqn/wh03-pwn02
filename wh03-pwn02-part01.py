import socket
HOST = '103.237.98.32'
PORT = 25032

for i in range(0, 1000):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	chall = s.recv(1024)
	while "Enter your number:" not in chall:
		chall+= s.recv(1024)
	s.send(str(i)+"\n")
	data = s.recv(1024)
	#print i, data
	if "Don't give up!" not in data:
		print data
		break
    
"""
I have two secret numbers, I like you guessing them. Are you ready?

        The first challenge: guessing one,
Enter your number:Well done! The secret numer is 576. Pass challenge 2 to get the flag
"""
