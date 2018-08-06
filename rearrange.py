import sys
import random
def rearrange(sentence):
    shuffled = list()
    while len(sentence) > 0:
        rand_int = random.randint(0, len(sentence)-1)
        popped = sentence.pop(rand_int)
        shuffled.append(popped)
    print(shuffled)


if __name__ == '__main__':
    rearrange(sys.argv[1:])
