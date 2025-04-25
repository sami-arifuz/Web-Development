from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/old")
def hello_world():
   return "<!doctype html><head><meta charset=utf-8><title>Hello World</title></head><body><p>Hello World</p></body>"



if __name__ == '__main__':
    app.run(debug=True)