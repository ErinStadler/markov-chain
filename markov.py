"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    contents = open(file_path).read()

    return contents

input_text = open_and_read_file("green-eggs.txt")


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}


    # your code goes here

    #split the string into individual words. .split()
    text_split = text_string.split()
    #loop over everything from index 0 to stopping range
    for i in range(len(text_split) - 2):  
        
        #create a tuple with the two indexes and add it to our dictionary if it is not there already.
        chains_key = text_split[i], text_split[i + 1]
        if chains_key in chains:
            chains[chains_key].append(text_split[i+2])
        else:
            chains_value = [text_split[i+2]]
            chains[chains_key] = chains_value
        
        
    return chains

#print(make_chains(input_text))

chains = make_chains(input_text)

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    #create a link to the chains key
    #link = key from chains + any 1 random item from the list(value of the dictionary) associated with that key
    #Make link a list

    list_keys = []

    for keys in chains:
        list_keys.append(keys)

        key_chosen = choice(list_keys)
        value_key_chosen = chains[key_chosen]
        value_chosen = choice(value_key_chosen)

        #words.extend([key_chosen[0], key_chosen[1], value_chosen])
        words.extend([key_chosen[1], value_chosen])
            

    #print(words)
        
    
    #print(list_keys)

    
    
    return ' '.join(words)

print(make_text(chains))

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

#print(random_text)


