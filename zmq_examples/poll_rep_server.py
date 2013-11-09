import zmq

def handle_web_req(sock):
    msg = sock.recv()
    if msg == "get":
        print "Gave pin statuses to web controller"
        sock.send("1=on,2=on,3=off")
    elif msg == "set":
        print "Setting pin"
        sock.send("successfully set pins")
    else:
        print "Bad command received"
        sock.send("error: bad command")

def handle_sensor_req(sock):
    msg = sock.recv()
    sock.send("") # Send an empty response to fullfill reply requirement
    if msg == "door:triggered":
        print "Sensor triggered...SOUND THE ALARM!"
 
context = zmq.Context()

web_watcher = context.socket(zmq.REP)
web_watcher.bind("tcp://127.0.0.1:2000")
sensor_watcher = context.socket(zmq.REP)
sensor_watcher.bind("tcp://127.0.0.1:2001")

poll = zmq.Poller()
poll.register(web_watcher, zmq.POLLIN)
poll.register(sensor_watcher, zmq.POLLIN)

while True:
    poll_result = dict(poll.poll())
    if (web_watcher in poll_result) and (poll_result[web_watcher] == zmq.POLLIN):
        handle_web_req(web_watcher)
    elif (sensor_watcher in poll_result) and (poll_result[sensor_watcher] == zmq.POLLIN):
        handle_sensor_req(sensor_watcher)

