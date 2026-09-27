def first[T](xs: list[T]) -> T:
    return xs[0]

print(tuple(t.__name__ for t in first.__type_params__))
