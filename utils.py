"""Create a utils.py file which has the following functions:
save_password(entity_name, password)
Takes in an entity name and password and saves it in a file.
The name of the file should in a file named “<entitiy_name>.passwd”
retrieve_password(entity_name)
Retrieves the password for a particular entity for its password file.
If the entitiy’s password file is not found, returns “error”
"""

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