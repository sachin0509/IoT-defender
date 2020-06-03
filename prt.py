import socket
import logging
import time
from prettytable import PrettyTable
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

    x = PrettyTable()
    port = {22: "close", 80: "close", 23: "close", 5060: "close", 8080: "close", 7547: "close", 2323: "close",
            81: "close", 25: "close", 2222: "close", 8081: "close", 9200: "close", 8090: "close", 52869: "close",
            37777: "close", 37215: "close", 2332: "close", 2223: "close", 5061: "close", 100: "close"}
    x.align = "l"
    x.title = "Portscan"
    x.field_names = ["Port No", "Status"]
    open_pcounter = 0

    closed_pcounter = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,)
    s.connect(("10.255.255.255", 80))
    v_ip = s.getsockname()[0]


    print(tabulate([['Sys name',(socket.gethostbyaddr(socket.gethostname())[0])], ['Sys ip', v_ip]], headers=['\nSystem details', '              ']))

    if v_ip is not None:
        for p in port:
            c = SConnect(v_ip, p)
            if c.portscan() == 0:
                port[p]="open"
    for i in port.keys():
        if port[i] == "close":
            x.add_row(['{}'.format(i), "\033[91m {}\033[00m".format(port[i])])
        else:
            x.add_row(['{}'.format(i), "\033[92m {}\033[00m".format(port[i])])
    print('\n')
    print(x)


if __name__ == '__main__':
    main()
