// A robot has been given a list of movement instructions. Each instruction
// is either left, right, up or down, followed by a distance to move. The
// robot starts at 0, 0. You want to calculate where the robot will end up
// and return its final position as a list. For example, if the robot is given
// the instructions ["right 10", "up 50", "left 30", "down 10"], it will end
// up 20 left and 40 up from where it started, so you should return [-20, 40].

fn mr_roboto(instructions: &[&str]) -> (i32, i32) {
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
