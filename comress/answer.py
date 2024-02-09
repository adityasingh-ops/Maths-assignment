import numpy as np
from PIL import Image
import hashlib

def load_img(img_path):
    img = Image.open(img_path)
    return np.array(img)

def save_img(img, file_path):
    im = Image.fromarray(np.uint8(img))
    im.save(file_path)

def compress_img(img, comp_ratio):
    if len(img.shape) == 3:
        img_gray = np.mean(img, axis=2)
    else:
        img_gray = img
    
    U, S, Vt = np.linalg.svd(img_gray, full_matrices=False)
    
    k = int(min(img_gray.shape) * comp_ratio)
    U_compressed = U[:, :k]
    S_compressed = np.diag(S[:k])
    Vt_compressed = Vt[:k, :]
    
    compressed_img = np.dot(U_compressed, np.dot(S_compressed, Vt_compressed))
    
    return compressed_img

def add_digital_fingerprint(img_path):
    with open(img_path, 'rb') as f:
        img_data = f.read()
        img_hash = hashlib.sha256(img_data).hexdigest()
    return img_hash

# Example usage:
img_path = "j.png"
comp_ratio = 0.1
img = load_img(img_path)
compressed_img = compress_img(img, comp_ratio)
fingerprint = add_digital_fingerprint(img_path)
compressed_img_with_fingerprint_path = "compressed_img_with_fingerprint.jpg"
save_img(compressed_img, compressed_img_with_fingerprint_path)
print("Digital fingerprint:", fingerprint)