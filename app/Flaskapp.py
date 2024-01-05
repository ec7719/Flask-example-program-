from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    return "Watashi wa "+name
if __name__ == '__main__':
    app.run(debug=True)
