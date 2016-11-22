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


def equilibrer_flotte(zones, clients, vehicules , vehicules_occupes):
    print("BEFORE")
    for zone in zones:
        print(zone.nb_vehicule)
    desequilibre = True
    while desequilibre :
        desequilibre = False
        done = False
        for zone1 in zones:
            for zone2 in zones:
                if not done and zone1.nb_vehicule - zone2.nb_vehicule > 1:
                    desequilibre = True
                    for vehicule in vehicules:
                        if not done and vehicule['zone'] == zone1.name:
                            vehicule['zone'] = zone2.name
                            vehicule['quartier'] = zone2.select_random_quartier()
                            vehicule['nb_trajet_vide'] +=1
                            zone1.nb_vehicule -= 1
                            zone2.nb_vehicule += 1
                            done = True
    print("AFTER")
    for zone in zones:
        print(zone.nb_vehicule)
    print("VEHICULE STATE ")
    for vehicule in vehicules:
        print(vehicule)

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

    """1- Noter les donner avant la simulation pour le tableau demande"""
    presimulation_zones = zones.copy()

    """2- faire la liste de tous les groupe present"""
    liste_groupes = []

    for client in clients:
        exists = False
        for groupe in liste_groupes:
            if groupe['number'] == client['groupe']:
                exists = True
        if not exists:
            liste_groupes.append({'number': client['groupe'],
                                 'clients': []
                                  },)

    """3- faire des liste contenant tous les client par groupe"""
    for client in clients:
        for groupe in liste_groupes:
            if groupe['number'] == client['groupe']:
                groupe['clients'].append(client)

    """4- deplacer les client du 1er groupe"""
    def moveclient(client,vehicule):
        for zone in zones:
            if zone.contains(client['destination']):
                vehicule['zone'] = zone
                vehicule['quartier'] = client['destination']
                vehicule['nb_trajet_plein'] += 1

    def getkey(item):
        return item['number']
    liste_groupes.sort(key=getkey)
    for groupe in liste_groupes:
        list_vehicules_occupes = []
        for client in groupe:
            zone_client = ''
            list_vehicules_in_client_zone = []
            list_vehicules_in_client_zone_libres = []
            for zone in zones:
                if zone.contains(client['depart']):
                    zone_client = zone
            for vehicule in vehicules:
                if vehicule['zone'] == zone_client:
                    list_vehicules_in_client_zone.append(vehicule)

            occupe = False
            for vehicule in list_vehicules_in_client_zone:
                for vehicule_occupe in list_vehicules_occupes:
                    if vehicule == vehicule_occupe:
                        occupe = True
                if not occupe:
                    list_vehicules_in_client_zone_libres.append(vehicule)
            moved = False
            for vehicule in list_vehicules_in_client_zone_libres:
                if vehicule['quartier'] == client['depart']:
                    list_vehicules_occupes.append(vehicule)
                    moveclient(client, vehicule)
                    moved = True
            if not moved:
                moveclient(client, list_vehicules_in_client_zone_libres[0])
        equilibrer_flotte(zones, clients, vehicules, list_vehicules_occupes)


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
                print("\tquartier_départ_1,quartier_destination_1,#groupe;"
                      + "\n\tquartier_départ_2,quartier_destination_2,#groupe;"
                      + "\n\tquartier_départ_3,quartier_destination_3,#groupe;")
                print("Chemin vers le fichier .txt: ", end="")

                file_name = input()
                try:
                    with open(file_name) as file:
                        print(file.read())
                        file.seek(0)
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
                        print("ERREUR: l'une des zones est invalide: depart={}  destination={}".format(depart, destination), file=sys.stderr)
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
                print("\tzone_départ_véhicule_1;"
                      + "\n\tzone_départ_véhicule_2;"
                      + "\n\tzone_départ_véhicule_3;")
                print("Chemin vers le fichier .txt: ", end="")
                file_name = input()
                try:
                    with open(file_name) as file:
                        print(file.read())
                        file.seek(0)
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
            lancer_simulation(zones, clients, vehicules)

        elif choix == 'd':
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
