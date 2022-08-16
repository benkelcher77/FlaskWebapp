from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form.to_dict()
        t = yf.Ticker(result["ticker"])
        return render_template("result.html", result=t.info, ticker=result["ticker"])

if __name__ == "__main__":
    app.run()
