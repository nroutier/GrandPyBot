from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from app import app
from app.forms import QueryForm


@app.route('/')
@app.route('/index/')
def index():
    form = QueryForm()
    return render_template('index.html', form=form)


@app.route('/formdata/', methods=['POST'])
#@crossdomain(origin='*')
def buildAndSendLocationData():
    flash('GrandPy a entendu la question !')
    return jsonify(request.form)
