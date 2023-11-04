# Think of five programming words you’ve learned about in the previous chapters. 
#Use these words as the keys in your glossary, and store their meanings as values.

#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
glossary = { 'loop' : ' are essential for iterating over data structures.',
             'variable' : ' are used to store and manipulate information',
             'function' : ' are used to organize code.',
             'statement' : ' is a single, complete instruction in a program.',
             'list' : ' is a built-in data structure that is used to store collections of items.',
                                                                                                        }
word = 'loop'
print(f"\n{word.title()}:{glossary[word]}")

word = 'variable'
print(f"\n{word.title()}:{glossary[word]}")

word = 'function'
print(f"\n{word.title()}:{glossary[word]}")

word = 'statement'
print(f"\n{word.title()}:{glossary[word]}")

word = 'list'
print(f"\n{word.title()}:{glossary[word]}")