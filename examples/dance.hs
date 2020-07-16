mrRoboto :: [String] -> (Int, Int)
mrRoboto =
    foldl (\(acc_l, acc_r) (cur_l, cur_r) -> (acc_l + cur_l, acc_r + cur_r)) (0, 0)
    . map (dirToIntPair . words)
    where dirToIntPair [dir, strVal] =
            case dir of
                "up"    -> (0, val)
                "down"  -> (0, -val)
                "right" -> (val, 0)
                "left"  -> (-val, 0)
                where val = read strVal :: Int

main :: IO()
main = do
    let t1 = mrRoboto ["right 10", "up 50", "left 30", "down 10"]
    putStrLn $ "test1: " ++ show t1
    let t2 = mrRoboto ["right 100", "right 100", "up 500", "up 10000"]
    putStrLn $ "test2: " ++ show t2
    let t3 = mrRoboto []
    putStrLn $ "test3: " ++ show t3

