import random


class Quartier(object):
    def __init__(self, name):
        self.name = name
        self._arcs = {}

    def ajouter_arc(self, arc_name):
        self._arcs[arc_name] = Quartier(self.name + arc_name)

    def get_noeud(self, arc):
        assert isinstance(arc, str)
        return self._arcs.get(arc, None)

    def get_random_noeud(self):
        return self._arcs[list(self._arcs.keys())[random.randint(0, len(self._arcs) - 1)]] if self._arcs else self
