"""
Author: B. Hedges
Date: 2024-06-12
Version: 1.0
Description: Program containes one function used to retreive variables stored in the config
file. This program is designed to save space but is technically an unnecessary extra step.
"""
import CredentialManager as CM
import configparser
import sys
import os

def Get_Config():
    #Assert that config exists
    if  os.path.isfile(os.path.join(sys.path[0],"config.ini")):
        return configparser.ConfigParser().read(os.path.join(sys.path[0],"config.ini"))
    else:
        raise Exception("config.ini does not exist in root directory")

def Get_Value(value):
    config = Get_Config()
    #Assert that value is not None
    if value is None:
        raise Exception("Missing value in Get_Config call (ConfigParser.Get_Config)")

def main():
    print("this only exists for testing purpopses numbnuts")

if __name__ == "__main__":
    main()
