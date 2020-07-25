-- At its core this algorithm is working in an incredibly similar way to the
-- Rust version. The biggest difference is the actual order the operations come
-- in the syntax. Haskell is a little different from most other languages in
-- that it doesn't have methods (functions that are defined on a type), rather
-- it exclusively relies on functions. Because of this the order the operation
-- that is ran first should be furthest right, and the one that runs first
-- should be furthest left. Another weird askect is that functions aren't
-- called using parenthesis, rather they are called by passing arguments to
-- them with spaces to seperate them. For example (+) 1 1 would call the +
-- function on the parameters 1 and 1, returning 2. Of course there are also 

mrRoboto :: [String] -> (Int, Int)
mrRoboto instructions =
    foldl (\(acc_l, acc_r) (cur_l, cur_r) -> (acc_l + cur_l, acc_r + cur_r)) (0, 0)
    $ map (dirToIntPair . words) instructions
  where dirToIntPair [dir, strVal] =
          let val = read strVal :: Int
          in case dir of
            "up"    -> (0, val)
            "down"  -> (0, -val)
            "right" -> (val, 0)
            "left"  -> (-val, 0)

main :: IO()
main = do
    let t1 = mrRoboto ["right 10", "up 50", "left 30", "down 10"]
    putStrLn $ "test1: " ++ show t1
    let t2 = mrRoboto ["right 100", "right 100", "up 500", "up 10000"]
    putStrLn $ "test2: " ++ show t2
    let t3 = mrRoboto []
    putStrLn $ "test3: " ++ show t3
