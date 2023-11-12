#!/usr/bin/python3
#-------------------------------------------------------------------------------------------------------------------
#Write a Python code that can handle the following Login system
#|-------------------------------------------------------|
#| username                 | Password                   |
#|-------------------------------------------------------|
#| Ahmed                    | 1394                       |
#| Ali                      | 6078                       |
#| Amr                      | 9345                       |
#|-------------------------------------------------------|
#If the data entered is correct, the system shall show a welcome message if not the system will print wrong entry
#-------------------------------------------------------------------------------------------------------------------
database={
    "Ahmed":1394,
    "Ali":6078,
    "Amr":9345
}
username=input("Enter your username: ")
password=input("Enter your password: ")
if username in database and database[username] == int(password):
    print("successful login")
elif username not in database:
     print("incorrect username")
elif username in database and database[username] != int(password): 
     print("incorrect password")
#-------------------------------------------------------------------------------------------------------------------