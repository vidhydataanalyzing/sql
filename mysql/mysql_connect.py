import mysql.connector
from password_utils import get_decrypted_password

def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=get_decrypted_password(),
            database="test"
        )
        print("Connection established!")
        print(get_decrypted_password())
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    connect_to_mysql()
