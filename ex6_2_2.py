def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def trace(f):
    f.indent = 0

    def g(x):
        print '|  ' * f.indent + '|--', f.__name__, x
        f.indent += 1
        value = f(x)
        print '|  ' * f.indent + '|--', 'return', repr(value)
        f.indent -= 1
        return value
    return g


def memorize(f):
    cache = {}

    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return g

fib = trace(fib)
fib = memorize(fib)
print fib(4)

# In this exercise we've learned the cache concept to
# minimize the use of memory & to prevent the execution time.
