def product(a, b):
    """
    >>> Product of the two numbers without using multiply
    """
    if(b == 0):
        return 0
    elif(a == 1):
        return a
    else:
        return a + product(a, b - 1)

print product(2, 4)

# Implement a function product to multiply 2 numbers
# recursively using + and - operators only.
