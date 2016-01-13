print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n',
'newline tabs.'

poem = """
\t The lovely world
with the logic so firmly planted
cannot discern \n the needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""

print "-----------------"
print poem
print "-----------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, %d crates." % (
    secret_formula(start_point)
)

# In this exercise we've revised the things which we
# had done in the previous exercises. for eg: print,
# triple double quotes, single quote, \n, \t & def
