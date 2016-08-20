from hanger2 import hanger

print 'how many times would you like to play?'
times = int(raw_input())

for looper in range(0, times):
    hanger()
