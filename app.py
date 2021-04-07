from flask import Flask, render_template
import unittest

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

class TestCode(unittest.TestCase):
    with open('index.html') as file:
    contents = file.read()
    storage = []
    for i in contents:
        if i == 'Hello World':
            storage.append(i)
            storage = "".join(storage)
       
    def test_greeting(self):
        self.assert_template_used('index.html')
        self.assert_equal(storage, 'Hello World')
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
