#include <iostream>

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
                char type;
                int autonomieMax, autonomieActuelle;

                // Determine le type de vehicule
                cout << "Entrez les caracteristique du vehicule selon la methode suivante:" << endl
                     << "Type de vehicule (choix: (e)ssence; e(l)ectrique; (h)ybrid): ";

                cin >> type;

                if (type != 'e' && type != 'l' && type != 'h') {
                    cerr << "ERREUR: Type de vehicule invalide" << endl;
                    break;
                }

                // Determine l'autonomie maximale et actuelle du vehicule
                cout << "Autonomie maximale du vehicule: ";
                cin >> autonomieMax;

                cout << "Autonomie actuelle du vehicule: ";
                cin >> autonomieActuelle;

                if (autonomieActuelle > autonomieMax) {
                    cerr << "ERREUR: L'autonomie actuelle ne peut pas etre superieure a l'autonomie maximale" << endl;
                    break;
                }

                // Cree le vehicule
                vehicule = new Vehicule(type, autonomieMax, autonomieActuelle);
            }
                break;

            case 'b':
            {
                string nomFichier;
                cout << "Entrez le nom du fichier contenant les informations sur la carte: ";
                cin >> nomFichier;

                // Cree et affiche le graphe
                graphe = creerGraphe(nomFichier);
                lireGraphe(graphe);
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
}

void equilibrerFlotte() {
    //TODO
}

void lancerSimulation(/*TODO: donnees de simulation*/) {
    //TODO
}
