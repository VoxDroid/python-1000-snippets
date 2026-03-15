# sample1.py
# Apply a built-in blur filter to an image using Pillow.

from PIL import Image, ImageFilter


if __name__ == '__main__':
    img = Image.new('RGB', (200, 120), color='orange')
    blurred = img.filter(ImageFilter.BLUR)
    blurred.save('filtered_blur.png')
    print('Saved blurred image to filtered_blur.png')
