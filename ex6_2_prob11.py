def passval(f):
    def g(x):
        if not isinstance(x, list):
            return 0

        is_integer = all(isinstance(a, int) for a in x)
        is_string = all(isinstance(a, str) for a in x)

        if is_integer:
            func = 'square'
        elif is_string:
            func = 'string'
        else:
            func = 'length'
        result = []
        result = f(x, func)
        return result
    return g


@passval  # declaring decorate directly above the function
def calculate(a, func=None):
    res = []
    if func == 'square':
        for i in a:
            sq = i * i
            res.append(sq)
    elif func == 'string':
        for i in a:
            length = len(i)
            res.append(length)
    else:
        for i in a:
            list_len = len(str(i))
            res.append(list_len)

    return res


# declaring decorator using the variable 'calculate'
# calculate = passval(calculate)
print calculate(['pranav', 'tush', 'daddy'])
print calculate([1, 5, 10, 2, 3])
print calculate([3, 4, 'hello', 7, 15, 'hi'])

# Write a function vectorize which takes a function f and
# return a new function, which takes a list as argument
# and calls f for every element and returns the result
# as a list.
