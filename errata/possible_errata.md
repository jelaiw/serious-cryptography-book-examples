**Page 14**: The equation that shows:

```math
E(K, R, P) = (DRBG(K\ \ R) \oplus P, R)
```

should probably read:

```math
E(K, R, P) = (DRBG(K || R) \oplus P, R)
```

At least for the seventh printing, the equation shows conspicuous whitespace where either || or , (at least for consistency with the rest of the text) should probably be.

**Page 148**: Typo in seventh printing epub (but not in PDF)

"plainte (P)" should be "plaintext (P)"

**Page 159**: Missing "H" term in equation that shows:

```math
C_{i}\ \oplus = 1 \oplus H = H
```

should read:

```math
C_{i} \oplus H = 1 \oplus H = H
```

In seventh printing ebug (but not in PDF)
