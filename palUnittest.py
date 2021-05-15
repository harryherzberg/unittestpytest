import unittest

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


class myTest(unittest.TestCase):

    #tests to see if you can input nothing 
    def testEmpt(self):
        print("testing to see if either can be empty")
        name = palendrome()
        name.takeSentance()
        name.countWords()
        self.assertNotEqual(name.sentance, "")

    #tests to see if it works in normal condition
    def testNorm(self):
        print("testing to see if it works in normal conditions")
        name = palendrome()
        name.sentance = "amanaplanacanalpanama"
        name.countWords()
        self.assertEqual(name.isPalendrome, True)



try:
  if __name__ == '__main__':
    unittest.main()
except:
  print("error")
