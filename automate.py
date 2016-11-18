# Standard library imports
import os
import sys

# Related third party imports
from zone import Zone


def creer_lexique(path):
    """
    Crée des zones à partir de tous les fichiers .txt d'un répertoire.

    :param path: Le chemin absolu ou relatif du répertoire.
    :return: Une liste contenant toutes les zones construites.
    """
    zones = []
    try:
        for file_name in os.listdir(path):
            if file_name.endswith(".txt"):
                with open("{}/{}".format(path, file_name)) as file:
                    zone = Zone(file_name.replace(".txt", ""))
                    zones.append(zone)
                    for line in file:
                        line = line.replace("\n", "")
                        zone.ajouter_quartier(line)

    except FileNotFoundError:
        print("ERREUR: Le chemin d’accès spécifié est introuvable : {}".format(path), file=sys.stderr)
        return []

    return zones


def equilibrer_flotte():
    pass


def lancer_simulation(zones, clients, vehicules):
    """
    Suggestion:
    1- Noter les donner avant la simulation pour le tableau demande
    2- faire la liste de tous les groupe present
    3- faire des liste contenant tous les client par groupe
    4- deplacer les client du 1er groupe
    5- equilibrer les vehicule
    6- refaire 4 avec prochain groupe
    7- afficher les 2 tableau demande
    """
    pass


def main():
    clients = []
    vehicules = []
    zones = []

    while True:
        print("====================================================")
        print("=== Veuillez choisir une option:")
        print("===     a: Créer les zones")
        print("===     b: Entrer les clients et les véhicules")
        print("===     c: Démarrer la simulation")
        print("===     d: Quitter")
        print("====================================================")
        print("Votre choix: ", end="")

        choix = input()
        if choix == 'a':
            print("Entrez le répertoire des zones: ", end="")
            path = input()
            zones = creer_lexique(path)
        elif choix == 'b':
            if not zones:
                print("ERREUR: Les zones doivent être créées avant de pouvoir entrer les clients et les véhicules", file=sys.stderr)
                continue

            # Reinitialise la liste de clients et de vehicule
            clients = []
            vehicules = []

            liste_client = ""
            liste_vehicule = ""

            print("Voulez-vous entrer les informations des clients à partir d'un fichier .txt? (o/n): ", end="")
            utiliser_fichier = input()

            if utiliser_fichier == 'o':
                print("Veuillez entrer le chemin vers le fichier .txt contenant les clients sous le format suivant:")
                print("\tquartier_départ_1,quartier_destination_1,#groupe;" \
                      + "\n\tquartier_départ_2,quartier_destination_2,#groupe;"\
                      + "\n\tquartier_départ_3,quartier_destination_3,#groupe;")
                print("Chemin vers le fichier .txt: ", end="")

                file_name = input()
                try:
                    with open(file_name) as file:
                        print(file.read())
                        liste_client = file.read().replace("\n", "")

                except FileNotFoundError:
                    print("Le fichier spécifié est introuvable: {}".format(file_name), file=sys.stderr)
                    continue

            elif utiliser_fichier == 'n':
                print("Veuillez entrer les clients selon le format suivant:")
                print("\tquartier_départ_1,quartier_destination_1,#groupe;quartier_départ_2,quartier_destination_2,#groupe;")
                print("Liste de client: ", end="")
                liste_client = input()

            else:
                print("Choix invalide.", file=sys.stderr)

            for client in liste_client.split(";"):
                if client:
                    # Valide les quartiers de depart et de destination des clients
                    depart = client.split(',')[0]
                    destination = client.split(',')[1]
                    groupe = int(client.split(',')[2])

                    depart_valide = False
                    destination_valide = False
                    for zone in zones:
                        if zone.contains(depart):
                            depart_valide = True
                        if zone.contains(destination):
                            destination_valide = True

                    if not depart_valide or not destination_valide:
                        print("ERREUR: zone invalide: {}  {}".format(depart, destination), file=sys.stderr)
                        clients = []
                        break

                    # Ajout du client a la liste
                    clients.append({'depart': depart,
                                    'destination': destination,
                                    'groupe': groupe,
                                    },
                                   )
            if not clients:
                continue

            print("Voulez-vous entrer les informations des véhicules à partir d'un fichier .txt? (o/n): ", end="")
            utiliser_fichier = input()

            if utiliser_fichier == 'o':
                print("Veuillez entrer le chemin vers le fichier .txt contenant les véhicules sous le format suivant: ")
                print("\tzone_départ_véhicule_1;" \
                      + "\n\tzone_départ_véhicule_2;" \
                      + "\n\tzone_départ_véhicule_3;")
                print("Chemin vers le fichier .txt: ", end="")
                file_name = input()
                try:
                    with open(file_name) as file:
                        print(file.read())
                        liste_vehicule = file.read().replace("\n", "")

                except FileNotFoundError as e:
                    print(e.strerror, file=sys.stderr)

            elif utiliser_fichier == 'n':
                print("Veuillez entrer les clients selon le format suivant:")
                print("zone_départ_véhicule_1;zone_départ_véhicule_2;zone_départ_véhicule_3;")
                print("Liste de vehicule: ", end="")
                liste_vehicule = input()

            else:
                print("Choix invalide.")
                continue

            for depart_vehicule in liste_vehicule.split(';'):
                if depart_vehicule:
                    # Valide la zone de depart des vehicule
                    for zone in zones:
                        if depart_vehicule == zone.name:
                            zone.nb_vehicule += 1
                            vehicules.append({'zone': depart_vehicule.strip(),
                                              'quartier': zone.select_random_quartier(),
                                              'nb_trajet_vide': 0,
                                              'nb_trajet_plein': 0,
                                              },
                                             )
                            break
                    else:
                        print("ERREUR: Zone de départ du véhicule inexistante: {}".format(depart_vehicule), file=sys.stderr)
                        vehicules = []
                        break

        elif choix == 'c':
            if not clients or not vehicules:
                print("ERREUR: Les clients et les véhicules doivent être créés avant de pouvoir lancer la simulation", file=sys.stderr)
                continue
            pass  # TODO: Complete choice c

        elif choix == 'd':
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
