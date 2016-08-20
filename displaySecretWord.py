def displaySecretWord(secret, guess, letter, appender, theTemplate):
    letters = len(secret)
    if appender:
        for looper in range(0, letters):
            theTemplate.append("-")
    else:
        for looper in range(0, len(guess)):
            theTemplate[guess[looper]] = letter

    return theTemplate
