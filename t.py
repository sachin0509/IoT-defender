from prettytable import PrettyTable
table=PrettyTable()
table.title="Data Encryption"
def dataenc():
    f = os.popen('blkid /dev/sda1')
    n = f.read
    flag = 0
    for s in f:
        for word in s.split():
            if word == 'TYPE="crypto_LUKS"':
                x.add_row(["Your Data is Encrypted"])
                flag = 1

    if flag == 0:
        x.add_row(["Your Data is Encrypted"])
print(table)
