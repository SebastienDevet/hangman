def isSecretSolved(secret, guessed):
    meep = 0
    for looper in range(0, secret):
        if guessed[looper] == '-':
            break
        else:
            meep = meep + 1
    if meep == secret:
        return True
    else:
        return False
