use std::cmp;
use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Should have been able to read the file");

    let contents = contents.split("\n");

    let mut highest_total: i32 = 0;
    let mut current_total = 0;
    for calorie in contents {
        if calorie.eq("") {
            match current_total.cmp(&highest_total) {
                cmp::Ordering::Greater => {
                    highest_total = current_total;
                }
                cmp::Ordering::Less => {}
                cmp::Ordering::Equal => {}
            }
            current_total = 0;
        } else {
            let calorie: i32 = calorie.parse().unwrap();
            current_total = current_total + calorie;
        }
    }
    println!("{highest_total}");
}
