import os
def dataenc():
    f = os.popen('blkid /dev/sda1')
    n = f.read
    flag=0
    for s in f:
        for word in s.split():
            if word=='TYPE="crypto_LUKS"':
                print('Your Data is Encrypted')
                flag=1

    if flag==0:
        print('Your Data is not encrypted')
            


