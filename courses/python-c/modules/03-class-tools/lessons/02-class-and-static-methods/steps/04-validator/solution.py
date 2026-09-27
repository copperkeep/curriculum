class Email:
    def __init__(self, address):
        if not Email.is_valid(address):
            raise ValueError(f"invalid email: {address}")
        self.address = address

    @staticmethod
    def is_valid(address):
        parts = address.split("@")
        return len(parts) == 2 and all(parts)
