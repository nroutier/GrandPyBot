""" Module that defines the class Wikimedia_api """

import wikipedia
import re

class Wikimedia_api:
    
    def __init__(self, coord, route):
        self.coord = coord
        self.route = route

    def get_about(self):
        wikipedia.set_lang("fr")
        res = wikipedia.geosearch(self.coord['lat'], self.coord['lng'], results=5)
        regex_route = r"" + self.route
        i = 0
        for i in range(len(res)):
            if re.match(regex_route, res[i]):
                page = wikipedia.page(res[i]).content
        regex = r'== Situation et accès ==\n.*'
        section = re.search(regex, page).group(0)
        regex_sub = r'== Situation et accès =='
        about = re.sub(regex_sub, "", section)
        return about.strip()
