Page 14: The equation that shows:

E(K, R, P) = (DRBG(K  R) XOR P, R)

should read:

E(K, R, P) = (DRBG(K || R) XOR P, R)
