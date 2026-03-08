# sample3.py
# read hidden password input and check length

import getpass

def main():
    pwd = getpass.getpass("Enter password: ")
    if len(pwd) < 8:
        print("Password too short!")
    else:
        print("Password accepted.")

if __name__ == '__main__':
    main()

