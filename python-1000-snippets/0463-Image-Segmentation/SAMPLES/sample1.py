# sample1.py
# Simple image segmentation via thresholding on a synthetic image.

import numpy as np


def make_synthetic_image(shape=(100, 150)) -> np.ndarray:
    # Create an image with two rectangles of different intensity.
    img = np.zeros(shape, dtype=np.uint8)
    img[10:60, 10:70] = 100
    img[40:90, 80:140] = 200
    return img


def segment_by_threshold(image: np.ndarray, threshold: int) -> np.ndarray:
    return (image > threshold).astype(np.uint8)


def main() -> None:
    img = make_synthetic_image()
    mask = segment_by_threshold(img, threshold=128)

    print("Image shape:", img.shape)
    print("Unique intensities in image:", np.unique(img))
    print("Threshold mask unique values:", np.unique(mask))
    print("Foreground pixel count:", int(mask.sum()))


if __name__ == "__main__":
    main()
