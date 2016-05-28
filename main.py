from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("guichu.html")

@app.route("/shi")
def shi():
    return render_template("sh.html")
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
