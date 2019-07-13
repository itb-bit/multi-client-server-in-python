# -*- coding: utf-8 -*-

import socket
import select
import msvcrt

def main():
    """
    Add Documentation here
    """
    my_socket = socket.socket()

    my_socket.connect((raw_input("Enter your server ip: ") ,23))
    my_socket.send("c")
    sentes = ""
    while True:
        rlist, wlist, xlist = select.select( [my_socket] ,  [my_socket], [])




        if  msvcrt.kbhit():


            i = msvcrt.getch()
            print i,
            if i == chr(13):
                if sentes=="quit":
                    break
                if len(wlist)>0:
                    my_socket.send(sentes)
                    sentes = ""
                print
            else:
                sentes += i





        if  len(rlist)>0:
            data =my_socket.recv(1024)
            if  data[-5::] == " quit":
                print  data[:-5:]
                break

            print data

    my_socket.close()

if __name__ == '__main__':
    main()