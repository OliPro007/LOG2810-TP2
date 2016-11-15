#include "Zone.h"

Zone::Zone(std::string name) : _name(name) {
    _start = new Quartier("");
}

Zone::~Zone() {
    delete _start;
}

void Zone::ajouterVehicule() {
    _nbVehicule++;
}

void Zone::retirerVehicule() {
    _nbVehicule--;
}

void Zone::ajouterQuartier(std::string quartier) {

}

bool Zone::contains(std::string) {
    return false;
}
