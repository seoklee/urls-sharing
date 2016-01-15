import json


class LinkEntry(object):
    def __init__(self, _id, links, description=None):
        self._id = _id
        self.links = links
        self.description = description

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
