# Write class Ignore(kind) so that `with Ignore(KeyError): ...` silently stops
# the block on a KeyError (or subclass), but lets other exceptions through.
