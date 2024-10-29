from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

BLOCKLEN = 16
def blocks(data):
    split = [data[i:i+BLOCKLEN].hex() for i in range(0, len(data), BLOCKLEN)]
    return " ".join(split)

k = urandom(16)
print(f"k = {k.hex()}")

# Create AES-128 cipher for encryption.
cipher = Cipher(algorithms.AES(k), modes.ECB())
aes_encrypt = cipher.encryptor()

# Set plaintext p (two blocks) to null bytes.
p = b'\x00'*BLOCKLEN*2

# Encrypt plaintext p to ciphertext c.
c = aes_encrypt.update(p) + aes_encrypt.finalize()
print(f"enc({blocks(p)}) = {blocks(c)}")
