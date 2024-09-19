fn main() {
    let plaintext: u8 = 0b0110_1101;
    let key: u8 = 0b1011_0100;

    let ciphertext = plaintext ^ key;
    println!("C = P ⨁ K = {:08b} ⨁ {:b} = {:b}", plaintext, key, ciphertext);

    assert_eq!(ciphertext ^ key, plaintext);
}
