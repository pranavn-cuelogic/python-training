env = {'a': 42}
exec('x = a + 1', env)
print env['x']


code = 'def add_%d(x): return x + %d'
for i in range(1, 6):
    exec(code % (i, i))

print add_3(10)
print add_4(5)

# In this exercise we've learned how to create function or
# classes dynamically using exec.
