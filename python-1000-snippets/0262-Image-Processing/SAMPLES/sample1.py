# sample1.py
# Create a simple image using Pillow and save it to disk.

from PIL import Image, ImageDraw


if __name__ == '__main__':
    img = Image.new('RGB', (200, 120), color='skyblue')
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), 'Hello, Image!', fill='black')
    img_path = 'image_processing_output.png'
    img.save(img_path)
    print('Saved image to', img_path)
