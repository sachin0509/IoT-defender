import os
import spwd
import crypt
import time
import subprocess
import socket
import paramiko

def DictionaryAttack() :
    hashedPassword = spwd.getspnam("pi")[1]
    file = open('/home/pi/Desktop/IoT-defender/password', 'r')
    if hashedPassword :
        if hashedPassword == 'x' or hashedPassword == '*' :
            raise NotImplementedError("Sorry, currently no support for shadow passwords")
        else :
            for password in file.read().splitlines() :
                if (crypt.crypt(password, hashedPassword) == hashedPassword) :
                    print("change the Default passowrd");


def MaximumAuthentication() :
    try :
        output = str(subprocess.check_output("grep 'deny=' /etc/pam.d/common-auth", shell=True));
        c = "deny="
        j = 0
        for i in range(len(output) - 5) :
            if output[i] == c[j] and output[i + 1] == c[j + 1] and output[i + 2] == c[j + 2] and output[i + 3] == c[
                j + 3] and output[i + 4] == c[j + 4] :
                print("Lock user account after", output[i + 5], "login attempts")
    except :
        print("Please set the Maximun authentication",
              "https://www.linuxtechi.com/lock-user-account-incorrect-login-attempts-linux/")


def BruteForceAttackSSh(hostname, port, password, username="pi") :
    client = paramiko.SSHClient()
    # add to know hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try :
        client.connect(hostname=hostname, port=port, username=username, password=password, timeout=3)
    except socket.timeout :
        # this is when host is unreachable
        print("[!] Host: {hostname} is unreachable, timed out.")
        return False
    except paramiko.AuthenticationException :
        print("[!] Invalid credentials for" ,username, password)
        return False
    except paramiko.SSHException :
        print("[*] Quota exceeded, retrying with delay...")
        # sleep for a minute
        time.sleep(60)
        return BruteForceAttackSSh(hostname, port, password, username)
    else :
        # connection was established successfully
        print("[+] Found combo:\n\tHOSTNAME:",hostname,"\n\tUSERNAME: {username}\n\tPASSWORD: {password}")
        return True


if __name__ == "__main__" :
    DictionaryAttack()
    MaximumAuthentication()
    try :
        string = str(subprocess.check_output("grep 'deny' /etc/ssh/sshd_config", shell=True));
        port = ""
        for i in range(7, len(string) - 3) :
            port += string[i]
    except :
        port = 22
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    userIP = socket.gethostbyname(hostname)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = paramiko.SSHClient()
    passwordlist= open('/home/pi/Desktop/IoT-defender/wordlist').read().splitlines()
    # add to know hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if s.connect_ex((userIP, int(port))) == 0 :
         for password in passwordlist :
             if BruteForceAttackSSh(hostname, int(port), password) :
                 break

