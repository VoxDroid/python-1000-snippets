# sample3.py
# Convert an image to grayscale and compute a simple histogram.

from PIL import Image
import numpy as np


if __name__ == '__main__':
    img = Image.new('RGB', (200, 120), color='teal')
    gray = img.convert('L')
    gray.save('image_grayscale.png')

    arr = np.array(gray)
    hist, bins = np.histogram(arr.flatten(), bins=16, range=(0, 255))

    print('Grayscale image saved as image_grayscale.png')
    print('Histogram bins:', hist.tolist())
