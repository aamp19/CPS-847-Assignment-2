from flask import Flask, render_template
import unittest

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
class TestCode(unittest.TestCase):
    with open('index.html') as file:
    contents = file.read()
    search_word = input("enter a word you want to search in file: ")
    storage = []
    if search_word in contents:
        storage.append(search_word)
        storage = "".join(storage)
    else:
        print ('word not found')
    def test_greeting(self):
        self.assert_template_used('index.html')
        self.assert_equal(storage, contents)
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
