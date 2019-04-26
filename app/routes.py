from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from app import app
from app.forms import QueryForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    form = QueryForm()
    if form.validate_on_submit():
        flash('GrandPy a entendu la question !')
    return render_template('index.html', form=form)
