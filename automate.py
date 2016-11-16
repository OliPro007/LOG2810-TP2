import os


def creer_lexique(path):
    try:
        for file in os.listdir(path):
            if file.endswith(".txt"):
                print(file)
    except FileNotFoundError as e:
        print("ERREUR: {err}: {dir}".format(err=e.strerror, dir=path))


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
            pass
        elif choix is 'c':
            pass
        elif choix is 'd':
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
