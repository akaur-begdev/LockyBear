
def encrypt (data):
    reversed_data = "$$" + data[::-1] + "$$"
    print(reversed_data)
    return reversed_data

def decrypt (encrypted_data):
    reverse = encrypted_data[::-1]
    print (reverse)
    remove = "$"
    new_reverse = reverse.replace(remove,"")
    print(new_reverse)
    return new_reverse



