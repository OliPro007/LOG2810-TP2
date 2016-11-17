from quartier import Quartier


class Zone(object):
    def __init__(self, name):
        self.name = name
        self.nb_vehicule = 0
        self._start = Quartier("")

    def ajouter_quartier(self, zip_code):
        """
        Ajoute un quartier (code postal) à la zone.
        Le quartier est décomposé en sous-quartiers de façon à former un automate à états finis.

        :param zip_code: Le code postal complet à ajouter.
        """
        current_state = self._start
        for char in zip_code:
            if current_state.get_noeud(char) is None:
                current_state.ajouter_arc(char)
            current_state = current_state.get_noeud(char)

    def contains(self, zip_code):
        """
        Détermine si le quartier est présent dans la zone.

        :param zip_code: Le code postal complet du quartier à chercher.
        :return: True si le quartier existe dans la zone, False sinon
        """
        current_state = self._start.get_noeud(zip_code[0])

        if current_state is not None:
            for char in zip_code[1:]:
                current_state = current_state.get_noeud(char)
                if current_state is None:
                    break

        return current_state is not None

    def select_random_quartier(self):
        """
        Sélectionne un quartier au hasard dans la zone.
        Utile pour initialiser le quartier de départ des véhicules.

        :return: Un quartier choisi au hasard.
        """
        return self._start.get_random_noeud()
