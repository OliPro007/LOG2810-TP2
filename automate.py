# Standard library imports
import os

# Related third party imports
import zone


def creer_lexique(path):
    zones = []
    try:
        for file_name in os.listdir(path):
            if file_name.endswith(".txt"):
                # TODO remove print of the file name
                print(file_name)
                with open(path+"/"+file_name) as file:
                    # TODO: Read the file and create the finite state automata
                    zones.append(zone.Zone(file_name))
                    print(file.read())

    except FileNotFoundError as e:
        print("ERREUR: Parcours vers le repertoire invalide : path={} erreur={}".format(path, e.strerror))
        return []

    return zones


def equilibrer_flotte():
    pass


def lancer_simulation(zones, clients, vehicules):
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
                print("ERREUR: Les zones doivent etre cree avant de pouvoir entrer les clients et les vehicules")
                continue

            liste_client = ""
            liste_vehicule = ""

            print("Voulez-vous entrer les informations des clients à partir d'un fichier .txt? (o/n): ", end="")
            utiliser_fichier = input()

            if utiliser_fichier == 'o':
                print("Veuillez entrer le chemin vers le fichier .txt contenant les clients sous le format suivant:")
                print("quartier_depart_1,quartier_destination_1,#groupe;quartier_depart_2,quartier_destination_2,#groupe;")
                print("Chemin vers le fichier .txt: ", end="")

                file_name = input()
                try:
                    with open(file_name) as file:
                        print(file.read())
                        liste_client = file.read()
                except FileNotFoundError as e:
                    print(e.strerror)

            elif utiliser_fichier == 'n':
                print("Veuillez entrer les clients selon le format suivant:")
                print("quartier_depart_1,quartier_destination_1,#groupe;quartier_depart_2,quartier_destination_2,#groupe;")
                print("Liste de client: ", end="")

                liste_client = input()

            else:
                print("Choix invalide.")
                continue

            # TODO populate client list

            print("Voulez-vous entrer les informations des vehicule à partir d'un fichier .txt? (o/n): ", end="")
            utiliser_fichier = input()

            if utiliser_fichier == 'o':
                print("Veuillez entrer le chemin vers le fichier .txt contenant les vehicules sous le format suivant: ")
                print("zone_depart_vehicule_1;zone_depart_vehicule_2;zone_depart_vehicule_3;")
                print("Chemin vers le fichier .txt: ", end="")
                file_name = input()
                try:
                    with open(file_name) as file:
                        print(file.read())
                        liste_vehicule = file.read()
                except FileNotFoundError as e:
                    print(e.strerror)

            elif utiliser_fichier == 'n':
                print("Veuillez entrer les clients selon le format suivant:")
                print("zone_depart_vehicule_1;zone_depart_vehicule_2;zone_depart_vehicule_3;")
                print("Liste de vehicule: ", end="")

                liste_vehicule = input()
            else:
                print("Choix invalide.")
                continue

            # TODO populate vehicule list

        elif choix == 'c':
            if not clients or not vehicules:
                print("ERREUR: Les clients et les vehicules doivent etre cree avant de pouvoir lancer la simulation")
                continue

            pass  # TODO: Complete choice c

        elif choix == 'd':
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
