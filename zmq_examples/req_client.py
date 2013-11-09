import zmq
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:1337")
socket.send("Hi there")
msg_in = socket.recv()
print msg_in
