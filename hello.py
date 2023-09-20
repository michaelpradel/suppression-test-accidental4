"""
Toy example.
"""

def hello():
    """ A fantastic docstring. """
    # pylint: disable=missing-format-string-key
    print("\n")
    print("Hello %(first)s %(last)s" % {"First": "John", "last": "Doe"})
