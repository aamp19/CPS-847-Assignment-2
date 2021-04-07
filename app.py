import unittest
import codecs



def to_string():
    f = codecs.open("index.html",'r')
    storage = f.read()
    for i in storage.split(" "):
      if "hello" in i:
        return True
  




                
class TestCode(unittest.TestCase):       
    def test_greeting(self):
        self.assertEqual(to_string(), True)



if __name__ == '__main__':
    unittest.main()
