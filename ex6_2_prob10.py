import time


def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def profile(f):
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

start = time.time()
fib = profile(fib)
fib = memorize(fib)
print fib(4)
end = time.time()
print(end - start)

# Write a function profile, which takes a function as
# argument and returns a new function, which behaves
# exactly similar to the given function,
# except that it prints the time consumed in executing it.
