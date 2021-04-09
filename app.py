import unittest
import codecs



def to_string():
    f = codecs.open("index.html",'r')
    storage = f.read()
    for i in storage.split(" "):
      if "hello" in i:
        return True
  

def addition():
    x = 1
    y = 1
    c = x+y
    return c

def subtraction():
    x = 2
    y = 1
    c = x-y
    return c
                
class TestCode(unittest.TestCase):       
    def test_greeting(self):
        self.assertEqual(to_string(), True)

    def test_addition(unittest.TestCase):
        self.assertEqual(addition(),2)
    
    def test_subtraction(unittest.TestCase):
        self.assertEqual(subtraction(),0)

if __name__ == '__main__':
    unittest.main()
