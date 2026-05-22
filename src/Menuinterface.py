"""from equipements import Routeur, Switch, Serveur, Firewall, PointAccesWifi, Terminal
from paquets import Paquet
from topologie import Topologie, Lien
from securite import RegleFiltrage
# from simulateur import SimulateurTrafic
from Moniteur import Moniteur


class MenuInteractif:

    def __init__(self):
        self.topologie = Topologie()
        #self.simulateur = SimulateurTrafic(self.topologie)
        self.moniteur = Moniteur(self.topologie)

    def lancer(self):
        print("SIMNet")

        while True:
            print("\n1. Equipements")
            print("2. Trafic")
            print("3. Firewall")
            print("4. Statistiques")
            print("5. Rapport")
            print("6. Topologie")
            print("0. Quitter")

            choix = input("Choix: ")

            if choix == "1":
                self.menu_equipements()
            elif choix == "2":
                self.menu_trafic()
            elif choix == "3":
                self.menu_firewall()
            elif choix == "4":
                self.menu_statistiques()
            elif choix == "5":
                self.moniteur.generer_rapport()
            elif choix == "6":
                self.topologie.afficher()
            elif choix == "0":
                break

    def menu_equipements(self):
        while True:
            print("\n1 Ajouter")
            print("2 Supprimer")
            print("3 Lien")
            print("0 Retour")

            c = input("Choix: ")

            if c == "1":
                self.ajouter()
            elif c == "2":
                ip = input("IP: ")
                self.topologie.supprimer_equipement(ip)
            elif c == "3":
                self.ajouter_lien()
            elif c == "0":
                break

    def ajouter(self):
        t = input("Type: ")
        nom = input("Nom: ")
        marque = input("Marque: ")
        adresse_ip = input("Adresse IP: ")

        if t == "routeur":
            e = Routeur(nom, marque,adresse_ip)
        elif t == "switch":
            e = Switch(nom, marque, adresse_ip)
        elif t == "serveur":
            e = Serveur(nom, marque, adresse_ip)
        elif t == "firewall":
            login = input("Login: ")
            mdp = input("MDP: ")
            e = Firewall(adresse_ip, nom, marque, login, mdp)
        elif t == "wifi":
            ssid = input("SSID: ")
            e = PointAccesWifi(nom, marque, adresse_ip, ssid)
        elif t == "terminal":
            type_t = input("Type: ")
            e = Terminal(nom, marque, adresse_ip, type_t)
        else:
            return

        self.topologie.ajouter_equipement(e)

    def ajouter_lien(self):
        ip1 = input("IP1: ")
        ip2 = input("IP2: ")

        e1 = self.topologie.get_equipement(ip1)
        e2 = self.topologie.get_equipement(ip2)

        if not e1 or not e2:
            return

        bp = float(input("Bande passante: "))
        lat = float(input("Latence: "))

        lien = Lien(e1, e2, bp, lat)
        self.topologie.ajouter_lien(lien)

    def menu_trafic(self):
        src = input("Source: ")
        dst = input("Destination: ")
        proto = input("Protocole: ")
        taille = input("Taille: ")
        prio = input("Priorite: ")
        port = input("Port: ")

        p = Paquet(src, dst, proto, taille, prio, port)

        chemin = self.simulateur.envoyer_paquet(p)

        if chemin:
            for c in chemin:
                print(c)
        else:
            print("Echec")

    def menu_firewall(self):
        fw = None
        for e in self.topologie.equipements.values():
            if isinstance(e, Firewall):
                fw = e
                break

        if not fw:
            return

        login = input("Login: ")
        mdp = input("MDP: ")

        if not fw.authentifier(login, mdp):
            return

        while True:
            print("\n1 Ajouter regle")
            print("2 Supprimer regle")
            print("3 Journal")
            print("0 Retour")

            c = input("Choix: ")

            if c == "1":
                action = input("Action: ")
                adresse_ip = input("IP: ")
                proto = input("Proto: ")
                port = input("Port: ")
                plage = input("Plage: ")
                r = RegleFiltrage(action, adresse_ip, proto, port, plage)
                fw.ajouter_regle(r)
            elif c == "2":
                i = int(input("Index: "))
                fw.supprimer_regle(i)
            elif c == "3":
                for j in fw.get_journal():
                    print(j)
            elif c == "0":
                break

    def menu_statistiques(self):
        stats = self.moniteur.collecter()
        print(stats)

        liens = self.moniteur.get_taux_utilisation_liens()
        print(liens) """
