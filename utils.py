import io
import os
import reversy

def save_password(entity_name, password):
    file = entity_name + ".passwd"
    f = io.open(file, "w")
    print(f"File '{f}' created successfully.")
    f.write(password)
    print("Password added successfully.")
    f.close()
    encrypted_password = reversy.encrypt(password)
    print(encrypted_password)

def retrieve_password(entity_name):
    if os.path.exists(entity_name):
        f = io.open(entity_name, "r")
        content = f.read()
        print(f"Password is {content}.")
        f.close()
        decrypted_password = reversy.decrypt(content)
        print(decrypted_password)
        return decrypted_password
    else:
        print ("Error")