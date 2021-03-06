# encoding: utf-8
# Python2 support
from __future__ import unicode_literals

import random
import sys


class Quartier(object):
    def __init__(self, name):
        if sys.version_info[0] < 3:
            assert isinstance(name, unicode)
        else:
            assert isinstance(name, str)

        self.name = name
        self._arcs = {}

    def __str__(self):
        return self.name

    def ajouter_arc(self, arc_name):
        """
        Ajoute un arc à l'automate. L'arc pointe du quartier englobant vers un sous-quartier.

        :param arc_name: Le nom de l'arc à créer. Il s'agit d'un seul caractère.
        """
        if sys.version_info[0] < 3:
            assert isinstance(arc_name, unicode)
        else:
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
        Sélectionne un quartier au hasard en parcourant des arcs de façon récursive.

        :return: Le résultat de la fonction sur un sous-quartier ou self s'il n'existe pas de sous-quartier.
        """
        return self._arcs[random.choice(list(self._arcs.keys()))].get_random_noeud() if self._arcs else self
