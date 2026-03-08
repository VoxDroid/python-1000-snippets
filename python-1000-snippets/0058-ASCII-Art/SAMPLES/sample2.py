# sample2.py
# Ask user for tree height and draw dynamically

from math import floor

def make_tree(height=4):
    art = []
    for i in range(height):
        spaces = ' ' * (height - i)
        leaves = '/' + ' ' * (2*i) + '\\'
        art.append(spaces + leaves)
    art.append('/' + '_' * (2*height) + '\\')
    art.append(' ' * (height-1) + '||||')
    art.append(' ' * (height-1) + '||||')
    return "\n".join(art)

if __name__ == '__main__':
    h = int(input('Height: '))
    print(make_tree(h))
