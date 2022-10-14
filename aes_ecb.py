from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from binascii import hexlify as hexa
from os import urandom

BLOCKLEN = 16
def blocks(data):
    split = [hexa(data[i:i+BLOCKLEN]).decode() for i in range(0, len(data), BLOCKLEN)]
    return " ".join(split)

k = urandom(16)
print("k = {}".format(hexa(k)))

# Create AES-128 cipher for encryption.
cipher = Cipher(algorithms.AES(k), modes.ECB())
aes_encrypt = cipher.encryptor()

# Set plaintext p (two blocks) to null bytes.
p = b'\x00'*BLOCKLEN*2

# Encrypt plaintext p to ciphertext c.
c = aes_encrypt.update(p) + aes_encrypt.finalize()
print("enc({}) = {}".format(blocks(p), blocks(c)))
