# Import Time
import time
import fileinput
# Welcome Message
print("WELCOME TO CONTACT BOOK MADE BY KUSH")
print("===================================")
# Sleep for 1 second
time.sleep(1)
# Print Instruction Stuff
print("---------------INSTRUCTIONS-------------------")
print("\n Add : to add a new contact in the book.")
print(" Show : to show all the contacts present in the book.")
print(" Exit : to exit the program")

# Function to Check whether the input is "y" or "Y" if so then it will return True else False


def exitChoice():
    # Ask the user to enter the choice
    exit = input("Done! Do you want to exit the program now? y/n : ")
    # If the user enters "y" or "Y" then return True else False
    if exit.lower() == "y":
        return True
    else:
        return False

def showFile():
        with open("/storage/emulated/0/Download/Learning Python/contacts.txt") as f:
            content = f.read()
            print(f"{content}")                              
                                       
 # Program Main loop keep running it until the user wants to exit the program
while True:
    # Ask the user to enter the choice
    choice = input("\nPlease Enter Your choice: ")
    # If the user wants to add a new contact
    if choice.lower() == "add":
        # Ask the user to enter the name of the contact
        name = input("Please Enter the Persons Name: ")
        # Ask the user to enter the phone number of the contact
        number = input("Now Please Enter the persons Mobile Number: ")
        # Open the file in append mode
        with open("/storage/emulated/0/Download/Learning Python/contacts.txt", "a") as f:
            # Write the name and number in the file
            f.write(f"\n{name}   {number}")
        # successfully added the contact
        print("Success!")
        # Ask if the user wants to exit the program if yes then exit the program
        if exitChoice():            
            break
    elif choice.lower() == "show":
             print("The Contacts Present In the Book are :")
             time.sleep(1)
             showFile()
             if exitChoice():
                 break
    elif choice.lower() == "exit":
         print("Okay, exiting the program..")
         time.sleep(1)
         break
    else:
     print(f"Sorry, There is no option named '{choice}' ")


     
     
     
