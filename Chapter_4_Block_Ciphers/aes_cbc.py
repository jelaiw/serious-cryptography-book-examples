from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

BLOCKLEN = 16
# Return data as a string, space delimited into blocks of size BLOCKLEN.
# Note, data are passed in as encoded bytes.
def blocks(data):
    split = [data[i:i+BLOCKLEN].hex() for i in range(0, len(data), BLOCKLEN)]
    return " ".join(split)

k = urandom(16)
print(f"k = {k.hex()}")

# Pick a random initial value.
iv = urandom(16)
print(f"iv = {iv.hex()}")

# Create an instance of AES-128 in CBC mode.
aes = Cipher(algorithms.AES128(k), modes.CBC(iv)).encryptor()

# Set plaintext p (two blocks) to all-zero string.
p = b'\x00'*BLOCKLEN*2

# Encrypt plaintext p to ciphertext c.
c = aes.update(p) + aes.finalize()
print(f"enc({blocks(p)}) = {blocks(c)}")

# Pick a different IV with the same key.
iv = urandom(16)
print(f"iv = {iv.hex()}")
aes = Cipher(algorithms.AES(k), modes.CBC(iv)).encryptor()
c = aes.update(p) + aes.finalize()
print(f"enc({blocks(p)}) = {blocks(c)}")
