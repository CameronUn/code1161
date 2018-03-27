"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this line will create a collection of the words: what, does, this, line, do, ?
some_words = ['what', 'does', 'this', 'line', 'do', '?']  #It created a collection of the words: what, does, this, line, do, ? under the name some_words

# I think this line will print all the words in the collection some_words in order.
for word in some_words: #It printed all the words in the some_words collection in order.
    print(word)

# I think this line will print all the words in the collection some_words in order.
for x in some_words: #It printed all of the words in the collection some_words in order.
    print(x)

# I think this line will display all of the words in the collection in order.
print(some_words) #It printed all of the words in the collection some_words in order.

# I think this will check if there are more than 3 entries in the collection. If there are more than 3 it will: 'print some_words contains more than 3 words'
if len(some_words) > 3: #It checked if there were more than 3 words in the collection some_words. There were more than 3 so it printed some_words contains more than 3 words
    print('some_words contains more than 3 words')

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
