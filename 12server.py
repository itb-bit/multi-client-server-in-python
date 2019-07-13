# -*- coding: utf-8 -*-
import os,socket,select
import time


def send_waiting_messages(wlist): # sending waiting messages, that was received from all the users and the system
    current_time = str(time.localtime(time.time())[3])+":"+str(time.localtime(time.time())[4])+":"+str(time.localtime(time.time())[5])
    for message in messages_to_send:
        (type_m,client_socket, data) = message
        if type_m  ==1:
            client_socket.send(data)
        elif type_m ==2:
            for i in wlist:

                if impo.has_key(str(i)) and i!= client_socket and (impo[str(i)][0]==6 or impo[str(i)][0]==7):

                    i.send(current_time+" "+impo[str(client_socket)][3]+": "+data)
                    impo[str(i)][5].write(current_time+" res from: "+impo[str(client_socket)][3]+" "+data+ ' \n')
        elif type_m ==3:
            for i in wlist:
                if i!= client_socket and (impo[str(i)][0]==6 or impo[str(i)][0]==7):

                    i.send(current_time+" "+impo[str(client_socket)][3]+": "+data)
                    impo[str(i)][5].write(current_time+" res from: "+impo[str(client_socket)][3]+" "+data+ ' \n')
                    print "Connection with "+ impo[str(client_socket)][3] +" closed."
                    impo[str(current_socket)][5].write(current_time + "left the server")
                    impo[str(current_socket)][5].close()
            if  impo[str(current_socket)][0]==5:

                os.remove(where_to_save + "\users_data\\"+impo[str(current_socket)][3]+".txt")
            open_client_sockets.remove(current_socket)
            del impo[str(current_socket)]


        elif  type_m ==4:

            for i in wlist:

                if (impo[str(i)][0]==6 or impo[str(i)][0]==7) and data[5:] == impo[str(i)][3].replace("@",""):

                    i.send(current_time+" "+impo[str(client_socket)][3]+": kicked you quit")
                    impo[str(i)][5].write( current_time+ " was kicked" + ' \n')

                    open_client_sockets.remove(i)
                    impo[str(i)][5].close()
                    del impo[str(i)]
                    messages_to_send.append((2,current_socket,impo[str(current_socket)][3]+ " kicked " +data[5:]))
                    break
        elif type_m ==5:
            for i in wlist:
                if impo[str(i)][0]==6 and data[7:] == impo[str(i)][3].replace("@",""):
                    i.send(current_time+" "+impo[str(client_socket)][3]+": silent you")
                    impo[str(i)][0] =7
                    messages_to_send.append((2,current_socket,impo[str(current_socket)][3]+ " silent " +data[7:]))
                    break




        messages_to_send.remove(message)
def file_find(file,sentense):
    fo = open(file,'a+')
    lines = [line.rstrip('\n') for line in fo]
    return (sentense) in lines!= 0




server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 23))
server_socket.listen(5)
impo = {}
open_client_sockets = []
messages_to_send = []
current_time= str(time.localtime(time.time())[3])+":"+str(time.localtime(time.time())[4])+":"+str(time.localtime(time.time())[5])
where_to_save = (raw_input("Enter where to save the files: "))



