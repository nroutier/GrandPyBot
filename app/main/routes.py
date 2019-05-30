""" Module that handles the routes and return the views of GrandPy app """

from flask import render_template, flash, redirect, url_for, request, jsonify, make_response, current_app
from app.main.forms import QueryForm
from app.main import bp
from app.main.classes.Parse_query import ParseQuery
from app.main.classes.Maps_api import MapsApi
from app.main.classes.Wikimedia_api import WikimediaApi
from app.main.classes.Granpy_dialog import GrandpyDialog


@bp.route('/')
def index():
    """ Function that render the index page """
    form = QueryForm()
    return render_template('index.html', form=form, static_maps_key=current_app.config['STATIC_MAPS_KEY'])


@bp.route('/query/', methods=['POST'])
def returning_location():
    """ Function that gets the query from the form and return a json response with all needed data """
    req = request.form['query']
    query = ParseQuery(req)
    place = query.parse_query()
    maps_place = MapsApi(place)
    address = maps_place.get_address()
    route = maps_place.get_route()
    coord = maps_place.get_coord()
    dialog = GrandpyDialog()
    if coord and route:
        wiki_req = WikimediaApi(coord, route)
        address_dialog = dialog.get_dialog("maps")
        info_place = wiki_req.get_about()
        if info_place:
            info_place_text = info_place['about_text']
            info_place_url = info_place['about_url']
            place_dialog = dialog.get_dialog("about")
        else:
            info_place_text = ""
            info_place_url = ""
            place_dialog = dialog.get_dialog("no_about")
    else:
        info_place_text = ""
        info_place_url = ""
        address = ""
        coord = ""
        route = ""
        address_dialog = dialog.get_dialog("no_maps")
    res = {
        "name": place.capitalize(),
        "address": address,
        "coord": coord,
        "info_place": info_place_text,
        "info_place_url": info_place_url,
        "address_dialog": address_dialog,
        "place_dialog": place_dialog
    }
    res = make_response(jsonify(res), 200)
    return res
