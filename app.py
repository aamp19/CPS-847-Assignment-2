import unittest
import codecs
def to_string():
    f = codecs.open("index.html",'r')
    storage = f.read()
    return (storage)
               
class TestCode(unittest.TestCase):       
    def test_greeting(self):
        self.assertEqual(to_string(), 'hello')

if __name__ == '__main__':
    unittest.main()
