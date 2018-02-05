"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

host = '127.0.0.1'
port = 6700
bufSize = 1024
address = (host, port)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(address)
SERVER.listen(10)
print("Server start...")
print("Waiting for connection...")

def handle_incoming_connections():
    """Sets up handling for incoming clients."""

    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        history.insert(tkinter.END,"%s:%s has connected. \n" % client_address)
        Thread(target=handle_client, args=(client,)).start()



def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    while True:

        msg = client.recv(bufSize)
        if msg != bytes("{quit}", "utf8"):
            client.send(bytes("Recieved : ", "utf8")+msg)
            print("recieved : %s" % msg.decode("utf8"))
        else:
            #history.insert(tkinter.END,"%s:%s has disconnected. \n" % client_address)
            #client.send(bytes("client left chat", "utf8"))
            print("client left chat")
            client.close()
            break

#create window
window = tkinter.Tk()
window.title("Connection [Server Mode]")
window.geometry('{}x{}'.format(400, 400))
#connection frame
Connection_info=tkinter.LabelFrame(window, text='Connection Informations', fg='green', bg='powderblue')
Connection_info.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)

#frame ip-address and port
Connect_frame=tkinter.Frame(Connection_info)
Connect_frame.pack(side=tkinter.TOP, padx=10,pady=10)

Ip= tkinter.Label(Connect_frame,text="Ip-address : ", relief="groove", anchor='center', width=15).grid(row=0,column=0, ipadx=10, ipady=5)
Ip = tkinter.Label(Connect_frame, text= host , relief='sunken', anchor='center', width=20).grid(row=0, column=2, ipadx=10, ipady=5)

Port = tkinter.Label(Connect_frame,text="Port : ", relief="groove", anchor='center', width=15).grid(row=1,column=0, ipadx=10, ipady=5)
Port = tkinter.Label(Connect_frame, text= port , relief='sunken', anchor='center', width=20).grid(row=1, column=2, ipadx=10, ipady=5)

#Connection history
history_frame=tkinter.LabelFrame(window, text='Connection history', fg='green', bg='powderblue')
history_frame.pack(side=tkinter.TOP)

history=tkinter.Text(history_frame, font=('arial 12 bold italic'), width=50, height=15)
history.pack()

#Thread
ACCEPT_THREAD = Thread(target=handle_incoming_connections)
ACCEPT_THREAD.start()
window.mainloop()
ACCEPT_THREAD.join()

SERVER.close()
