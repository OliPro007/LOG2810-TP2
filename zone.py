from quartier import Quartier


class Zone(object):
    def __init__(self, name):
        self.name = name
        self.nb_vehicule = 0
        self._start = Quartier("")

    def ajouter_quartier(self, zip_code):
        pass

    def contains(self, zip_code):
        current_state = self._start.get_noeud(zip_code[0])

        if current_state is not None:
            for i in zip_code[1:]:
                current_state = current_state.get_noeud(i)
                if current_state is None:
                    break

        return current_state is not None

    def select_random_quartier(self):
        return self._start.get_random_noeud()
