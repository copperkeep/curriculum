def check_age(age):
    if age < 0 or age > 150:
        raise ValueError("age out of range")
    return age
