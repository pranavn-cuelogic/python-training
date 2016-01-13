def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split()
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word


def sort_sentence(sentence):
    """Takes in a full sentence & returns the sorted."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first & last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words the prints the first & last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# In this exercise we've learned how to import the file in
# python shell & how to assign variable & calling the function
# inside the shell.
# NOTE: Changes do not reflect when you are in shell, you'll
# need to terminate the shell & agagin import the file
