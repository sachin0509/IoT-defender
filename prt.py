import socket
import logging
import time
from tabulate import tabulate


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

    port = [22, 80, 23, 5060, 8080, 7547, 2323, 81, 25, 2222, 8081, 9200, 8090, 52869, 37777, 37215, 2332, 2223, 5061,
            100]
    n = (
        "22 \n80 \n23 \n5060 \n8080 \n7547 \n2323 \n81 \n25 \n2222 \n8081 \n9200 \n8090 \n52869 \n37777 \n37215 \n2332 \n2223 \n5061 \n100")
    open_pcounter = 0

    closed_pcounter = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,)
    s.connect(("10.255.255.255", 80))
    v_ip = s.getsockname()[0]


    print(tabulate([['Sys name',(socket.gethostbyaddr(socket.gethostname())[0])], ['Sys ip', v_ip]], headers=['\nSystem details', '              ']))
    print(tabulate([['\nport numbers',  n]], headers=['\nList of ports being scanned', '                           ']))

    if v_ip is not None:
        for p in port:
            start_ptime = time.time()
            c = SConnect(v_ip, p)
            if c.portscan() == 0:
                print(tabulate([['\nport number', p]], headers=['\nList of ports open', '                  ']))
                open_pcounter += 1
    else:
        print("You failed, terminating.\n")
    print(tabulate([['\nnumber of open ports', open_pcounter]],
                   headers=['\nTotal number of ports open', '                          ']))
    logging.info("Finished")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
