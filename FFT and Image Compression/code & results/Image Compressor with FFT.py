import cv2
import numpy as np
from matplotlib import pyplot as plt

# ------------------------ Compression Functions ------------------------ #

def discard_less_important(img: np.ndarray, threshold) -> np.ndarray:
    """Discard 'threshold'% of small-magnitude coefficients."""
    sorted_coefficients: np.ndarray = np.sort(np.abs(img.flatten()))
    threshold_index = int((threshold / 100.0) * sorted_coefficients.shape[0])
    threshold_value = sorted_coefficients[threshold_index]
    mask = np.abs(img) > threshold_value
    new_coefficients = img * mask
    return new_coefficients

def discard_less_important_multi_channel(img, threshold):
    new_coefficients = np.zeros(img.shape, dtype=np.complex128)
    for channel in range(img.shape[2]):
        new_coefficients[:, :, channel] = discard_less_important(img[:, :, channel], threshold)
    return new_coefficients

# ------------------------ Load and Preprocess Image ------------------------ #

# Load color image in BGR, convert to RGB
image_bgr = cv2.imread('20240323_133304.jpg')
image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
image = image.astype(np.float64)

# Apply FFT to each channel
f_transform = np.zeros(image.shape, dtype=np.complex128)
for c in range(3):
    f_transform[:, :, c] = np.fft.fftshift(np.fft.fft2(image[:, :, c]))

# Show FFT magnitude spectrum of one channel (e.g., Red)
magnitude_spectrum = np.log(np.abs(f_transform[:, :, 0]) + 1)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1), plt.imshow(image.astype(np.uint8))
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('FFT Spectrum (Red Channel)'), plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.savefig("fft_spectrum_comparison.png", dpi=300)
plt.show()

# ------------------------ Compression and Reconstruction ------------------------ #

thresholds = [90, 99, 99.5, 99.9]
compressed_images = [np.clip(image, 0, 255).astype(np.uint8)]
estimated_sizes = []

original_size_mb = image.nbytes / (1024 * 1024)
estimated_sizes.append(original_size_mb)

for threshold_percent in thresholds:
    # Apply compression
    f_compressed = discard_less_important_multi_channel(f_transform, threshold_percent)

    # Estimate storage
    nonzero_coeffs = np.count_nonzero(f_compressed)
    estimated_size_bytes = nonzero_coeffs * 16  
    estimated_size_mb = estimated_size_bytes / (1024 * 1024)
    estimated_sizes.append(estimated_size_mb)

    # Reconstruct image
    img_compressed = np.zeros(image.shape, dtype=np.float64)
    for c in range(3):
        f_ishift = np.fft.ifftshift(f_compressed[:, :, c])
        img_back = np.fft.ifft2(f_ishift)
        img_compressed[:, :, c] = np.abs(img_back)

    img_compressed = np.clip(img_compressed, 0, 255).astype(np.uint8)
    compressed_images.append(img_compressed)

# ------------------------ Plot All Results ------------------------ #

titles = [
    f'Original\n{estimated_sizes[0]:.2f} MB'
] + [
    f'{t}% Discarded\n{sz:.2f} MB' for t, sz in zip(thresholds, estimated_sizes[1:])
]

plt.figure(figsize=(20, 5))
for i, (img, title) in enumerate(zip(compressed_images, titles)):
    plt.subplot(1, 5, i + 1)
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')

plt.tight_layout()
plt.savefig("compressed_image_comparison.png", dpi=300)
plt.show()