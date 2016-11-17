import random


class Quartier(object):
    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name
        self._arcs = {}

    def ajouter_arc(self, arc_name):
        """
        Ajoute un arc à l'automate. L'arc pointe du quartier englobant vers un sous-quartier.

        :param arc_name: Le nom de l'arc à créer. Il s'agit d'un seul caractère.
        """
        assert isinstance(arc_name, str)
        assert len(arc_name) == 1
        self._arcs[arc_name] = Quartier(self.name + arc_name)

    def get_noeud(self, arc):
        """
        Getter.

        :param arc: Le nom du quartier à obtenir.
        :return: Le quartier correspondant, None si le quartier n'existe pas.
        """
        return self._arcs.get(arc, None)

    def get_random_noeud(self):
        """
        Sélectionne un quartier au hasard.

        :return: Un sous-quartier ou self s'il n'existe pas de sous-quartier.
        """
        return self._arcs[list(self._arcs.keys())[random.randint(0, len(self._arcs) - 1)]] if self._arcs else self
