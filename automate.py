# encoding: utf-8
# Python2 future imports
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement

# Standard library imports
import copy
import os
import random
import sys

# Related third party imports
from zone import Zone

# Other Python2 support
try:
    input = raw_input
except NameError:
    pass


def client_dans_groupe(groupe, client):
    return client['groupe'] == groupe


def selectionner_vehicule(vehicules, client):
    for vehicule in vehicules:
        if vehicule['quartier'] == client['depart']:
            return vehicule

    if vehicules:
        return random.choice(vehicules)
    else:
        return None


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
    except EnvironmentError:
        print("ERREUR: Le chemin d’accès spécifié est introuvable : {}".format(path), file=sys.stderr)
        return []
    else:
        print("Fichiers lus avec succès!")
        return zones


def equilibrer_flotte(zones, vehicules, zone_manque):
    zone_max = None
    nb_vehicule_max = 0
    for zone in zones:
        nb_vehicule_zone = len(list(filter(lambda x: x['zone'] == zone.name and not x['occupe'], vehicules)))
        if nb_vehicule_zone > nb_vehicule_max:
            zone_max = zone
            nb_vehicule_max = len(list(filter(lambda x: x['zone'] == zone_max.name and not x['occupe'], vehicules)))

    if zone_max is not None:
        for i in range(0, nb_vehicule_max//2):
            vehicule = random.choice(list(filter(lambda x: x['zone'] == zone_max.name, vehicules)))
            vehicule['zone'] = zone_manque.name
            vehicule['quartier'] = zone_manque.select_random_quartier().name
            zone_max.nb_vehicule -= 1
            zone_manque.nb_vehicule += 1
            vehicule['nb_trajet_vide'] += 1


def lancer_simulation(clients, vehicules, zones):
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

    # 1- Noter les donner avant la simulation pour le tableau demande
    presimulation_zones = copy.deepcopy(zones)

    # 2- faire la liste de tous les groupe present
    liste_groupes = list(set(map(lambda x: x['groupe'], clients)))
    liste_groupes.sort()

    for groupe in liste_groupes:
        for client in filter(lambda x: client_dans_groupe(groupe, x), clients):
            zone_client = ''
            vehicule_disponible = []

            for zone in zones:
                if zone.contains(client['depart']):
                    zone_client = zone
                    break

            for vehicule in vehicules:
                if vehicule['zone'] == zone_client.name and not vehicule['occupe']:
                    vehicule_disponible.append(vehicule)

            vehicule_choisi = selectionner_vehicule(vehicule_disponible, client)
            if not vehicule_choisi:
                equilibrer_flotte(zones, vehicules, zone_client)
                vehicule_disponible = []
                for vehicule in vehicules:
                    if vehicule['zone'] == zone_client.name and not vehicule['occupe']:
                        vehicule_disponible.append(vehicule)
                vehicule_choisi = selectionner_vehicule(vehicule_disponible, client)
                if not vehicule_choisi:
                    print("Aucun vehicule disponible")
                    continue

            for zone in zones:
                if zone.contains(client['destination']):
                    vehicule_choisi['zone'] = zone.name
                    vehicule_choisi['quartier'] = client['destination']
                    vehicule_choisi['nb_trajet_plein'] += 1
                    zone.nb_vehicule += 1
                    vehicule_choisi['occupe'] = True
                if zone.contains(client['depart']):
                    zone.nb_vehicule -= 1

            for vehicule in vehicules:
                vehicule['occupe'] = False

    # Apres simulation
    print("État des véhicules:")
    for vehicule in vehicules:
        print("\tzone : {}, quartier : {}, nb trajets plein : {}, nb trajets vides : {}"
              .format(vehicule['zone'], vehicule['quartier'], vehicule['nb_trajet_plein'], vehicule['nb_trajet_vide']))
    print("\nDebut:")
    for zone in presimulation_zones:
        print("\t{} : {} véhicules".format(zone.name, zone.nb_vehicule))
    print("\nFin:")
    for zone in zones:
        print("\t{} : {} véhicules".format(zone.name, zone.nb_vehicule))


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
                        liste_client = file.read().replace("\n", "")
                except EnvironmentError:
                    print("ERREUR: Le fichier spécifié est introuvable: {}".format(file_name), file=sys.stderr)
                    continue
                else:
                    print("Fichier lu avec succès!")

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
                        print("ERREUR: l'une des zones est invalide: départ={}  destination={}".format(depart, destination), file=sys.stderr)
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
                        liste_vehicule = file.read().replace("\n", "")
                except EnvironmentError:
                    print("ERREUR: Le fichier spécifié est introuvable: {}".format(file_name), file=sys.stderr)
                else:
                    print("Fichier lu avec succès!")

            elif utiliser_fichier == 'n':
                print("Veuillez entrer les clients selon le format suivant:")
                print("zone_départ_véhicule_1;zone_départ_véhicule_2;zone_départ_véhicule_3;")
                print("Liste de vehicule: ", end="")
                liste_vehicule = input()

            else:
                print("ERREUR: Choix invalide.")
                continue

            for depart_vehicule in liste_vehicule.split(';'):
                if depart_vehicule:
                    # Valide la zone de depart des vehicule
                    for zone in zones:
                        if depart_vehicule == zone.name:
                            zone.nb_vehicule += 1
                            vehicules.append({'zone': depart_vehicule.strip(),
                                              'quartier': zone.select_random_quartier().name,
                                              'nb_trajet_vide': 0,
                                              'nb_trajet_plein': 0,
                                              'occupe': False,
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
            lancer_simulation(clients, vehicules, zones)

        elif choix == 'd':
            break

        else:
            print("ERREUR: Choix invalide.")


if __name__ == "__main__":
    main()
