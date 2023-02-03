import random
from random import shuffle


def wordJumble(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)


wordList = ['feigned', 'past', 'sign', 'smile', 'field', 'push', 'collect', 'abnormal', 'sisters', 'annoying', 'influence', 'lumpy']
wordListLength = len(wordList)
randomWordListIndex = random.randint(0, wordListLength)
randomWord = wordList[randomWordListIndex]
randomWordShuffle = wordJumble(randomWord)
wordGuess = randomWordShuffle

while randomWord != wordGuess:
    wordGuess = input("Guess the jumbled word ({}): ".format(randomWordShuffle))
    if randomWord == wordGuess:
        print("That is correct, the word is ({})".format(randomWord))
    else:
        print("Wrong! answer try again")
