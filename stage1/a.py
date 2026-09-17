from PIL import Image
import numpy as np
import os

print("[*] Splitting Orange.png into two XOR shares...")

# 1. Load the original Orange.png (which already contains the hidden LSB URL)
img_array = np.array(Image.open("Orange.png"))

# 2. Generate a "Key" image made of completely random pixels of the exact same size
key_array = np.random.randint(0, 256, img_array.shape, dtype=np.uint8)

# 3. XOR the original image with the key to create the "Share" image
share_array = np.bitwise_xor(img_array, key_array)

# 4. Save both images
Image.fromarray(key_array).save("Image_A.png")
Image.fromarray(share_array).save("Image_B.png")

print("[+] Created Image_A.png and Image_B.png.")
print("[+] Give these two files to the solvers. You can now delete Orange.png.")
