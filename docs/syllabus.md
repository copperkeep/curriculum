# Syllabus

What the three Python courses cover, lesson by lesson. Generated from the course tree —
the tree is the source of truth, so regenerate this rather than hand-editing the tables.

## Python A — Foundations

Printing, variables, numbers, loops, input, choices, lists, while, and your own functions. Target age: 8 and up. 10 modules, 28 lessons, 134 steps.

| Module | Lesson | Claim |
|---|---|---|
| Making the computer talk | Say hello | print shows words on the screen |
|  | Numbers and words | Numbers need no quote marks, and Python can do sums with them |
|  | Notes in your code | Python skips any line that starts with a hash mark |
| Giving things names | Store a value | A variable is a name for a value |
|  | Change a value | Giving a variable a new value throws the old one away |
|  | Join text together | A plus mark joins two bits of text into one |
| Loops | Repeating with for | Loops repeat things |
|  | What repeats | Only the pushed-in lines repeat |
| Doing sums | Plus, minus, times, divide | Python does sums with + - * and / |
|  | Sharing and leftovers | // shares things out and % finds what is left over |
|  | Which sum goes first | Times and divide go before plus and minus, unless brackets say so |
|  | Add it up with a loop | A loop can keep a running total |
| Asking questions | Ask a question | input waits for an answer and gives it back as text |
|  | Turn text into a number | int turns text into a number you can do sums with |
| Making choices | True or False | A question like 3 > 2 has an answer of True or False |
|  | If this, else that | if runs its lines only when the question is True |
|  | More than two choices | elif checks the next question only when the ones before were False |
|  | And, or, not | and needs both sides True, or needs just one |
| Lists | Make a list | A list keeps many values in one box |
|  | Find a thing in a list | Each thing in a list has a number, and the first one is 0 |
|  | Grow a list | append adds to the end of a list, and len counts what is in it |
|  | Loop over a list | for can walk through a list, one thing at a time |
| Repeating until done | Repeat while it is true | while keeps going as long as its question is True |
|  | Leaving a loop early | break stops a loop, and continue skips to the next go |
| Your own commands | Make your own command | def gives a few lines a name you can run again and again |
|  | Give a function something to use | A parameter is a box that gets its value when the function is called |
| Put it together | Times table | Loops, sums and functions together can make a whole times table |
|  | Guess the number | A game is just a loop, some checks, and a way to stop |

## Python B — Working Programs

Functions that return, text and list tools, tuples, dictionaries, sets, comprehensions, errors, files, modules and debugging. Target age: 10 and up. 11 modules, 37 lessons, 176 steps.

| Module | Lesson | Claim |
|---|---|---|
| Functions that give back | Return a value | return hands a value back to whoever called the function |
|  | Defaults and keyword arguments | A parameter can have a default, and an argument can be passed by name |
|  | Any number of arguments | *args collects extra positional arguments and **kwargs collects extra keyword ones |
|  | Where a name lives | A name made inside a function lives only inside that function |
| Working with text | Slicing text | s[start:stop] cuts out a piece of a string |
|  | Text tools | Strings come with methods that return new, changed strings |
|  | Splitting and joining | split turns text into a list, and join turns a list back into text |
|  | Filling in text | An f-string fills values straight into text |
|  | Formatting numbers | A format spec after a colon controls how a value is shown |
| More with lists | Slicing lists | A slice copies out part of a list |
|  | List tools | Lists change in place with insert, remove, pop, extend and more |
|  | Sorting | sorted returns a new sorted list, and sort sorts in place |
|  | Lists inside lists | A list of lists makes a grid, indexed row first |
|  | Two names, one list | Assignment never copies — two names can share one list |
| Tuples and unpacking | Tuples | A tuple is a fixed group of values that cannot change |
|  | Unpacking | Unpacking gives each value in a sequence its own name in one line |
|  | enumerate and zip | enumerate counts as you loop, and zip walks two lists side by side |
| Dictionaries and sets | Dictionaries | A dictionary looks up a value by its key |
|  | Looping over a dictionary | items gives each key and value together |
|  | Counting with a dictionary | A dictionary of counts answers "how many of each?" |
|  | Sets | A set holds each value at most once and answers "is it in here?" fast |
| Comprehensions | List comprehensions | A comprehension builds a list from a loop in one expression |
|  | Filtering in a comprehension | An if at the end of a comprehension keeps only some items |
|  | Dict and set comprehensions | Braces make the same comprehension build a dict or a set |
| When things go wrong | Reading an error | An error message names what went wrong and where |
|  | Catching an error | try runs risky code, and except says what to do if it fails |
|  | Raising an error | raise stops a function when it has been given something it cannot use |
|  | else and finally | else runs when nothing failed, and finally runs no matter what |
| Files | Writing a file | open with "w" and a with block writes text that outlives the program |
|  | Reading a file | A file opened for reading can be looped over line by line |
|  | CSV and JSON | The csv and json modules read and write structured data for you |
| Modules | Importing modules | import brings in code someone else already wrote |
|  | Counter and defaultdict | collections has ready-made versions of the dict patterns you wrote by hand |
| Debugging | Tracing a program | Debugging is checking what the program actually does against what you think it does |
|  | Checking with assert | assert stops the program the moment something you believe is not true |
| Working programs | Word report | Reading, cleaning, counting and formatting make a complete tool |
|  | Gradebook | A real program reads data, survives bad rows, and summarises |

