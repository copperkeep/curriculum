from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube_of_two = partial(power, 2)
print(cube_of_two(3), square(3))
