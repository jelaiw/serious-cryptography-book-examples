"If you know approximately how many operations it takes to break a cipher, you can determine its security level in bits by taking the binary logarithm of the number of operations" (Aumasson 2017).

If it takes $1,000,000$ operations, then the security level is $log_2 (1000000)$ or about $20$ bits.

```sh
$ rustc bit_security.rs && ./bit_security 
Number of operations: 1000000
Security level in bits: 19.931568
$
```
