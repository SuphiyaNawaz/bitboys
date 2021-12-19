from flask import Flask, render_template,request
from bs4 import BeautifulSoup

soup=BeautifulSoup()

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/Coin Details",methods=["post"])
def receive_data():
    coin=request.form["coin"]
    return render_template('newIndex.html', coin= coin)



if __name__ == '__main__':
    app.run(debug=True)