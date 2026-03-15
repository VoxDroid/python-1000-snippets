# sample2.py
# Resize, rotate, and crop an image using Pillow.

from PIL import Image


if __name__ == '__main__':
    # Create a base image
    img = Image.new('RGB', (200, 120), color='navy')

    # Resize
    resized = img.resize((100, 60))
    resized.save('image_resized.png')

    # Rotate
    rotated = img.rotate(45, expand=True)
    rotated.save('image_rotated.png')

    # Crop
    cropped = img.crop((20, 20, 180, 100))
    cropped.save('image_cropped.png')

    print('Saved resized, rotated, and cropped images.')
