
class Quartier(object):
    def __init__(self, name):
        self.name = name
        self._arcs = {}

    def ajouter_arc(self, arc_name):
        self._arcs[arc_name] = Quartier(self.name + arc_name)
