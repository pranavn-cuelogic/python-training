class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_bday = Song([
    "Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"
])

bulls_on_parade = Song([
    "They rally around tha family",
    "With pockets full ofo shell"
])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# In this exercise we've learned how to declare the class &
# its object. Also we've learned how to use the class function
# using the object variable.
