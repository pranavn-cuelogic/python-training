from sys import argv
script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# In this exercise we have learned how to read a file
# using the read method by passsing the file name using the
# argument & the using the raw_input
