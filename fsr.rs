// Feedback function that XORs all 4 bits together.
fn f(x: u8) -> u8 {
    let bit1 = x >> 3;
    let bit2 = x >> 2 & 0b0001;
    let bit3 = x >> 1 & 0b0001;
    let bit4 = x & 0b0001;
    
    bit1 ^ bit2 ^ bit3 ^ bit4   
}

fn main() {
    // Mock up a 4-bit FSR.
    let mut state: u8 = 0b1100;
    println!("{:b}", state);

    for _i in 0..9 {
        let new_bit = f(state);
        state = state << 1;
        state = state & 0b0000_1111; // Keep 4 bits only.
        state |= new_bit;
        println!("{:04b}", state);
    }
}
