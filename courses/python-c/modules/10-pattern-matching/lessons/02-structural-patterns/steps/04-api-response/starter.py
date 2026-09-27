# Write describe(resp) for JSON-like dicts:
#   {"status": "ok", "data": {"user": {"name": N}}}  -> "Hello, N"
#   {"status": "error", "code": C}                  -> "Error C"
#   anything else                                   -> "Bad response"
