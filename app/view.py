from app import app
from flask import render_template, jsonify
import played_json as pl


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/played.json')
def played_api():
    played = pl.main()
    return jsonify(played)

@app.route('/cover')
def cover():
    return render_template('cover.html')

@app.route('/sw')
def sw():
    return render_template('sw.html')
