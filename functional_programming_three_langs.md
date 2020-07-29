# Functional Programming in Three Languages: A dive into how functional programing leads to programmatic "truth"
## Intro
- Why am I writing this?
  - Learning Python and found some missing features that I had grown accustomed to
  - Want to help others understand how they can use functional programing to write more elegant, more easily understood algorithms
  - To explain lazy evaluation of iterators, which I think is a kind of _weird_ concept if you're used to imperative programming
  - To analyze what "truth" is and how we can implement an understanding of truth to create better programing languages.
- How this article is formated:
  - Code examples, I'm going to give you some examples in order to ground our later discussion of what Functional programming is. These sub-sections will be an example followed by a brief bit of exposition that will seek to help you understand exactly what is happening in the algorithm.
	- Python: Begin with a language that is not intuitive to use for functional programming, but is easy to understand to reach a broad audience
	- Rust: Example of a language that allows for functional programming, but isn't strictly functional
	- Haskell: A true functional language.
  - Examination of why functional programming is valuable (beyond aesthetics)
	- Programming as an evaluation of logic in the pursuit of "truth"
	- Why it is valuable to understand programming as being about "truth"
	  - Our brains are more comfortable handling static truth vs. mutable truth. This in itself will lead you to write more robust code as you'll have an easier time understanding your own code.
	  - Imperative programing leads to multiple/variable accounts of truth. This makes it harder to understand what the outcome of the program should be and can lead to a strictly "wrong" return value.

## Main Body 1
### Python
- Python leans strongly into the object oriented paradigm, which is imperative in nature. Can be used for functional programming, but is missing some fundamental components of a true functional language:
  - Everything but tuples are mutable - This encourages changing values
  - Functional programming tools like reduce are hidden away in the `functools` library that must be manually loaded when needed.
  - Because of its imperative nature iterators aren't able to be processed nearly as efficiently as in Rust and Haskell. Although Lazily evaluated iterators are a feature of the language, they aren't evaluated _as_ lazily as they are in a more functional forward language.
  - No multi-line lambdas. This is actually what drove me to write this article. Multi-line lambdas are a fundamental part of my workflow, when I learned that Python had no syntax to possibly allow for this it quickly made me realize that Python isn't a strong language pick for functional programming. Unfortunately it seems like this will always be the case because Pythons creator doesn't like how multi-line lambdas look and many Python developers seem to discourage lambda use all together.

#### Examples 
Before I give any examples heres the prompt that describes the problem that all of our algorithms will solve:
> A robot has been given a list of movement instructions. Each instruction
is either left, right, up or down, followed by a distance to move. The
robot starts at 0, 0. You want to calculate where the robot will end up
and return its final position as a list. For example, if the robot is given
the instructions ["right 10", "up 50", "left 30", "down 10"], it will end
up 20 left and 40 up from where it started, so you should return [-20, 40].  
  
To be explicitly clear as we get into this first set of examples, all of these algorithms strictly _work_ and produce the correct result. They also all have the time complexity of `O(n)` where n is the number of instructions in list that is passed into the algorithm. So, from the beginning I want you to know that I am not trying to argue that functional programming produces code that is better for technical reasons, but rather that you can use functional programming to write code that is easier for anyone looking at it to understand and allows you to more easily break down the logic in the problem into easier to tackle tasks that allow you to solve a programming problem quicker.  
  
