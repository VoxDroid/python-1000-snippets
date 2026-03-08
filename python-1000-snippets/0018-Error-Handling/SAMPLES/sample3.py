# sample3.py
# Use finally to ensure cleanup.

def main():
    f = None
    try:
        f = open("tempfile.txt", "w")
        f.write("data")
    except Exception as e:
        print("Error writing file", e)
    finally:
        if f:
            f.close()
            print("File closed")

if __name__ == '__main__':
    main()

