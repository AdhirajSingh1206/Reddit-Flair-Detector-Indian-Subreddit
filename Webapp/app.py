
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('main.html')

    if request.method == 'POST':
        link = request.form['link']
        result = 88
        print(link , result) 
        return render_template('main.html',original_input={'URl of post':link}, result=result)

@app.route('/automated_testing', methods=['GET', 'POST'])
def automated_testing():
    if request.method == 'POST':
        file = request.files['file'] 
        content = file.read()
        print(content)
        return jsonify(content)
    if request.method == 'GET':
        return "hello"

if __name__ == '__main__':
    app.run(debug = True)