while True: # main loop. Receive input from the users, and send to the waiting messages the appropriate response.

    rlist, wlist, xlist = select.select( [server_socket] + open_client_sockets,  open_client_sockets, [])
    for current_socket in rlist:
        if current_socket is server_socket:
            (new_socket, address)= server_socket.accept()
            open_client_sockets.append(new_socket)
            impo[str(new_socket)]= [1,new_socket,address,"i","i","",False]

        else:
            data = current_socket.recv(1024)

            if data == "":
                messages_to_send.append((3,current_socket,"left the server"))

            elif impo[str(current_socket)][0]==1:
                if data == "c":
                    messages_to_send.append((1,current_socket,"sign in or regester"))
                elif data == "sign in":
                    impo[str(current_socket)][0]=2
                    messages_to_send.append((1,current_socket,"enter your user name"))
                elif data == "register":
                    impo[str(current_socket)][0]=3
                    messages_to_send.append((1,current_socket,"enter user name"))
                else:
                    messages_to_send.append((1,current_socket,"sign in or register"))
            elif impo[str(current_socket)][0]==2:
                if os.path.isfile(where_to_save + "\users_data\\"+data.replace("\n","").replace(" ","").replace("\\","").replace("\x08","").replace("/","")+".txt"):
                    impo[str(current_socket)][3] =data.replace("\n","").replace(" ","").replace("\\","").replace("\x08","").replace("/","")
                    impo[str(current_socket)][5] = open(where_to_save + "\users_data\\"+data.replace("\n","").replace(" ","").replace("\\","").replace("\x08","").replace("/","")+".txt",'a+')
                    impo[str(current_socket)][0]=4
                    messages_to_send.append((1,current_socket,"enter your password"))
                else:
                     messages_to_send.append((1,current_socket,"enter your user name"))
            elif impo[str(current_socket)][0]==3:
                if  data[0] != "@" and not os.path.isfile(where_to_save + "\users_data\\"+data.replace("\n","").replace(" ","").replace("\\","").replace("\x08","").replace("/","")+".txt"):
                    impo[str(current_socket)][3] =data.replace("\n","").replace(" ","").replace("\\","").replace("\x08","").replace("/","")
                    impo[str(current_socket)][5] = open(where_to_save + "\users_data\\"+data.replace("\n","").replace(" ","").replace("\\","").replace("\x08","").replace("/","")+".txt",'a+')
                    impo[str(current_socket)][0]=5
                    impo[str(current_socket)][5].write(data.replace("\n","").replace(" ","").replace("\\","").replace("\x08","").replace("/","")+' \n')
                    messages_to_send.append((1,current_socket,"enter password"))
                else:
                    messages_to_send.append((1,current_socket,"enter user name"))
            elif impo[str(current_socket)][0]==4:
                impo[str(current_socket)][5].seek(0, 0)
                print str(impo[str(current_socket)][5].readline()).replace("\n","").replace(" ","").replace("\\","").replace("\x08","").replace("/","")
                if str(impo[str(current_socket)][5].readline()).replace("\n","").replace(" ","").replace("\\","").replace("\x08","").replace("/","")==data.replace("\n","").replace(" ","").replace("\\","").replace("\x08","").replace("/",""):
                    impo[str(current_socket)][0]=6
                    messages_to_send.append((1,current_socket,"you have singed in"))
                    impo[str(current_socket)][5].seek(0, 2)
                    messages_to_send.append((2,current_socket,"joined the server"))
                    impo[str(current_socket)][6]=file_find(where_to_save + "\managers.txt",impo[str(current_socket)][3])
                    if impo[str(current_socket)][6]:
                        impo[str(current_socket)][3]= "@"+impo[str(current_socket)][3]

                else:
                     messages_to_send.append((1,current_socket,"Wrong Password, enter your password"))
            elif impo[str(current_socket)][0]==5:

                impo[str(current_socket)][5].write(data.replace("\n","").replace(" ","").replace("\\","").replace("\x08","").replace("/","")+' \n')

                messages_to_send.append((1,current_socket,"you have register successfully"))
                impo[str(current_socket)][0]=6
                messages_to_send.append((2,current_socket,"joined the server"))
            elif impo[str(current_socket)][0]==6:
                if  impo[str(current_socket)][6] and data[0:4]== "kick":
                    messages_to_send.append((4,current_socket,data.replace("@","")))
                if  impo[str(current_socket)][6] and data[0:6]== "silent":
                    messages_to_send.append((5,current_socket,data.replace("@","")))
                if  impo[str(current_socket)][6] and data[0:11]== "make manger":
                    messages_to_send.append((6,current_socket,data.replace("@","")))
                messages_to_send.append((2,current_socket,data))
                impo[str(current_socket)][5].write(current_time+" send: "+data+' \n')
            elif impo[str(current_socket)][0]==7:

                messages_to_send.append((1,current_socket,"you cant speak you are silent"))


    send_waiting_messages(wlist)


