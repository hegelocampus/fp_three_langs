# Functional Programming in Three Languages: A dive into how functional programing leads to programmatic "truth"
## Intro
- Why am I writing this?
  - Learning Python and found some missing features that I had grown accustomed to
  - Want to help others understand how they can use functional programing to write more elegant, more easily understood algorithms
  - To analyze what "truth" is and how we can implement an understanding of truth to create better programing languages.
- How this article is formated:
  - Code examples, I'm going to give you some examples in order to ground our later discussion of what Functional programming is:
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
  - No multi-line lambdas. This is actually what drove me to write this article. Multi-line lambdas are a fundamental part of my workflow, when I learned that Python had no syntax to possibly allow for this it quickly made me realize that Python will never be my go-to for writing more complex programs.

#### Examples 
- First, an example of a non-functional, imperative implementation in order to ground our understanding of functional programming against what it is not.
- Second, an example of a recursive, functional algorithm that doesn't use the build in tools for writing functional algorithms
- Third, an example of a functional solution that takes advantage of the languages `functools` library

## Main Body 2
### Rust
- Not a strictly functional language and it can be (and often is) used imperatively,
- Although it is strictly typed and all values are static unless denoted otherwise using the `mut` keyword
- Also has built in superstructure to allow for much

#### Examples
- Example

## Main Body 3
### Haskell

## Main Body 4
### But Why Functional Programming?: The value of working within systems of "Truth"

## Main Body 4
