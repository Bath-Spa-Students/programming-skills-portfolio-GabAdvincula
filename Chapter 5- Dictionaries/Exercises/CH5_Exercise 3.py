#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#When you’re sure that your loop works, add five more Python terms.
#When you run your program again, these new words and meanings should automatically be included in the output.

glossary = { 'loop' : 'are essential for iterating over data structures.',
             'variable' : 'are used to store and manipulate information',
             'function' : 'are used to organize code.',
             'statement' : 'is a single, complete instruction in a program.',
             'list' : 'is a built-in data structure that is used to store collections of items.',
             
             
             'dictionary' : 'are widely used in Python for organizing and retrieving data',
             'mutable' : 'objects are objects whose state can be modified after they are created.',
             'immutable' : 'objects, on the other hand, cannot be modified after they are created.',
             'integer' : 'is a data type that represents whole numbers.',
             'boolean' : 'are used to express the truth or falsehood of a statement.',
}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")
