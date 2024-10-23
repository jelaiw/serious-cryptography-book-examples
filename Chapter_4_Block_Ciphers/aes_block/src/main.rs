use rand::{rngs::OsRng, RngCore};
use aes::Aes128;
use aes::cipher::{
    BlockCipher, BlockEncrypt, BlockDecrypt, KeyInit,
    generic_array::GenericArray,
};

fn main() {
    let mut key = [0u8; 16];
    // https://rust-random.github.io/rand/rand_core/struct.OsRng.html
    // https://stackoverflow.com/q/71048413
    // https://docs.rs/rand/latest/rand/trait.RngCore.html#tymethod.try_fill_bytes
    OsRng.try_fill_bytes(&mut key).unwrap();
    println!("key is {:?}", key);

    // https://docs.rs/aes/latest/aes/#examples
    let plaintext = GenericArray::from([0u8; 16]);
    println!("plaintext is {:?}", plaintext);

    let mut block = plaintext.clone();

    let cipher = Aes128::new(&GenericArray::from(key));

    // https://docs.rs/cipher/0.4.4/cipher/trait.BlockEncrypt.html#method.encrypt_block.
    // Encrypt a single block in place.
    cipher.encrypt_block(&mut block);
    println!("ciphertext is {:?}", block);

    cipher.decrypt_block(&mut block);
    assert_eq!(plaintext, block);
    println!("decrypted ciphertext is {:?}", block);
}
