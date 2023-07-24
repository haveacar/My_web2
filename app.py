from flask import Flask, render_template, url_for

# config flask
app = Flask(__name__)

images = images = [
        "img/cer1.jpg",
        "img/cer2.jpg",
        "img/certificate_python_institute.png",
        "img/spectr.jpg",
    ]

# home page
@app.route('/')
@app.route('/home')
def main_page():
    return render_template('index.html', images=images)


if __name__ == '__main__':
    app.run(debug=False, port=5000)
