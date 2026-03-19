# sample3.py
# Connected component labeling for a binary segmentation mask.

import numpy as np
from collections import deque


def make_blob_mask(shape=(80, 120)) -> np.ndarray:
    mask = np.zeros(shape, dtype=np.uint8)
    mask[10:40, 10:40] = 1
    mask[20:60, 60:90] = 1
    mask[50:70, 30:80] = 1
    return mask


def connected_components(mask: np.ndarray) -> np.ndarray:
    """Label connected components (4-connectivity) in a binary mask."""
    h, w = mask.shape
    labels = np.zeros_like(mask, dtype=np.int32)
    label = 0

    for i in range(h):
        for j in range(w):
            if mask[i, j] == 0 or labels[i, j] != 0:
                continue
            label += 1
            queue = deque([(i, j)])
            labels[i, j] = label
            while queue:
                y, x = queue.popleft()
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < h and 0 <= nx < w:
                        if mask[ny, nx] and labels[ny, nx] == 0:
                            labels[ny, nx] = label
                            queue.append((ny, nx))
    return labels


def main() -> None:
    mask = make_blob_mask()
    labels = connected_components(mask)
    unique_labels = np.unique(labels)

    print("Binary mask shape:", mask.shape)
    print("Number of connected components:", len(unique_labels) - (1 if 0 in unique_labels else 0))
    print("Label counts:")
    for lab in unique_labels:
        if lab == 0:
            continue
        print(f"  component {lab}:", int((labels == lab).sum()), "pixels")


if __name__ == "__main__":
    main()
