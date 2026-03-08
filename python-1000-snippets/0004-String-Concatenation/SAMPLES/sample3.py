# sample3.py
# demonstrate concatenating file paths safely

import os

def main():
    base = "/home/user"
    folder = "documents"
    filename = "notes.txt"
    path = os.path.join(base, folder, filename)
    print("Full path:", path)
    # show manual concatenation (not recommended)
    manual = base + "/" + folder + "/" + filename
    print("Manual path:", manual)

if __name__ == '__main__':
    main()

