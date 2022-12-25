from binascii import hexlify as hexa
from os import urandom
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Pick a random 16-byte key using Python's crypto PRNG.
k = urandom(16)
print(f"k = {hexa(k)}")

# Create AES-128 block cipher to encrypt a single block.
cipher = Cipher(algorithms.AES(k), modes.ECB())
aes_encrypt = cipher.encryptor()

# Set plaintext block p to all-zero bytes.
p = b'\x00'*16

# Encrypt plaintext p (to ciphertext c).
c = aes_encrypt.update(p) + aes_encrypt.finalize()
print(f"enc({hexa(p)}) = {hexa(c)}")

# Decrypt ciphertext c to plaintext p.
aes_decrypt = cipher.decryptor()
p = aes_decrypt.update(c) + aes_decrypt.finalize()
print(f"dec({hexa(c)}) = {hexa(p)}")
