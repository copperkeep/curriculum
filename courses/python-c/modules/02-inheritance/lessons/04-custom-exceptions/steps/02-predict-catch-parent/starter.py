class BankError(Exception): pass
class InsufficientFunds(BankError): pass

try:
    raise InsufficientFunds()
except BankError:
    print("bank problem")
