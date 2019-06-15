""" Module that defines the class Wikimedia_api """

from mediawiki import MediaWiki
import re


class WikimediaApi:
    """ Class that interact with wikimedia api """

    def __init__(self, coord, route):
        """ Function that instanciate a WikimediaApi object """

        self.lat = str(coord['lat']) if coord else ""
        self.lng = str(coord['lng']) if coord else ""
        self.route = route
        self.wikipedia = MediaWiki(lang=u'fr')

    def geosearch(self):
        """ Function that return a list of pages from wikipedia
         and coordinate """
        try:
            geores = self.wikipedia.geosearch(self.lat, self.lng, results=5)
        except:
            geores = []
        return geores

    def get_pagetitle(self):
        """ Function that return the title of a page that match the route """

        geores = self.geosearch()
        pagetitle = ""
        try:
            regex_route = r"" + self.route
            i = 0
            for i in range(len(geores)):
                if re.match(regex_route, geores[i]):
                    pagetitle = geores[i]
        except:
            pass
        if not pagetitle:
            pagetitle = geores[0] if geores else ""
        return pagetitle

    def get_about(self):
        """ Function that return a summary and the url of a wikipedia page """

        pagetitle = self.get_pagetitle()
        page = self.wikipedia.page(pagetitle) if pagetitle else ""
        about_url = page.url if page else ""
        try:
            regex = r'== Situation et accès ==\n.*'
            section = re.search(regex, page.content).group(0)
            regex_sub = r'== Situation et accès =='
            about_text = (re.sub(regex_sub, "", section)).strip()
        except:
            about_text = page.summary if page else ""
        return {"about_text": about_text, 'about_url': about_url}
