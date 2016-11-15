#include <iostream>
#include <fstream>
#include <stdexcept>
#include <string>
#include <vector>

#ifdef WIN32
#include <Windows.h>
#elif __APPLE__ || __linux__ 
#include <dirent.h>
#endif

#include "Client.h"
#include "Vehicule.h"
#include "Zone.h"


//TODO: Complete return types and parameters.
void creerLexique(const std::string& repertoire);
void equilibrerFlotte();
void lancerSimulation(/*TODO: donnees de simulation*/);

using namespace std;

int main() {
    char choix = 0;
    vector<Zone> zones;
    vector<Client> clients;
    vector<Vehicule> vehicules;

    while (true) {
        cout << "====================================================" << endl
             << "=== Veuillez choisir une option:" << endl
             << "===     a: Creer les zones" << endl
             << "===     b: Entrer les clients et les vehicules" << endl
             << "===     c: Demarrer la simulation" << endl
             << "===     d: Quitter" << endl
             << "====================================================" << endl
             << "Votre choix: ";

        cin >> choix;

        if (choix == 'd')
            break;

        switch (choix) {
            case 'a':
            {
                std::string repertoire;

                // Determine le type de vehicule
                cout << "Entrez le repertoire contenant les fichier .txt des differentes zones avec le parcours relatif ou absolue:" << endl;
                cin >> repertoire;

                try {
                    creerLexique(repertoire);
                } catch(std::exception& e) {
                    std::cerr << "ERREUR: " << e.what() << std::endl;
                }
            }
                break;

            case 'b':
            {
                if (zones.size() == 0) {
                    cerr << "ERREUR: Les zones doivent etre configure avant de pouvoir entrer les client et les vehicule"
                         << endl;
                    break;
                }

                int fichierClient = 0, fichierVehicule = 0;

                cout << "Voulez-vous entrer les clients via un fichier .txt?" << endl
                     << "Oui (1) ou Non (2)" << endl;
                cin >> fichierClient;

                if (fichierClient == 1) {
                    // Lire client d'un fichier

                } else if (fichierClient == 2) {
                    // Lire client du command line

                } else {
                    cerr << "ERREUR: Choix invalide" << endl;
                    break;
                }


                cout << "Voulez-vous entrer les vehicules via un fichier .txt?" << endl
                     << "Oui (1) ou Non (2)" << endl;
                cin >> fichierVehicule;

                if (fichierVehicule == 1) {
                    // Lire vehicule d'un fichier

                } else if (fichierVehicule == 2) {
                    // Lire vehicule du command line

                } else {
                    cerr << "ERREUR: Choix invalide" << endl;
                    break;
                }

            }
                break;

            case 'c':
            {
                string depart, arrive;
                if (!vehicule || vehicule->getTypeCarburant() == 'r') {
                    cerr << "ERREUR: Les caracteristiques du vehicule sont necessaire a la recherche d'un itineraire"
                         << endl;
                    break;
                } else if (!graphe) {
                    cerr << "ERREUR: Une carte est necessaire a la recherche d'un itineraire" << endl;
                    break;
                }

                cout << "Entrez la station de depart: ";
                cin >> depart;

                cout << "Entrez la station d'arrive: ";
                cin >> arrive;

                Sommet* a = nullptr; Sommet* z = nullptr;
                for (auto sommet : graphe->getSommet()) {
                    if (sommet->getName() == depart.at(0)) {
                        a = sommet;
                    }
                    else if (sommet->getName() == arrive.at(0)) {
                        z = sommet;
                    }
                }
                if (a != nullptr && z != nullptr) {
                    vehicule->setAutonomieActuelle(plusCourtChemin(extractionGraphe(graphe, vehicule->getAutonomieMax()), a, z, vehicule));

                }
            }
                break;

            default:
                cerr << "ERREUR: Choix invalide" << endl;
                break;
        }
    }

    delete vehicule;
    delete graphe;
}

void creerLexique(const std::string& repertoire) {
    //TODO
    std::vector<std::string> fichiers;
#ifdef WIN32
    std::string regex = repertoire + "/*.txt";
    WIN32_FIND_DATAA data;
    HANDLE handle = FindFirstFileA(regex.c_str(), &data);
    if(handle != INVALID_HANDLE_VALUE) {
        do {
            if(!(data.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY))
                fichiers.push_back(data.cFileName);
        }while(FindNextFileA(handle, &data));

        FindClose(handle);
    } else {
        throw std::exception("Repertoire invalide ou ne contient pas de fichiers valides.");
    }
#elif __APPLE__ || __linux__
    DIR* dir = opendir(repertoire.c_str());
    struct dirent* fich;
    if(dir != nullptr) {
        while((fich = readdir(dir)) != nullptr) {
            std::string nomFichier(fich->d_name);
            if(nomFichier != "." && nomFichier != ".." && nomFichier.substr(nomFichier.size() - 4) == ".txt")
                fichiers.push_back(nomFichier);
        }

        closedir(dir);
    } else {
        throw std::exception("Repertoire invalide ou ne contient pas de fichiers valides.");
    }
#endif

    for(auto fichier : fichiers) {
        std::ifstream stream(fichier);
        while(!stream.eof()) {

        }
    }
}

void equilibrerFlotte() {
    //TODO
}

void lancerSimulation(/*TODO: donnees de simulation*/) {
    //TODO
}
