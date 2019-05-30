""" Module that defines the class Wikimedia_api """

import wikipedia
import re


class WikimediaApi:
    """ Class that interact with wikimedia api """

    def __init__(self, coord, route):
        """ Function that instanciate a WikimediaApi object """
        self.coord = coord
        self.route = route

    def get_about(self):
        """ Function that return a short description of a location from its coordonate and street name """
        wikipedia.set_lang("fr")
        res = wikipedia.geosearch(self.coord['lat'], self.coord['lng'], results=5)
        try:
            regex_route = r"" + self.route
            i = 0
            for i in range(len(res)):
                if re.match(regex_route, res[i]):
                    page = wikipedia.page(res[i]).content
                    about_url = wikipedia.page(res[i]).url
            regex = r'== Situation et accès ==\n.*'
            section = re.search(regex, page).group(0)
            regex_sub = r'== Situation et accès =='
            about = re.sub(regex_sub, "", section)
            about = {"about_text": about.strip(), 'about_url': about_url}
            return about
        except:
            return
