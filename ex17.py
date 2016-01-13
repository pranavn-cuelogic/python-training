from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
in_data = in_file.read()

print "The input file is %d bytes long" % len(in_data)

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit ENTER to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print "Alright, all done."

out_file.close()
in_file.close()

# In this exercise we have learned how to copy the content
# of one file to another using the previous exercise commands
# i.e. open, read, write & close
