from password_utils import encrypt_password
from cryptography.fernet import Fernet

def generate_key():
    key=Fernet.generate_key()
    with open("secret.key","wb") as f:
        f.write(key)
    print("key saved to secret.key")

if __name__ =="__main__":
    generate_key()
    encrypted=encrypt_password(input("enter password"))
    print("encrypted password:",encrypted)

