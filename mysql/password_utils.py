from cryptography.fernet import Fernet


class Fakestr(str):
    def __str__(self):
        return "*****"
    def __repr__(self):
        return "*****"

def load_key():
    return open("secret.key","rb").read()

def encrypt_password(password):
    key=load_key()
    f=Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(encrypt_password):
    key=load_key()
    f=Fernet(key)
    decrypted=f.decrypt(encrypt_password).decode()
    return Fakestr(decrypted)

def get_decrypted_password():
    encrypted_password = b'gAAAAABo4AB3Ii0Mrh2Ucl5mViktoP4GnBrscfvWIfXy2-PK-99K-n5hL_xPKXBMSf7Oh00K7XAHp-awtjRzDZYbX9cXW742dg=='
    return decrypt_password(encrypted_password)
