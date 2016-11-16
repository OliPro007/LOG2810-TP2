import random


class Quartier(object):
    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name
        self._arcs = {}

    def ajouter_arc(self, arc_name):
        assert isinstance(arc_name, str)
        assert len(arc_name) == 1
        self._arcs[arc_name] = Quartier(self.name + arc_name)

    def get_noeud(self, arc):
        return self._arcs.get(arc, None)

    def get_random_noeud(self):
        return self._arcs[list(self._arcs.keys())[random.randint(0, len(self._arcs) - 1)]] if self._arcs else self
