import re
# Write redact(text) replacing every 16-digit card number written as four
# groups of four digits separated by spaces with "**** **** **** " plus the
# last four digits.
# redact("card 1234 5678 9012 3456 ok") -> "card **** **** **** 3456 ok"