## Python C — Real Code

Classes, iterators and generators, functional tools, decorators, context managers, types, pattern matching, regex, testing, algorithms, and how Python works underneath. Target age: 12 and up. 16 modules, 47 lessons, 205 steps.

| Module | Lesson | Claim |
|---|---|---|
| Classes and objects | Classes and objects | A class is a blueprint, and each object made from it has its own data |
|  | Methods | A method is a function that belongs to a class and receives the object as self |
|  | Class and instance attributes | An attribute on the class is shared by every instance |
|  | Special methods | Double-underscore methods let your objects work with Python's operators and built-ins |
| Inheritance | Subclasses | A subclass gets everything its parent has and can change or add to it |
|  | Calling the parent with super | super() lets a subclass extend its parent's method instead of replacing it |
|  | Abstract base classes | An abstract base class refuses to be created until its subclass fills in the gaps |
|  | Your own exceptions | Subclassing Exception gives your errors names callers can catch precisely |
| Class tools | Properties | A property looks like an attribute but runs code when read or set |
|  | Class and static methods | classmethod receives the class, and staticmethod receives nothing extra |
|  | Dataclasses | @dataclass writes __init__, __repr__ and __eq__ for you |
|  | Enums | An Enum is a fixed set of named values that cannot be misspelt |
| How objects behave | Identity and equality | == asks "same value?" and is asks "same object?" |
|  | Shallow and deep copies | A shallow copy shares the insides, and a deep copy duplicates everything |
| Iterators and generators | Iterators | A for loop calls iter once and next until StopIteration |
|  | Generators | A function with yield pauses at each value and resumes where it left off |
|  | Generator expressions | A comprehension in parentheses makes values lazily instead of building a list |
|  | itertools | itertools has fast building blocks for combining and slicing iterators |
| Functions as values | Functions are values | A function can be stored, passed in and returned like any other value |
|  | Lambdas | lambda writes a small one-expression function inline |
|  | map, filter, any and all | map transforms, filter selects, any and all answer yes-or-no over a whole sequence |
|  | Closures | An inner function remembers the variables of the function that made it |
|  | functools | functools packages common function-building patterns |
| Decorators | Writing a decorator | A decorator is a function that takes a function and returns a replacement |
|  | Decorators that take arguments | @repeat(3) calls repeat(3) first, and what that returns is the decorator |
| Context managers | How with works | with calls __enter__ on the way in and __exit__ on the way out, whatever happens |
|  | contextlib | @contextmanager turns a generator with one yield into a context manager |
| Type hints | Type hints | Type hints document what a function takes and returns, and tools check them |
|  | Generic types | A type variable says "whatever type goes in, the same type comes out" |
|  | Protocols | A Protocol describes the methods an object must have, not the class it must be |
| Pattern matching | match and case | match compares a value against patterns and runs the first case that fits |
|  | Matching structure | Patterns can look inside dicts and objects and pull out the parts you need |
| Regular expressions | Searching text with patterns | A regular expression describes a family of strings to search for |
|  | Groups and substitution | Parentheses capture parts of a match, and sub rewrites every match |
| Testing | unittest | A test suite is code that checks your code, and runs every time you change it |
| Algorithms | Recursion | A recursive function solves a problem by solving a smaller copy of it |
|  | Searching | Binary search finds an item in a sorted list by halving the search each step |
|  | Sorting algorithms | Merge sort sorts by splitting in half, sorting each half, and merging |
|  | How work grows | Big-O describes how the work grows as the input grows |
| Idioms and the standard library | One-line if | x if condition else y picks a value without a full if statement |
|  | Assignment expressions | := assigns a value and uses it in the same expression |
|  | Scripts and modules | if __name__ == "__main__" separates what a file does when run from what it offers when imported |
|  | Dates and times | datetime does calendar arithmetic so you never count days by hand |
| Under the hood | Dynamic attributes | getattr, setattr and __getattr__ let code choose attribute names at runtime |
|  | Descriptors | A descriptor is a reusable property, defined once and attached to many attributes |
|  | How classes are made | A class is an object too, made by calling its metaclass, usually type |
| Capstone | A library system | Classes, errors, iteration, serialisation and tests together make a real program |

## Not covered yet

Deliberately out of scope for this pass, with the reason:

| Topic | Why not yet |
|---|---|
| `input()` as a graded exercise | The grading harness runs every program once with empty stdin before any case, so `input()` raises `EOFError` for everyone. Taught with predict, parsons and explain-back steps until the harness skips that pass for stdin cases. |
| `async` / `await` | Pyodide runs Python on the browser's own event loop, so `asyncio.run()` does not behave as it does in CPython. Needs a runtime spike before a lesson can be graded. |
| Threads and processes | Pyodide is single-threaded; `threading` and `multiprocessing` cannot be demonstrated honestly in the browser. |
| Packaging, `pip`, virtual environments | Nothing to run in the browser. Mentioned in *Scripts and modules*; a project outside the platform suits it better. |
| Third-party packages via micropip | Needs wheels vendored into the runtimes image and listed in `allowedPackages`. |
