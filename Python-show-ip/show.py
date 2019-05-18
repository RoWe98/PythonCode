import socket
import time

def get_time():
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip       

print ("Current time is：" + get_time())
print ("Your ip is：" + get_host_ip())
