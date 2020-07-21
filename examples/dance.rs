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
    // because Rust has a thoughtful implementation of Lazy iterators. This is what is created with
    // the iter() method call. This data structure allows for the later processing to be sort of
    // added on to each individual element in the iterator. The actual processing of that function
    // isn't actually done until the result is actually needed. In this step that would be during
    // the fold method call, as the result of each of the steps is actually needed to produce the
    // desired result. This lazy iteration allows for this algorithm to have a time complexity of
    // O(n). If you aren't used to lazy iteration you may have thought that this algorithm has a
    // time complexity of O(2n) because it appears that each of the objects in the list must be
    // processed twice. But, because of the very clever optimizations provided by lazy evaluation,
    // the logic of this algorithm is able to be broken up while retaining the same optimal time
    // complexity.
    return instructions
        .iter()
        .map(|d_val_str| {
            let d_val_arr: Vec<&str> = d_val_str.split_whitespace().collect();
            let direction = d_val_arr[0];
            let val = d_val_arr[1].parse::<i32>().unwrap();
            return match direction {
                "up" => (0, val),
                "down" => (0, -val),
                "right" => (val, 0),
                "left" => (-val, 0),
                _ => panic!(),
            };
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
