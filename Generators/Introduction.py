                                                    # Generators in Python
# Sometimes data is large. Sometimes data is produced over time. Sometimes storing everything at once is unnecessary.
# Generators solve this by producing values one at a time.
# A generator does not store all values in memory. It gives you the next value only when you ask for it.

# This makes generators memory efficient.

# Generator Using yield
def get_numbers():
    for i in range(5):
        yield i

# Using it:

for x in get_numbers():
    print(x**2)

# Values are generated one by one, not all at once.