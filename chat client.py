from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

host = "127.0.0.1"
port = 6700
BUFSIZ = 1024
address = (host, port)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(address)

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            msg_list.insert(tkinter.END, "client left chat")
            break

def send(event=None):

        #while True:
            #message = input("Type message here: ")
            msg = entry_field.get("1.0",'end-1c')
            entry_field.delete("1.0",'end-1c')  # Clears input field.
        #    my_msg.set("")  # Clears input field.
        #    if not message: break
            client_socket.send(bytes(msg, "utf8"))
            if msg == "{quit}":
                client_socket.close()

#ui window
top = tkinter.Tk()
top.title("Chatter [Client Mode]")
top.geometry('{}x{}'.format(400, 400))
my_msg = tkinter.StringVar()
my_msg.set("")
messages_frame = tkinter.Frame(top)

scrollbar = tkinter.Scrollbar(messages_frame)
msg_list = tkinter.Listbox(messages_frame, height=20, width=65, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

#entry_field = tkinter.Entry(top, textvariable=my_msg,width=50)
#entry_field.bind("<Return>", send)
#entry_field.pack()
#send_button = tkinter.Button(top, text="Send", command=send)
#send_button.pack()

# Creating Third For Sending Text Message
#Sending_panel=tkinter.LabelFrame(top, text='Send Text', fg='green', bg='powderblue')
#Sending_panel.pack(side=tkinter.TOP)

#Sending_data=tkinter.Text(Sending_panel,font=('arial 12 italic'), width=35, height=5)
#Sending_data.bind("<Return>", send)
#Sending_data.pack(side=tkinter.LEFT)
#Sending_Trigger=tkinter.Button(Sending_panel, text='Send', width=15, height=5, bg='orange',command=send,activebackground='lightgreen')
#Sending_Trigger.pack(side=tkinter.LEFT)


entry_field =tkinter.Text(top, width=35, height=5)
entry_field.pack(side=tkinter.LEFT)
entry_field.bind("<Return>", send)
entry_field.index(tkinter.INSERT)
send_button=tkinter.Button(top, text='Send', width=15, height=5, bg='orange',command=send ,activebackground='lightgreen')
send_button.pack()

#
receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()
