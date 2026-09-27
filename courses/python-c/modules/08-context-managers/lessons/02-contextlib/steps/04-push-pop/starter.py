from contextlib import contextmanager
# Write pushed(stack, item): a context manager that appends item to the list
# stack on entry and pops it on exit, even if the block raises.
