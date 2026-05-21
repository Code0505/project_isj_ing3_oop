from equipements import Routeur, Switch, Serveur, Firewall, PointAccesWifi, Terminal
from paquets import Paquet
from topologie import Topologie, Lien
from securite import RegleFiltrage
from simulateur import SimulateurTrafic
from moniteur import Moniteur

class MenuInteractif:

    def __init__(self):
        self.topologie  = Topologie()
        self.simulateur = SimulateurTrafic(self.topologie)
        self.moniteur   = Moniteur(self.topologie)

    # LANCEMENT

    def lancer(self):
        print("=" * 50)
        print("   Bienvenue dans SIMNet")
        print("   Simulateur de Réseau Intelligent")
        print("=" * 50)

        while True:
            print("\n===== MENU PRINCIPAL =====")
            print("1. Gérer les équipements")
            print("2. Gérer le trafic réseau")
            print("3. Gérer le Firewall")
            print("4. Afficher les statistiques")
            print("5. Générer un rapport")
            print("6. Afficher la topologie")
            print("0. Quitter")

            choix = input("\nVotre choix : ")

            if choix == "1":
                self.menu_equipements()
            elif choix == "2":
                self.menu_trafic()
            elif choix == "3":
                self.menu_firewall()
            elif choix == "4":
                self.menu_statistiques()
            elif choix == "5":
                self.menu_rapport()
            elif choix == "6":
                self.topologie.afficher()
            elif choix == "0":
                print("\nAu revoir !")
                break
            else:
                print("Choix invalide, réessayez.")

    # MENU ÉQUIPEMENTS

    def menu_equipements(self):
        while True:
            print("\n--- Gestion des équipements ---")
            print("1. Ajouter un équipement")
            print("2. Supprimer un équipement")
            print("3. Ajouter un lien")
            print("4. Supprimer un lien")
            print("0. Retour")

            choix = input("\nVotre choix : ")

            if choix == "1":
                self._ajouter_equipement()
            elif choix == "2":
                self._supprimer_equipement()
            elif choix == "3":
                self._ajouter_lien()
            elif choix == "4":
                self._supprimer_lien()
            elif choix == "0":
                break
            else:
                print("Choix invalide.")

    def _ajouter_equipement(self):
        print("\nTypes disponibles :")
        print("1. Routeur")
        print("2. Switch")
        print("3. Serveur")
        print("4. Firewall")
        print("5. PointAccesWifi")
        print("6. Terminal")

        choix = input("Type : ")
        nom    = input("Nom    : ")
        marque = input("Marque : ")
        ip     = input("IP     : ")

        if choix == "1":
            equip = Routeur(nom, marque, ip)
        elif choix == "2":
            equip = Switch(nom, marque, ip)
        elif choix == "3":
            equip = Serveur(nom, marque, ip)
        elif choix == "4":
            login = input("Login admin   : ")
            mdp   = input("Mot de passe  : ")
            equip = Firewall(ip, nom, marque, login, mdp)
        elif choix == "5":
            ssid = input("SSID  : ")
            equip = PointAccesWifi(nom, marque, ip, ssid)
        elif choix == "6":
            type_t = input("Type terminal : ")
            equip = Terminal(nom, marque, ip, type_t)
        else:
            print("Type invalide.")
            return

        self.topologie.ajouter_equipement(equip)
        print(f"Équipement {nom} ajouté.")

    def _supprimer_equipement(self):
        ip = input("IP de l'équipement à supprimer : ")
        self.topologie.supprimer_equipement(ip)
        print(f"Équipement {ip} supprimé.")

    def _ajouter_lien(self):
        ip1 = input("IP équipement 1 : ")
        ip2 = input("IP équipement 2 : ")

        eq1 = self.topologie.get_equipement(ip1)
        eq2 = self.topologie.get_equipement(ip2)

        if eq1 is None or eq2 is None:
            print("Un des équipements est introuvable.")
            return

        bande_passante = float(input("Bande passante (Mbps) : "))
        latence        = float(input("Latence (ms)          : "))

        lien = Lien(eq1, eq2, bande_passante, latence)
        self.topologie.ajouter_lien(lien)
        print(f"Lien {lien} ajouté.")

    def _supprimer_lien(self):

        ip1 = input("IP équipement 1 : ")
        ip2 = input("IP équipement 2 : ")
        self.topologie.supprimer_lien(ip1, ip2)
        print(f"Lien entre {ip1} et {ip2} supprimé.")

