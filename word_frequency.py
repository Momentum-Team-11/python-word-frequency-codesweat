STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


f = open("alice_quote.txt", "r")

print(f.read())

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as file:
        lines = file.read()
    # how do we make this string into a list of words?
    lines = lines.split()  # turns the string into a list of words
    # We can count words now
    count_words(lines)


def count_words(lines):
    print("len:", len(lines))
    # how can we take this list and turn it into a dictionary that tracks occurences of each word?
    # create a dictionary
    word_count = {}
    # take the list and add each word to the dictionary as a key
    # and record the occurence of the word
    # How could we get the words from the list into the dict as keys?
    # we could do a for loop using the list!
    for word in lines:
        print(word)
        # now that I have each word, I can add it to the dict as a key

        # if word in word_count:
        # increment the value by 1
        # else:
        # add key and value pair with the word as the key, and set the value to 1
        word_count[word] = 1
    print(word_count)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description="Get the word frequency in a text file."
    )
    parser.add_argument("file", help="file to read")
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
