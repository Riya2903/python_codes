
from cryptography.fernet import Fernet

       
key = Fernet.generate_key()
fernet = Fernet(key)

def encrypt(message):


    encMessage = fernet.encrypt(message.encode())
    print("message: ",encMessage)
    print("key: ",key)

    decMessage = fernet.decrypt(encMessage).decode()

    print("decrypted string: ", decMessage)


def Main():
    choice = input("Would you like to (E)ncrypt :")
    if choice == 'E' or choice == 'e':
        print("please enter your message")
        message = str(input())
        
        encrypt(message)
        print("Done.")
        

    else:
        print("No Option selected, closing…")

if __name__ == '__main__':
    Main()

        
