#ifndef TP1_ZONE_H
#define TP1_ZONE_H

#include <string>

#include "Quartier.h"


class Zone {
public:
    Zone(std::string name);
    ~Zone();

    void ajouterVehicule();
    void retirerVehicule();

    void ajouterQuartier(std::string quartier);

    bool contains(std::string);

private:
    int _nbVehicule;
    std::string _name;
    Quartier* _start;
};


#endif //TP1_ZONE_H
