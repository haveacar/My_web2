from flask import Flask, render_template, url_for

# config flask
app = Flask(__name__)


# home page
@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, port=5007)
