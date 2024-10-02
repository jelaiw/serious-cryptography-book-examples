fn main() {
    let num_ops: f32 = 1_000_000.0;
    let bits = num_ops.log2();
    println!("Number of operations: {}", num_ops);
    println!("Security level in bits: {}", bits);
}
