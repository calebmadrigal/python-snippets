import zmq

context = zmq.Context()
puller = context.socket(zmq.PULL)
puller.bind("tcp://127.0.0.1:30000")

while True:
    msg = puller.recv()
    print "Received:", msg

