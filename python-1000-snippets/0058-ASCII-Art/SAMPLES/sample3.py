# sample3.py
# Build a pyramid shape using loops

if __name__ == '__main__':
    height = 5
    for i in range(height):
        print(' '*(height-i-1) + '*'*(2*i+1))
