import socket
import json
import threading
import sys

stopping = False
chat_with = -1
this_user_id = int(sys.argv[1])
def send_message(message, to_user, sock): 
    if message:
        result = json.dumps({"action": "send",
                                                "message": message,
                                                "to_user": to_user})

        sock.send(result.encode("utf-8"))

def upload_open_key(key):
    pass

def refresh(sock):
    global stopping
    while not stopping:
        data = sock.recv(1024)
        if data:
            raw = json.loads(data.decode("utf-8"))
            print(raw["message"])

        

def main():
    global stopping, chat_with
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.connect(('localhost', 9091)) 
    print("[LOG] Connected")
    #Auth
    sock.send(json.dumps({"action": "auth", "user_id" : this_user_id}).encode("utf-8"))
    threading.Thread(target=refresh, args=(sock, )).start()
    if chat_with == -1:
        chat_with = int(input("Введите id пользователя с которым хотите переписываться: "))
    cmd = input(f"To {chat_with}>>>")
    while cmd != "/exit":
        send_message(cmd, chat_with, sock)
        cmd = input(f"To {chat_with}>>")

        
       
    stopping = True
    sock.close()



if __name__ == "__main__":
    main()
