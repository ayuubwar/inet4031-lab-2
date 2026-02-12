def main():
    import os
    print("Python is running from:", os.getcwd())

    #open the user list file
    try:
        userFile = open("list-of-users.txt", "r")
    except:
        print("\nCould not read the file specified.\n")
        exit()

    #load the lines of the file into a list
    listOfUsers = userFile.readlines()
    print("\nlist-of-users was read.")

    #ask the user to proceed
    answer = input("\nDo you want to print out the list of users? (Y or N)")

    if answer == "Y" or answer == "y":
        for userline in listOfUsers:
            print("\n", userline)
    else:
        print("\nOk not printing, ending program.")

    print("\nEnd of User Processing\n")


main()




