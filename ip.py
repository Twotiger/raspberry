#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
import logging
import threading

socket.setdefaulttimeout(3)
logging.basicConfig(level=logging.DEBUG,  
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def scan_port(ip, port):
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=s.connect_ex((ip,port))
        t = s.recv(1024)
        if t:
            logging.debug(t)
            logging.info(ip)

        s.close()
    except Exception as e:
        # print 'ERROR %s' %e
        pass


if __name__ == '__main__':

    # input_ip = raw_input('input ip')
    input_ip = sys.argv[1]
    temp_ip = '.'.join(input_ip.split('.')[:-1]) + '.{0}'

    for i in range(1, 255):
        ip = temp_ip.format(i)
        port = 22
        t = threading.Thread(target=scan_port, args=(ip, port))
        t.start()


