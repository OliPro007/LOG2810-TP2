import os


def creer_lexique(path):
    try:
        for file_name in os.listdir(path):
            if file_name.endswith(".txt"):
                print(file_name)
                with open(path+"/"+file_name) as file:
                    # TODO: Read the file and create the finite state automata
                    print(file.read())
    except FileNotFoundError as e:
        print("ERREUR: {err}: {dir}".format(err=e.strerror, dir=path))


def equilibrer_flotte():
    pass


def lancer_simulation():
    pass


def main():
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
        if choix is 'a':
            print("Entrez le répertoire des zones: ", end="")
            path = input()
            creer_lexique(path)
        elif choix is 'b':
            print("Voulez-vous entrer les informations du client à partir d'un fichier? (o/n): ", end="")
            utiliser_fichier = input()

            if utiliser_fichier is 'o':
                file_name = input()
                try:
                    with open(file_name) as file:
                        print(file.read())
                except FileNotFoundError as e:
                    print(e.strerror)

                pass  # TODO: Complete when using a file
            elif utiliser_fichier is 'n':
                pass  # TODO: Complete when not using a file
            else:
                print("Choix invalide.")
        elif choix is 'c':
            pass  # TODO: Complete choice c
        elif choix is 'd':
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
