use std::cmp;
use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Should have been able to read the file");

    let contents = contents.split("\n");

    let mut highest_totals: [i32; 3] = [0, 0, 0];
    let mut minimum_highest = 0;
    let mut current_total = 0;
    for calorie in contents {
        if calorie.eq("") {
            minimum_highest = highest_totals.iter().min();
            match current_total.cmp(minimum_highest) {
                cmp::Ordering::Greater => {
                    let mut minimum_position = highest_totals
                        .iter()
                        .position(|&x| x == minimum_highest)
                        .unwrap();
                    //highest_total = current_total;
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
    //println!("{highest_total}");
}
