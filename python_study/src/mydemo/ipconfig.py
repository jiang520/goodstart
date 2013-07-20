
# given ip and subnet_mask, find neighbor in the same subnet

def ipToInt(ip):
    ip_items = ip.split('.')

    ip_int = 0
    for item in ip_items:
        ip_int = ip_int * 256 + int(item)
    return ip_int

def intToIp(ip_int):
    ip_items = ['0','0','0','0']
    for i in range(0,4):
        ip_items[3-i] = str(ip_int % 256)
        ip_int = int((int(ip_int) - int(ip_items[3-i])) / 256) 

    seq = '.'
    ip = seq.join(ip_items)

    return ip

ip = '192.168.1.1'
sm = '255.255.255.128'

ip_int = ipToInt(ip)
sm_int = ipToInt(sm)

total = 256 ** 4

subnet_int = total - sm_int
net_int = int(ip_int / subnet_int) * subnet_int

neibor_ip = []
for i in range(1,subnet_int - 1):
    neibor_int = net_int + i
    neibor_ip.append(intToIp(neibor_int))
print(neibor_ip)
