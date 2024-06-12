"""
Author: B. Hedges
Date: 2024-06-11
Version: 1.0
Description: Program designed around saving credentials in windows credential locker.
Saving credentials in the WCL has the benefit of ensuring credentails are saved securly
without the need for storing in environment variables.
"""
import keyring
import getpass

def main():
    terminalEntry = input("Enter new credentials (Y/N): ")
    if terminalEntry.upper() == "Y":
        Create_Creds()
    else:
        terminalEntry = input("Delete existing  credentials (Y/N): ")
        if terminalEntry.upper() == "Y":
            Delete_Creds()
        else:
            terminalEntry = input("Update existing  credentials (Y/N): ")
            if terminalEntry.upper() == "Y":
                Update_Creds()

    print("Credential Manager Closing")

def Create_Creds():
    serviceName = input("Enter Service Name: ")
    userName = input("Enter User Name: ")
    password = getpass.getpass(prompt="Enter Password: ", stream=None)
    keyring.set_password(serviceName,userName,password)
    print("Credentials Saved!")
    return

def Delete_Creds():
    serviceName = input("Enter Service Name: ")
    userName = input("Enter User Name: ")
    keyring.delete_password(serviceName,userName)
    print("Password Deleted")
    return

def Update_Creds():
    serviceName = input("Enter Service Name: ")
    userName = input("Enter User Name: ")
    keyring.delete_password(serviceName,userName)
    password = getpass.getpass(prompt="Enter Password: ", stream=None)
    keyring.set_password(serviceName,userName,password)
    print("Password Updated")
    return

def Remote_Creds(serviceName,userName):
    serviceName = input("Enter Service Name: ")
    userName = input("Enter User Name: ")
    password = getpass.getpass(prompt="Enter Password: ", stream=None)
    keyring.set_password(serviceName,userName,password)
    return userName,Get_Password(serviceName,userName)

def Get_Password(serviceName,userName):
     return keyring.get_password(serviceName,userName)

if __name__=="__main__":
    main()
