from flask import render_template, flash, redirect, url_for, request, jsonify, make_response, current_app
from app.main.forms import QueryForm
from app.main import bp
from app.main.parse_query import parse_query


@bp.route('/')
@bp.route('/index/')
def index():
    form = QueryForm()
    return render_template('index.html', form=form)


@bp.route('/query/', methods=['POST'])
def returning_location():
    print(request.form)
    req = request.form['query']
    res = parse_query(req)
    # print(req)
    # res = make_response(jsonify({"req": req}), 200)
    res = make_response(jsonify({"res": res}), 200)
    return res
