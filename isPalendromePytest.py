import pytest
class palendrome:
  def __init__(self):
    self.sentance = ""
    self.isPalendrome = False
  def takeSentance(self):
    filler = input ( "sentance: ")
    self.sentance = filler
  def countWords(self):
      self.isPalendrome = self.sentance == self.sentance[::-1]
      print("is it a palendrome?: "+ str(self.isPalendrome))



    #tests to see if you can input nothing
def testEmpt():
    print("testing to see if either can be empty")
    name = palendrome()
    name.takeSentance()
    name.countWords()
    assert name.sentance != ""


#tests to see if it works in normal condition
def testNorm():
    print("testing to see if it works in normal conditions")
    name = palendrome()
    name.sentance = "amanaplanacanalpanama"
    name.countWords()
    assert name.isPalendrome == True

testEmpt()
testNorm()
