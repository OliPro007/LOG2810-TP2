from quartier import Quartier


class Zone(object):
    def __init__(self, name):
        self.name = name
        self.nb_vehicule = 0
        self._start = Quartier("")

    def ajouter_quartier(self, zip_code):
        current_state = self._start
        for char in zip_code:
            if current_state.get_noeud(char) is None:
                current_state.ajouter_arc(char)
            current_state = current_state.get_noeud(char)

    def contains(self, zip_code):
        current_state = self._start.get_noeud(zip_code[0])

        if current_state is not None:
            for char in zip_code[1:]:
                current_state = current_state.get_noeud(char)
                if current_state is None:
                    break

        return current_state is not None

    def select_random_quartier(self):
        return self._start.get_random_noeud()
