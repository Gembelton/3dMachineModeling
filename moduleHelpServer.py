import socket
print("Сервер запущен.")
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
print ('connected:', addr)
helpMessage = (b"Hello!\n"
               b"This program made by Rafael Mirzad.\n"
               b"vk.com/rafisgood/\n\n\n"
               b"P.S.this is the implementation of \n"
               b"the client-server application\n"
               b"\n\n                       22.04.2019")
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(helpMessage)
conn.close()