// A robot has been given a list of movement instructions. Each instruction
// is either left, right, up or down, followed by a distance to move. The
// robot starts at 0, 0. You want to calculate where the robot will end up
// and return its final position as a list. For example, if the robot is given
// the instructions ["right 10", "up 50", "left 30", "down 10"], it will end
// up 20 left and 40 up from where it started, so you should return [-20, 40].

fn mr_roboto(instructions: &[&str]) -> (i32, i32) {
    // At its core this implementation is doing almost exactly the same actual processing of the
    // input as the second Python functional implementation. The biggest difference is that the
    // steps can be broken up in the implementation into more easily understandable steps. This is
    // because Rust has a thoughtfully implementated Lazy iterators.
    // With that being said, what do you think is the Big O time complexity of this
    // algorithm? In other words, how many times do we need to iterate over a set of data to
    // generate the needed results?
    return instructions
        .iter()
        .map(|d_val_str| -> (&str, i32) {
            let d_val_arr: Vec<&str> = d_val_str.split_whitespace().collect();
            println!("{} {}", d_val_arr[0], d_val_arr[1]);
            // Here we are costructing a tuple out of the first element and the
            // second element, which is also converted into a 32bit int.
            return (d_val_arr[0], d_val_arr[1].parse().unwrap());
        })
        .map(|(direction, val)| {
            println!("{} {}", direction, val);
            match direction {
                "up" => (0, val),
                "down" => (0, -val),
                "right" => (val, 0),
                "left" => (-val, 0),
                _ => panic!(),
            }
        })
        .fold((0, 0), |(acc_l, acc_r), (cur_l, cur_r)| {
            (acc_l + cur_l, acc_r + cur_r)
        });
}

fn main() {
    let test_1 = mr_roboto(&["right 10", "up 50", "left 30", "down 10"]);
    println!("test1: {:?}", test_1);
    let test_2 = mr_roboto(&["right 100", "right 100", "up 500", "up 10000"]);
    println!("test2: {:?}", test_2);
    let test_3 = mr_roboto(&[]);
    println!("test3: {:?}", test_3);
}
