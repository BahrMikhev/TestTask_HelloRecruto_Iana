# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)


@app.route('/')
def query_example():
    name = request.args.get('name')
    message = request.args.get('message')
    return f'<h1>Hello {name}! {message}</h1>'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
