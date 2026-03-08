# sample3.py
# compute approximate size and height for various depths

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
    for d in range(1,5):
        tri = sierpinski_triangle(d)
        print('depth', d, 'height', len(tri))
