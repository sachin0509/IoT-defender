import socket
import logging
import time

class SConnect:
    def __init__(self, ip, port=None):
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.s_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_connection.settimeout(0.3)

    def portscan(self):
        return self.s_connection.connect_ex(self.address)


def main():
    logging.basicConfig(filename="errlog.log", format="%(asctime)s : %(message)s")
    logging.info("Start")
    print("\nHello user and welcome to Network Port Scanner!")
    print("Please insert a IP address that you want to scan for open and closed ports.")
    print("The range of ports scanned is 1-65535.")
    port = [22, 80, 23, 5060, 8080, 7547, 2323, 81, 25, 2222, 8081, 9200, 8090, 52869, 37777, 37215, 2332, 2223, 5061,
            100]
    open_pcounter = 0
    closed_pcounter = 0

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("10.255.255.255", 80))
    userIP=s.getsockname()[0]
    print(userIP)


    if userIP is not None:
        for p in port:
            start_ptime = time.time()
            c = SConnect(userIP, p)
            if c.portscan() == 0:
                print("Port {} is open".format(p))
                open_pcounter += 1
    else:
        print("You failed, terminating.\n")

    print("Total open ports:", open_pcounter)
    logging.info("Finished")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
