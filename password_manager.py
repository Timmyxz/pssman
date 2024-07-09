#Password Manager





import json
import getpass
from cryptography.fernet import Fernet
import pyperclip


def generate_key():
    return Fernet.generate_key()

def encrpyt_data(key, data):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()


def decrypt_data(key, encrpyted_data):
    fernet = Fernet(key)
    return fernet.decrypt(encrpyted_data.encode()).decode()


def save_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)
        
        
def load_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        return {}
    

def main():
        key = generate_key()
        
        passwords = load_file('password.json')
        
        
        
        while True:
            print('/n1. Add a new password')
            print('2. Retrieve a passwprd')
            print('3. Exit')
            choice = input('Enter your choice(1/2/3): ')
            
            
            if choice == '1':
                website = input('Enter the website name: ')
                username = input('Enter your username: ')
                password = getpass.getpass('Enter your password: ')
                
                
                encrypted_password = encrpyt_data(key, password)
                passwords[website] = {"username": username, "password": encrypted_password}
                save_file("passwords.json", passwords)
                print(f"Password for {website} saved successfully!")
            
            elif choice == '2':
                website = input('Enter the website name:')
                if website in passwords:
                   decrypted_password = decrypt_data(key, passwords[website]['password'])
                   print(f'Username: {passwords[website]['username']}')  
                   print(f'Password: {decrypted_password}')
                   pyperclip.copy(decrypted_password)
                else:
                    print(f'No password found for {website}')
                    
                    
                    
            elif choice == '3':                 
                print('Exiting the password manager!')
                break
            
           
                                  
if __name__ == "__main__":
    main()       
       
            
            
   