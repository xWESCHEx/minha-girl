from flask import Flask, render_template

app = Flask("Web_en_python")

@app.route("/")
def hello_world():
    return render_template('web/index.html')

@app.route('/fototeca')
def fototeca():
    return render_template('web/fototeca.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='5000')