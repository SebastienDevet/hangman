from isLetterValid import isLetterValid
from displaySecretWord import displaySecretWord
from secret import isSecretSolved
from findLetters import findLetters
import random


def hanger():
    myRoll = random.randint(1, 65)

    words = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat',
             'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey',
             'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk',
             'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule',
             'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python',
             'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark',
             'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan',
             'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale',
             'wolf', 'wombat', 'zebra']
    wrong = 0
    secret = words[myRoll]
    wf = True
    template = []
    used = ""
    foobar = ()

    while (True):
        if wrong == 6:
            print "Hangman! You lose!"
            print "The secret word was: " + secret
            break
        else:
            print "Please enter a guess: "
            foobar = raw_input()
            if used.find(foobar) >= 0:
                print "you already used that letter"
                used = used + foobar
            else:
                mep = findLetters(secret, foobar)
                used = used + foobar
                if len(foobar) == 1:
                    meem = isLetterValid(secret, foobar)
                    if meem:
                        for looper in range(0, len(secret) + 1):
                            template = displaySecretWord(secret, mep, foobar, wf, template)
                            wf = False
                        print template
                        narc = isSecretSolved(len(secret), template)
                        if narc:
                            print "you win!"
                            print 'the secret word was:', secret
                            break
                        else:
                            print "good guess!"
                    else:
                        print "wrong guess!"
                        wrong = wrong + 1
                else:
                    print 'one letter at a time please!'
