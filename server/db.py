import sqlite3

def base_struct(connection, cursor):
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER AUTO_INCREMENT,
                                pass_hash TEXT NOT NULL,
                                username TEXT NOT NULL,
                                PRIMARY KEY (id));
                                
                                
                                '''
    cursor.execute(sqlite_create_table_query)


    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS users_messages(
                                    id INTEGER AUTO_INCREMENT,
                                    from_user_id INTEGER NOT NULL,
                                    to_user_id INTEGER NOT NULL,
                                    message_text TEXT,
                                    PRIMARY KEY (id));
                                '''
    cursor.execute(sqlite_create_table_query)
    
    connection.commit()
    

if __name__ == "__main__":
    sqlite_connection = sqlite3.connect('data/db.db')
    cursor = sqlite_connection.cursor()
    base_struct(sqlite_connection, cursor)
    cursor.close()
