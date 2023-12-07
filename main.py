# import main Flask class and request object
from flask import Flask, request, render_template

# create the Flask app
app = Flask(__name__)


@app.route('/')
def query_example():
    name = request.args.get('name') or ''
    message = request.args.get('message') or ''
    return render_template('index.html', name=name, message=message)

# local debug environment
if __name__ == '__main__':
    app.run(debug=True, port=5000)
