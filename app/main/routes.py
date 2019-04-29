from flask import render_template, flash, redirect, url_for, request, jsonify, current_app
from app.main.forms import QueryForm
from app.main import bp


@bp.route('/')
@bp.route('/index/')
def index():
    form = QueryForm()
    return render_template('index.html', form=form)


@bp.route('/formdata/', methods=['POST'])
# @crossdomain(origin='*')
def buildAndSendLocationData():
    # flash('GrandPy a entendu la question !')
    return jsonify(request.form)
