import logging
import socketserver
import time
import sipfullproxy

if __name__ == "__main__":
    HOST = sipfullproxy.HOST
    PORT = sipfullproxy.PORT
    UDPHandler = sipfullproxy.UDPHandler
    socket = sipfullproxy.socket
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    ipaddress = socket.gethostbyname(hostname)
    ipaddress = "10.10.37.166"
    print(ipaddress)
    #if ipaddress == "127.0.0.1":
    #    ipaddress = sys.argv[1]
    logging.info(ipaddress)
    recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    server = socketserver.UDPServer((HOST, PORT), UDPHandler)
    server.serve_forever()