def show_homepage():

    print("      === DonateMe Homepage ===      ")

    print("-----------------------------------------------")
    print("| 1.      Login      | 2.      Register       |")
    print("-----------------------------------------------")
    print("| 3.      Donate     | 4.      Show Donations |")
    print("-----------------------------------------------")
    print("|               5.   Exit                     |")
    print("-----------------------------------------------")

    

def donate(username):
   
    donation_amt = input("Enter amount to donate: ")
    donation_string = (donation_amt, "Bob donated $1000.0")

    print("Thank you for your donation", username)
    return donation_string

def show_donations(donations):
    print("")
    print("      === All donations ===      ")

    print("Currently, there are no donations.")

    for i in donations:
        print(i) 
     
