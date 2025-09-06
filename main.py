import utils

print (" Welcome to LockyBear! I am going to help you manage passwords! 🐻")

task = input("What would you like to do? (save password or retrieve password)?")

if task == "save password":
    entity_name = input ("What entity are you saving the password for?")
    password = input ("What is the password for this?")
    utils.save_password(entity_name, password)
    print(f"The password for {entity_name} is saved." )

if task == "retrieve password":
    entity_name = input ("What entity are you retrieving the password for?")
    file = entity_name + ".passwd"
    print(file)
    retrieved_password = utils.retrieve_password(file)
    print(f"The password for {entity_name} is {retrieved_password}." )


