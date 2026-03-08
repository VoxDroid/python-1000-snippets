# sample1.py
# print a small Sierpinski triangle

def sierpinski_triangle(n):
    if n == 0:
        return ["*"]
    smaller = sierpinski_triangle(n-1)
    size = len(smaller)
    result = []
    for line in smaller:
        result.append(" " * size + line + " " * size)
    for line in smaller:
        result.append(line + " " + line)
    return result

if __name__ == '__main__':
    for line in sierpinski_triangle(2):
        print(line)
