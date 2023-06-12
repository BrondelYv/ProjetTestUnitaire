# -*- coding: utf-8 -*- 
from flask import Flask, render_template  
import pandas as pd

app = Flask(__name__)  
df = pd.read_csv('drought-tv-news.csv')
df.to_csv('drought-tv-news.csv', index=None)

@app.route("/") 
@app.route('/table')

def table():
    data = pd.read_csv('drought-tv-news.csv')
    return render_template('table.html', tables=[data.to_html()], titles=[''])

def calculate(a,b):
    res=a+b
    return res


if __name__ == "__main__":     
    app.run(debug=True)