I also want to make sure that you are aware that all of these examples are hosted at the GitHub repository for this article [here.](https://github.com/hegelocampus/fp_three_langs/tree/master/examples) Feel free to clone or fork this repository and do whatever you'd like with these, run them, modify them, break them; anything you'd like!

This first example will be a imperative (therefore, not functional) implementation, I hope that we can use this example ground our understanding of functional programming against what it is not.

##### Python Imperative Example
```python
from typing import List

def mr_roboto(instructions) -> List[int]:
    """This imperative implementation relies on setting a mutable variable and
    changing that variables value with each instruction in the list of
    instructions.
    """
    # This initial declaration of a mutable variable is the core feature of an
    # imperative algorithm. We are defining this value only to later change it.
    result = [0, 0]
    for instruction in instructions:
        direction, v_str = instruction.split(' ')
        val = int(v_str)

        if direction == "up":
            cur_left, cur_right =  [0, val]
        elif direction == "down":
            cur_left, cur_right = [0, -val]
        elif direction == "right":
            cur_left, cur_right = [val, 0]
        elif direction == "left":
            cur_left, cur_right = [-val, 0]
        else:
            # This should never happen, but will catch cases where the direction
            # is invalid.
            cur_left, cur_right = [0, 0]

        # With each iteration we are incrementing the initial value
        result = [res[0] + cur_left, res[1] + cur_right]

    return result
```
If you are used to the imperative programming paradigm then this implementation should probably be pretty easy for you to understand. Essentially what is happening in this algorithm is that we initialize a value that will be our result, and then we iterate over each element in the instructions list, processing that string into a from that can be easily parsed for the desired value, and then updating the result to be the sum of the old result and the new value. Then, after we've added each item onto the result, we return the result.  
  
Now, onto the driving question: Why isn't this a _functional_ algorithm? What would we have to change to make this a functional algorithm? Well to understand why this isn't functional lets again take a look at the definition of _functional_ programming. According to Wikipedia:
> Functional programming is a programming paradigm where programs are constructed by applying and composing functions. It is a declarative programming paradigm in which function definitions are trees of expressions that each return a value, rather than a sequence of imperative statements which change the state of the program.  
  
So there are two clear, defining components for an algorithm to be considered functional:
- It must apply and compose functions as a means to arrive at the solution.
- It must use a **declaration** which defines the solution to be the result of a series of function applications. This means that **all the data structures within the function ought to be immutable if the algorithm is to be considered functional.**

With these criteria in hand, lets see how our imperative algorithm stands up against them. 

##### An example of a recursive, functional algorithm that doesn't use the build in tools for writing functional algorithms
- Third, an example of a functional solution that takes advantage of the languages `functools` library

## Main Body 2
### Rust
- Not a strictly functional language and it can be (and often is) used imperatively,
- Although it is strictly typed and all values are static unless denoted otherwise using the `mut` keyword
- Also has built in superstructure to allow for much more intuitive functional programming:
  - Lazy iterators:
	- Lazy iterators are operations on lists that aren't actually evaluated until the value needs to be displayed. For example: if you were to do something like `putStrLn . sum . map (/2) . map (*4) $ map (+2) [x, y, z]`, each of the values in the list would be a pure function value until it needs to be displayed. This results in this complex operation only needing to actually access each of the elements in the list a single time rather then the 4 times it appears they are operated on. To make it abundantly clear here: The way the compiler actually tackles this operation is by doing something like creating a list like this `[(((x + 2) * 4) / 2), (((y + ) * 4) / 2), (((y + ) * 4) / 2)]` and then when the value actually needs to shown, all of the values are assessed in one single iteration.
  - Multi-line lambdas

#### Examples
- Example

## Main Body 3
### Haskell
At its core this algorithm is working in an incredibly similar way to the Rust version. The biggest difference is the actual order the operations come in the syntax. Haskell is a little different from most other languages in that it doesn't have methods (functions that are defined on a type), rather it exclusively relies on functions. Because of this the order the operation that is ran first should be furthest right, and the one that runs first should be furthest left. Another weird aspect is that functions aren't called using parenthesis, rather they are called by passing arguments to them with spaces to separate them. For example `(+) 1 1` would call the `+` function on the parameters 1 and 1, returning 2. Of course there are also _infix_ operators that can be placed between two parameters to increase readability. The `+` operation is actually an infix operator and can of course be called like: `1 + 1`, it is only made a _normal_ function by being wrapped in parenthesis.

#### Example
```haskell
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
```

## Main Body 4
### But Why Functional Programming?: The value of working within systems of "Truth"

## Main Body 4
