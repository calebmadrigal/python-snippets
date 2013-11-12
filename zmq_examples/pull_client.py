import zmq

context = zmq.Context()
pullerg = context.socket(zmq.PULL)
pullerg.connect("tcp://127.0.0.1:30000")

while True:
    msg = pullerg.recv()
    print "Received message:", msg

