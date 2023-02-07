
#import show_homepage function
from optparse import Option, Values
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register 


#Declare a variable database and assign as its value a datat structure that holds a single key:value pair, with a key of "admin" and a password of "password123".

database = {"admin", "password123"}
donations= []
autholized_user = ""

show_homepage()
if autholized_user == "":
    print("You must be logged in to donate.")
else:
    print("Logged in as.", autholized_user)
     
    

while True:

    show_homepage()
    database = {"admin": "password123"}
   
    option = input("Choose option: ")
    if option =="1" or option.lower == "login":
        username = input("Enter username: ")
        password = input("Enter password: ")
        autholized_user = login(database, username,password)
    if login == database:
        print("Logged in as", autholized_user)

               
    elif option =="2" or option.lower == "register":
        
        username = input("Enter username: ")
        password = input("Enter password: ")
        autholized_user = register(database, username) 

    
    elif option =="3" or option.lower == "donate":
        
        if autholized_user == "":
            print("You are not logged in." )
            donation_string = donate(autholized_user)
            donations.append(donation_string)


    elif option =="4" or option.lower == "show_donations":
        show_donations(donations)
       
        










    