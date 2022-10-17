#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2022 Summer)
# Michiharu Takemoto (takemoto.development@gmail.com)
#
# 2022/05/13
# Socket Client WITH BLANK

import sys
import json

#SERVER = 'localhost'
SERVER = '127.0.0.1'
WAITING_PORT = 8765
WAIT_INTERVAL = 5
PIN = "D4"

def client_test(hostname_v1=SERVER, waiting_port_v1=WAITING_PORT):
    import socket
    import time

    node_s = hostname_v1
    port_s = waiting_port_v1

    try:
        count = 0
        while True:

            # socoket for receiving and sending data
            # AF_INET     : IPv4
            # SOCK_STREAM : TCP
            socket_r_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_r_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            print("node_s:", node_s,  " port_s:", str(port_s))
            socket_r_s.connect((node_s, port_s))
            print('Connecting to the server. '
                  + 'node: ' + node_s + '  '
                  + 'port: ' + str(port_s))
            dht11Data = True,20,30
            data_s_list = [{"tempe_dht_1": dht11Data[1], "humid_dht_1":dht11Data[2]}]
            data_s_json = json.dumps(data_s_list)
            # data_s = bytes(data_s_str, encoding = 'utf-8')
            data_s = data_s_json.encode('utf-8')
            socket_r_s.send(data_s)

            socket_r_s.close()

            time.sleep(WAIT_INTERVAL)

            count = count + 1
            if count > 10:
                break

    except KeyboardInterrupt:
        print("Ctrl-C is hit!")
        print("End of this client.")


if __name__ == '__main__':
    print("Start if __name__ == '__main__'")

    sys_argc = len(sys.argv)
    count = 1
    hostname_v = SERVER
    waiting_port_v = WAITING_PORT

    while True:
        print(count, "/", sys_argc)
        if(count >= sys_argc):
            break

        option_key = sys.argv[count]
        #print(option_key)
        if ("-h" == option_key):
            count = count + 1
            hostname_v = sys.argv[count]
            #print(option_key, hostname_v)
        if ("-p" == option_key):
            count = count + 1
            waiting_port_v = int(sys.argv[count])
            #print(option_key, port_v)

        count = count + 1

    print(hostname_v)
    print(waiting_port_v)

    client_test(hostname_v, waiting_port_v)
