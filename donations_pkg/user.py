
def login(database, username, password):

    #if username in database.keys() and password == database[username]:
    if username in database.keys() and password == database[username]:
        print("\n" "Welcome back", username+"!")
        return (username)

    #elif username in database.keys() and database[username] is not password:
    elif username in database.keys() and database[username] != password:
        print("password fail for", username)
        return ""

    else:
        print("\n" "user not found. please register.")
        return ""

def register(database, username):
    if username in database.keys():
        print("\n" "Username already register.")
        return ""
    else:
        print("Username", username, "register!")
        return ""



    
