from itertools import accumulate

def balances(start, amounts):
    return list(accumulate(amounts, initial=start))
