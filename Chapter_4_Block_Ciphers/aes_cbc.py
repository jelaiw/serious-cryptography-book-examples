from binascii import hexlify as hexa
from os import urandom
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

BLOCKLEN = 16
# Return data as a string, space delimited into blocks of size BLOCKLEN.
# Note, data are passed in as encoded bytes.
# See https://docs.python.org/3/library/binascii.html#binascii.hexlify.
def blocks(data):
    split = [hexa(data[i:i+BLOCKLEN]).decode() for i in range(0, len(data), BLOCKLEN)]
    return " ".join(split)

k = urandom(16)
print(f"k = {hexa(k)}")

# Pick a random initial value.
iv = urandom(16)
print(f"iv = {hexa(iv)}")

# Create an instance of AES-128 in CBC mode.
aes = Cipher(algorithms.AES(k), modes.CBC(iv)).encryptor()

# Set plaintext p (two blocks) to all-zero string.
p = b'\x00'*BLOCKLEN*2

# Encrypt plaintext p to ciphertext c.
c = aes.update(p) + aes.finalize()
print(f"enc({blocks(p)}) = {blocks(c)}")

# Pick a different IV with the same key.
iv = urandom(16)
print(f"iv = {hexa(iv)}")
aes = Cipher(algorithms.AES(k), modes.CBC(iv)).encryptor()
c = aes.update(p) + aes.finalize()
print(f"enc({blocks(p)}) = {blocks(c)}")
