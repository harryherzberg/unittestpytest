import pytest


class wordCounter:
    def __init__(self):
        self.sentance = ""
        self.length = 0

    def takeSentance(self):
        filler = input("sentance: ")
        self.sentance = filler

    def countWords(self):
        self.length = len(self.sentance.split())
        print("length is: " + str(self.length))


    #tests to see if you can input nothing
def testEmpt():
    print("testing to see if either can be empty")
    name = wordCounter()
    name.takeSentance()
    name.countWords()
    assert name.sentance != ""


#tests to see if it works in normal condition
def testNorm():
    print("testing to see if it counts correctly")
    name = wordCounter()
    name.sentance = "I like videogames"
    name.countWords()
    assert name.length == 3

testEmpt()
testNorm()
