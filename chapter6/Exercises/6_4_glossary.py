# Glossary
glossary = {
    'variable': 'a named storage location that holds a value which can change during program execution',
    'data type': 'the kind of value a variable can hold (e.g. integer, string, boolean)',
    'loop': 'a structure that repeats a block of code while a condition is true or for a set number of times',
    'conditional': 'a decision-making structure that runs certain code only if a specified condition is met',
    'function': 'a reusable block of code that performs a specific task and can be called when needed'
    }

for word, definition in glossary.items():
    print(f'\n{word.title()}: {definition.title()}')