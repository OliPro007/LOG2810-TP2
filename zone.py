from quartier import Quartier


class Zone(object):
    def __init__(self, name):
        self.name = name
        self.nb_vehicule = 0
        self._start = Quartier("")

    def ajouter_quartier(self, zip_code):
        current_state = self._start
        partial_zip = ""
        for char in zip_code:
            partial_zip = partial_zip + char
            if current_state.get_noeud(partial_zip) is None:
                current_state.ajouter_arc(partial_zip)
            current_state = current_state.get_noeud(partial_zip)



        # for i in range(0, len(zip_code)-1):
        #     partial_zip = zip_code[0:i]
        #     if not self.contains(partial_zip):
        #         self._start.ajouter_arc(partial_zip)
        # current_state = self._start.get_noeud(zip_code[0])
        #
        # if current_state is not None:
        #     for char in zip_code[1:]:
        #
        # else:
        #     self._start.ajouter_arc(zip_code[0])

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
