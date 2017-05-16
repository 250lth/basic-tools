#/usr/bin/python3

'''
Example Map-Reduce job: pig latinize words
'''

import sys, re

WORD_RE = re.compile(r"\b([bcdfghjklmnpqrstvwxz]*)([\w\']+)")
CAPITAL_RE = re.compile(r"[A-Z]")


def mapper(line):
    words = WORD_RE.findall(line)
    pig_latin_words = []
    for word in words:
        original_word = ''.join(word)
        head, tail = word
        head = 'w' if not head else head
        pig_latin_word = tail + head + 'ay'
        if CAPITAL_RE.match(pig_latin_word):
            pig_latin_word = pig_latin_word.lower().capitalize()
        else:
            pig_latin_word = pig_latin_word.lower()
        pig_latin_words.append(pig_latin_word)
    return " ".join(pig_latin_words)


if __name__ == '__main__':
    for line in sys.stdin:
        print(mapper(line))