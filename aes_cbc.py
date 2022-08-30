from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from binascii import hexlify as hexa
from os import urandom

BLOCKLEN = 16
def blocks(data):
    split = [hexa(data[i:i+BLOCKLEN]).decode() for i in range(0, len(data), BLOCKLEN)]
    return " ".join(split)

k = urandom(16)
print("k = {}".format(hexa(k)))

# Pick a random initial value.
iv = urandom(16)
print("iv = {}".format(hexa(iv)))

# Create an instance of AES-128 in CBC mode.
aes = Cipher(algorithms.AES(k), modes.CBC(iv)).encryptor()

# Set plaintext p (two blocks) to all-zero string.
p = '\x00'*BLOCKLEN*2
p = p.encode()

# Encrypt plaintext p to ciphertext c.
c = aes.update(p) + aes.finalize()
print("enc({}) = {}".format(blocks(p), blocks(c)))

# Pick a different IV with the same key.
iv = urandom(16)
print("iv = {}".format(hexa(iv)))
aes = Cipher(algorithms.AES(k), modes.CBC(iv)).encryptor()
c = aes.update(p) + aes.finalize()
print("enc({}) = {}".format(blocks(p), blocks(c)))
