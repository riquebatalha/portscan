import socket

ports = [21,22,25,80,443,445,3306]
print("--------\PORT SCAN/--------")
for port in ports:
    client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)
    code = client.connect_ex(("baconcn.com", port))
    # CODE 0 SIGNIFICA QUE ESTÁ ABERTA, CASO CONTRÁRIO, ESTÁ FECHADA.
    if code == 0:
        print("Porta {} OPEN   | CODE: {}".format(port, code))
    else:
        print("Porta {} CLOSE  | CODE: {}".format(port, code))
print("Created by riquebatalha")