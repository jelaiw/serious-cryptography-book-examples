from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import hexlify as hexa
from os import urandom
from struct import unpack

k = urandom(16)
print("k = {}".format(hexa(k)))

# Pick a starting value for counter.
nonce = unpack('<Q', urandom(8))[0]
print(nonce)

# Pick an instance of AES in CTR mode, using ctr as counter.
ctr = Counter.new(128, initial_value=nonce)
aes = AES.new(k, AES.MODE_CTR, counter=ctr)

# No need for an entire block with CTR.
p = '\x00\x01\x02\x03'
p = p.encode()

# Encrypt plaintext.
c = aes.encrypt(p)
print("enc({}) = {}".format(hexa(p), hexa(c)))

# Decrypt ciphertext (using the encrypt function).
ctr = Counter.new(128, initial_value=nonce)
aes = AES.new(k, AES.MODE_CTR, counter=ctr)
p = aes.encrypt(c)
print("enc({}) = {}".format(hexa(c), hexa(p)))
