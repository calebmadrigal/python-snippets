import zmq

context = zmq.Context()
pusher = context.socket(zmq.PUSH)
pusher.bind("tcp://127.0.0.1:30000")
for num in xrange(20):
    msg = "Message {0}".format(num)
    print "Sending:", msg
    pusher.send(msg)

