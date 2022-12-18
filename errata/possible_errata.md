Page 14: The equation that shows:

```math
E(K, R, P) = (DRBG(K\ \ R) \oplus P, R)
```

should probably read:

```math
E(K, R, P) = (DRBG(K || R) \oplus P, R)
```

At least for the seventh printing, the equation shows conspicuous whitespace where either || or , (at least for consistency with the rest of the text) should probably be.
