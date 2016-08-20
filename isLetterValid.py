def isLetterValid(secret, guess):
    bleh = secret.find(guess)
    if bleh == -1:
        return False
    else:
        return True
