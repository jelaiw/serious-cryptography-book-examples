use rand::{rngs::OsRng, RngCore};

fn main() {
    let mut key = [0u8; 16];
    // https://rust-random.github.io/rand/rand_core/struct.OsRng.html
    // https://stackoverflow.com/q/71048413
    // https://docs.rs/rand/latest/rand/trait.RngCore.html#tymethod.try_fill_bytes
    OsRng.try_fill_bytes(&mut key).unwrap();

    println!("{:?}", key);
}
