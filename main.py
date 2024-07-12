from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def landing_page():
    return render_template('landing.html')


if __name__ == '__main__':
    app.run(debug=True)
