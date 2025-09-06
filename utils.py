import io
import os

def save_password(entity_name, password):
    file = entity_name + ".passwd"
    f = io.open(file, "w")
    print(f"File '{f}' created successfully.")
    f.write(password)
    print(f"Password '{password}' added successfully.")
    f.close()

def retrieve_password(entity_name):
    if os.path.exists(entity_name):
        f = io.open(entity_name, "r")
        content = f.read()
        print(f"Password is {content}.")
        f.close()
        return content
    else:
        print ("Error")