**Page 14**: The first equation in the "Achieving Semantically Secure Encryption" section (both PDF and epub, seventh printing):

```math
E(K, R, P) = (DRBG(K\ \ R) \oplus P, R)
```

should probably be:

```math
E(K, R, P) = (DRBG(K || R) \oplus P, R)
```

In other words, the equation shows conspicuous whitespace where we expect either || or , (at least for consistency with rest of section).

**Page 148**: Typo in seventh printing epub (but not in PDF)

"plainte (P)" should be "plaintext (P)"

**Page 159**: Missing "H" term (in seventh printing epub, but not in PDF) in equation that shows:

```math
C_{i}\ \otimes = 1 \otimes H = H
```

should read:

```math
C_{i} \otimes H = 1 \otimes H = H
```

**Page 167**: The sentence that begins "We know for sure that there’s no way to beat the O(2N) complexity" formats the big-O notation as a uppercase "N" subscript.

```math
O(2_{N})
```

This error occurs in the seventh printing epub, but is correct in the PDF. Should be lowercase "n" superscript for correctness (and consistency with the PDF printing).

```math
O(2^{n})
```

**Page 172**: Missing division operator symbol "/" (both epub and PDF) in expression that reads

```math
1/log\sqrt{N} = 1/(n/2) = 2n
```

Should simplify to:

```math
1/log\sqrt{N} = 1/(n/2) = 2/n
```

**Page 175**: Fix modular math expression that reads

*2 × 3 = 1 (because 6 = 1 mod 5)*

Should read:

*2 × 3 = 1 (because 1 = 6 mod 5)*

Needs to be corrected in both epub and PDF.

**Page 175**: Consider clarifying modular math expression that reads

*4 × 4 = 16 = 1 mod 5*

Should probably read:

*4 × 4 = 16 mod 5 = 1*

**Page 182**: Missing word "it" in seventh printing epub (correct in PDF) for sentence that reads

*and call the multiplicative group of integers modulo n*

Should read:

*and call it the multiplicative group of integers modulo n*
