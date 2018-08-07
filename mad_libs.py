import sys
class MadLibs:
    """This is class that takes a system argument and returns the madLibs"""
    def __init__(self,sentence):
        self.sentence = sentence
    def construct_madlib(self):
        print("{} went to {} to see {}".format(self.sentence[0],self.sentence[1],self.sentence[2]))



if __name__ == '__main__':

    new_madlib = MadLibs(sys.argv[1:])
    new_madlib.construct_madlib()
