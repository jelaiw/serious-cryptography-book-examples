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

**Page 159**: Missing "H" term (in seventh printing epub, but not in PDF) in equation that shows:

```math
C_{i}\ \otimes = 1 \otimes H = H
```

should read:

```math
C_{i} \otimes H = 1 \otimes H = H
```

**Page 167**: The sentence that reads "We know for sure that there’s no way to beat the O(2N) complexity" (in the seventh printing epub, correct in PDF) formats the big-O notation as a uppercase "N" subscript.

Should be lowercase "n" superscript for correctness (and consistency with the PDF printing).
