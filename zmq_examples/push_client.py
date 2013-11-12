import zmq

context = zmq.Context()
pusher = context.socket(zmq.PUSH)
pusher.connect("tcp://127.0.0.1:30000")

for i in xrange(20):
    msg = "Message {0}".format(i)
    print "Sending:", msg
    pusher.send(msg)

