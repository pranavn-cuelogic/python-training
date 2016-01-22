print eval("2 + 3")
a = 5
print eval("a * a")
env = {'x': 45}
print eval('x + 1', env)

# In this exercise we've learned the eval function it is
# similar to exec but it takes an expression & returns its
# value.
