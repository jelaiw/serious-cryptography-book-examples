fn main() {
    assert!(0b0000_1111 << 1 == 0b0001_1110);
    assert!(0b0001_1110 << 1 == 0b0011_1100);
    assert!(0b0011_1100 << 1 == 0b0111_1000);
}
