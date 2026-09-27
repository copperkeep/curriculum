try:
    {}["missing"]
except ValueError:
    print("caught")
