
import socket

from psutil import users
import db
import json
import sqlite3
import threading

def reg():
    pass

def login():
    pass

def client_thread(conn):
    while True:
        data = conn.recv(1024)
        if data:
            try:
                raw = json.loads(data.decode("utf-8"))
                if raw["action"] == "auth":
                    users_connected[raw["user_id"]] = conn
                elif raw["action"] == "send":
                    if conn in users_connected.values():
                        message = raw["message"]
                        to_ = raw["to_user"]
                        print(message, "to", to_)
                        if to_ in users_connected:
                            print("Socket active")
                            send_to(json.dumps({"message": message}), users_connected[to_])
            except json.decoder.JSONDecodeError:
                pass

def send_to(data, connection_to_send):
    connection_to_send.send(data.encode("utf-8"))

users_connected = {} #user_id : connection

def main():
    sqlite_connection = sqlite3.connect('data/db.db')
    cursor = sqlite_connection.cursor()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 9091))
    sock.listen()
    print("[LOG] Server started; Waiting for clients")
    while True:
        conn, addr = sock.accept()
        print("[LOG] New client connected")
        threading.Thread(target=client_thread, args=(conn, )).start()
        


if __name__ == "__main__":
    main()
