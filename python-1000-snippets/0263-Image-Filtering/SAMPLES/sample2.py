# sample2.py
# Apply a custom convolution kernel (sharpen) using Pillow.

from PIL import Image, ImageFilter


if __name__ == '__main__':
    img = Image.new('RGB', (200, 120), color='lightgreen')

    # Sharpen kernel
    kernel = [
        0, -1, 0,
        -1, 5, -1,
        0, -1, 0,
    ]

    sharpened = img.filter(ImageFilter.Kernel((3, 3), kernel, scale=None, offset=0))
    sharpened.save('filtered_sharpen.png')
    print('Saved sharpened image to filtered_sharpen.png')
