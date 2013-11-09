import zmq
context = zmq.Context()
socket = context.socket(zmq.REQ)

# Test 'get' command with the web connection
socket.connect("tcp://127.0.0.1:2000")
socket.send("get")
msg_in = socket.recv()
print msg_in

# Test 'set' command with the web connection
socket.send("set")
msg_in = socket.recv()
print msg_in

socket2 = context.socket(zmq.REQ)
socket2.connect("tcp://127.0.0.1:2001")
socket2.send("door:triggered")
print "Sent 'door:triggered' message"
