from os import urandom
from struct import unpack
from Crypto.Cipher import AES
from Crypto.Util import Counter

k = urandom(16)
print(f"k = {k.hex()}")

# Pick a starting value for counter.
nonce = unpack('<Q', urandom(8))[0]
print(nonce)

# Pick an instance of AES in CTR mode, using ctr as counter.
ctr = Counter.new(128, initial_value=nonce)
aes = AES.new(k, AES.MODE_CTR, counter=ctr)

# No need for an entire block with CTR.
p = b'\x00\x01\x02\x03'

# Encrypt plaintext.
c = aes.encrypt(p)
print(f"enc({p.hex()}) = {c.hex()}")

# Decrypt ciphertext (using the encrypt function).
ctr = Counter.new(128, initial_value=nonce)
aes = AES.new(k, AES.MODE_CTR, counter=ctr)
p = aes.encrypt(c)
print(f"enc({c.hex()}) = {p.hex()}")
