""" Module that define the class GrandpyDialog """

import random
from pathlib import Path
import json


class GrandpyDialog:
    """ Class that generate grandpy dialogs """
    def __init__(self):
        """ Function that instantiate an object GrandpyDialog from a json """\
            """file """
        path = Path(__file__).parents[3]
        file_path = path / "grandpy_dialog.json"

        with open(file_path, encoding='utf-8') as json_file:
            self.dialog = json.load(json_file)

    def get_dialog(self, dialog_key):
        """ Function that return a random sentence from the json for a """\
            """specified key """
        return random.choice(self.dialog[dialog_key])
