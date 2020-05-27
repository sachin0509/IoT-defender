import socket
import struct
import smtplib

from datetime import datetime

def main():
    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)
    dict = {}
    file_txt = open("attack_DDoS.txt", 'a')
    t1 = str(datetime.now())
    file_txt.writelines(t1)
    file_txt.writelines("\n")
    No_of_IPs = 20
    R_No_of_IPs = No_of_IPs + 10
    c = 1
    while c :
        pkt = s.recvfrom(2048)
        ipheader = pkt[0][14 :34]
        ip_hdr = struct.unpack("!8sB3s4s4s", ipheader)
        IP = socket.inet_ntoa(ip_hdr[3])
        print("The Source of the IP is:", IP)
        if IP not in dict.keys() :
            dict[IP] = 0
        if IP in dict.keys() :
            dict[IP] = dict[IP] + 1
            if (dict[IP] >= No_of_IPs) :
                line = "DOS attack is Detected: "
                print(line, dict[IP])
                file_txt.writelines(line)
                file_txt.writelines(IP)
                file_txt.writelines("\n")
                c = 0

