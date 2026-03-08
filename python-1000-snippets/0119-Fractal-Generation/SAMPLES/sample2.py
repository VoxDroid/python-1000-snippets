# sample2.py
# display deeper triangle and count lines

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
    tri = sierpinski_triangle(3)
    print('depth 3 has', len(tri), 'lines')
    for line in tri:
        print(line)
