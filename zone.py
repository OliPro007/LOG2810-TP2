from quartier import Quartier


class Zone(object):
    def __init__(self, name):
        self.name = name
        self.nb_vehicule = 0
        self._start = Quartier("")

    def ajouter_quartier(self, zip_code):
        pass

    def contains(self, zip_code):
        pass
