import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:1337")
 
while True:
    msg = socket.recv()
    print "Got", msg
    socket.send(msg)

