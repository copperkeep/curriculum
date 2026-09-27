import functools
# Write retry(times) so @retry(3) calls the function up to 3 times while it
# raises, returning the first successful result, or re-raising the last error.
